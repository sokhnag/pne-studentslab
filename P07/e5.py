import termcolor
import json
from Seq1 import Seq
import http.client

genes = {"FRAT1": "ENSG00000165879",
         "ADA" : "ENSG00000196839",
        "FXN" : "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633" : "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP":"ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052" ,
         "ANK2" : "ENSG00000145362" }

server = "rest.ensembl.org"
endpoint = "/sequence/id/"
for gene in genes:
    parameters = f"{genes[gene]}?content-type=application/json"

    url = server + endpoint + parameters
    print()
    print(f"Server: {server}")
    print(f"URL: {url}")


    connect = http.client.HTTPSConnection(server)
    connect.request("GET", endpoint + parameters )
    response = connect.getresponse()
    res = response.read().decode()
    data = json.loads(res)
    print(f"Response received!: {response.status} {response.reason}\n")
    print(f"{termcolor.colored("Gene", "yellow")}: {gene}")
    print(f"{termcolor.colored("Description", "yellow")}: {data["desc"]}")
    seq = Seq(data["seq"])
    print(f"{termcolor.colored("Total length", "yellow")}: {seq.len()}")
    bases = []
    mx = 0
    b = None
    for a in seq.count_base().split(", "):
        base = (a.split(" : ")[0])
        if seq.len() != 0:
            n = int(a.split(" : ")[1])
            if n > mx:
                mx = n
                b = base
            bases.append(f"{termcolor.colored(base, "blue")}: {n} ({str(round(n / seq.len() * 100, 2))}%)")
        else:
            bases.append(f"{termcolor.colored(a, "blue")} (0%)")
    print("\n".join(bases))
    print(f"{termcolor.colored("Most common base", "yellow")}: {b}")

