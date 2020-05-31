#Soru : Kullanıcıdan İki vize notu alıp bir de final notu alın ve ortalamasını çıkartın.Ekrana geçti ise geçti
#kaldı ise kaldır yazdırın!


 vizebir = int(input ("İlk Vize Notunuzu Giriniz :"))
 vizeiki = int(input ("İkinci Vize Notunuzu Giriniz :"))
 final   = int(input ("Lütfen Final Notunuzu Giriniz :"))

 hesaplama = vizebir + vizeiki + final  / 3
 if hesaplama > 50:
     print ("Geçtiniz !")

 if hesaplama < 50:
    print ("Kaldınız Malesef !")
