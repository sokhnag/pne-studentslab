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
PARAM = "content-type=application/json"
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

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        global res
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        content_json = {}
        error_code = 200
        if "json" in arguments and arguments["json"][0] == "1":
            type = "application/json"
        else:
            type = "text/html"

        if path == "/" and arguments == {} :
            content_html = Path('main.html').read_text()
        else:
            contents_list = []
            try:
                if path == "/listSpecies" or "listSpecies" in arguments:
                    ENDPOINT = "/info/species" + "?"
                    data = dat(ENDPOINT)
                    if "limit" in arguments:
                        lim = int(arguments["limit"][0])
                        a = 1
                        content_json["Limit"] = lim
                        for b in data["species"]:
                            if a <= lim:
                                contents_list.append(f"{a}) {b["common_name"]}")
                                content_json[f"Species {a}"] = b["common_name"]
                                a += 1
                        content_html = read_html_file("Species.html").render(
                            context={"todisplay": "<p></p>".join(contents_list), "number": lim, "total": len(data["species"])})
                    else:
                        a = 1
                        for b in data["species"]:
                            contents_list.append(f"{a}) {b["common_name"]}")
                            content_json[f"Species {a}"] = b["common_name"]
                            a += 1
                        content_html = read_html_file("Species.html").render(context={"todisplay": "<p></p>".join(contents_list),
                                                                                  "number": "ALL" ,"total": len(data["species"])})
                elif path == "/karyotype" or "karyotype" in arguments:
                    ENDPOINT = "/info/assembly/" + arguments["species"][0].replace(" ", "%20") + "?"
                    data = dat(ENDPOINT)
                    content_html = read_html_file("ka.html").render(
                        context={"todisplay": "<p></p>".join(data["karyotype"]), "number": f"Species: {arguments["species"][0]}"})
                    content_json["Species"] = arguments["species"][0]
                    content_json["Karyotype"] = data["karyotype"]
                elif path == "/chromosomeLength" or "chromosomeLength" in arguments:
                    ENDPOINT = "/info/assembly/" + arguments["species"][0] + "?"
                    data = dat(ENDPOINT)
                    l = "Not found"
                    for a in data["top_level_region"]:
                        if a["name"] == arguments["chromo"][0]:
                            if a["coord_system"] == "chromosome":
                                l = a["length"]
                    content_html = read_html_file("le.html").render(
                        context={"todisplay": l,
                                 "s": f"Species: {arguments["species"][0]}", "chro": arguments["chromo"][0]})

                    content_json["Species"] = arguments["species"][0]
                    content_json["Chromosome"] = arguments["chromo"][0]
                    content_json["Lenght"] = l
                elif path == "/geneLookup" or "geneLookup" in arguments:
                    ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0] + "?"
                    data = dat(ENDPOINT)
                    content_html = read_html_file("look.html").render(
                        context={"gene": "Gene: " + arguments["gene"][0],
                                 "what": f"Stable identifier: {data[0]["id"]}"})
                    content_json["Gene"] = arguments["gene"][0]
                    content_json["Stable identifier"] = data[0]["id"]
                elif path == "/geneSeq" or "geneSeq" in arguments:
                    ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0] + "?"
                    data = dat(ENDPOINT)
                    ENDPOINT2 = "/sequence/id/" + data[0]["id"] + "?"
                    data2 = dat(ENDPOINT2)
                    s = Seq(data2["seq"])
                    content_html = read_html_file("look.html").render(
                        context={"gene": "Gene: " + arguments["gene"][0],
                                 "what": f"Sequence: <p></p><textarea rows='8' cols='70'>{s}</textarea>" })
                    content_json["Gene"] = arguments["gene"][0]
                    content_json["sequence"] = str(s)
                elif path == "/geneInfo" or "geneInfo" in arguments:
                    ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0]+ "?"
                    data = dat(ENDPOINT)
                    ENDPOINT2 = "/lookup/id/" + data[0]["id"]+ "?"
                    data2 = dat(ENDPOINT2)
                    start = 0
                    end = 0
                    length = 0
                    c = ""
                    if data2["id"] == data[0]["id"]:
                            start = int(data2["start"])
                            end = int(data2["end"])
                            length = end - start + 1
                            c = data2["seq_region_name"]
                    content_html = read_html_file("look.html").render(
                            context={"gene": "Gene: " + arguments["gene"][0],
                                "what": f"Info <p></p>Start: {start}<p></p>End: {end}<p></p>Length: {length}<p></p>Id: {data[0]["id"]}"
                                f"<p></p>Name of the chromosome: {c}"})
                    content_json["Gene"] = arguments["gene"][0]
                    content_json["Start"] = start
                    content_json["End"] = end
                    content_json["Length"] = length
                    content_json["Id"] = data[0]["id"]
                elif path == "/geneCalc" or "geneCalc" in arguments:
                    ENDPOINT = "/xrefs/symbol/homo_sapiens/" + arguments["gene"][0] + "?"
                    data = dat(ENDPOINT)
                    ENDPOINT2 = "/sequence/id/" + data[0]["id"]+ "?"
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
                    content_html = read_html_file("look.html").render(context={"gene": "Gene: " + arguments["gene"][0],
                            "what": f"Calculations <p></p>Length: {s.len()}<p></p> {"<p></p>".join(bases)}"})
                    content_json["Gene"] = arguments["gene"][0]
                    content_json["Calculations"] = {"Length": s.len(), "Bases": bases}
                elif path == "/geneList" or "geneList" in arguments:
                    ENDPOINT = f"/overlap/region/human/{arguments["chromo"][0]}:{arguments["start"][0]}-{arguments["end"][0]}?feature=gene;"
                    data = dat(ENDPOINT)
                    what = []
                    for a in data:
                        try:
                            what.append(f"{a["id"]}({a["external_name"]})")
                        except KeyError:
                            what.append(f"{a["id"]}()")
                    content_html = read_html_file("look.html").render(context={"gene": f"Chromosome: {arguments["chromo"][0]}, start: {arguments["start"][0]}, end: {arguments["end"][0]}",
                               "what": f"Gene(s): {"<p></p>".join(what)}"})
                    content_json["Chromosome"] = arguments["chromo"][0]
                    content_json["Start"] = arguments["start"][0]
                    content_json["End"] = arguments["end"][0]
                    content_json["Genes"] = what
                else:
                    content_html = Path('error.html').read_text()
                    type = "text/html"
                    error_code = 404
            except KeyError:
                error_code = 404
                content_html = Path('error.html').read_text()
                type = "text/html"


        if "json" in arguments and arguments["json"][0] == "1" and error_code != 404:
            contents = json.dumps(content_json)
        else:
            contents = content_html



        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', type)
        self.send_header('Content-Length', str(len(str.encode(contents))))

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