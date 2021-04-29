
d9 = 9
a = [[0,8,0,0,0,0,0,5,0], 
     [3,0,0,0,9,0,0,1,2],
     [4,0,7,0,0,0,0,0,0],
     [7,0,0,0,0,3,0,0,6],
     [1,0,0,9,0,0,0,7,0],
     [0,4,2,0,5,0,0,0,0],
     [0,0,0,2,0,0,6,0,0],
     [0,0,0,8,0,0,0,0,0],
     [8,0,0,0,1,4,9,2,0]]


def print_ground():
    '''
    打印整个题目
    '''
    for i in range(len(a)):
        if i % 3 == 0:
            print('--'*d9+'----')
        
        for j in range(len(a[i])):
            if j % 3 == 0:
                print('|', end='')
            print(a[i][j], end=' ')
        print('|')

    print('--'*d9+'----')


def check_get_next_fill_pos(row, col):
    '''
    从 (row, col) 这个位置开始找可以填写的下一个位置
    '''
    
    # 先找当前行的可填位置
    for j in range(col, d9):
        if a[row][j] == 0:
            return row, j

    # 再从当前行的下一行开始找下一个可填的位置
    for i in range(row+1, d9):
        for j in range(d9):
            if a[i][j] == 0:
                return i, j

    return -1, -1


def can_fill_digital(row, col, val):
    '''
    位置 (row, col) 是否可填 val
    '''
    # 判断入参的有效性
    if val <= 0 or val > d9 or row < 0 or row >= d9 or col < 0 or col >= d9:
        return False

    # 已经填过值了
    if a[row][col] != 0:
        return False

    # 检查行
    for i in range(d9):
        if a[row][i] == val:
            return False

    # 检查列
    for j in range(d9):
        if a[j][col] == val:
            return False

    # 检查 (row, col) 所在的三角形
    r = (row // 3) * 3
    c = (col // 3) * 3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if a[i][j] == val:
                return False
    
    return True


def get_fillable_digital(row, col):
    '''
    得到 (row, col) 的可填数字列表
    '''
    lst = []
    for val in range(d9):
        if can_fill_digital(row, col, val+1):
            lst.append(val+1)
    return lst


def try_fill_digital(row, col):
    '''
    递归填空
    '''
    row, col = check_get_next_fill_pos(row, col)
    if row == -1 or col == -1:
        return True     # 没有可填的空格了

    can_fill_lst = get_fillable_digital(row, col)
    if not can_fill_lst:
        return False    # 没有可填的数字了

    for val in can_fill_lst:
        a[row][col] = val
        if try_fill_digital(row, col):
            return True

    a[row][col] = 0

    return False


print_ground()
# print(check_get_next_fill_pos(8, 4))
# print(get_fillable_digital(8, 4))
if (try_fill_digital(0, 0)):
    print('可以填写，答案如下：')
    print_ground()
