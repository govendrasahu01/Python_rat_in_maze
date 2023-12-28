import random

def generat_maze(n):
    data = []
    for i in range(n):
        temp = []
        for j in range(n):
            chance = random.random()
            if chance <= .25:
                temp.append("▒")
            else:
                temp.append("○")
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


print()
print()
print("\033[0;31;40m ------",sep='',end='')
print("\033[1;33;40m Rat in Maze",sep='',end='')
print("\033[0;31;40m ------",sep='',end='')
print()
print()

n = 12
data = generat_maze(n)

print_maze(data)
