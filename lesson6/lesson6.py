'''
Ex1
Считать из файла input1.txt 10 чисел (числа записаны через пробел). 
Затем записать их произведение в файл output.txt.
'''

def zabratzapisat(a):
    file1 = open("K:\Python_Courses\\tms2\\tms\lesson6\index1.txt", "r")
    print(file1)
    F = ''
    for i in file1.read():
        if len(F)!= a:
            if i == " ":
                pass
            else:
                F = F + i
    return F
print(zabratzapisat(5))
Z = open("K:\Python_Courses\\tms2\\tms\lesson6\output.txt", "w")
Z.write(zabratzapisat(5))
print(Z)




"""Ex2
В файле input2.txt записаны целые числа. Найти максимальное и минимальное число и записать в другой файл."""
F1 = open("K:\Python_Courses\\tms2\\tms\lesson6\index2.txt")
R = F1.read()
R = R.split()
Fmax = max(R)
Fmin = min(R)
Finalfile = open("K:\Python_Courses\\tms2\\tms\lesson6\index2_final.txt", "w")
Thingtowrite = ("Maximal value is " + str(Fmax) + "\nMinimal value is " + str(Fmin))
print(Thingtowrite)
Finalfile.write(Thingtowrite)


'''
Ex3
В файл input3.txt записаны сведения о сотрудниках некоторой фирмы в виде:
Иванов 45 бухгалтер
Необходимо записать в текстовый файл сведения о сотрудниках, возраст которых меньше 40.
'''
F2 = open("K:\Python_Courses\Fromscratch\\tms\lesson6\index3.txt","r",encoding="UTF-8")
R2 = F2.read()
R2 = R2.split()
wholelst = []
lst = []

#Создание листа из листов про каждого сотрудника
for k in range(len(R2)//3):
    if lst == []:
        for i in R2[0:3]:
            lst.append(i)
        wholelst.append(lst)
    elif lst != []:
        lst = []
        f = 3
        for i in R2[f*k:f*k+3]:
            lst.append(i)
        wholelst.append(lst)
    else:
        pass
#Отсеивание
for i in wholelst:
    if int(i[1])<40:
        wholelst.remove(i)
    else:pass
Sotrudniki = open("K:\Python_Courses\Fromscratch\lesson6\index3_final.txt", "w")
Finalstring = ""
for i in wholelst:
    # print(i)
    str_ = ""
    for j in i:
        # print(j)
        j = str(j)
        str_ = (str_ + " " + j)
    Finalstring = str_ + "\n"
    #Не понимаю почему появились пробелы в начале каждой строки,
    #Код ниже удаляет их при добавлении
    Sotrudniki.writelines(Finalstring[1:])


'''
Ex4
В файле input4.txt записаны в столбик целые числа.
Отсортировать их по возрастанию суммы цифр и записать в другой файл.
'''
F4 = open("K:\Python_Courses\Fromscratch\\tms\lesson6\index4.txt",'r')
R4 = F4.read()
R4 = R4.split()
lstofsums = []
for i in R4:
    if i[0] == "-":
        S = 0
        for j in i[1:]:
            j = int(j)
            S += j
    else:
        S = 0
        for j in i:
            j = int(j)
            S += j
    lstofsums.append(S)

SRT = (str(sorted(lstofsums))).strip("[]")
print(SRT)
FF = open("K:\Python_Courses\Fromscratch\\tms\lesson6\index4_final.txt","w")
FF.write(SRT)


'''
Ex5
Вводится буква. Определить, это код английской буквы или какой-либо иной символ.
'''


'''
Ex6
Дано натуральное число n. Выведите все числа от 1 до n. (использовать рекурсию)
'''
# n = input()
n = 55
def Vyvesty_vse_chisla(c):
    if c<=1:
        return 1
    else:
        print(c)
        c = c-1
    return Vyvesty_vse_chisla(c)
print(Vyvesty_vse_chisla(n))


'''
Ex7
Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя их пробелами или новыми строками.
Разрешена только рекурсия и целочисленная арифметика.
Пример:
179

9 7 1
'''
N = 4432
def obratno(a):
    a = str(a)[::-1]
    return " ".join(a)
print(obratno(N))



'''
Ex8
Написать функцию, которая принимает произвольное количество позиционных и ключевых аргументов.
Функция возвращает произведение всех ключевых и позиционных аргументов, являющихся целыми числами, 
объединение в одну строку всех ключевых и позиционных аргументов, являющихся строками, 
в качестве разделителя использовать '_'.

Пример
foo(1, 2, 2.0, 'str', 6, a='key', b=12, c=3.56, d='world', e=-11, f='2') == 10, 'str_key_world_2'
'''


'''
Ex9
Написать функцию, которая принимает на вход 2 списка lst1, lst2, содержащих только целые числа, 
и возвращает список, элементами которого будут lst1[i]**lst2[i]

Пример:
foo([-2, 2, 4], [3, 0, 2] == [-8, 1, 16]
foo([1, 2, 3], [4, 5]) == [1, 32]
'''


'''
Ex10
Напишите декоратор с параметрами bucket, который будет делать так, 
что задекорированная функция, прежде чем возвращать результат, 
будет распечатывать в стандартный поток вывода все переданные bucket аргументы в следующем формате:  

аргументы распечатаны в виде пары (кортежа размера два)
первый элемент пары --  кортеж со значениями переданных bucket аргументов без имени 
(значения в этом кортеже следуют в том же порядке, в котором соответствующие аргументы были переданы bucket)
второй элемент пары -- словарь с элементами вида имя: значение для всех переданных bucket именованных аргументов.

Пример:
@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one = 1, two = 2, three = 3)
def identity(x):
  return x


print(identity(42))
>>> ((1, 2, 3, [1, 2, 3], 'one', 'two', 'three'), {'two': 2, 'one': 1, 'three': 3})
42

@bucket()
def identity(x):
  return x


print(identity(42))
>>> ((), {})
42 
'''
