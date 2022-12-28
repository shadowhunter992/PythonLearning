#HOMEWORK
import string


def vol(rad):
    result = rad ** 3 * 3.14
    result2 = 4/3 * result
    print(result2)
vol(2)

def ran_check(num,low,high):
    if num > low and num < high:
        print(num, "is in the range between", low, "and", high)
    else:
        print(num, "is in not the range between", low, "and", high)

ran_check(9,2,7)

s = "Hello Mr. Rogers, how are you this fine Tuesday?"
def up_low(s):
    spl = s.split()
    uppercase = []
    lowercase = []
    for letter in spl:
        if letter[0].isupper():
            uppercase.append(letter)
        elif letter[0].islower():
            lowercase.append(letter)
    print("The number of uppercase words is", len(uppercase))
    print("The number of lowercase words is", len(lowercase))

up_low(s)

def unique_list(lst):
    lst2 = []
    for num in lst:
        if num not in lst2:
            lst2.append(num)
    print(lst2)

unique_list([1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,4,4,5,5,5,6,6,6,6,6,6,6,7,7,8,8,8,8,8,8,8,8,8,8,9])

def multiply(numbers):
    result = 1
    for num in numbers:
        result = result * num
    print(result)

multiply([1,2,3,-4])

def palindrome(s):
    s = s.replace(" ","").lower()
    revs ="".join(reversed(s))
    if s == revs:
        print(True)
    else:
        print(False)

palindrome("helleh")

def pangram(str1, aplhabet=string.ascii_lowercase):
    str1 = str1.replace(" ","").lower()
    str2 = []
    for let in str1:
        if let not in str2:
            str2.append(let)
    str2 = ("".join(sorted(str2)))


    if str2 == aplhabet:
        print(True)
    else:
        print(False)

pangram("The quick brown fox jumps over the lazy dog")