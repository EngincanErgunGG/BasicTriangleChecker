import time

def start(printstart: bool = False):
    if printstart:
        print("Bu program girdiğiniz açılar bir üçgeni oluşturuyor mu? sorunuza cevap verir.")
        print("Çalışma Yöntemi: Girdiğiniz 3 açının toplamının 180 olup olmadığını kontrol eder. Programdan çıkmak için CTRL+C tuşlarına basınız!")
    inputNumber()

def inputNumber():
    try:
        a1 = int(input("1. açıyı giriniz: "))
        a2 = int(input("2. açıyı giriniz: "))
        a3 = int(input("3. açıyı giriniz: "))
        totalDeggre = a1 + a2 + a3
        if totalDeggre == 180:
            print("Bu bir üçgendir.")
            start()
        else:
            print("Bu bir üçgen değildir.")
            print("Üçgen olması için gereken değer: 180 / " + str(totalDeggre))
            start()
    except ValueError:
        print("Lütfen sayısal rakamlar kullanınız!")
        start()
    except KeyboardInterrupt:
        print("\nProgram sonlandırıldı. Pencere 1 saniye içerisinde kapatılıyor..")
        time.sleep(1)

start(True)