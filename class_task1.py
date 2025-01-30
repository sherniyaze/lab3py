class MyClass:
    def __init__(self):
        self.stringus = ""
        self.conditio = ""  
    def getstring(self):
        self.stringus = input()  
        if len(self.stringus) == 0:
            print("У тебя пустая строка! шуруй обратно!")
        else:
            self.conditio = input("Какие буквы? Большие или маленькие?")
    def printstring(self):
        if "пер" in self.conditio or "бір" in self.conditio or "caps" in self.conditio or "боль" in self.conditio or "1" in self.conditio:
            print(self.stringus.upper())  
        elif "втор" in self.conditio or "екі" in self.conditio or "no caps" in self.conditio or "не капс" in self.conditio or "маль" in self.conditio or "3" in self.conditio:
            print(self.stringus.lower())
        else:
            print(self.stringus.swapcase())




obj = MyClass()
obj.getstring() 
obj.printstring() 
