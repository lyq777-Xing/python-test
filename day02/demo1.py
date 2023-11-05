# 默认是十进制表示整数
num = 987

# 使用二进制表示整数
num1 = 0b1010101

# 使用八进制表示整数
num2 = 0o765

# 使用十六进制表示整数
num3 = 0x87ABF

print(num, num1, num2, num3)

# round可以保留小数，逗号后的1表示保留一位小数
print(round(0.1 + 0.2, 1))

# 复数类型的使用
x = 123 + 456j
# 输出实数部分
print(x.real)
# 输出虚数部分
print(x.imag)