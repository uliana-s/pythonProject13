import math

class M13(Theme):
    discipline = "Математика"
    topic = "НСД двох чисел"
    def realisation(self):
        a = int(myinput("Введіть одне число :"))
        b = int(myinput("Введіть друге число :"))
        while a * b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a<b:
            a=b
        myprint("НСД:"+str(a))

class M17(Theme):
    discipline = "Математика"
    topic = "Скалярний добуток векторів"
    def realisation(self):
        a = int(myinput("Введіть |a|:"))
        b = int(myinput("Введіть |b|:"))
        r = int(myinput("Введіть кут:"))
        myprint(self.topic+": "+str(a*b*math.cos(r)))

class M21(Theme):
    discipline = "Математика"
    topic = "Довжина відрізка"
    def realisation(self):
        x1 = int(myinput("Введіть x1:"))
        y1 = int(myinput("Введіть y1:"))
        x2 = int(myinput("Введіть x2:"))
        y2 = int(myinput("Введіть y2:"))
        myprint(self.topic+": "+str(((x1-x2)^2+(y1-y2)^2)^0.5))

class M25(Theme):
    discipline = "Математика"
    topic = "Площа трапеції"
    def realisation(self):
        a = int(myinput("Введіть a:"))
        b = int(myinput("Введіть b:"))
        h = int(myinput("Введіть h:"))
        myprint(self.topic+": "+str((a+b)/2*h))

class M29(Theme):
    discipline = "Математика"
    topic = "Центр кола за трьома точками кола"
    def realisation(self):
        x1 = int(myinput("Введіть x1:"))
        y1 = int(myinput("Введіть y1:"))
        x2 = int(myinput("Введіть x2:"))
        y2 = int(myinput("Введіть y2:"))
        x3 = int(myinput("Введіть x3:"))
        y3 = int(myinput("Введіть y3:"))
        xc1=(x1+x2)/2
        yc1=(y1+y2)/2
        xc2=(x1+x3)/2
        yc2=(y1+y3)/2
        nx1=x2-x1
        ny1=y2-y1
        nx2=x3-x1
        ny2=y3-y1
        n1=nx1/ny1
        n2=nx2/ny2
        if (n1-n2) == 0:
            n1=n2+1
        y = (n1*yc1-n2*yc2)/(n1-n2)
        x = (nx1*y-nx1*yc1)/ny1+xc1
        myprint("("+str(x)+";"+str(y)+")")

class G33(Theme):
    discipline = "Географія"
    topic = "Який океан найбільший за площею?"
    def realisation(self):
        myprint("Тихий океан")

class G37(Theme):
    discipline = "Географія"
    topic = "Яка держава має найбільшу кількість озер в світі?"
    def realisation(self):
        myprint("Канада")

class G41(Theme):
    discipline = "Географія"
    topic = "Дві держави, які мають найбільшу кількість водосховищ в світі."
    def realisation(self):
        myprint("Не знаю")

class F50(Theme):
    discipline = "Філологія"
    topic = "Які відмінки є в українській мові?"
    def realisation(self):
        myprint("називний, родовий, давальний, знахідний, орудний, місцевий і кличний")

class T54(Theme):
    discipline = "Робота з текстом"
    topic = "Для кожного зі слів тексту підрахувати, скільки разів воно зустрічається у тексті"
    def realisation(self):
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                list2.append(i)
        for i in list2:
            file2.write(str(i) + " " + str(list1.count(i))+"\n")

class T58(Theme):
    discipline = "Робота з текстом"
    topic = "Знайти всі слова, що містять певну літеру"
    def realisation(self):
        s = myinput("Вкажіть літеру")
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                list2.append(i)
        for i in list2:
            if s in i:
                file2.write(str(i)+"\n")

class T62(Theme):
    discipline = "Робота з текстом"
    topic = "Знайти кількість слів у тексті"
    def realisation(self):
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        file2.write(str(len(list1))+"\n")

class T66(Theme):
    discipline = "Робота з текстом"
    topic = "Перевести текст в верхній регістр"
    def realisation(self):
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        s2 = s1.upper()
        file2.write(s2+"\n")

class T70(Theme):
    discipline = "Робота з текстом"
    topic = "Знайти найдовші слова, які починаються з голосної літери"
    def realisation(self):
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if (i not in list2) and (i[0] in "АаУуЕеІіОоЄєЯяИиЮюЇї"):
                list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l==len(i):
                file2.write(str(i)+"\n")

class T74(Theme):
    discipline = "Робота з текстом"
    topic = "Знайти найдовші слова, які не містять голосних літер"
    def realisation(self):
        f1 = myinput("Вкажіть назву вхідного файлу")
        f2 = myinput("Вкажіть назву вихідного файлу")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                for j in i:
                    if j not in "АаУуЕеІіОоЄєЯяИиЮюЇї":
                        list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l == len(i):
                file2.write(str(l) + "\n")

class Z78(Theme):
    discipline = "Загальні"
    topic = "Скільки днів до Нового Року?"
    def realisation(self):
        start_date = date.today()
        end_date = date(2024,1,1)
        myprint(str((end_date - start_date).days))

class Z82(Theme):
    discipline = "Загальні"
    topic = "Пограти у відгадай число між 1 та 10."
    def realisation(self):
        a = randint(1, 10)
        b = myinput("Я загадав число між 1 та 10. Відгадай його:")
        if a == b:
            myprint("Молодець")
        else:
            myprint("Ну нічого")

class Z91(Theme):
    discipline = "Загальні"
    topic = "Перевірка таблички множення"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        с = myinput("Скільки буде "+str(a)+"*"+str(b)+":")
        if c == a*b:
            myprint("Молодець")
        else:
            myprint("Ну нічого")

class Z95(Theme):
    discipline = "Загальні"
    topic = "Перевірка додавання"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        с = myinput("Скільки буде "+str(a)+"+"+str(b)+":")
        if c == a+b:
            myprint("Молодець")
        else:
            myprint("Ну нічого")

class Z99(Theme):
    discipline = "Загальні"
    topic = "Перевірка віднімання"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        с = myinput("Скільки буде "+str(a)+"-"+str(b)+":")
        if c == a-b:
            myprint("Молодець")
        else:
            myprint("Ну нічого")

class Z103(Theme):
    discipline = "Загальні"
    topic = "Посмішка"
    def realisation(self):
        myprint(")")

class Z107(Theme):
    discipline = "Загальні"
    topic = """Хто є виконавцем композиції "Call me"?"""
    def realisation(self):
        myprint("Blondie")

class Z111(Theme):
    discipline = "Загальні"
    topic = """Приспів "Call me" """
    def realisation(self):
        myprint("""Call me (call me) on the line
                Call me, call me any, anytime
                Call me (call me) I'll arrive
                You can call me any day or night
                Call me""")

class Z115(Theme):
    discipline = "Загальні"
    topic = "Скільки днів у високосному році?"
    def realisation(self):
        myprint("366")

class Z119(Theme):
    discipline = "Загальні"
    topic = "Які є знаки зодіаку?"
    def realisation(self):
        myprint("Овен, Телець, Близнюки, Рак, Лев, Діва, Терези, Скорпіон, Стрілець, Козеріг,Водолій, Риби")

