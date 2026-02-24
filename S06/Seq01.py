import termcolor

termcolor.cprint("Hey! this is printed in magenta!", 'magenta')

class Seq:
    """A class for representing sequences"""
    def __init__(self , attribute1):
        self.attribute1 = attribute1


    def method_name(self , parameter):
        pass

    def __str__(self):
        return self.attribute1

    def len(self):
        return len(self.attribute1)

class Gene(Seq):
    """This class is derived from the Seq S06
       All the objects of class Gene will inherit
       the methods from the Seq class
    """
    def __init__(self, attrib, name=""):
        # -- Call first the Seq initializer and then the
        # -- Gene init method
        super().__init__(attrib)
        self.name = name


# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
gene = Gene("AGTCGAT" , "FRAT1")
print(f"Sequence 1: {s1} \nlength: {s1.len()}\nGene and name: {gene} , {gene.name}\nLength: {gene.len()}")