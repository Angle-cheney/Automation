"""Python基础"""
print('Life your short, you need Python!')

print("3-4_常用的数据类型")

"""整数"""
a = 444
print(a)

"""浮点数"""
a = 4.44
b = 4.44
print(a+b)

"""字符串"""
a = "LuckyHo"
b = 'LuckyHo'
print(a,b)

"""转义字符"""
a = 'Lucky \n Ho' #换行
b = 'C:\\python' #路径读取
print(a,b)

"""布尔值"""
#逻辑判断
a = True
b = False
print(a and b)
print(a or b)


print("3-5_数组定义与访问")

"""数组(list)"""
#定义：是一种有序的集合，可以随时添加和删除其中的严肃
a = ['Jack','Mark','Jams']
print(a)

#访问数据元素
a = ['Jack','Mark','Jams']
print(a[-1])      #访问最后一个-1
print(a[1])
#!!!注意索引不要越界


print("3-6_数组元素添加修改删除")
#添加元素
b = ['Jack','Mark','Jams']
b.append('Tony')    #末尾添加
b.insert(0,'Aris')  #指定位置添加元素
b[0] = 'Tom'        #修改元素
b.pop()   #末尾删除元素
b.pop(1)  #删除指定元素
print(b)
#！！！通过索引访问数据

print("3-7_元组数据")
#定义：元组与列表相似，不同之处在于元组的元素一旦定义不能修改，元组使用小括号，列表使用方括号。元组创建很简单，主需要在括号中添加元素，并使用逗号隔开即可

c = ('Jack','Mark','Jams')
d = ('22','33','44')
print(c)
print(c[1])
print(c[-1])  #显示最后一个元素
print(c[1:3]) #显示1-2的元素
print(c[1:])  #显示1之后的元素
print(c[:1])  #显示1之前的元素
print(len(c)) #通过len方法，能够显示元组中元素的个数
print(max(d))
#！！！通过索引访问数据



print("3-8_字典")
#定义：字典时另一种可变的容器模型，且可存储任意类型数据，字典的每个键值对（key=values)用（：）分割，每个对之间用（，）分割，整个字典包括在花括号{}中
#     键必须是唯一的，但值却未必，只可以取任何数据类型，但键必须是不可变的，
e = {1:'Jack',2:'Mark',3:'Jams'}
print(e[2])     #显示键对应的值
e[3] = 'Aris'   #添加字典
e[1] = 'JackMa' #编辑字典
del e[1]        #删除字典中的元素
e.clear()       #清空字典中的元素
#del e           #删除字典
print(e)

#！！！通过键来访问数据


print("3-9_条件判断")
#if语句用户控制程序的执行
f = 44
if f>44:
    print("成绩及格！")
else:
    print("成绩不合格！")

#elif就是else if 的缩写，完全可以有多个elif

g = 44
if g > 44:
    print("恭喜！")
elif g <= 44:
    print("刚好及格 ！")
else:
    print("遗憾！")


print("3-10_循环语句")
#允许我们执行一个语句或语句组多次，提供了for和while循环

#for循环，将数组中的值全部打印出来
h = ['Jack','Mark','Jams']
for h1 in h:
    print(h1)

#range循环，可以生成整数数列，比如range(10)生成的序列是从0开始小于10的证书
sum = 0
for i in range(11):
    sum = sum+i
print(sum)

#while循环，只要条件满足，就不断循环，条件不满足就退出循环

i = 10
while i>0:
    i = i-1
    print(i)
print("Over!")

"""
print("3-11_实例_猜数小游戏")
#生成一个指定范围的随机数，然后玩家输入数值猜答案，屏幕会根号有玩家输入的数字给出大小提示，一直到玩家猜出准确答案，则代表游戏胜利并结束

#生成随机数
import random
answer = random.randint(1,100)

#玩家输入数值
n = int(input("Please input number(1-100): "))

#判断输入数字的大小
while n != answer:
    if n > answer:
        n = int(input("Number is More Please Continue input number: "))
    elif n < answer:
        n = int(input("Number is Less Please Continue input number: "))

#输入答案正确，游戏结束
print("You Win the Game")
"""


