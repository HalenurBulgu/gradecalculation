
adısoyadı="Halenur Bulgu"



adsoyad = input("lütfen adınızı ve soyadınızı boşluk bırakarak yazınız")



if (adısoyadı==adsoyad.title()):
    print("adınız ve soyadınız sistemde kayıtlı olanla eşleşmektedir. Giriş başarılı. Hoşgeldiniz")
elif (adısoyadı!=adsoyad.title()):
    adsoyad = input("lütfen adınızı ve soyadınızı boşluk bırakarak kontrol ederek tekrar yazınız")
    if (adısoyadı==adsoyad.title()):
        print("adınız ve soyadınız sistemde kayıtlı olanla eşleşmektedir. Giriş başarılı. Hoşgeldiniz")
    elif (adısoyadı!=adsoyad.title()):
         adsoyad = input("lütfen adınızı ve soyadınızı boşluk bırakarak kontrol ederek tekrar yazınız")
         if (adısoyadı==adsoyad.title()):
             print("adınız ve soyadınız sistemde kayıtlı olanla eşleşmektedir. Giriş başarılı. Hoşgeldiniz")
         elif (adısoyadı!=adsoyad.title()):
            print("üçüncü yanlış girişten sonra sistem kapanmaktadır. Daha sonra tekrar deneyin.")
else:
    print("sistem hatası")
            


secim1=input("seçtiğiniz 1.ders")
secim2=input("seçtiğiniz 2.ders")
secim3=input("seçtiğiniz 3.ders")
secim4=input("seçtiğiniz 4.ders")
secim5=input("seçtiğiniz 5.ders")

secilen = [secim1,secim2,secim3,secim4,secim5]
secim = []
for i in secilen:
    if len(i)>0:
        secim.append(i)
        
print(secim)
 
print(len(secim))    

if len(secim)<3:
    print("snıfta kaldınız")
elif 2<len(secim)<6:
    sınavdersi = input("lütfen sınav olmak istediğiniz dersi seçiniz.")
    if sınavdersi not in secilen:
        print("lütfen sınava girmek istediğiniz dersi yukarıda seçtiğiniz derslerden alınız")
    else:
        print("sınavdersi:"+" " +sınavdersi)
else:
    print("lütfen seçtiğiniz ders sayısı 3 ile 5 arasında olmalıdır")



not1=int(input("sınav dersi için midtermden aldığınız notunuzu giriniz"))
not2=int(input("sınav dersi için finalden aldığınız notu giriniz"))
not3=int(input("sınav dersi için projeden aldığınız notu giriniz"))
notlar={"midterm":not1,"final":not2,"project":not3}
print(notlar)

midtermhesap=not1*0.3
finalhesap=not2*0.5
projecthesap=not3*0.2

nothesap=midtermhesap+finalhesap+projecthesap
print(nothesap)

if nothesap>90:
    print(sınavdersi+" "+"AA")
elif 70<nothesap<90:
    print(sınavdersi+" "+"BB")
elif 50<nothesap<70:
    print(sınavdersi+" "+"CC")
elif 30<nothesap<50:
    print(sınavdersi+" "+"BB")
else:
    print(sınavdersi+" "+"FF"+"dersten kaldınız.")



        
   


