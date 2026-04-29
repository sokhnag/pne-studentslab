import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

from certifi import contents

PORT = 8080
IP = "212.128.255.74"
socketserver.TCPServer.allow_reuse_address = True
SERVER = "rest.ensembl.org"
PARAM = "?content-type=application/json"

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

#

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        global res
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(path)
        print(arguments)

        if path == "/" and arguments == {} :
            contents = Path('main.html').read_text()
        else:
            connect = http.client.HTTPSConnection(SERVER)
            contents_list = []
            if path == "/listSpecies" or "listSpecies" in arguments:
                ENDPOINT = "/info/species"
                connect.request("GET", ENDPOINT + PARAM)
                response = connect.getresponse()
                res = response.read().decode()
                data = json.loads(res)
                if "limit" in arguments:
                    lim = int(arguments["limit"][0])
                    a = 1
                    for b in data["species"]:
                        if a <= lim:
                            contents_list.append(f"{a}) Common name: {b["common_name"]}")
                            a += 1
                    contents = read_html_file("Species.html").render(
                        context={"todisplay": "<p></p>".join(contents_list), "number": lim, "total": len(data["species"])})
                else:
                    for b in data["species"]:
                        contents_list.append(b["common_name"])
                    contents = read_html_file("Species.html").render(context={"todisplay": "<p></p>".join(contents_list),
                                                                              "number": "ALL" ,"total": len(data["species"])})
            elif path == "/karyotype" or "karyotype" in arguments:
                print("%20".join((arguments["species"][0]).split(" ")))
                ENDPOINT = "/info/assembly/" + arguments["species"][0].replace(" ", "%20")
                print(ENDPOINT + PARAM)
                connect.request("GET", ENDPOINT + PARAM)
                response = connect.getresponse()
                res = response.read().decode()
                data = json.loads(res)
                print(data)
                contents = read_html_file("ka.html").render(
                    context={"todisplay": "<p></p>".join(data["karyotype"]), "number": f"Species: {arguments["species"][0]}"})
            elif path == "/chromosomeLength" or "chromosomeLength" in arguments:
                ENDPOINT = "/info/assembly/" + arguments["species"][0]
                connect.request("GET", ENDPOINT + PARAM)
                response = connect.getresponse()
                res = response.read().decode()
                data = json.loads(res)
                print(data)
                for a in data["top_level_region"]:
                    if a["name"] == arguments["chromo"][0]:
                        print(a["name"], a["coord_system"], a["length"])
                        if a["coord_system"] == "chromosome":
                            l = a["length"]

                contents = read_html_file("le.html").render(
                    context={"todisplay": l,
                             "s": f"Species: {arguments["species"][0]}", "chro": arguments["chromo"][0]})
            elif path == "/geneLookup" or "geneLookup" in arguments:
                ENDPOINT = "?" + arguments["gene"][0]
                connect.request("GET", ENDPOINT + PARAM)
                response = connect.getresponse()
                res = response.read().decode()
                data = json.loads(res)
                print(data)

            else:
                contents = Path('error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# - Server MAIN program

Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()