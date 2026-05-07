import http.client
import json
import termcolor
from Seqclass import Seq
PORT = 8080
SERVER = 'localhost'

def lst(title, data):
    termcolor.cprint(f"{title}:", "blue")
    for b in data:
        print(b)
def dct(title, data):
    termcolor.cprint(f"{title}:", "blue")
    for b in data:
        if type(data[b]) == list:
            lst(b, data[b])
        else:
            print(f"{b}: {data[b]}")

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
    exercise = url.split("?")[0][1:].capitalize()
    termcolor.cprint(f"\n{exercise}", "yellow")
    termcolor.cprint("CONTENT:", "magenta")
    for a in info:
        if type(info[a]) == list:
            lst(a, info[a])
            for c in info[a]:
                if type(c) == list:
                    lst(c, info[a][c])
        elif type(info[a]) == dict:
            dct(a, info[a])
        else:
            termcolor.cprint(a, "blue", end="")
            print(f": {info[a]}")