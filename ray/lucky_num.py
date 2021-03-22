
def is_lucky_num(n):
    # 返回 n 是否为幸运数

    # 求 n 的位数
    s = str(n)
    length = len(s)

    # 累加求和初始为0
    m = 0
    # 循环计算累加数
    for i in range (0, length):
        # 取第 i 位为 t
        t = int(s[i])
        
        # 计算 t 的几次方
        t2 = t
        j = 1
        while j < length:
            t2 *= t
            j += 1

        # 累加
        m += t2

        # 优化，假如累加值过大，则退出循环
        if m > n:
            break

    # 返回是否为幸运数
    return n == m


def test_input_num():
    # 测试一个数 是否为 幸运数
    ok = False
    while not ok:
        s_input = input("请输入一个数字：")
        try:
            n = int(s_input)
            print("你输入的数字是: ", str(n))
            print(is_lucky_num(n))
            ok = True
        except:
            print("输入错误")
    
    
# test_input_num()


def n_min(n):
    # 计算 n 位数的最小值
    m = 1
    j = 1
    while j < n:
        m *= 10
        j += 1
    return m

def each_digit(t):
    # 返回数字 t 的每一位
    s = str(t)
    lst = []
    for i in range(0, len(s)):
        lst.append(int(s[i]))
    return lst


def lucky_num(n):
    # 求 n 位的幸运数

    # 对 n 的有效性判断，太大的数计算太慢，就不作了 。。。
    if n <= 0 or n > 7:
        return None

    ret_list = []

    # 计算 n 位数的最小值, m
    m = n_min(n)

    for i in range(m, m*10):
        # 遍历 n 位数的每一个数字
        
        # 初始化 n 次方的和为 0
        total = 0
        for k in each_digit(i):
            # 遍历每一位

            # 求 n 次方
            j = 1
            t = k
            while j < n:
                t *= k
                j += 1

            # 求和
            total += t

            # 优化，假如累加值过大，则退出循环
            if total > i:
                break
        
        if total == i:
            ret_list.append(i)

    return ret_list
    

print(lucky_num(5))


# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# []
# [153, 370, 371, 407]
# [1634, 8208, 9474]
# [54748, 92727, 93084]
# [548834]
# [1741725, 4210818, 9800817, 9926315]