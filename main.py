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
                temp.append("◌")
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
            print("\033[0;31;40m| ",sep='',end='')
            if j == "▒":
                print("\033[0;33;40m",j,' ',sep='',end='')
            elif j == "◌":
                print("\033[0;34;40m",j,' ',sep='',end='')
            else:
                print("\033[0;37;40m",j,' ',sep='',end='')

        print("\033[1;31;40m| ",sep='',end='')

    # last row border with red color
    print("\033[0;31;40m\n",end='')
    print("+---"*n,"+",sep='')
    print("\033[0;37;40m",end='')
    # print()

def highlight(s):
    print()
    print("\033[0;31;40m ------",sep='',end='')
    print("\033[1;33;40m ",s,sep='',end='')
    print("\033[0;31;40m ------",sep='',end='')
    print("\033[0;37;40m",sep='')

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
            solved_data[i+1][j] = "◌"
    
    if flag == False and j < n-1 and solved_data[i][j+1] not in "▒☻":
        solved_data[i][j+1] = "☻"
        # print("right")
        solve(i,j+1)
        if flag == False:
            solved_data[i][j+1] = "◌"

def solve_all_ways(i = 0,j=0):
    global solved_data
    global flag
    n = len(solved_data)

    if flag or (i == n-1 and j == n-1):
        flag = True
        return
    
    if flag == False and i < n-1 and solved_data[i+1][j] not in "▒☻":
        solved_data[i+1][j] = "☻"
        # print("down")
        solve_all_ways(i+1,j)
        if flag == False:
            solved_data[i+1][j] = "◌"

    if flag == False and j < n-1 and solved_data[i][j+1] not in "▒☻":
        solved_data[i][j+1] = "☻"
        # print("right")
        solve_all_ways(i,j+1)
        if flag == False:
            solved_data[i][j+1] = "◌"
    
    if flag == False and i>0 and solved_data[i-1][j] not in "▒☻":
        solved_data[i-1][j] = "☻"
        # print("up")
        solve_all_ways(i-1,j)
        if flag == False:
            solved_data[i-1][j] = "◌"

    if flag == False and j>0 and solved_data[i][j-1] not in "▒☻":
        solved_data[i][j-1] = "☻"
        # print("left")
        solve_all_ways(i,j-1)
        if flag == False:
            solved_data[i][j-1] = "◌"

def int_input(place_holder ="",minimum = float('-inf'),maximum= float('inf')):
    n = 0
    while not n:
        try:
            n = int(input(place_holder))
            while n< minimum or n > maximum:
                print()
                print("enter number between",minimum, "to",maximum)
                n = int(input(place_holder))
        except:
            n = 0
            print()
            print("Enter only number")
    return n

# main programm start here -----
# ○ ▒ ☻
            
highlight("Well-Come To")
highlight("Rat in Maze")
print()

choice = 2
while choice != 3:

    if choice == 2:
        n = int_input("Maze Size?: ",3,15)
        data = generate_maze(n)
        print_maze(data)

    elif choice == 1:
        flag = False
        solved_data = data.copy()

        solve()
        if flag == False:
            solve_all_ways()
        if flag:
            solved_data[-1][-1] = "E"
            
            highlight("Solved Maze")
            print_maze(solved_data)
        else:
            highlight("Rat can't cross the maze 😟")
            print()
        
        flag = False
        solved_data = data.copy()


    if choice != 1:
        print()
        print("1. Print the Path")
        print("2. Generate another Maze")
        print("3. Exit the Game")

        choice = int_input("Enter your choice (1/2/3): ",1,3)
    else:
        print()
        print("1. XXXXXXXXXXXXX")
        print("2. Generate another Maze")
        print("3. Exit the Game")

        choice = int_input("Enter your choice (1/2/3): ",2,3)
print(int_input())