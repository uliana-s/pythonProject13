import math

class M13(Theme):
    discipline = "����������"
    topic = "��� ���� �����"
    def realisation(self):
        a = int(myinput("������ ���� ����� :"))
        b = int(myinput("������ ����� ����� :"))
        while a * b != 0:
            if a >= b:
                a = a % b
            else:
                b = b % a
        if a<b:
            a=b
        myprint("���:"+str(a))

class M17(Theme):
    discipline = "����������"
    topic = "��������� ������� �������"
    def realisation(self):
        a = int(myinput("������ |a|:"))
        b = int(myinput("������ |b|:"))
        r = int(myinput("������ ���:"))
        myprint(self.topic+": "+str(a*b*math.cos(r)))

class M21(Theme):
    discipline = "����������"
    topic = "������� ������"
    def realisation(self):
        x1 = int(myinput("������ x1:"))
        y1 = int(myinput("������ y1:"))
        x2 = int(myinput("������ x2:"))
        y2 = int(myinput("������ y2:"))
        myprint(self.topic+": "+str(((x1-x2)^2+(y1-y2)^2)^0.5))

class M25(Theme):
    discipline = "����������"
    topic = "����� ��������"
    def realisation(self):
        a = int(myinput("������ a:"))
        b = int(myinput("������ b:"))
        h = int(myinput("������ h:"))
        myprint(self.topic+": "+str((a+b)/2*h))

class M29(Theme):
    discipline = "����������"
    topic = "����� ���� �� ������ ������� ����"
    def realisation(self):
        x1 = int(myinput("������ x1:"))
        y1 = int(myinput("������ y1:"))
        x2 = int(myinput("������ x2:"))
        y2 = int(myinput("������ y2:"))
        x3 = int(myinput("������ x3:"))
        y3 = int(myinput("������ y3:"))
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
    discipline = "���������"
    topic = "���� ����� ��������� �� ������?"
    def realisation(self):
        myprint("����� �����")

class G37(Theme):
    discipline = "���������"
    topic = "��� ������� �� �������� ������� ���� � ���?"
    def realisation(self):
        myprint("������")

class G41(Theme):
    discipline = "���������"
    topic = "�� �������, �� ����� �������� ������� ���������� � ���."
    def realisation(self):
        myprint("�� ����")

class F50(Theme):
    discipline = "Գ������"
    topic = "�� ������ � � ��������� ���?"
    def realisation(self):
        myprint("��������, �������, ���������, ���������, �������, ������� � �������")

class T54(Theme):
    discipline = "������ � �������"
    topic = "��� ������� � ��� ������ ����������, ������ ���� ���� ����������� � �����"
    def realisation(self):
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
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
    discipline = "������ � �������"
    topic = "������ �� �����, �� ������ ����� �����"
    def realisation(self):
        s = myinput("������ �����")
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
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
    discipline = "������ � �������"
    topic = "������ ������� ��� � �����"
    def realisation(self):
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        file2.write(str(len(list1))+"\n")

class T66(Theme):
    discipline = "������ � �������"
    topic = "��������� ����� � ������ ������"
    def realisation(self):
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        s2 = s1.upper()
        file2.write(s2+"\n")

class T70(Theme):
    discipline = "������ � �������"
    topic = "������ �������� �����, �� ����������� � ������� �����"
    def realisation(self):
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if (i not in list2) and (i[0] in "�����岳���������"):
                list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l==len(i):
                file2.write(str(i)+"\n")

class T74(Theme):
    discipline = "������ � �������"
    topic = "������ �������� �����, �� �� ������ �������� ����"
    def realisation(self):
        f1 = myinput("������ ����� �������� �����")
        f2 = myinput("������ ����� ��������� �����")
        file1 = open(f1, "r")
        file2 = open(f2, "w")
        s1 = file1.read()
        list1 = s1.split()
        list2 = []
        for i in list1:
            if i not in list2:
                for j in i:
                    if j not in "�����岳���������":
                        list2.append(i)
        l = 0
        for i in list2:
            if len(i) > l:
                l = len(i)
        for i in list2:
            if l == len(i):
                file2.write(str(l) + "\n")

class Z78(Theme):
    discipline = "�������"
    topic = "������ ��� �� ������ ����?"
    def realisation(self):
        start_date = date.today()
        end_date = date(2024,1,1)
        myprint(str((end_date - start_date).days))

class Z82(Theme):
    discipline = "�������"
    topic = "������� � ������� ����� �� 1 �� 10."
    def realisation(self):
        a = randint(1, 10)
        b = myinput("� ������� ����� �� 1 �� 10. ³������ ����:")
        if a == b:
            myprint("��������")
        else:
            myprint("�� �����")

class Z91(Theme):
    discipline = "�������"
    topic = "�������� �������� ��������"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        � = myinput("������ ���� "+str(a)+"*"+str(b)+":")
        if c == a*b:
            myprint("��������")
        else:
            myprint("�� �����")

class Z95(Theme):
    discipline = "�������"
    topic = "�������� ���������"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        � = myinput("������ ���� "+str(a)+"+"+str(b)+":")
        if c == a+b:
            myprint("��������")
        else:
            myprint("�� �����")

class Z99(Theme):
    discipline = "�������"
    topic = "�������� ��������"
    def realisation(self):
        a = randint(1, 10)
        b = randint(1, 10)
        � = myinput("������ ���� "+str(a)+"-"+str(b)+":")
        if c == a-b:
            myprint("��������")
        else:
            myprint("�� �����")

class Z103(Theme):
    discipline = "�������"
    topic = "�������"
    def realisation(self):
        myprint(")")

class Z107(Theme):
    discipline = "�������"
    topic = """��� � ���������� ���������� "Call me"?"""
    def realisation(self):
        myprint("Blondie")

class Z111(Theme):
    discipline = "�������"
    topic = """������ "Call me" """
    def realisation(self):
        myprint("""Call me (call me) on the line
                Call me, call me any, anytime
                Call me (call me) I'll arrive
                You can call me any day or night
                Call me""")

class Z115(Theme):
    discipline = "�������"
    topic = "������ ��� � ����������� ����?"
    def realisation(self):
        myprint("366")

class Z119(Theme):
    discipline = "�������"
    topic = "�� � ����� ������?"
    def realisation(self):
        myprint("����, ������, ��������, ���, ���, ĳ��, ������, �������, �������, ������,������, ����")

