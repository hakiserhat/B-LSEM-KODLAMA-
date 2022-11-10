
print("eminim bu sınavı geçemezsin")
cevapilk=input("ingilizcede go kelimesinin geçmiş zamanı: ").lower()
cevapiki=input("alfabede kaç harf vardır?: ").lower()
cevapuc=input("bir ... ekmek. Cümlesindeki boşluğa uygun kelimeyi getiriniz. ").lower()
cevapdort=input("şiir kelimesi kaç harflidir? harfle yazınız. ").lower()
cevapbes=input("bu son soru olduğuna göre bu test kaç sorudan oluşur? harfle yazınız. ").lower()
puan=0
if cevapilk=="went":
    puan=puan+1
else:
    puan=puan
if cevapiki=="29":
    puan=puan+1
else:
    puan=puan
if cevapuc=="somun":
    puan=puan+1
else:
    puan=puan
if cevapdort=="dört":
    puan=puan+1
else:
    puan=puan+0
if cevapbes=="beş":
    puan=puan+1
else:
    puan=puan
if puan>=4:
    print("sınavı geçtiniz. :(")
else:
    print("sınavı geçemediniz. :)")
print("puanınız: ",puan)


