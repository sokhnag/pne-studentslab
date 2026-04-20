import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq
from certifi import contents

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

sequences = ["AGTGATAGATAGTC", "CAGTCGACGTCATG", "AGCTGACGTCGCGCGCGCG", "AGGAGAAGGAGGTGTGTG", "GACTAGCGT"]

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        global res
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/" :
            contents = Path('html/index.html').read_text()
        elif path == "/myserver" and "N" in arguments:
            number = int((arguments["number"])[0])
            contents = read_html_file("get.html").render(context={"todisplay": sequences[number], "number": number })
        elif path == "/myserver" and "G" in arguments:
            genename = (arguments["gene"])[0]
            geneseq = Seq()
            contents = read_html_file("gene.html").render(context={"todisplay": geneseq.read_fasta(f"sequences/{genename}.txt"), "seq": genename })
        elif path == "/myserver" and "OP" in arguments:
            seq = Seq(arguments["seq"][0])
            op = arguments["op"][0]
            if op == "Info":
                bases = []
                for a in seq.count_base().split(", "):
                    if seq.len() != 0:
                        bases.append(f"{a} ({str(round(int(a.split(" : ")[1]) / seq.len() * 100, 2))}%)")
                    else:
                        bases.append(f"{a} (0%)")
                res = f"Sequence: {seq}<p><p>Total lenght: {str(seq.len())} <p><p>{"<p><p>".join(bases)}"

            elif op == "Comp":
                res = seq.complement()
            elif op == "Rev":
                res = seq.reverse()
            contents = read_html_file("operation.html").render(
                context={"seq": seq, "op": op , "res": res})
        elif path == "/myserver" and "P" in arguments:
            contents = Path('html/ping.html').read_text()
        else:
            contents = Path('html/error.html').read_text()

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
