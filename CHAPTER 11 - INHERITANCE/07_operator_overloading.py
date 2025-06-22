class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)    #PYTHON ME SAB KUVH HI CLASS HOTA HE , JAB HM TYPE NIKALTE HE KISI KA BHI TO CLASS INT, CLASS TUPLE, CLASS LIST AISA HI TO AATA HE