import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json
from Seqclass import Seq


PORT = 8080
IP = "212.128.255.74"
socketserver.TCPServer.allow_reuse_address = True
SERVER = "rest.ensembl.org"
PARAM = "?content-type=application/json"
connect = http.client.HTTPSConnection(SERVER)
def dat(e):
    connect.request("GET", e + PARAM)
    response = connect.getresponse()
    res = response.read().decode()
    data = json.loads(res)
    return data

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

            contents_list = []
            if path == "/listSpecies" or "listSpecies" in arguments:
                ENDPOINT = "/info/species"
                data = dat(ENDPOINT)
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
                ENDPOINT = "/info/assembly/" + arguments["species"][0].replace(" ", "%20")
                data = dat(ENDPOINT)
                contents = read_html_file("ka.html").render(
                    context={"todisplay": "<p></p>".join(data["karyotype"]), "number": f"Species: {arguments["species"][0]}"})
            elif path == "/chromosomeLength" or "chromosomeLength" in arguments:
                ENDPOINT = "/info/assembly/" + arguments["species"][0]
                data = dat(ENDPOINT)
                for a in data["top_level_region"]:
                    if a["name"] == arguments["chromo"][0]:
                        print(a["name"], a["coord_system"], a["length"])
                        if a["coord_system"] == "chromosome":
                            l = a["length"]

                contents = read_html_file("le.html").render(
                    context={"todisplay": l,
                             "s": f"Species: {arguments["species"][0]}", "chro": arguments["chromo"][0]})
            elif path == "/geneLookup" or "geneLookup" in arguments:
                ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0]
                data = dat(ENDPOINT)
                contents = read_html_file("look.html").render(
                    context={"gene": arguments["gene"][0],
                             "what": f"Stable identifier: {data[0]["id"]}"})
            elif path == "/geneSeq" or "geneSeq" in arguments:
                ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0]
                data = dat(ENDPOINT)
                ENDPOINT2 = "/sequence/id/" + data[0]["id"]
                data2 = dat(ENDPOINT2)
                s = Seq(data2["seq"])
                contents = read_html_file("look.html").render(
                    context={"gene": arguments["gene"][0],
                             "what": f"Sequence: <p></p><textarea rows='8' cols='70'>{s}</textarea>" })
            elif path == "/geneInfo" or "geneInfo" in arguments:
                ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0]
                data = dat(ENDPOINT)
                ENDPOINT2 = "/overlap/id/" + data[0]["id"]
                data2 = dat(ENDPOINT2)
                for a in data2:
                    if a["id"] == data[0]["id"]:
                        start = a["start"]
                contents = read_html_file("look.html").render(
                    context={"gene": arguments["gene"][0],
                             "what": f"Info <p></p>Start: {start}<p></p>End: {start}<p></p>Length: {start}<p></p>Id: {start}<p></p>Name of the chromosome: {start}"})
            elif path == "/geneCalc" or "geneCalc" in arguments:
                ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0]
                data = dat(ENDPOINT)
                ENDPOINT2 = "/sequence/id/" + data[0]["id"]
                data2 = dat(ENDPOINT2)
                s = Seq(data2["seq"])
                bases = []
                for a in s.count_base().split(", "):
                    base = (a.split(" : ")[0])
                    if s.len() != 0:
                        n = int(a.split(" : ")[1])
                        bases.append(f"{base}: {n} ({str(round(n / s.len() * 100, 2))}%)")
                    else:
                        bases.append(f"{a} (0%)")
                contents = read_html_file("look.html").render(context={"gene": arguments["gene"][0],
                        "what": f"Calculations <p></p>Length: {s.len()}<p></p> {"<p></p>".join(bases)}"})
            elif path == "/geneList" or "geneList" in arguments:#estamal
                ENDPOINT = f"/overlap/region/human/{arguments["chromo"][0]}:{arguments["start"][0]}-{arguments["end"][0]}"
                data = dat(ENDPOINT)
                print(data)
                contents = read_html_file("look.html").render(context={"gene": arguments["chromo"][0],
                           "what": f"Genes: {"<p></p>".join(contents_list)}"})
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