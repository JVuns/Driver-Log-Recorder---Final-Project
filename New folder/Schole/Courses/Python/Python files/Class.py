class Hammer:
    #constructor method
    def __init__(self,mat):
        self.material = mat
    #method
    def printer(self):
        print("yes I am made of " + self.material)

#instantiation
my_hammer = Hammer("titanium")
our_hammer = Hammer("Comm")

#call methods
our_hammer.printer()

#getting attributes
print(our_hammer.material)