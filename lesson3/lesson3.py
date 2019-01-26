'''
Ex1
The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers"
array and contains student's answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each
correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.

For example:

checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0
'''


def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
    if score < 0:
        score = 0
    return score



assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7
assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
assert check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) == 0


'''
Ex2
You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:
get_middle("test") should return "es"
get_middle("testing") should return "t"
get_middle("middle") should return "dd"

#Input
A word (string) of length 0 < str < 1000.

#Output
The middle character(s) of the word represented as a string.
'''


def get_middle(s):
    b = len(s)
    if b % 2 == 0:
        d = s[int(int(b)/2)-1:int(int(b)/2)+1]
    else:
        d = s[int(b//2):int(b//2)+1]
    return d


assert get_middle("test") == "es"
assert get_middle("testing") == "t"
assert get_middle("middle") == "dd"
assert get_middle("A") == "A"
assert get_middle("of") == "of"


'''
Ex3
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''


def high_and_low(numbers):
    b = sorted(numbers.split())
    findlist = []
    for i in b:
        c = int(i)
        findlist.append(c)
    Ma = max(findlist)
    Mi = min(findlist)
    return str(Ma) + ' ' + str(Mi)


assert high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") == "542 -214"
assert high_and_low("1 2 -3 4 5") == "5 -3"


'''
Ex4
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. 
When writing on Twitter, he is known for almost always capitalizing every word.

Your task is to convert strings to how they would be written by Jaden Smith. 
The strings are actual quotes from Jaden Smith, but they are not 
capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''
string = "How can mirrors be real if our eyes aren't real"
def toJadenCase(string):
    a = string.split()
    b = ""
    c = len(string)
    for i in a:
        if i[0].islower():
             b +=i[0].upper() + i[1:] + " "
        else:
            b += i + " "
    return b[:c]

assert toJadenCase(string) == "How Can Mirrors Be Real If Our Eyes Aren't Real"


'''
Ex5
Implement a function that adds two numbers together and returns their sum in binary. 
The conversion can be done before, or after the addition.

The binary number returned should be a string
'''


def add_binary(a, b):
    return str(bin(a + b))[2:]


assert add_binary(1, 1) == "10"
assert add_binary(0, 1) == "1"
assert add_binary(1, 0) == "1"
assert add_binary(2, 2) == "100"
assert add_binary(51, 12) == "111111"


'''
Ex6*
Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).

Consonants are letters used in English other than "a", "e", "i", "o", "u". We will count "y" as a consonant.

Remember, your function needs to return the number of unique consonants - disregarding duplicates. 
For example, if the string passed into the function reads "add", 
the function should return 1 rather than 2, since "d" is a duplicate.

Similarly, the function should also disregard duplicate consonants of differing cases. 
For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.

Examples

"add" ==> 1
"Dad" ==> 1
"aeiou" ==> 0
"sillystring" ==> 7
'''


def count_consonants(text):
    goodlist = []
    badlist = []
    bastuff = ["a", "e", "i", "o", "u"]
    for c in range(len(text)):
        if text[c].isalpha():
            if text[c] in bastuff:
                badlist.append(text[c].lower())
            elif text[c] != text[c]:
                badlist.append(text[c].lower())
            else:
                goodlist.append(text[c].lower())
        else:
            pass
    F = len(set(goodlist))
    return F



assert count_consonants('sillystring') == 7
assert count_consonants('aeiou') == 0
assert count_consonants('abcdefghijklmnopqrstuvwxyz') == 21
assert count_consonants('Count my unique consonants!!') == 7


'''
Ex7
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
'''


def fake_bin(x):
    newstring = ""
    for i in x:
        if int(i) < 5:
            newstring += "0"
        else:
            newstring += "1"
    return newstring


tests = [
        # [expected, input]
        ["01011110001100111", "45385593107843568"],
        ["101000111101101", "509321967506747"],
        ["011011110000101010000011011", "366058562030849490134388085"],
        ["01111100", "15889923"],
        ["100111001111", "800857237867"],
        ]

for exp, inp in tests:
    assert fake_bin(inp) == exp




'''
Ex8
In your class, you have started lessons about arithmetic progression. 
Since you are also a programmer, you have decided to write a function 
that will return the first n elements of the sequence with the given 
common difference d and first element a. Note that the difference may be zero!

The result should be a string of numbers, separated by comma and space.

Example

# first element: 1, difference: 2, how many: 5
arithmetic_sequence_elements(1, 2, 5) == "1, 3, 5, 7, 9"
'''


def arithmetic_sequence_elements(start, difference, quantity):
    newlist = [start]
    for i in range(quantity-1):
         if difference >=0:
             start += difference
             newlist.append(start)
         else:
             start += difference
             newlist.append(start)
    Finalstring = ""
    for i in newlist:
        Finalstring += str(i) + ", "
    c = len(Finalstring)
    return  Finalstring[:c-2]


assert arithmetic_sequence_elements(1, 2, 5) == '1, 3, 5, 7, 9'
assert arithmetic_sequence_elements(1, 0, 5) == '1, 1, 1, 1, 1'
assert arithmetic_sequence_elements(1, -3, 10) == '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'


'''
Ex9
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
'''


def solution(number):
    newlist = [i for i in range(number)]
    forsumming = []
    for s in range(len(newlist)):
        if newlist[s] % 3 and newlist[s] % 5 == 0:
            forsumming.append(newlist[s])
        elif newlist[s] % 3 == 0:
            forsumming.append(newlist[s])
        elif newlist[s] % 5 == 0:
            forsumming.append(newlist[s])
        else:
            pass
    return sum(forsumming)

assert solution(10) == 23


'''
Ex10
My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!

In honor of my grandfather's memory we will write a function using his formula!

Take a list of ages when each of your great-grandparent died.
Multiply each number by itself.
Add them all together.
Take the square root of the result.
Divide by two.
Example

predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
Note: the result should be rounded down to the nearest integer.
'''


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    agelist = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    listforsum = []
    for i in agelist:
        b = i * i
        listforsum.append(b)
    c = sum(listforsum)
    return int(c ** 0.5 / 2)


assert predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86


'''
Ex11
Complete the function so that it takes an array of keys and a default value and returns a dictionary 
with all keys set to the default value.

Example

["draft", "completed"], 0   # should return {"draft": 0, "completed: 0}
'''


def populate_dict(keys, default):
    newdefault = [default for i in range(len(keys))]
    keys = sorted(keys)
    newdict = zip(keys, newdefault)
    newdict = dict(newdict)


    return newdict

assert populate_dict(["draft", "completed"], 0) == {"completed": 0, "draft": 0}
assert populate_dict(["a", "b", "c"], None) == {"c": None, "b": None, "a": None}
assert populate_dict([1, 2, 3, 4], "OK") == {1: "OK", 2: "OK", 3: "OK", 4: "OK"}
