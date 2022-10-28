#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import random


# In[39]:


print("""[Atan kişi]: [Atış sayısı]d[Yüz sayısı] [komutlar]

(/ * - +) # zarların toplamına girilen işlemi uygular.
e# girilen sayı ve üstü çıkarsa tekrar atar ve toplamı yazar.
ie# girilen sayı ve üstü çıkmayana kadar tekrar atar ve toplamı yazar.
r# girilen sayı ve üstü çıkarsa tekrar atar.
ir# girilen sayı çıkmayana kadar tekrar atar.
t# girilen sayı ve üstüne çıkan zar başarı puanı 1 arttırır.
f# girilen sayı ve altına inen zar başarı puanını 1 azaltır.
k# girilen sayı kadar en yüksek değerli zarı tutar.
kl# girilen sayı kadar en düşük değerli zarı tutar.\n""")


# In[12]:


class Zar:
    def __init__(self, atanKişi, atışSayısı, yüzSayısı, özellikler, özellikSayısı, yorum):
        self.ak = atanKişi
        self.ats = atışSayısı
        self.ys = yüzSayısı
        self.ö = özellikler
        self.ös = özellikSayısı
        self.y = yorum
    def at(self):
        çıktılar = []
        ösi = 0
        toplam = 0
        tsayaç = 0
        for sonuç in range(0,self.ats):
            çıktılar.append(random.randint(1,self.ys))
        print(self.ak + " zar atıyor:")
        print(str(çıktılar))
        print()
        if self.ö != None:
            for özellik in self.ö:
                if özellik == "/" :
                    if toplam == 0:
                        for çıktı in çıktılar:
                            toplam = toplam + çıktı
                        toplam = toplam / int(self.ös[ösi])
                        print(str(çıktılar) + " " + özellik + " " + self.ös[ösi])
                        print("= " + str(toplam))
                        print()
                    else:
                        print(str(toplam), end=" ")
                        toplam = toplam / int(self.ös[ösi])
                        print(özellik + " " + self.ös[ösi] + " = " + str(toplam))
                        print()
                if özellik == "*" :
                    if toplam == 0:
                        for çıktı in çıktılar:
                            toplam = toplam + çıktı
                        toplam = toplam * int(self.ös[ösi])
                        print(str(çıktılar) + " " + özellik + " " + self.ös[ösi])
                        print("= " + str(toplam))
                        print()
                    else:
                        print(str(toplam), end=" ")
                        toplam = toplam * int(self.ös[ösi])
                        print(özellik + " " + self.ös[ösi] + " = " + str(toplam))
                        print()
                if özellik == "-" :
                    if toplam == 0:
                        for çıktı in çıktılar:
                            toplam = toplam - çıktı
                        toplam = toplam / int(self.ös[ösi])
                        print(str(çıktılar) + " " + özellik + " " + self.ös[ösi])
                        print("= " + str(toplam))
                        print()
                    else:
                        print(str(toplam), end=" ")
                        toplam = toplam - int(self.ös[ösi])
                        print(özellik + " " + self.ös[ösi] + " = " + str(toplam))
                        print()
                if özellik == "+" :
                    if toplam == 0:
                        for çıktı in çıktılar:
                            toplam = toplam + çıktı
                        toplam = toplam + int(self.ös[ösi])
                        print(str(çıktılar) + " " + özellik + " " + self.ös[ösi])
                        print("= " + str(toplam))
                        print()
                    else:
                        print(str(toplam), end=" ")
                        toplam = toplam + int(self.ös[ösi])
                        print(özellik + " " + self.ös[ösi] + " = " + str(toplam))
                        print()
                if özellik == "e":
                    print("Patlama sayısı(sınırlı) " + self.ös[ösi])
                    for çıktı in e(çıktılar, self.ös[ösi], self.ys):
                        toplam = toplam + çıktı
                    print("Yeni değerler " + str(çıktılar))
                    print("= " + str(toplam))
                    print()
                if özellik == "ie":
                    print("Patlama sayısı(sınırsız) " + self.ös[ösi])
                    for çıktı in ie(çıktılar, self.ös[ösi], self.ys):
                        toplam = toplam + çıktı
                    print("Yeni değerler " + str(çıktılar))
                    print("= " + str(toplam))
                    print()
                if özellik == "k":
                    çıktılar.sort(reverse = True)
                    print("En yüksek " + self.ös[ösi] + " tutuldu.", end=" ")
                    çıktılar = çıktılar[:int(self.ös[ösi])]
                    print(çıktılar)
                    print()
                if özellik == "r":
                    print("Tekrar atış(sınırlı) sayısı " + self.ös[ösi] + ". Yeni değerler " + str(r(çıktılar, self.ös[ösi], self.ys)))
                    print()
                if özellik == "ir":
                    print("Tekrar atış(sınırsız) yeni değerler " + self.ös[ösi] + ". Yeni değerler" + str(ir(çıktılar, self.ös[ösi], self.ys)))
                    print()
                if özellik == "t":
                    for çıktı in çıktılar:
                        if çıktı >= int(self.ös[ösi]):
                            tsayaç = tsayaç + 1
                    print("hedef sayı " + self.ös[ösi])
                    print("Başarı sayısı " + str(tsayaç))
                    print()
                if özellik == "f":
                    for çıktı in çıktılar:
                        if çıktı <= int(self.ös[ösi]):
                            tsayaç = tsayaç - 1
                    print("hedef sayı " + self.ös[ösi])
                    print("Başarı sayısı " + str(tsayaç))
                    print()
                if özellik == "kl":
                    çıktılar.sort()
                    print("En düşük " + self.ös[ösi] + " tutuldu.", end=" ")
                    çıktılar = çıktılar[:int(self.ös[ösi])]
                    print(çıktılar)
                    print()
                ösi = ösi + 1
            print("Son zar durumu " + str(çıktılar))
            print("Son toplam " + str(toplam))
            print("Son başarı sayısı " + str(tsayaç))
            print()
        if yorum != None:
            print(yorum)


