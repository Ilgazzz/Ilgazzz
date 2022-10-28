while 1 == 1:
 print('Bir derecenin radyan cinsini ve esas ölçüsünü bulmak için \"d\",')
 print('bir radyanın derece cinsini ve esas ölçüsünü için \"r\" yazınız')
 anahtar = input()
 import fractions
 if anahtar == "d":
   print("Lütfen bir derece giriniz.")
   drc = int(input())
   drc = drc - (drc // 360) * 360
   rdy = fractions.Fraction(drc,180)
   print("Radyan cinsinden: " + str(rdy) + "π")
   print("Esas ölçüsü: " + str(drc))
 elif anahtar == "r":
   print("Lüfen bir radyan giriniz. π'yi yazmanıza gerek yoktur.")
   rdy = input()
   for i in range(0, len(rdy)):
       if rdy[i] == "/":
           pay = rdy[0:i]
           payda = rdy[i + 1:len(rdy)]
           break
       else:
           pay = rdy
           payda = 1
   rdy = fractions.Fraction(int(pay),int(payda))
   pay = rdy.numerator
   payda = rdy.denominator
   if abs(pay) >= abs(payda) * 2:
    rdy = fractions.Fraction((pay % (payda * 2)), payda)
   if rdy < 0:
    rdy = rdy + 2
   drc = float(rdy) * 180
   drc = drc - (drc // 360) * 360
   print("Derece cinsinden: " + str(drc))
   print("Esas ölçüsü: " + str(rdy) + " π")
 elif anahtar == "çıkış":
   1 / 0
 else:
   print("hata")


