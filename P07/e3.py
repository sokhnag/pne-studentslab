
import http.client
import json
import termcolor

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
parameters = f"{genes["MIR633"]}?content-type=application/json"

url = server + endpoint + parameters
print()
print(f"Server: {server}")
print(f"URL: {url}")


connect = http.client.HTTPSConnection(server)
connect.request("GET", endpoint + parameters )
response = connect.getresponse()
data = json.loads(response.read().decode())

print(f"Response received!: {response.status} {response.reason}\n")
print()
print(f"{termcolor.colored("Gene", "yellow")}: MIR633")
print(f"{termcolor.colored("Description", "yellow")}: {data["desc"]}")
print(f"{termcolor.colored("Bases", "yellow")}: {data["seq"]}")

