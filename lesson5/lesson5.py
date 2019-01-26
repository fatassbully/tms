'''
Ex1
Это простое упражнение на использование упаковок.
Определите функцию print_given, которая для каждого переданного аргумента
будет распечатывать на отдельной строке через пробел имя аргумента (если таковое имеется),
значение аргумента, тип аргумента.
Аргументы без имени должны быть распечатаны раньше именованных.
Порядок печати аргументов без имени важен: он должен совпадать с порядком,
в котором аргументы передаются. Порядок печати аргументов с именем неважен.
Пример:
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)
>>> 1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
[1, 2, 3] <class 'list'>
one <class 'str'>
two <class 'str'>
three <class 'str'>
one 1 <class 'int'>
two 2 <class 'int'>
three 3 <class 'int'>
print_given()
'''
def print_given(*args,two,one,three):
    for i in args:
        print(i,type(i))
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)





'''
Ex2
Если вы не использовали раньше сортировку по заданному ключу при помощи встроенной функции sorted, 
рекомендую прочитать вот этот python-howto(https://docs.python.org/3/howto/sorting.html) 
(упражнение про это, да и вообще возможность чрезвычайно полезная).
На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).
Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, 
поскольку слово two в словаре встречается позже слова three, 
а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
Пример:
Sample Input:
0 1 1 2 3 5 8 13
Sample Output:
8 5 1 1 13 3 2 0
Использовать
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
'''
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'
                }

lst = [0,1,1,2,3,5,8,13]
print (lst)
keys = number_names.keys()
A = sorted (lst, key = lambda x : number_names[x])
print (A)









'''
Ex3
Напишите функцию composition(f, g), которая принимает на вход две функции: f и g, -- и возвращает их композицию.
Не вдаваясь в лишние сейчас детали,  назовём композицией 𝑓∘𝑔 двух заданных функций 𝑓, 𝑔 функцию ℎ, для которой
  ℎ(𝑥)=𝑓(𝑔(𝑥))
Определите функцию композиции, предполагая, что аргументы у функции g могут быть какие угодно, 
и любое возвращаемое функцией g значение будет корректным аргументом для функции f.
Примеры:
h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))
>>> 36
h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))
>>> 36
h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))
>>> 6592
'''
def g(*args):
    return args
def f(*args):
    return args*2

# def composition(f,g):
#     return
print(g(1))








'''
Ex4
Напишите декоратор flip, который делает так, что задекорированная функция 
принимает все свои неименованные аргументы в порядке, обратном тому, 
в котором их передали (для аргументов с именем не вполне правильно учитывать порядок, в котором они были переданы)
Пример:
@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)
>>> 2.0
'''










'''
Ex5
Напишите декоратор introduce_on_debug, который делает так, что задекорированная функция печатает своё имя 
при вызове, но только если константа debug имеет значение True.
Пример:
@introduce_on_debug
def identity(x):
    return x

# debug == False
identity(239)
>>> 239
# debug == True
identity(57)
>>> identity
57
'''

@introduce_on_debug
def identity(x):
    if debug==True:
        print(x)
    return x

debug == False
identity(239)
debug == True