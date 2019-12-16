"""How To Play?
Caranya hampir sama seperti game tictactoe pada umumnya,ada team X juga team O.Pada game ini team X
mempunyai 4 sektor berupa 1-4,sedangkan sektor team O adalah 6-9.Setiap team X melakukakan fungsi untuk
mengambil sektor maka ada dua hal yg akan terjadi (Valu pada sektor tersebut akan bertambah,dan sektor
tersebut akan jadi milik team X).Dan jika team O melakukan fungsi maka akan terjadi(value pada sektor
tersebut akan berkurang,dan sektor tersebut akan jadi milik team O).Pemenang ialah yg berhasil memiliki 
3 sektor dgn value yg sama dan membentuk pola polygon 1 garis(*).Tembahan untuk tanda( ☺ )yg berada ditengah
-tengah board,kami menyebutnya joker 'sesuatu yg bisa jadi apapun'"""

invar = 2
turn = "x"
a = 1
b = 2 
c = 3
d = 4
e = "☺"
f = "6"
g = "7"
h = "8"
i = "9"
def main():
    print("|"+str(a)+"|"+str(b)+"|"+str(c)+"|")
    print("|"+str(d)+"|"+str(e)+"|"+str(f)+"|")
    print("|"+str(g)+"|"+str(h)+"|"+str(i)+"|")

def ready(x):
    if a == b == c:
        x = 1
        if b == int(b):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x    
    if g == h == i:
        x = 1
        if h == int(h):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if a == d == g:
        x = 1
        if d == int(d):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x  
    if c == f == i:
        x = 1
        if f == int(f):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if d == f:
        x = 1
        if d == int(d):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x    
    if b == h:
        x = 1
        if b == int(b):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if a == i:
        x = 1
        if a == int(a):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x  
    if g == c:
        x = 1
        if g == int(g):
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x  
        
main()
while ready(0) != 1:            

    npush = input(turn + " Turn : ")

    if npush == "a":
        if a == int(a) and turn == "x":
            a += 1
            turn = "o"
        elif a == int(a) and turn == "o":
            a -= 1
            a = str(a)
            turn = "x"
        elif a == str(a) and turn == "o":
            a = int(a)
            a -= 1
            a = str(a)
            turn = "x"
        else:
            a = int(a)
            a += 1
            turn = "o"

    if npush == "b":
        if b == int() and turn == "x":
            b += 1
            turn = "o"
        elif b == int(b) and turn == "o":
            b -= 1
            b = str(b)
            turn = "x"
        elif b == str(b) and turn == "o":
            b = int(b)
            b -= 1
            b = str(b)
            turn = "x"
        else:
            b = int(b)
            b += 1
            turn = "o"        
    if npush == "c":
        if c == int(c) and turn == "x":
            c += 1
            turn = "o"
        elif c == int(c) and turn == "o":
            c -= 1
            c = str(c)
            turn = "x"
        elif c == str(c) and turn == "o":
            c = int(c)
            c -= 1
            c = str(c)
            turn = "x"
        else:
            c = int(c)
            c += 1
            turn = "o"

    if npush == "d":
        if d == int(d) and turn == "x":
            d += 1
            turn = "o"
        elif d == int(d) and turn == "o":
            d -= 1
            d = str(d)
            turn = "x"
        elif d == str(d) and turn == "o":
            d = int(d)
            d -= 1
            d = str(d)
            turn = "x"
        else:
            d = int(a)
            d += 1
            turn = "o"        
    
    if npush == "e":
        print("Created by = SumCode")
      
    if npush == "f":
        if f == int(f) and turn == "x":
            f += 1
            turn = "o"
        elif f == int(f) and turn == "o":
            f -= 1
            f = str(f)
            turn = "x"
        elif f == str(f) and turn == "o":
            f = int(f)
            f -= 1
            f = str(f)
            turn = "x"
        else:
            f = int(f)
            f += 1
            turn = "o"
    
    if npush == "g":
        if g == int(g) and turn == "x":
            g += 1
            turn = "o"
        elif g == int(g) and turn == "o":
            g -= 1
            g = str(g)
            turn = "x"
        elif g == str(g) and turn == "o":
            g = int(g)
            g -= 1
            g = str(g)
            turn = "x"
        else:
            g = int(g)
            g += 1
            turn = "o"
    
    if npush == "h":
        if h == int(h) and turn == "x":
            h += 1
            turn = "o"
        elif h == int(h) and turn == "o":
            h -= 1
            h = str(h)
            turn = "x"
        elif h == str(h) and turn == "o":
            h = int(h)
            h -= 1
            h = str(h)
            turn = "x"
        else:
            h = int(h)
            h += 1
            turn = "o"
    
    if npush == "i":
        if i == int(i) and turn == "x":
            i += 1
            turn = "o"
        elif i == int(i) and turn == "o":
            i -= 1
            i = str(i)
            turn = "x"
        elif i == str(i) and turn == "o":
            i = int(i)
            i -= 1
            i = str(i)
            turn = "x"
        else:
            i = int(i)
            i += 1
            turn = "o"
    main()


            
    
