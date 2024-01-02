import numpy as np

text = open("input.txt").readlines()

def parser(text):
    data = []
    tab = []
    for row in text:
        if row[0] == '\n':
            data.append(tab)
            tab = []
        else:
            row_ = []
            for col in row:
                if col != '\n':
                    row_.append(col)
            tab.append(row_)
    data.append(tab)
    return data

def search_row_reflection(data):
    top_data = [data[0]]
    liste_reflection = []
    botom_data = []
    for i in range(1,len(data)):
        botom_data.append(data[i])
    for i in range(1,len(data)):
        mini = min(len(top_data),len(botom_data))
        if top_data[0:mini] == botom_data[0:mini]:
            liste_reflection.append(i)
        del botom_data[0]
        top_data.insert(0,data[i])
    return liste_reflection


def print_tab(tab):
    for row in tab:
        for col in row:
            print(col, end = "")
        print("")

data = parser(text)


def rotate_tab(tab):
    matrice_rotated = [[0 for j in range(len(tab))] for i in range(len(tab[0]))]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            matrice_rotated[j][len(tab)-1-i] = tab[i][j]
    return matrice_rotated

s=0
for tab in data:
    try:
        s+= 100*search_row_reflection(tab)[0]
        # print(search_row_reflection(tab))
    except:
        s+= search_row_reflection(rotate_tab(tab))[0]
        # print(search_row_reflection(rotate_tab(tab)))
print(s)