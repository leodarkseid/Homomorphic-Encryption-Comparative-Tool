import numpy as np
import pandas as pd

d = [{"id":2, "name":"Sfsf", "age":23},{"id":12, "name":"Sfsfsf", "age":243},{"id":22, "name":"Sfdsfasf", "age":324324}]

class Hu:
    def __init__(self) -> None:
        self.a = ''
        self.b = ''
        self.c = ''

    
 
s = pd.DataFrame(d)
s.set_index('id', inplace=True)

def ca():
    l = {}
    for i in range(2):
        x = Hu()
        x.a = 1
        x.b = 2
        x.c = 3
        l.append(x)
    fg = ([{"a":i.a, "b":i.b, "c":i.c} for i in l])
    tut = pd.DataFrame(fg)
    tut.set_index('a', inplace=True)
    print(tut)
   
   
# print(s)
# print(Hu.__dict__)

ca()