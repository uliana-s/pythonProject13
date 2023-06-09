from datetime import datetime, date
import abc
import json

rez1 = True
rez2 = True
def myprint(s: str):
    print("\033[1;31m", end='')
    print("Бот: " + s)
    file.write("Бот: "+ s+"\n")
    file1.write("Бот: "+ s+"\n")

def myinput(s: str, lst = []):
    global rez1
    global rez2
    print("\033[1;31m", end='')
    print("Бот: "+s)
    a = input("\033[34m{}".format("Користувач: "))
    file.write("Бот: "+s+"\n")
    file.write("Користувач: "+a+"\n")
    file1.write("Бот: "+s+"\n")
    file1.write("Користувач: "+a+"\n")
    for i in lst:
        if a in i:
            a=i
    if a == "Назад":
        rez2 = False
    if a == "Вихід":
        rez1 = False
        rez2 = False
        print("\033[1;31m", end='')
        print("Бот: На все добре")
        return ("")
    return a
class Theme(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def realisation(self):
        pass
class JobTheme:
    def __init__(self, theme: Theme):
        self.__theme = theme
    def job_realisation(self):
        self.__theme.realisation()
    def get_discipline(self):
        return self.__theme.discipline
    def get_topic(self):
        return self.__theme.topic

exec(open("Theme.py").read())

class Singleton:
    isinstance = None

    def __new__(cls):
        if Singleton.isinstance is None:
            Singleton.isinstance = super().__new__(cls)
        return Singleton.isinstance

    def dialog(self):
        global rez1
        global rez2
        object_list = []
        discipline_list = []
        class_list = Theme.__subclasses__()
        for i1 in class_list:
            object_list.append(JobTheme(i1()))
        for i1 in object_list:
            t1 = i1.get_discipline()
            if not discipline_list.count(t1):
                discipline_list.append(t1)
        while rez1:
            myprint("Можемо поговорити з таких дисциплін: (можете ввести лише ключове слово)")
            myprint(str(discipline_list)[1:-1] + ",'Допомога', 'Вихід'")
            answer1 = myinput("Виберіть дисципліну :", discipline_list)
            rez2 = True
            if answer1 in discipline_list:
                while rez2:
                    myprint("Ви вибрали дисципліну " + answer1)
                    myprint("Я можу поговорити на такі теми:")
                    topic_list = []
                    for i2 in object_list:
                        tema = i2.get_discipline()
                        if tema == answer1:
                            topic_list.append(i2.get_topic())
                    myprint(str(topic_list)[1:-1] + ",'Допомога', 'Назад', 'Вихід'")
                    answer2 = myinput("Виберіть тему :", topic_list)
                    if answer2 in topic_list:
                        myprint("Ви вибрали " + answer2)
                        for i3 in object_list:
                            if i3.get_topic() == answer2:
                                i3.job_realisation()
                    else:
                        if answer2 == "Назад":
                            myprint("Зараз перейдемо до вибору дисципліни")
                        elif answer2 == "Допомога":
                            myprint("Зараз оберіть тему з обраної дсиципліни")
                        elif answer2 != "":
                            myprint("Я не знаю такої теми. Спробуємо ще раз вибрати тему?")
            else:
                if answer1 != "":
                    myprint("Я не знаю такої дисципліни. Спробуємо ще раз вибрати дисципліну?")


if __name__ == '__main__':
    datetime = datetime.now()
    file = open(
        "dialog-" + str(datetime)[0:10] + "-" + str(datetime)[11:13] + "-" + str(datetime)[14:16] + "-" + str(
            datetime)[17:19] + ".txt", 'w')
    with open("config.json", 'r') as file3:
        text = json.load(file3)
    file1 = open(text['path'] + "\dialog.txt", "a")

    first = Singleton()
    first.dialog()
