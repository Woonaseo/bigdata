

a = 3

b = 4

a + b

a * b

a / b


7 % 3

3 % 7

7 / 4

7 // 4 


"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

"Python\'s favorite food is perl"

food = 'python\'s favorite food is perl'
say = "\"python is very easy. \" he says."
say


multiline = "life is too short \nyou need python"
print ( multiline)


multiline = '''
life is too short
you need python
'''
print ( multiline )




head = "Python"
tail = " is fun! "

head + tail


a = "python"
a * 2

print("=" * 50)
print("my program")
print("=" * 50)


a = "Life is too short"
len(a)

a = "Life is too short, You need Python"
len(a)
a[3]
a[0:4]
a[5:7]
a[8:11]
a[12:18]
a[19:22]
a[23:27]
a[28:34]

a[-1]
a[-0]
a[0:4]



a[0:2]
a[5:7]
a[12:17]


a[-1]

a[0:-1]




a = "20010331rainy"
date = a[:8]
weather = a[8:]
date
weather

year = a[:4]
day = a[4:8]
weather = a[8:]

year
day
weather


a = "pithon"
a[1]
a[1] = 'y'
a[1]


a[0]
a[2:]

a[0] + "y" + a[2:]



"I eat %d apples." %3
"I eat %s apples." % "five"


number = 3
"I eat %d apples. " % number

number = 18
day = "three"
"I ate %d apples . so I was sick for %s days" % (number , day)

a = 5
b = "시월이"
c = "귀엽다"

"우리 %s 는 벌써 %d살이 되었다. 정말 %s" %(b , a , c)

"I have %s apples" %3
"rate is %s" %3.234
"Error is %d%%" %98

"%10s" % "hi"
"%-10sjane." % 'hi'

"%0.4f" % 3.42134234




"%10.4f" % 3.41234234 #앞에 10개 뒤에 소숫점 4개까지 표시

"%10.4f" % 3.41234234





"I eat {0} apples" .format(3)

"I eat {0} apples" .format("five")


number = 3
"I eat {0} apples" .format(number)


number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} dyas" .format(number , day)



"I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3)


"I ate {0} apples . so I was sick for {day} days." .format(10 , day=30)

"{0:>10}".format("hi")
"{0:<10}".format("hi")

"{0:^10}" .format("hi") #가운데

"{0:=^10}" .format("hi")



y = 3.41234234
"{0:0.4f}" .format(y)

"{0:>10.5f}" .format(y)
"{0:-^20.3f}" .format(y)
"{{ and }}" .format()






name = "홍길동"
age = 30
f"나의 이름은 {name}입니다. 나이는 {age}입니다."

f"나는 내년이면 {age+1}살이 된다"





d = {'name' : '홍길동' , 'age' : 30 }
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":-<10}'
f'{"hi":->10}'
f'{"hi":*^10}'

y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'
ds = "hello word ahahhahahahha"
len(a)


a = "hobby"
a.count('b')
ds.count("h")


a = "Python is the best choice"
a.find('b')

a.find("i")
ds.find("l")




a = "Life is too short"
a.index('f')
a.index('ㅇ')
a.find('ㅇ')




",".join('abcd')



a = "hi"
a.upper()

b = "HELLO"
b.lower()

a = "       hi        "



m = """

life is too short
you need 
"""

print(m)


a.lstrip()
a.rstrip()
a.strip()


a = "Life is too short"
a.replace("Life","Your leg")

a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(':')
c = "854329-2256948"
c.split('-')



print("lifr \n ddo")


print("=" * 50)
print("my program")
print("=" * 50)


odd = [1, 3, 5, 7, 9]


a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e - [1, 2, ['life', 'is']]




a = [1, 2, 3]
a
a[0]
a[0] + a[2]
a[-1]


a = [1, 2, 3, ['a' , 'b', 'c']]
a[-1]
a[3]

a[-1][0]


a[-1][1]
a[-1][2]

a = [1, 2,['a' , 'b', ['life', 'is']]]

a[2][2][0]




a = [1, 2, 3, 4, 5]
a[0:2]

a = "12345"
a[0:2]




a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
b
c

a = [1, 2, 3]
b = [4, 5, 6]
a  + b 

a * 3
len(a)


del a[1]
a


a = [1, 2, 3]
a[2] = 4
a

a = [1, 2, 3, 4, 5]
del a[2:]
a



a = [1, 2, 3]
a.append(4)
a
a.append("hi")
a
del a[4:]
a
a.append([5,6])
a



a = [1, 4, 3, 2]
a.sort()
a

a = ['a' , 'e' , 'c']
a.sort()
a

a.reverse()
a
a.index('a')

a.reverse()
a

a = [1, 2, 3]
a.insert(0, 4)
a

a.insert(3,5)
a
a.remove(4)
a


a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a
a.remove(3)
a


a = [1,2,3]
a.pop()
a
a = [1, 2, 3]
a.pop(1)
a

a = [1, 2, 3]
b = a * 3

b.count(2)



a = [1, 2, 3]
a.extend([4,5])
a





