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

def nb_pos(data,tab_pos, bool):
    row = list(data[0])
    indice = list(data[1])
    s = 0
    nb_try = row.count("?")
    tab_possibilitie = tab_pos[row.count("?")-1]
    tab_position = []
    for index, elem in enumerate(row):
        if elem == '?':
            tab_position.append(index)
    for possibiliti in tab_possibilitie:
        cpt = 0
        for pos in tab_position:
            row[pos] = possibiliti[cpt]
            cpt+=1
        if row.count('#') == sum(indice):
            tab = []
            av = 0
            for i in range(len(row)):
                cpt = 0
                if av != 0:
                    av-=1
                else:
                    while i+av < len(row) and (row[i+av] == '#'):
                        cpt+=1
                        av+=1
                    if cpt != 0:
                        tab.append(cpt)
            if tab == indice:
                if bool < 2:
                    print([row+['?']+list(data[0]),indice+indice])
                    s+= nb_pos([row+['?']+list(data[0]),indice+indice],tab_pos,bool+1)
                else:
                    s+=1
    print(s)
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
    for i in range(19):
        tab_pos.append(all_possibilities(i))
    return tab_pos

tab_pos = generate_pos()
text = open("example.txt").readlines()
data = parser(text)


for row in data:
    # print("ici on fait le calcul de base",nb_pos(row, tab_pos, 1))
    print("ici on fait le calcul de l'etendue",nb_pos(row, tab_pos, 1))