
text = str(input("Введите текст : "))
text = text.lower()
d = list()

for i in text:
    if text.count(i) < 2:
       i = "("
       d.append(i)
    else:
        i=")"
        d.append(i)

print ("Результат - "," ".join(d))

