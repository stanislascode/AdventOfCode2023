



def parser(text):
    data = []
    for row in text:
        ligne = [[i for i in row.split(" ")[0]], [ int(i) for i in row.split(" ")[1].split("\n")[0].split(",")]]
        data.append(ligne)
    return data

def print_tab(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end = "")
        print("")

def travail(data,tab_pos,bol):
    s = 0
    for row in data:
        initial_row = list(row[0])
        nb_try = row[0].count("?")
        tab_possibilitie = tab_pos[row[0].count("?")-1]
        tab_position = []
        for index, elem in enumerate(row[0]):
            if elem == '?':
                tab_position.append(index)
        for possibiliti in tab_possibilitie:
            cpt = 0
            for pos in tab_position:
                row[0][pos] = possibiliti[cpt]
                cpt+=1
            if row[0].count('#') == sum(row[1]):
                tab = []
                av = 0
                for i in range(len(row[0])):
                    cpt = 0
                    if av != 0:
                        av-=1
                    else:
                        while i+av < len(row[0]) and (row[0][i+av] == '#'):
                            cpt+=1
                            av+=1
                        if cpt != 0:
                            tab.append(cpt)
                if tab == row[1]:
                    if bol < 2:
                        s+= travail([[row[0]+['?']+initial_row, row[1]+list(row[1])]],tab_pos,bol+1)
                    else:
                        s+=1
    return s
                    
                
            
            



def all_possibilities(nb_try):
    L = [['.'],['#']]
    for i in range(nb_try):
        time = int(len(L))
        for j in range(time):
            E = list(L[j])
            E.append('.')
            L.append(E)
            L[j].append('#')
    return L

def generate_pos():
    tab_pos = []
    for i in range(17):
        tab_pos.append(all_possibilities(i))
    return tab_pos

tab_pos = generate_pos()
text = open("example.txt").readlines()
data = parser(text)

# print(data)
# print_tab(data)

print(travail(data,tab_pos,1))