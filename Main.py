# Case-study #4
# Developers:   Aksenov A. (%),
#               Soloveychik D. (%),
#               Labuzov A. (%)
from textblob import TextBlob
text=input("Введите текст:").lower()
a=0
print("Предложений:",text.count(".")+text.count("!")+text.count("?")+text.count("..."))
print("Слов:",text.count(" ")+1)
vowels=["ё","у","е","а","о","э","я","и","ю","ы","e","y","u","i","o","a"]

for i in range (len(vowels)):
    a+=text.count(vowels[i])
print("Слогов:",a)
print("Средняя длина предложения в словах:",(text.count(" ")+1)/(text.count(".")+text.count("!")+text.count("?")+text.count("...")))
print("Средняя длина слова в слогах:",a/(text.count(" ")+1))
ASL=(text.count(" ")+1)/(text.count(".")+text.count("!")+text.count("?")+text.count("..."))
ASW=a/(text.count(" ")+1)
if ord(text[0])>500:
    FRE=206.835 - (1.3 * ASL ) - (60.1 * ASW)
    print("Индекс удобочитаемости Флеша:",FRE)
else:
    FRE=206.835 - 1.015 * ASL - 84.6 * ASW
    print("Индекс удобочитаемости Флеша:",FRE)
if FRE<=25:
    print("Текст трудно читается (для выпускников ВУЗов).")
elif FRE>25 and FRE<=50:
    print("Текст немного трудно читать (для студентов).")
elif FRE>50 and FRE<=80:
    print("Простой текст (для школьников).")
else:
    print("Текст очень легко читается (для младших школьников).")
lang=TextBlob(text).detect_language()
if lang!="en":
    text = str(TextBlob(text).translate(to="en"))
pol = TextBlob(text).polarity
if -1<=pol<=-0.5:
    print("Тональность текста: негативный")
elif -0.5<pol<=0.5:
    print("Тональность текста: нейтральный")
elif 0.5<pol<=1:
    print("Тональность текста: позитивный")
obj = (1-TextBlob(text).sentiment.subjectivity)
print("Объективность:",obj*100,"%")
