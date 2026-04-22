import http.client
import json

server = "rest.ensembl.org"
endpoint = "/info/ping"
parameters = "?content-type=application/json"

url = server + endpoint + parameters

print()
print(f"Server: {server}")
print(f"URL: {url}")

connect = http.client.HTTPSConnection(server)
connect.request("GET", endpoint + parameters )

response = connect.getresponse()
data = json.loads(response.read().decode())
print(f"Response received!: {response.status} {response.reason}\n")
if data["ping"] == 1:
    print("ALIVE!")
