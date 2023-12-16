text = open("input.txt").readlines()

def parser(text):
    instruction = text[0].split("\n")[0]
    dico = {}
    liste_begining = []
    for row in text[2::]:
        treated_row = row.split("\n")[0].split("=")
        index = row.split("\n")[0].split("=")[0].split(" ")[0]
        guide = treated_row
        guide = [row.split("\n")[0].split("=")[1].split(" ")[1].split("(")[1].split(",")[0],row.split("\n")[0].split("=")[1].split("(")[1].split(")")[0].split(",")[1].split(" ")[1]]
        if index[2] == 'A':
            liste_begining.append(index)
        dico[index] = guide
    return [instruction, dico, liste_begining]

def parcours(instruction, dico, liste_begining):
    nb_step = 0
    liste_z = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    liste_nb_z = [0]*len(liste_begining)
    not_done_collecting_data = True
    while not_done_collecting_data:
        #print(" ")
        for i in range(6):
            #print("je suis a la ligne ", liste_begining[i], " j'ai l'instruction ", instruction[nb_step%len(instruction)], " donc je vais vers ", end = " ")
            if instruction[nb_step%len(instruction)] == 'R':
                liste_begining[i] = dico[liste_begining[i]][1]
             #   print(liste_begining[i])
            else:
                liste_begining[i] = dico[liste_begining[i]][0]
              #  print(liste_begining[i])
            if liste_begining[i][2] == 'Z':
                liste_nb_z[i]+=1
                if liste_nb_z[i] <=2:
                    liste_z[i][liste_nb_z[i]-1] = nb_step
        cpt=0
        for i in range(len(liste_begining)):
            if liste_nb_z[i] >2:  
                cpt+=1
        if cpt == 6:
            not_done_collecting_data = False        
        nb_step+=1
    ppcm_liste = 1
    for i in range(len(liste_begining)):
        liste_nb_z[i] = liste_z[i][1]-liste_z[i][0]
        ppcm_liste = ppcm(ppcm_liste,liste_nb_z[i])

    return ppcm_liste

def ppcm(a,b):
    p=a*b
    while(a!=b):
        if (a<b): b-=a
        else: a-=b
    return p/a
data = parser(text)

parcours(data[0], data[1], data[2])

