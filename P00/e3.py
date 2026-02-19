from Seq0 import seq_len

print("-----| Exercise 3 |------")
for a in ["U5", "ADA" , "FRAT1", "FXN"]:
    print(f"Gene {a} ---> long.: {seq_len(f"sequences/{a}.txt")}")


