def tipuri_de_date():
    x=5
    y=10
    z= "MAP"
    print(type(x), "",type(y),"",type(z))

def verificare_numere():
    x=5
    y=10
    if x>y:
        print("X>Y")
    else:
        print("Y>X")

def tuplu():
    black_friday = ["emag","altex","flaco"]
    e,a,f = black_friday
    print(e,"",a,"",f)

def interpolare():
    x=2
    text= "lorem ipsum {}"
    print(text.format(x))

interpolare()
# tuplu()

#verificare_numere()