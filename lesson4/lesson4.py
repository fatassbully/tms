'''
Ex1
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between numbers x and y (both included). Return list of this numbers.
Use list comprehension.
'''

#
# def divisor(x: int, y: int):
#     newlist = []
#     for i in range(x, y + 1):
#         if i % 7 == 0 and i % 5 != 0:
#             newlist.append(i)
#         else:
#             pass
#     return newlist

def divisor(x: int, y: int):
    c = [i for i in range(x, y + 1) if i % 7 == 0 and i % 5 != 0]
    return c


assert divisor(0, 36) == [7, 14, 21, 28]
assert divisor(9, 13) == []
assert divisor(-100, 100) == [-98, -91, -84, -77, -63, -56, -49, -42, -28, -21, -14, -7, 7, 14, 21, 28, 42, 49, 56, 63,
                              77, 84, 91, 98]

'''
Ex2
With a given number n, write a program to generate a dictionary that contains (i, i*i) such that is number 
between 1 and n (both included). The program returns the dictionary. Use dict comprehension.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

def dict_gen(n: int):
    newkeys = [i for i in range(1,n+1)]
    newvalues = [i*i for i in range (1,n+1)]
    F = zip(newkeys,newvalues)
    F = dict(F)
    return F


assert dict_gen(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



'''
Ex3
Return a list of integers from 0 to n with step m. Use list comprehension.
'''

def list_gen(n, m):
    k = [i for i in range(0,n,m)]
    return k


assert list_gen(10, 2) == [0, 2, 4, 6, 8]
assert list_gen(-25, -2) == [0, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24]
assert list_gen(1, 3) == [0]
assert list_gen(1, -1) == []


'''
Ex4
Suppose you have a dictionary where the keys are integers, return a list of values where the key is an odd number.
'''

def odd_keys(dict):
    newlist = []
    for i in dict.keys():
        if i % 2 == 1:
            newlist.append(dict[i])
    return newlist


assert odd_keys({1: 'One', 2: 'Two', 4: 'Four', 7: 'Seven'}) == ['One', 'Seven']
assert odd_keys({12: [1, 2, 3], 2: 'str', 9: ['Hello', 'name', '?']}) == [['Hello', 'name', '?']]
assert odd_keys({}) == []
assert odd_keys({34: 234, 78: 99}) == []


'''
Ex5
Given a phrase, count the occurrences of each word in that phrase and return result as a dictionary where key is a word 
and value is a count the occurrences.

For example for the input "olly olly in come free"

olly: 2
in: 1
come: 1
free: 1
'''

def words_counter(line):
    newdict = []
    S = line.split()
    M = set(S)
    for i in M:
        newdict.append(S.count(i))
    F = dict(zip(M,newdict))
    return F

assert words_counter("olly olly in come free") == {"olly": 2, "in": 1, "come": 1, "free": 1}
assert words_counter("") == {}


'''
Ex6
Convert a phrase to its acronym.

Techies love their TLA (Three Letter Acronyms)!

Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG).
'''


def acronym(phrase):
    newphrase = phrase.split()
    final = ''
    for i in newphrase:
        final = final+i[0]

    return final
    
    
assert acronym("World Wide Web") == "WWW"
assert acronym("Portable Network Graphics") == "PNG"



"""PFD EXERCISES"""

"""
111111111
Дан список чисел. Определите, сколþко в ÿтом списке ÿлементов, которýе болþше двух своих соседей, и
вýведите количество таких ÿлементов. Крайние ÿлементý списка никогда не учитýваĀтсā, посколþку у них
недостаточно соседей.
"""

lst = [1,3,5,76,55,343,54,33,2,1,3,4,5]
finallist = []
for i in range(len(lst)-1):
    if lst[i] == lst[0]:
        pass
    elif lst[i] == lst[len(lst)-1]:
        pass
    elif lst[i] > lst[i-1] and lst[i] > lst[i+1]:
        finallist.append(lst[i])
    else:
        pass
print(finallist)






"""
22222222
Дан список чисел. Вýведите значение наиболþшего ÿлемента в списке, а затем индекс ÿтого ÿлемента в

списке. Если наиболþших ÿлементов несколþко, вýведите индекс первого из них.
"""

I = [1,3,5,76,55,343,54,33,344,2,1,3,4,5]
A = max(lst)
C = I.index(max(lst))
print(A, C)






"""
33333333333
У вас есть список чисел. Напишите три функции, которые вычисляют сумму этих чисел: с for-циклом, с while-циклом, с
использованием встроенного метода sum"""


lst = [1,3,5,76,55,343,54,33,344,2,1,3,4,5]
def one(lst):
    c = 0
    for i in lst:
        c +=i
    return c

def two(lst):
    working = lst.copy()
    i = 0
    b = 0
    while len(working) != 0:
        b += working[i]
        del(working[i])
    return b


def three(lst):
    return sum(lst)
print(one(lst),two(lst),three(lst))





"""
4444444444444444
Напишите функцию, которая создаёт комбинацию двух списков таким образом
[1,2,3] + [11,22,33] -> [1,11,2,22,3,33]"""
lst1 = [1,3,2,4]
lst2 = [11,22,33,44]
def labuda(a,b):
    worklist = a + b
    return sorted(worklist, key= lambda x: str(x)[0])
print(labuda(lst1,lst2))



"""55555555555555555
У вас есть массив чисел, составьте из них максимальное число. Например"""
massiv = [61, 228, 9, 888]
s_massiv = sorted(massiv,key=lambda x: str(x)[0],reverse=True)
F = [str(x) for x in s_massiv]
print("".join(F))


"""
66666666666666
В списке все ÿлементý различнý. Поменāйте местами минималþнýй и максималþнýй ÿлемент ÿтого
списка.
"""
spisok = [1,2,3,4,5,88]
def podmena(lst):
    Mai = lst.index(max(lst))
    Mii = lst.index(min(lst))
    lst[Mai], lst[Mii] = lst[Mii], lst[Mai]
    return lst
print(spisok)
print(podmena(spisok))


"""
7777777777777777777
В единственной строке записан текст. Длā каждого слова из данного текста подсчитайте, сколþко раз оно
встречалосþ в ÿтом тексте ранее.
Словом считаетсā последователþностþ непробелþнýх символов идущих подрāд, слова разделенý одним
или болþшим числом пробелов или символами конца строки."""

stroka = "Hello, Hello, what is going up? How many times we encountered this word in current string?"
# stroka = "1 1 1 1 2 2 2 2 2"

def schet(string):
    b = list(string.split())
    a = set(b)
    for j in a:
        C = ""
        for i in b:
            L = str(len(C))
            if j == i:
                if C == "":
                    C+="1"
                    print(j + " " + "0")
                elif C!="":
                    C+="1"
                    print(j + " " + L)
            else : continue
        # print(j + " " + str(len(C)))
    return
print(schet(stroka))






"""
88888888888888888888888888
Дан текст: в первой строке задано число строк, далее идут сами строки. Вýведите слово, которое в ÿтом
тексте встречаетсā чаще всего. Если таких слов несколþко, вýведите то, которое менþше в
лексикографическом порāдке"""

text = """5
Hello how are you doing?
I am fine! How about you?
Not so much...
Why is that?
FUCK OFF!"""
def find
