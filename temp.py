# def solve_maze(i=0,j=0):
#     global flage
#     global solved_data

#     n = len(data)
#     if flage:
#         return
    
#     if i == n-1 and j == n-1:
#         flage = True
#         return
    
#     if i<n-1 and solved_data[i+1][j] != "▒" :
#         solved_data[i+1][j] = "☻"
#         solve_maze(i+1,j)
        
#         if flage == False:
#             solved_data[i+1][j] = "."

#     if flage == False and j<n-1 and solved_data[i][j] != "▒":
#         solved_data[i][j+1] = "☻"
#         solve_maze(i,j+1)
#         if flage == False:  
#             solved_data[i][j+1] = "."


[['S', '▒', '.', '.', '.', '.'],['.', '▒', '.', '▒', '▒', '.'],['.', '▒', '.', '▒', '.', '.'],['.', '▒', '.', '▒', '.', '▒'],['.', '▒', '.', '▒', '.', '.'],['.', '.', '.', '▒', '▒', 'E']]