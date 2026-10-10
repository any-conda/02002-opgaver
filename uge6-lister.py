
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