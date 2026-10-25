countv=0
countw=0
counts=0


#list الاحرف الصوتية
letter_sound=["i","o",'u',"y","e"]
sentences=input("enter the sentences:\n")
#for علي الجملة المدخلة
for letter in sentences:
    if letter in letter_sound:
        countv +=1
    if letter.isspace():
        counts+=1
#تقسيم الجملة لكلمات لنسطتيع عدها
sent=len(sentences.split())

countw+=sent
print("coun letter sound is",countv)
print("count sentences word is",countw)
print("coun spaces is",counts)

