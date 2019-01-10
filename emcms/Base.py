class MyBase:
    s = "Niwat"
    def __init__(self,str):
        self.str = str
if __name__=="__main__":
    print ("main")
    mb = MyBase("Niwat")
    print(mb.s)
