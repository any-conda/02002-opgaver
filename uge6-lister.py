
my_name=['vera','liv','andreasen']
print('My first name is '+ my_name[0] +' and my last name is '+my_name[-1] +'. In total, I have '+ str(len(my_name)) +' names.')

a=3
n=5

def power(somthing):
    results=[]
    for i in range(somthing):
        results.append(a**(i+1))
    return results


print(power(n))

def aveerage(num):
    length=len(num)
    return sum(num)/length

print(aveerage(power(n)))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
spring=months[2:5]
summer=months[5:8]
quarter_starts=months[::3]
quarter_ends=months[2::3]
reversed_months= months[::-1]
winter=months[:2] + months[-1:]

dayses=30
def long_months():
    listicle=[]
    for i in range (len(days)):
        if days[i]>dayses:
            listicle.append(months[i])
    return listicle

print(long_months())

names = ['James', 'Julie', 'Josh', 'John', 'Josh', 'Jill', 'Josh', 'Jenny', 'Josh']

def joshcount(list):
    listicle=[]
    for i in range (len(list)):
            if names[i]in 'Josh':
                listicle.append(names[i])
    return len(listicle)

print(joshcount(names))


def duplicator(number,multi):
    listicle=[]
    for i in range (len(number)):
        for x in range (multi):
            listicle.append(number[i])
    return listicle

print(duplicator([4, "B", 3.9], 3))

def duplicator2(number, multi):
    return [item for item in number for _ in range(multi)]

print(duplicator2([4,'no',100],3))



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

def rainfall(r0,r):
    internal=r0
    for i in r:
        if internal+i-2<0:
            internal=0
        else:
            internal=internal+i-2
    return internal

print(rainfall(10,[3,2,1]))


def rainfall2(r0, r):
    internal = r0

    for i in r:
        internal = max(0, internal + i - 2)

    return internal

print(rainfall(10,[3,2,1]))


#thing to be rewrittten with list comprehension

vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = list('abcdefghijklmnopqrstuvwxyz')
consonants = []
for letter in alphabet:
    if letter not in vowels:
        consonants.append(letter)
print(consonants)

def rewrite():
    consonants=[ x for x in alphabet if x not in vowels]
    return consonants

print(rewrite())


names = ["Anne-marie", "Benjamin", "Cirkeline"]
ages = [25, 30, 35]
occupations = ["Engineer", "Doctor", "Artist"]
for name, age, occupation in zip(names, ages, occupations):
    print(f"{name} is {age} years old and works as a {occupation}")


def sum_of_squares(number):
    return sum([x**2 for x in range(1, number + 1)])

print(sum_of_squares(3))

def is_prime(n):
    return all([False for x in range(2, n) if n%x ==0 ])

print(is_prime(4))

def zero_list(n):
    return [0 for x in range(n)]

print(zero_list(3))

def many_zero(multiple,length):
    return [zero_list(length) for x in range(multiple)]

print(many_zero(3,3))

my_list = [1, 2, 3, 4, 5]
for f in [len, min, max, sum]:
    print("f =", f.__name__, ", result =", f(my_list))


my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(my_list[1:4])
print(my_list[4:1])
print(my_list[4:1:-1])

len1 = len('Maja')
len2 = len('Maja ')
len3 = len('')
len4 = len('   ')

print(len1, len2, len3, len4)