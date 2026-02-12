text = "  Hello, world! welcome to python programming.  "

print(f"Stripped: {text.strip()}\n"
        f"Word count: {len(text.strip().split(" "))} \n"
        f"Title case: {text.title()} \n"
        f"Starts with Hello: {text.strip().startswith(("Hello"))} \n"
        f"Ends with ing.: {text.strip().endswith(("ing."))} \n"
        f"Python position: {text.strip().find("Python")} \n"
        f"Joined: {"-".join(text.strip().split(" "))}\n")
