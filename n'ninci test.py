#Fonksiyon
def örüntü(a,b,c):
    for i in range(0,c):
        print(a * i + b, end=", ")

#Arayüz
print("Görmek istediğiniz örüntüyü \"an + b\" biçiminde giriniz.")
ab = input()
print("Kaçıncı terimine kadar görmek istiyorsunuz?")
c = int(input())
#Zor kısım
a = ""
b = ""
z = 0
y = 0
for i in range(z,len(ab)):
    if str.isdigit(ab[i]):
        z = i
        break
    else:
        pass
for i in range(z,len(ab)):
    if str.isdigit(ab[i]):
        pass
    else:
        a = int(ab[0:i])
        z = int(i)
        break
for i in range(z,len(ab)):
    if str.isdigit(ab[i]):
        z = i
        break
    else:
        pass
for i in range(z,len(ab)+1):
    if str.isdigit(ab):
        pass
    else:
        y = i
b = int(ab[z:y])

#örüntü
örüntü(a,b,c)