print("3-12_函数定义与调用")
#函数是组织好的，可重复使用，用来实现单一，或相关功能的代码块，能提高应用的模块性，和代码重复利用率，如print(),range()也可以自定义函数
#函数定义：定义函数Max_num（），用来比较两个数字的大小，将数值的的数字返回
def Max_num(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

result = Max_num(10,4)
print(result)

print("3-13_面向对象（1）")

name = 'Jack'
city = 'Beaijing'
age = 19
print("MY name is %s and come from %s today now age %i" %(name,city,age))  #字符串类型%s整数类型%i
print("Hello LuckyHo!")

name = 'Mark'
city = 'Shanghai'
age = 44
print("MY name is %s and come from %s today now age %i" %(name,city,age))  #字符串类型%s整数类型%i
print("Hello LuckyHo!")

#思考？
#1.如果老师要求全班50个同学以此以以上形式自我介绍，怎么办？
#2.每个同学介绍自己姓名和城市和年纪后，再顺便介绍一下自己的性别？
#3.每个同学自我介绍的代码块有何特征

"""
print("3-14_面向对象（2）")
#现实生活中，随处可见的事物就是对象，对象是事物存在的实体，如：人类，汽车，动物，都是一个抽象的类别，我们所见的实物都是这些类的具体存在，
#因此类是对象的抽象集合，对象是类的具体表现，现实世界是万物皆对象！
#学生：属性-姓名、学号、城市。功能-听、说、读、写。具体对象-Jack、mark

#类（class）：用来描述相同属性和方法的对象的集合，定义了该集合中每个对象所共有的属性和方法
#数据成员：类的不同属性数据
#对象：类的实例
#方法：类中定义的函数，实现相关的功能

#面向对象变成，简称OOP，是一种程序设计思想，是把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
#面向对象设计思想是从自然中来的，类class和实例Instance的概念也是很自然的，class是一种抽象概念，比如我们定义Student类，是指学生这个概念，
#而实例Instance则是一个个体的Student对象
#三大特征：封装、继承、多态
"""

print("3-15_Python类与对象")

"""
定义类：class Student(object):
class是类的定义的关键词，后边紧跟类名，类名通常是大写开头的单词，紧接着是object，表示该类是从哪个类继承的，通常如果没有明确的继承类，就是要object
括号内一般为空默认就是继承object类，这是所有类最终都会继承的类，也就是基类。

属性初始化：
由于类起到模板的作用，因此，可以创建实例对象的时候，把一些认为必须绑定的属性强制填写进去.通过定义一个特殊的__init__方法
如：在创建student实例的时候，就把name，city等属性绑定上

__init__方法的第一个参数永远是self，表示创建实例本身，因此在这个方法内部，就可以把各种属性绑定到self，因为self就是指向创建的实例本身，有了这个方法
在创建实例的时候，就不能传入空的参数了，必须传入__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进入

定义方法：
类的方法除了第一个参数是self外，其他和普通函数一样，要调用一个方法，只需要在实例变量了直接调用

生成实例：

stu1=Student('Aris','Beijing')
stu1.talk()
"""

class Student():
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.age = age
        print("MY name is %s and come from %s" %(name,city))

    def talk(self):
        print("Hello LuckyHo!")

stu1=Student('Aris','Beijing')
stu1.talk()


print("3-16_Python模块引用")
"""
为何使用模块？
随着项目和需求增对，代码量会增大，把全部代码放在一个文件显得荣誉，因此需要使用模块进行分区管理
Python模块是什么？
Python的模块module是一个python文件，以py结尾，包含了Python对象定义和语句
使用模块的好处？
最大的好处是提高了代码的可维护性，其次，编写代码不必从零开始，当一个模块编写完毕，就可以被其他模块引用，如：时间模块，随机数模块
"""
import time
print(time.ctime())
from time import sleep
sleep(1)

print("3-17_Python跨模块调用")
from untitled.Drive.Myunittest import Lucky