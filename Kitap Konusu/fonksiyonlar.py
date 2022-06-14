"""Dosya yolu belirt"""
import time
import os

def yeni_kitap_olustur():
    kitap_olustur=input("Kitap Adını Giriniz: ".upper())+".txt"#oluşturmak istenilen dosya adı alınır +".txt" ile metin belgesine çevrilir.
    print("Dosya Oluşturuluyor...")
    dosya= open(kitap_olustur,"x",encoding="utf-8") #"x" modülü ile yeni dosya oluşturulur, encoding ile türkçe karakter tanımlanır ve bunlar DOSYA denilen bir değişkene atanır.
    time.sleep(0.5)
    print("\t****Dosya Oluşturuldu****")
    dosya=open(kitap_olustur,"w",encoding="utf-8")#Bu kısımda oluşturulan dosyaya (metin belgesine) "w" modülü ile notlar eklenir.
    icerik=input("Kitap Hakkındaki Notlarınızı Giriniz: ")
    print("İçerik Ekleniyor...")
    dosya.write(icerik)#Dosyaya içerik eklenir.
    time.sleep(0.5)
    print("\t****İçerik Eklendi****")
    dosya.close() #Dosya kapatılır.

def icerik_ekle(): #Daha önce açılan dosyaya yeni notlar ekleme fonksiyonu
    kitaba_eris=input("Erişmek İstediğiniz Kitap Adını Giriniz: ".upper())+".txt"#Halihazırda olan dosya adı alınır
    print("{} adlı Kitap Sorgulanıyor...".format(kitaba_eris))
    if os.path.isfile(kitaba_eris):#Girilen dosya adı ile daha önce dosya açılmış mı kontrolünü yapar
        time.sleep(0.5)
        print("\t****{} adlı kitap bulundu.****".format(kitaba_eris))
        dosya_eris=open(kitaba_eris,"a",encoding="utf-8")#Eğer daha önce aynı ad ile dosya oluşturulduysa bu bloğa girer ve "a" metoduyla metnin sonuna not ekler
        not_ekle=input("Kitap Hakkındaki Eklemek İstediğiniz Notları Girin: ")
        print("{} adlı kitaba girilen içerik ekleniyor...".format(kitaba_eris))
        dosya_eris.write(not_ekle)
        time.sleep(0.5)
        print("\t****İçerik Eklendi****")
        dosya_eris.close()#Dosya kapatılır
    else:
        print("{} adlı kitap bulunamadı".format(kitaba_eris))
        while True:
            islem=input("\t Yeni bir dosya Oluşturmak İster Misiniz (E/H): ")#Eğer girilen dosya adıyla bir dosya bulunmadıysa Yeni bir dosya açmak için izin ister.
            print("Sadece E ya da H karakterlerinden birini giriniz: ")
            if (islem=="E") or (islem=="e"):#E ye basılırsa 
                    print("\t\t{} Adlı Yeni Kitap Oluşturuluyor...".format(kitaba_eris))
                    time.sleep(0.5)
                    yeni_kitap_olustur()#bu fonksiyon çalıştırılır
                    print("\t\t\t*** {} Adlı Yeni Kitap Oluşturuldu***".format(kitaba_eris))
                    break
            elif(islem=="H") or (islem=="h"):
                    print("Dosya oluşturma işlemi İptal Ediliyor...")
                    time.sleep(0.5)
                    print("***Dosya oluşturma işlemi iptal edildi.***")
                    break
            else:
                print("Lütfen sadece E ya da H karakterlerinden birini giriniz, çıkmak için 'Q' ya basın: ")
                continue
     
           
         

                
def kitap_oku():#Daha önce var olan dosyaya erişip içeriği okumamızı sağlar
    while True:
            kitaba_eris=input("Erişmek İstediğiniz Kitap Adını Giriniz: ".upper())+".txt"
            if os.path.isfile(kitaba_eris):
               print("\t{} adlı dosya çağrılıyor...".format(kitaba_eris))
               dosya_eris=open(kitaba_eris,"r",encoding="utf-8")#Erişilen dosyayı "r" modülü ile okur
               icerik=dosya_eris.read()
               time.sleep(0.5)
               print(icerik)
               dosya_eris.close()
               break
            else:
               print("{} adlı kitap bulunamadı".format(kitaba_eris))
               while True:
                    islem=input("\t{} adlı yeni bir dosya Oluşturmak İster Misiniz (E/H): ".format(kitaba_eris))#Eğer girilen dosya adıyla bir dosya bulunmadıysa Yeni bir dosya açmak için izin ister.

                    if (islem=="E") or (islem=="e"):#E ye basılırsa 
                     print("\t\t{} Adlı Yeni Kitap Oluşturuluyor...".format(kitaba_eris))
                     time.sleep(0.5)
                     yeni_kitap_olustur()#bu fonksiyon çalıştırılır
                     print("***\t\t\t {} Adlı Yeni Kitap Oluşturuldu***".format(kitaba_eris))
                     break
                    elif(islem=="H") or (islem=="h"):
                      print("Dosya oluşturma işlemi İptal Ediliyor...")
                      time.sleep(0.5)
                      print("***Dosya oluşturma işlemi iptal edildi.***")
                      break
                    else:
                        print("Sadece E ya da H karakterlerinden birini giriniz: ")
                        continue
            break



def kitap_sil():
    while True:
        kitap_adi=input("Silmek İstediğiniz Kitabın Adını Giriniz: ".upper())+".txt"
        if os.path.isfile(kitap_adi):
            print("{} adlı kitap siliniyor....".format(kitap_adi))
            os.remove(kitap_adi) #Girilen dosya adının sadece içeriğini temizler
            time.sleep(0.5)
            print("\t****{} adlı kitap silindi****".format(kitap_adi))
            continue
        else:
            print("{} adlı kitap bulunamadı...".format(kitap_adi))
            break
  






