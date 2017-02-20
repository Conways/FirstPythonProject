#
#
#
#
#
#
#
import re
import sys;

a = 2
b = 3

print(a + b);

print(5 ** 2);  ##乘方运算

print(3 % 2);  ##求余

print(5 / 2);  ##除法运算，结果是浮点数

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

########转义   Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('Ru\noob')
print(r'Ru\noob')

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

'''
与Python字符串不一样的是，列表中的元素是可以改变的：
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
'''

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

'''
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
'''

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

x = 15
y = 16
print(x);
x += y;
print(x);

######################

'''
函数功能
'''


def test(a):
    print(a);
test("hello python")


def test(a):
    return a;
print(test(2))



input=input("请输入:")
print("你输入了："+input);


f=open("G:/test.txt","w")
f.write("向tset文本写入字符")
f.close();


f1=open("G:/test.txt","r")
str=f1.read()
print(str);





class people:
    name=''
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age;


    def getName(self):
        return  self.name;



    def getAge(self):
        return  self.age;


peole=people("john",12)


print(peole.getAge())
print(peole.getName())

class oldPeople(people):
    print("aa")

old=oldPeople("conways",18)
print(old.getAge())
print(old.getName())




print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配



'''
CGI示例
'''


