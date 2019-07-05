class SampleClass:
    def __init__(self,id):
        self.id = id

    def getString(self):
        inp = input("Class function to get the input; type something:")
        return inp

    def printString(self,toPrint):
        print(str(toPrint))
        return