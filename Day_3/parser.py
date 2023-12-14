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

def parser3(matrice):
    tab = []
    for i in range(len(matrice)):
        poscarspe =[]
        for j in range(len(matrice[i])):
            if (not(matrice[i][j][0].isdigit() or matrice[i][j][0].isspace() or matrice[i][j][0]=='.')):
                poscarspe.append(j)
        tab.append(poscarspe)
    return tab

def marquage_case_adj(matrice,tab_poscar):
    for i in range(len(tab_poscar)):
        for j in range(len(tab_poscar[i])):
            for k in range(9):
                matrice[i+(k//3)-1][tab_poscar[i][j]+(k%3)-1][1] = 1
    return matrice

def nettoyage(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if not(matrice[i][j][0].isdigit()):
                matrice[i][j][1]=0
    return matrice

def marquage_nb_adj(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            
            if matrice[i][j][1] == 1:
                k=0
                while matrice[i][j+k][0].isdigit():
                    matrice[i][j+k][1] = 1
                    k+=1
                k = 0
                while matrice[i][j-k][0].isdigit():
                    matrice[i][j-k][1] = 1
                    k+=1
    return matrice 

def calcul(matrice):
    s=0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            k=0
            while matrice[i][len(matrice[i])-j-1][1] == 1:
                matrice[i][len(matrice[i])-j-1][1] = 0
                s+=int(matrice[i][len(matrice[i])-j-1][0])*10**k
                k+=1
                j+=1
    return s

matrice = preambule("input.txt")
matrice = ajout_cadre(matrice)
tab = parser3(matrice)
matrice = marquage_case_adj(matrice,tab)
matrice = nettoyage(matrice)
matrice = marquage_nb_adj(matrice)
print(calcul(matrice))
