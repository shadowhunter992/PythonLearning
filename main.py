#LEVEL 1

def even_numbers(a,b):
    if (a % 2) == 0 and (b % 2) == 0:
        print(min(a,b))
    else:
        print(max(a,b))

even_numbers(2,5)



def animal_crackers(text):
    words = text.lower().split()
    a = words[0]
    b = words[1]

    if a[0] == b[0]:
        print(True)
    else:
        print(False)


animal_crackers("Crazy cangaroo")

def makes_twenty(a,b):
    if a + b == 20 or a == 20 or b == 20:
        print(True)
    else:
        print(False)


def capname(text1):
    first_half = text1[:3]
    second_half = text1[3:]
    print(first_half.capitalize() + second_half.capitalize())

capname("macdonald")

def master_yoda(reverse):
    jedi = reverse.split()
    print(" ".join(jedi[::-1]))


master_yoda("I am home")

def almost_there(x):
    y = (abs(100-x) <= 10 or (abs(200-x)) <= 10)
    if y == True:
        print(True)

    else:
        print(False)

almost_there(6)



#LEVEL 2

def has_33(ab):
    for i in range(0,len(ab)-1):
        if ab[i] == 3 and ab [i+1] == 3:
            print(True)

        else:
            print(False)

has_33 ([1, 3, 3])

def paper_doll(text2):
    text22 = ""
    for h in text2:
        text22 += h*3
    print(text22)

paper_doll("Mississippi")

def blackjack(s,d,f):
    if sum([s,d,f]) <= 21:
        print(sum([s,d,f]))
    elif 11 in [s,d,f] and sum([s,d,f]) <= 31:
        print(sum([s,d,f])-10)
    elif sum([s,d,f]) >= 21:
        print("BUST")

blackjack(5,50,11)


def summer69(abc):
    result = 0
    add = True

    for num in abc:
        while add:
            if num != 6:
                result += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    print(result)

summer69([6,1,3,5,9,11,12])



