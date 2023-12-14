def preambule(file):
    file = open(file)
    text = file.readlines()
    matrice = []
    
    for i in range(len(text)):
        row = []
        for j in range(len(text[i])):
            row.append([text[i][j],0])
        matrice.append(row)
    return matrice

def ajout_cadre(matrice):
    ligneblanche = []
    for i in range(len(matrice[0])):
        ligneblanche.append(['.', 0])
    
    for i in range(len(matrice)):
        matrice[i].append(['.', 0])
        matrice[i].insert(0,['.', 0])
    matrice.append(ligneblanche)
    matrice.insert(0,ligneblanche)
    return matrice


def parser_gear(matrice):
    tab = []
    for i in range(len(matrice)):
        poscarspe =[]
        for j in range(len(matrice[i])):
            if (matrice[i][j][0]=='*'):
                poscarspe.append(j)
        tab.append(poscarspe)
    return tab

def marquage_case_adj(matrice,tab_poscar):
    nb_gear = 1
    for i in range(len(tab_poscar)):
        for j in range(len(tab_poscar[i])):
            for k in range(9):
                matrice[i+(k//3)-1][tab_poscar[i][j]+(k%3)-1][1] = nb_gear
            nb_gear+=1
    return [matrice,nb_gear]

def nettoyage(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if not(matrice[i][j][0].isdigit()):
                matrice[i][j][1]=0
    return matrice

def marquage_nb_adj(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            
            if matrice[i][j][1] != 0:
                k=0
                gear_nb = matrice[i][j][1]
                while matrice[i][j+k][0].isdigit():
                    matrice[i][j+k][1] = gear_nb
                    k+=1
                k = 0
                while matrice[i][j-k][0].isdigit():
                    matrice[i][j-k][1] = gear_nb
                    k+=1
    return matrice 

def tableau_correspondance(matrice):
    tab = []
    l=0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            nb = []
            if l >0:
                l-=1
            else:
                k=0
                while matrice[i][j+k][1] != 0:
                    nb.append(matrice[i][j+k][0])
                    k+=1
                l = k
            if len(nb)>0:
                tab.append([nb,matrice[i][j][1]])
    return tab

def calcul(tab_gear, nb_gear):

    tab_occurence =[0]*nb_gear
    multi = 0
    for i in range(len(tab_gear)):
        tab_occurence[tab_gear[i][1]]+=1
    for i in range(nb_gear):
        if tab_occurence[i] == 2:
            tab = []
            for j in range(len(tab_gear)):
                if tab_gear[j][1] == i:
                    s = 0
                    for k in range(len(tab_gear[j][0])):
                        s+= int(tab_gear[j][0][k])*10**(len(tab_gear[j][0])-k-1)
                    tab.append(s)
            multi += tab[0]*tab[1]
    return multi


matrice = preambule("input.txt")
matrice = ajout_cadre(matrice)
tab_gear = parser_gear(matrice)
matrice = marquage_case_adj(matrice, tab_gear)[0]
nb_gear = marquage_case_adj(matrice, tab_gear)[1]
matrice = nettoyage(matrice)
matrice = marquage_nb_adj(matrice)
tab_gear = tableau_correspondance(matrice)
result = calcul(tab_gear, nb_gear)
print(result)