# In[4]:

    while True:
        girdi = input()
        while (re.search(r".+:\s\d+d\d+\s(((/|\*|-|\+)\d+)|((e|ie|k|r|ir|kl|t|f)\d+)|!.+)|(\w|\s)+:\s\d+d\d+", girdi)) == None:
            print("Lütfen geçerli bir komut giriniz.")
            girdi = input()


# In[5]:


    atanKişi = girdi[:re.search(r".+:", girdi).end()-1]
    atışSayısı = int(re.findall(r"\d+", girdi)[0])
    yüzSayısı = int(re.findall(r"\d+", girdi)[1])
    özellikler = None
    özellikSayısı = None
    yorum = None


# In[11]:


    try:
        yorum = re.findall(r"\s!.+", girdi)[0][2:]
    except:
        pass
    else:
        yorum = re.findall(r"\s!.+", girdi)[0][2:]
        ünlemYeri = re.search("!",girdi).start()
        if len(re.findall(r"\d+", girdi)) > 2:
            özellikler = re.findall(r"\s(e|ie|k|{kl}|r|ir|t|f|\*|\+|-|/)", girdi[:ünlemYeri])[0:]
            özellikSayısı = re.findall(r"\d+", girdi[:ünlemYeri])[2:]
            if len(re.findall(r"\d+", girdi)) > 2:
                özellikler = re.findall(r"\s(e|ie|k|{kl}|r|ir|t|f|\*|\+|-|/)", girdi)[0:]
                özellikSayısı = re.findall(r"\d+", girdi)[2:]


# In[13]:


    def ir(liste, hedef, tavan):
            for i in range(0,len(liste)):
                if liste[i] <= int(hedef):
                    liste[i] = random.randint(1,tavan)
                    ir(liste, hedef, tavan)
                    return liste
            
            def r(liste, hedef, tavan):
                for i in range(0,len(liste)):
                    if liste[i] <= int(hedef):
                        liste[i] = random.randint(1,tavan)
                        return liste
    
    def ie(liste, hedef, tavan):
            for i in range(0,len(liste)):
                if liste[i] >= int(hedef):
                    liste[i] = random.randint(1,tavan)
                    ie(liste, hedef, tavan)
                    return liste
    
    def e(liste, hedef, tavan):
            for i in range(0,len(liste)):
                if liste[i] >= int(hedef):
                    liste[i] = random.randint(1,tavan)
                    return liste
            

# In[15]:


    zar = Zar(atanKişi, atışSayısı, yüzSayısı, özellikler, özellikSayısı, yorum)


# In[36]:


   print(zar.at())

