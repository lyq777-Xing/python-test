# \n表示换行

print("hello\tlyq")

print("hello:\'111\'")

print("hello:\"111\"")

# r或R会使转义字符失效

# 字符串的索引和切片
s = 'hello,lyq!'
# 实际上0和-10表示的是同一个字符 负数是从右边开始数的
print(s[0], s[-10])
# 获取字符串索引为7的字符
print('hello,lyq'[8])
# 冒号前面没有数字表示从0开始的
print(s[:5])
# 冒号右边没有数字 默认切片到最后一个
print(s[5:])

x = 'hi~'
y = 'lyq'
# 链接x和y两个字符串
print(x + y)
# 对x的内容复制十次
print(x * 10)
# 判断前面一个字符串是否为后面一个字符串的字串
print('q' in y)

print("--------------------------")

# 非零的整数布尔值都为True
print(bool(0), bool(1))
print(True)
print(False)
print(True + 10)
# None的布尔值也为False
print(bool(None))

print("--------------------------")

# 进制之间的转换
print('十进制转为十六进制--', hex(26472))
print('十进制转为八进制--', oct(26472))
print('十进制转为二进制--', bin(26472))

print("--------------------------")

s1 = '3.14 + 7'
print(s1, type(s1))
# eval的函数是去掉s1这个字符串左右两边的引号
x = eval(s1)
print(x, type(x))
# eval函数经常与input()函数一起使用，用于获取用户输入的数值
# 将字符串类型转为int类型，相当于int(age)
age = eval(input('请输入您的幸运数字：'))
print(age, type(age))

print("--------------------------")

# python支持系列解包赋值
a, b = 10, 20
print(a, b)
print('交换两个变量的值:')
a, b = b, a
print(a, b)

print("--------------------------")

print("98大于90吗？", 98 > 90)
print("98小于90吗？", 98 < 90)
print("98等于90吗？", 98 == 90)
print("98不等于90吗？", 98 != 90)
