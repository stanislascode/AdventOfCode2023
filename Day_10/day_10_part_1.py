import sys
down_pipe = ['|','7','F']
right_pipe = ['-','L','F']
left_pipe = ['-','J','7']
up_pipe = ['|','L','J']

sys.setrecursionlimit(1000000)

def copy_text(text):
    i=0
    tableau = []
    for row in text:
        ligne = []
        nb_car = 0
        for car in row:
            if car != '\n':
                ligne.append(car)
            if car == 'S':
                pos_serpent = [i+1,nb_car]
            nb_car+=1
        tableau.append(ligne)
        i+=1
    tableau.insert(0, ['.']*(len(text[0])-1))
    # tableau.insert(len(text), ['.']*(len(text[0])-1))
    return (tableau, pos_serpent)

def connection(car):
    connection = [0,0,0,0]
    if car in down_pipe:
        connection[0] = 1
    if car in right_pipe:
        connection[1] = 1
    if car in left_pipe:
        connection[2] = 1
    if car in up_pipe:
        connection[3] = 1
    return connection

def voisin(data, pos, connected_to, path):
    if connected_to[3] == 1 and data[pos[0]-1][pos[1]] in down_pipe:
        new_pos = [pos[0]-1,pos[1]]
        new_connection = connection(data[pos[0]-1][pos[1]])
        data[pos[0]-1][pos[1]] = 0
        voisin(data,new_pos,new_connection,path)
    if connected_to[2] == 1 and data[pos[0]][pos[1]-1] in right_pipe:
        new_pos = [pos[0],pos[1]-1]
        new_connection = connection(data[pos[0]][pos[1]-1])
        data[pos[0]][pos[1]-1] = 0
        voisin(data,new_pos,new_connection,path)
    if connected_to[1] == 1 and data[pos[0]][pos[1]+1] in left_pipe:
        new_pos = [pos[0],pos[1]+1]
        new_connection = connection(data[pos[0]][pos[1]+1])
        data[pos[0]][pos[1]+1] = 0
        voisin(data,new_pos,new_connection,path)
    if connected_to[0] == 1 and data[pos[0]+1][pos[1]] in up_pipe:
        new_pos = [pos[0]+1,pos[1]]
        new_connection = connection(data[pos[0]+1][pos[1]])
        data[pos[0]+1][pos[1]] = 0
        voisin(data,new_pos,new_connection,path)
    path.append(pos)
    data[pos[0]][pos[1]] = 0
    return path

def print_tab(tableau,path):
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if [i,j] not in path:
                tableau[i][j] = '.'
            print(tableau[i][j], end = " ")
        print("")

def droite_D_gauche_G(tableau,path):
    for index in range(len(path)):
        if path[index+1][0] > path[index][0]:
            if tableau[path[index][0]][path[index][1]+1] != 0:
                tableau[path[index][0]][path[index][1]+1] = 'D'
            if tableau[path[index][0]][path[index][1]-1] != 0:
                tableau[path[index][0]][path[index][1]-1] = 'G'
        # if path[index+1][0] < path[index][0]:
        #     je monte 
        # if path[index+1][1] > path[index][1]:
        #     je vais a droite
        # if path[index+1][1] < path[index][1]:
        #     je vais a gauche


text = open("example.txt").readlines()
data = copy_text(text)
print(data)
path = voisin(data[0],data[1], [1,1,1,1],[])
print_tab(data[0],path)


print(len(path)/2)