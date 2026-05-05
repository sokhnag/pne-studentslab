try:
    contents = read_html_file("ka.html").render(
        context={"todisplay": "<p></p>".join(data["karyotype"]), "number": f"Species: {arguments["species"][0]}"})
except KeyError:
    contents = Path('error.html').read_text()