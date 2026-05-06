import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
urls = ["/listSpecies?limit=10",
"/listSpecies?",
"/karyotype?species=mouse",
"/karyotype?species=Shrew+mouse",
"/chromosomeLength?species=mouse&chromo=18",
"/geneLookup?gene=FRAT1",
"/geneSeq?gene=FRAT1",
"/geneInfo?gene=FRAT1",
"/geneCalc?gene=FRAT1",
"/geneList?chromo=9&start=22125500&end=22136000"]

for url in urls:
    try:
        conn.request("GET", url + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    response = conn.getresponse()

    data1 = response.read().decode("utf-8")

    info = json.loads(data1)

    termcolor.cprint(url.split("?")[0][1:].capitalize(), "yellow")
    print(f"CONTENT: {info}")
