#Email ve Parola bilgileri ile giriş kontrolü yapınız.

email = "ahmetelif@tugba.com"
sifre = "eslemzeynep"

girbir = input ("Lütfen Mail Adresi Giriniz :")
giriki = input ("Lütfen Şifre Giriniz :")


 if girbir==email:
     print("E-Mail Doğru!")

 else:
     girbir != email
     print("E-Mail Hatalı")

 if giriki == sifre:
     print("Şifre Doğru!")

 if giriki != sifre:
     print("Şifre Doğru Değil!")

 if girbir==email and giriki == sifre:
      print("Giriş Yapılıyor Lütfen Bekleyin....")
