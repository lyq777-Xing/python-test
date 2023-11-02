# 输入函数input

# 语法结构
# 注：不论输入的数据是什么，x的数据类型都是字符串
# x = input('提示语句')

# name = input('请输入姓名：')
# print(name)

num = input('请输入幸运数字：')
# 没有报错，说明num为字符串类型
print('幸运数字为：' + num)
print(type(num))
# 将num转为int类型（使用内置函数转换）
num = int(num)
print('幸运数字为：', num)
print(type(num))

