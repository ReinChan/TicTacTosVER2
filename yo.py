invar = 2
turn = "x"
a = 8
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
def main():
    print("|"+str(a)+"|"+str(b)+"|"+str(c)+"|")
    print("|"+str(d)+"|"+str(e)+"|"+str(f)+"|")
    print("|"+str(g)+"|"+str(h)+"|"+str(i)+"|")

def ready(x):
    if a == b == c:
        x = 1
        if a == int(a):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x    

while ready(0) != 0:            
    main()
    npush = input(turn + " Turn : ")

    if npush == "a":
        if a == int(a) and turn == "x":
            a += 1
            turn = "o"
        elif a == int(a) and turn == "o":
            int(a)
            if a != 0:
                a -= 1
            else:
                a += 1
            str(a)
            turn = "x"
        elif a == str(a) and turn == "o":
            int(a)
            a += 1
            str(a)
            turn = "x"
        else:
            int(a)
            if a != "0":
                a -= 1
            else:
                a += 1
            turn = "o"

    if npush == "b":
        if b == int() and turn == "x":
            b += 1
            turn = "o"
        elif b == int(b) and turn == "o":
            int(b)
            b -= 1
            str(b)
            turn = "x"
        elif b == str(b) and turn == "o":
            int(b)
            b += 1
            str(b)
            turn = "x"
        else:
            int(b)
            b -= 1
            turn = "o"        
    if npush == "c":
        if c == int(c) and turn == "x":
            c += 1
            turn = "o"
        elif c == int(c) and turn == "o":
            int(c)
            c -= 1
            str(c)
            turn = "x"
        elif c == str(c) and turn == "o":
            int(c)
            c += 1
            str(c)
            turn = "x"
        else:
            int(c)
            c -= 1
            turn = "o"

    if npush == "d":
        if d == int(d) and turn == "x":
            d += 1
            turn = "o"
        elif d == int(d) and turn == "o":
            int(d)
            d -= 1
            str(d)
            turn = "x"
        elif d == str(d) and turn == "o":
            int(d)
            d += 1
            str(d)
            turn = "x"
        else:
            int(a)
            a -= 1
            turn = "o"        
    
    if npush == "e":
        if e == int(e) and turn == "x":
            e += 1
            turn = "o"
        elif e == int(e) and turn == "o":
            int(e)
            e -= 1
            str(e)
            turn = "x"
        elif e == str(e) and turn == "o":
            int(e)
            e += 1
            str(e)
            turn = "x"
        else:
            int(e)
            e -= 1
            turn = "o"
      
    if npush == "f":
        if f == int(f) and turn == "x":
            f += 1
            turn = "o"
        elif f == int(f) and turn == "o":
            int(f)
            f -= 1
            str(f)
            turn = "x"
        elif f == str(f) and turn == "o":
            int(f)
            f += 1
            str(f)
            turn = "x"
        else:
            int(f)
            f -= 1
            turn = "o"
    
    if npush == "g":
        if g == int(g) and turn == "x":
            g += 1
            turn = "o"
        elif g == int(g) and turn == "o":
            int(g)
            g -= 1
            str(g)
            turn = "x"
        elif g == str(g) and turn == "o":
            int(g)
            g += 1
            str(g)
            turn = "x"
        else:
            int(g)
            g -= 1
            turn = "o"
    
    if npush == "h":
        if h == int(h) and turn == "x":
            h += 1
            turn = "o"
        elif h == int(h) and turn == "o":
            int(h)
            h -= 1
            str(h)
            turn = "x"
        elif h == str(h) and turn == "o":
            int(h)
            h += 1
            str(h)
            turn = "x"
        else:
            int(h)
            h -= 1
            turn = "o"
    
    if npush == "i":
        if i == int(i) and turn == "x":
            i += 1
            turn = "o"
        elif i == int(i) and turn == "o":
            int(i)
            i -= 1
            str(i)
            turn = "x"
        elif i == str(i) and turn == "o":
            int(i)
            i += 1
            str(i)
            turn = "x"
        else:
            int(i)
            i -= 1
            turn = "o"


            
    
