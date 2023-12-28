import random

def generate_maze(n):
    data = []
    for i in range(n):
        temp = []
        for j in range(n):
            chance = random.random()
            if chance <= .25:
                temp.append("▒")
            else:
                temp.append(".")
        data.append(temp)
    data[0][0] = "S"
    data[-1][-1] = "E"
    return data

def print_maze(data):
    n = len(data)
    for i in range(n):
        print("\033[0;31;40m\n",end='')
        print("+---"*n,"+",sep='',end='')
        print("\033[0;37;40m\n",end='')

        temp = data[i]
        for j in temp:
            print("\033[1;31;40m| ",sep='',end='')
            print("\033[1;37;40m",j,' ',sep='',end='')
        # print("|",end='')
        print("\033[1;31;40m| ",sep='',end='')

    # last row border with red color
    print("\033[0;31;40m\n",end='')
    print("+---"*n,"+",sep='')
    print("\033[0;37;40m\n",end='')
    print()

def print_banner():
    print()
    print()
    print("\033[0;31;40m ------",sep='',end='')
    print("\033[1;33;40m Rat in Maze",sep='',end='')
    print("\033[0;31;40m ------",sep='',end='')
    print()
    print()

def solve(i = 0,j=0):
    global solved_data
    global flag
    n = len(solved_data)

    if flag or (i == n-1 and j == n-1):
        flag = True
        return
    
    if i < n-1 and solved_data[i+1][j] not in "▒☻":
        solved_data[i+1][j] = "☻"
        # print("down")
        solve(i+1,j)

        if flag == False:
            solved_data[i+1][j] = "."
    
    if flag == False and j < n-1 and solved_data[i][j+1] not in "▒☻":
        solved_data[i][j+1] = "☻"
        # print("right")
        solve(i,j+1)
        if flag == False:
            solved_data[i][j+1] = "."
    
    if flag == False and i>0 and solved_data[i-1][j] not in "▒☻":
        solved_data[i-1][j] = "☻"
        # print("up")
        solve(i-1,j)
        if flag == False:
            solved_data[i-1][j] = "."

    if flag == False and j>0 and solved_data[i][j-1] not in "▒☻":
        solved_data[i][j-1] = "☻"
        # print("left")
        solve(i,j-1)
        if flag == False:
            solved_data[i][j-1] = "."

# main programm start here -----
    # ○
    # ▒
    # ☻

print_banner()
n = 6
data = generate_maze(n)
# data = [['S', '▒', '.', '.', '.', '.'],['.', '▒', '.', '▒', '▒', '.'],['.', '▒', '.', '▒', '.', '.'],['.', '▒', '.', '▒', '.', '▒'],['.', '▒', '.', '▒', '.', '.'],['.', '.', '.', '▒', '▒', 'E']]

print_maze(data)

flag = False
solved_data = data
solve()
print(flag)
print_maze(solved_data)
