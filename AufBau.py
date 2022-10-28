# AufBau
n = ""
def aufbau():
    for i in range(1, 8):
        if e == 0:
            break
        global n
        n = str(i)
        if i == 1:
            print(n + "s" + str(s(e)), end="")
        elif i == 2 or i == 3:
            print(" " + n + "s" + str(s(e)), end="")
            if ptest(e) == 0:
                break
            print(" " + n + "p" + str(p(e)), end="")
        elif i == 4 or i == 5:
            print(" " + n + "s" + str(s(e)), end="")
            if dtest(e) == 0:
                break
            print(" " + str(i-1) + "d" + str(d(e)), end="")
            if ptest(e) == 0:
                break
            print(" " + n + "p" + str(p(e)), end="")
        elif i == 6 or i == 7:
            print(" " + n + "s" + str(s(e)), end="")
            if ftest(e) == 0:
                break
            print(" " + str(i-2) + "f" + str(f(e)), end="")
            if dtest(e) == 0:
                break
            print(" " + str(i-1) + "d" + str(d(e)), end="")
            if ptest(e) == 0:
                break
            print(" " + n + "p" + str(p(e)), end="")

#Kısaltma
def kısaltma():
    global e2
    global n
    if e2 == 0:
        pass
    elif e2 == 1:
        n = 1
        print(str(n) + "s" + str(s2(e2)), end="")
    elif e2 == 2:
        print("[He]")
    elif 2 < e2 and e2 < 10:
        e2 = e2 -2
        n = 2
        print("[He]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    elif e2 == 10:
        print("[Ne]")
    elif 10 < e2 and e2 < 18:
        n = 3
        e2 = e2 - 10
        print("[Ne]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    elif e2 == 18:
        print("[Ar]")
    elif 18 < e2 and e2 < 36:
        e2 = e2 - 18
        n = 4
        print("[Ar]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if dtest(e2) == 0:
            pass
        else:
            print(" " + str(n - 1) + "d" + str(d2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    elif e2 == 36:
        print("[Kr]")
    elif 36 < e2 and e2 < 54:
        e2 = e2 - 36
        n = 5
        print("[Kr]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if dtest(e2) == 0:
            pass
        else:
            print(" " + str(n - 1) + "d" + str(d2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    elif e2 == 54:
        print("[Xe]")
    elif 54 < e2 and e2 < 86:
        e2 = e2 - 54
        n = 6
        print("[Xe]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if ftest(e2) == 0:
            pass
        else:
            print(" " + str(n - 2) + "f" + str(f2(e2)), end="")
        if dtest(e2) == 0:
            pass
        else:
            print(" " + str(n - 1) + "d" + str(d2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    elif e2 == 86:
        print("[Rn]")
    elif 86 < e2 and e2 < 118:
        e2 = e2 - 86
        n = 7
        print("[Rn]" + " " + str(n) + "s" + str(s2(e2)), end="")
        if ftest(e2) == 0:
            pass
        else:
            print(" " + str(n - 2) + "f" + str(f2(e2)), end="")
        if dtest(e2) == 0:
            pass
        else:
            print(" " + str(n - 1) + "d" + str(d2(e2)), end="")
        if ptest(e2) == 0:
            pass
        else:
            print(" " + str(n) + "p" + str(p2(e2)), end="")
    else:
        print("[Og]")

# s orbitali
def s(esayısı):
    global e
    global n
    if e == 0:
        return e
    e = e - 2
    if e > 0:
        if (dtest(e) == 4 or dtest(e) == 9) and (int(n) == 4 or int(n) == 5):
            e = e + 1
            return 1
        return 2
    if e < 2:
        x = e
        e = 0
        return x + 2

# p orbitali
def p(esayısı):
    global e
    if e == 0:
        return e
    e = e - 6
    if e > 0:
        return 6
    if e < 6:
        x = e
        e = 0
        return x + 6

# d orbitali
def d(esayısı):
    global e
    if e == 0:
        return e
    e = e - 10
    if e > 0:
        return 10
    if e < 10:
        x = e
        e = 0
        return x + 10

# f orbitali
def f(esayısı):
    global e
    if e == 0:
        return e
    e = e - 14
    if e > 0:
        return 14
    if e < 14:
        x = e
        e = 0
        return x + 14

# p test
def ptest(esayısı):
    if esayısı == 0:
        return esayısı
    esayısı = esayısı - 6
    if esayısı > 0:
        return 6
    if esayısı < 6:
        x = esayısı
        esayısı = 0
        return x + 6
# d test
def dtest(esayısı):
    if e == 0:
        return esayısı
    esayısı = esayısı - 10
    if esayısı > 0:
        return 10
    if esayısı < 10:
        x = esayısı
        esayısı = 0
        return x + 10

# f test
def ftest(esayısı):
    if esayısı == 0:
        return esayısı
    esayısı = esayısı - 14
    if esayısı > 0:
        return 14
    if esayısı < 14:
        x = esayısı
        esayısı = 0
        return x + 14

# s orbitali2
def s2(esayısı):
    global e2
    global n
    if e2 == 0:
        return e2
    e2 = e2 - 2
    if e2 > 0:
        if (dtest(e2) == 4 or dtest(e2) == 9) and (int(n) == 4 or int(n) == 5):
            e2 = e2 + 1
            return 1
        return 2
    if e2 < 2:
        x = e2
        e2 = 0
        return x + 2

# p orbitali2
def p2(esayısı):
    global e2
    if e2 == 0:
        return e2
    e2 = e2 - 6
    if e2 > 0:
        return 6
    if e2 < 6:
        x = e2
        e2 = 0
        return x + 6

# d orbitali2
def d2(esayısı):
    global e2
    if e2 == 0:
        return e2
    e2 = e2 - 10
    if e2 > 0:
        return 10
    if e2 < 10:
        x = e2
        e2 = 0
        return x + 10

# f orbitali2
def f2(esayısı):
    global e2
    if e2 == 0:
        return e2
    e2 = e2 - 14
    if e2 > 0:
        return 14
    if e2 < 14:
        x = e2
        e2 = 0
        return x + 14

while 1 == 1:
    print("Konfigürasyonunu bulmak istediğiniz atomun numarası:", end=" ")
    e = int(input())
    e2 = e
    aufbau()
    print("")
    kısaltma()
    print("")