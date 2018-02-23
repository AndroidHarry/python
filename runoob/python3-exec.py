
import sys # 引入 sys 模块

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# 右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。
a, b = 0, 1
while b < 100:
    print(b, end=',')
    a, b = b, a+b
    
def fab(n):
    if n<1:
        print('输入有误！')
        return -1    
    if n==1 or n==2:
        return 1    
    else:
        return fab(n-1)+fab(n-2)
    
print (fab(10))


# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
'''
print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print(" ")
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2)*5
            print("相当于人类：",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
input("点击 enter 键退出")
'''


'''
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
'''

        
# 同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))


# 在 while … else 在条件语句为 false 时执行 else 的语句块：
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")
    

# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：
'''
flag = 1
while (flag): print ('欢迎访问菜鸟教程!')
print ("Good bye!")
'''

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
while 循环语句和 for 循环语句使用 else 的区别：
1、如果 else 语句和 while 循环语句一起使用，则当条件变为 False 时，则执行 else 语句。
2、如果 else 语句和 for 循环语句一起使用，else 语句块只在 for 循环正常终止时执行！
break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。 实例如下：
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
'''
for letter in 'Runoob': # 第一个实例
    if letter == 'b':
        break
    print ('当前字母为 :', letter)
var = 10 # 第二个实例
while var > 0:
    print ('当期变量值为 :', var)
    var = var -1
    if var == 5:
        break
print ("Good bye!")
'''


sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)


#外边一层循环控制行数
#i是行数
i=1
while i<=9:
     #里面一层循环控制每一行中的列数
     j=1
     while j<=i:
          mut =j*i
          print("%d*%d=%-2d"%(j,i,mut), end="  ")
          j+=1
     print("")
     i+=1


#十进制转化
while True:
    number = input('请输入一个整数(输入Q退出程序)：') 
    if number in ['q','Q']:
        break                #如果输入的是q或Q,结束退出
    elif not number.isdigit():
        print('您的输入有误！只能输入整数(输入Q退出程序)！请重新输入')
        continue         #如果输入的数字不是十进制,结束循环,重新开始
    else :
        number = int(number)
        print('十进制 --> 十六进制 ：%d -> 0x%x' %(number,number))
        print('十进制 -->   八进制 ：%d -> 0o%o' %(number,number))
        print('十进制 -->   二进制 ：%d ->'%number,bin(number))







