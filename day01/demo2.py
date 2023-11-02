# python中的print会自动换行
a = 100
b = 50
print(90)
print(a)
print(a * b)
print('hello，小李1')
print('''hello，小李2''')
print("hello，小李3")

# 如果不需要换行，则可以直接用逗号隔开，输出的内容会用空格隔开
print(a, b, "小李加油")

# 输出ascii码对应的值
print('b')
# 也会输出字符，因为98对应ASCII表中的b
print(chr(98))

# 用print函数输出中文unicode码
print(ord('李'))

# 使用print函数在在文件中写入内容
# 打开名为demo2.txt的文件，若该文件不存在则会创建文件，并且授予写入权力
fp = open('demo2.txt', 'w')
# 将内容输出（写入）到文件中
print('hello，小李！', file=fp)
# 关闭文件
fp.close()

# print函数的完整语法格式
# print(value,...,sep='',end='\n',file=None)
print("小李", end='-->')
# 因为没有设置结尾，所以会有换行
print("要加油")
# 这样中间没有空格，但是需要注意的是，加号只能连接字符串
print("小李" + "fighting！")
