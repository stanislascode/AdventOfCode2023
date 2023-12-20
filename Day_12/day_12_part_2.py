colle_hash = ['#','##','###','####','#####','######','#######','########','#########',]

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

def print_row(row):
    for car in row[0]:
        print(car, end="")
    print("", end=" ")
    for i in range(len(row[1])-1):
        print(row[1][i], end = ",")
    print(row[1][len(row[1])-1])
    

def reduire_expression(row):
    expression = row[0]
    indices = row[1]
    ligne = ''.join(expression)
    if ligne.find('#') < ligne.find('?'):
        for i in range(indices[0]):
            expression[ligne.find('#')+i] = '#'
        expression[ligne.find('#')+indices[0]] = '.'
    for i in range(1,len(expression)+1):
        if expression[len(expression)-i] == '?':
            break
        elif expression[len(expression)-i] == '#':
            for j in range(indices[-1]):
                expression[len(expression)-i-j] = '#'
            if len(expression)-i-indices[-1]>0:
                expression[len(expression)-i-indices[-1]] = '.'
            break

    tab = []
    tab_indice= []
    av = 0
    for i in range(len(expression)):
        cpt = 0
        if av != 0:
            av-=1
        else:
            while i+av < len(expression) and (expression[i+av] == '#'):
                cpt+=1
                av+=1
            if cpt != 0:
                tab.append(cpt)
                tab_indice.append(i)
    for elem in tab:
        if elem == max(indices):
            indice_debut_hash = tab_indice[tab.index(elem)]
            if indice_debut_hash -1 >=0:
                expression[indice_debut_hash-1] = '.'
            if indice_debut_hash+elem < len(expression):
                expression[indice_debut_hash+elem] = '.'
        tab[tab.index(elem)] = 0

    maxim = max(indices)
    indice_sans_max = list(indices)
    for i in range(len(indices)):
        if indices[i] == maxim:
            indice_sans_max[i] = 0


    tab = []
    tab_indice= []
    av = 0
    for i in range(len(expression)):
        cpt = 0
        if av != 0:
            av-=1
        else:
            while i+av < len(expression) and (expression[i+av] == '#'):
                cpt+=1
                av+=1
            if cpt != 0:
                tab.append(cpt)
                tab_indice.append(i)

    for elem in tab:
        if elem > max(indice_sans_max) and elem != maxim:
            if tab_indice[tab.index(elem)]-1 >0 and tab_indice[tab.index(elem)]+maxim < len(expression):
                if expression[tab_indice[tab.index(elem)]-1] == '.':
                    expression[tab_indice[tab.index(elem)]+maxim] = '#'
            if tab_indice[tab.index(elem)]-1+maxim < len(expression) and tab_indice[tab.index(elem)]-1 >0:
                if expression[tab_indice[tab.index(elem)]-1+maxim] == '.':
                    expression[tab_indice[tab.index(elem)]-1] = '#'
        tab[tab.index(elem)] = 0
    return row 

def etendre_expression(row):
    expression = list(row[0])
    indices = list(row[1])
    for i in range(5):
        row[0] = list(row[0]) + list(['?']) +list(expression)
        row[1] = list(row[1])+list(indices)
    return row


def recherche(li, index):
    for i in reversed(range(len(li))):
        if li[i] == index:
            return i
    return len(li)



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
text = open("input.txt").readlines()
data = parser(text)

# for row in data:
#     print_row(etendre_expression(row))
for i in range(2):  
    data[i] = reduire_expression(data[i])
    print_tab(data[i])
