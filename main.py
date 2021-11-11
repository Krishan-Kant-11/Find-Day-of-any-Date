a = int(input("Year: "))                       # Input start here.
b = int(input("Month number: "))
c = int(input("Date: "))

def function(a):                               
    if a%4 == 0 and a%100 != 0:
        return "leap"
    elif a%100 == 0 and a%400 != 0:
        return "not leap"
    elif a%100 == 0 and a%400 == 0:
        return "leap"
    else:
        return "not leap"


 # Algorith start here.

d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    #Non-leap Year.
e = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     #Leap Year

totaldays1 = 0
totaldays2 = 0

if function(a) == "leap" :
    for i in e[0:(b-1)]:
        totaldays2 += i
elif function(a) == "not leap" :
    for i in d[0:(b-1)]:
        totaldays1 += i

f = totaldays1 + c
g = totaldays2 + c

j = a -1
y = abs(int(str(j)[-2:]))
m = int((y/4))
n = int(str(j)[:2])
h = int((n*100) % 400)

def century(h) :

    if h == 0:

        return '0'

    elif h == 100:

        return '5'

    elif h == 200:

        return '3'

    elif h == 300:

        return '1'

k = int(century(h))

def last():
    if function(a) == "not leap":
        return (f + y + m + k)%7
    elif function(a) == "leap":
        return (g + y + m + k)%7

def day():
    if last() == 0:
        return "Day: Sunday"
    elif last() == 1:
        return "Day: Monday"
    elif last() == 2:
        return "Day: Tuesday"
    elif last() == 3:
        return "Day: Wednesday"
    elif last() == 4:
        return "Day: Thursday"
    elif last() == 5:
        return "Day: Friday"
    elif last() == 6:
        return "Day: Saturday"

print(day())                                          # Final output.
