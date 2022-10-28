"""a = 0
girdi = input()
S = int(input())
for i in girdi:
    a = ord(i) + S
    print(chr(a),end="")"""
for i in range(0,110000):
    try:
        print(i, ":", chr(i))
    except:
        print(i, ":", "hata")
