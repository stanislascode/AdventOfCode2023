def copy_text(text):
    i=0
    tableau = []
    for row in text:
        ligne = []
        for car in row:
            if car != '\n':
                ligne.append(car)
        tableau.append(ligne)
    return (tableau)


def expantion(text, data):
    empty_row = []
    empty_col = []
    cpt = 0
    for i in range(len(text)):
        if text[i].find("#") == -1:
            empty_row.append(i)

    for j in range(len(text[0])-1):
        this_row = True
        for i in range(len(text)):
            if text[i][j] == '#':
                this_row = False
                break
        if this_row:
            empty_col.append(j)
    cpt = 0
    for i in empty_row:
        data.insert(i+cpt,['.']*(len(text[i])-1))
        cpt+=1
    cpt = 0
    for j in empty_col:
        for i in range(len(text)+len(empty_row)):
            data[i].insert(j+cpt,'.')
        cpt+=1
    return(empty_row,empty_col)

def galaxie_position(data):
    pos_galaxie = []
    cpt = 1
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                data[i][j] = cpt
                cpt+=1
                pos_galaxie.append([i,j])
    return pos_galaxie


def print_tab(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end = "")
        print("")

def calcul_distance_min(pos_galaxie,):
    s = 0
    cpt=1
    for i in range(len(pos_galaxie)):
        for j in range(i,len(pos_galaxie)):
            s+=abs(pos_galaxie[i][0]-pos_galaxie[j][0])+abs(pos_galaxie[i][1]-pos_galaxie[j][1])
            print(" entre ",i," et ", j, " il y a une distance de ",abs(pos_galaxie[i][0]-pos_galaxie[j][0])+abs(pos_galaxie[i][1]-pos_galaxie[j][1]))
    return s

text = open("example.txt").readlines()
data = copy_text(text)
expantion(text, data)
pos_galaxie = galaxie_position(data)
print(calcul_distance_min(pos_galaxie))

