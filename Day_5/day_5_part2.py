def liste_seed_range(text):
    liste = [int(i) for i in text[0].split(":")[1].split("\n")[0].split(" ")[1::]]
    liste2 = []
    for i in range(len(liste)//2):
        liste2.append([liste[2*i],liste[2*i]+liste[2*i+1]])
    return liste2

keyword = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location", "fin"]

def dico(text):
    table_conversion = []
    for i in range(7):
        table_conversion_inter = []
        debut = find(text, keyword[i])
        fin = find(text, keyword[i+1])-2
        for row in text[debut:fin]:
            convertisseur = row.split("\n")[0].split(" ")
            table_conversion_inter.append([int(convertisseur[i]) for i in range(3)])
        table_conversion.append(table_conversion_inter)
    return table_conversion

def find(text, texte):
    found = False
    index_row = 0
    for row in text:
        if found:
            return(index_row)
        else:
            if row.find(texte) != -1:
                found = True
        index_row+=1
    return index_row

def searchvalue(dico, seed_liste):
    tableau_final_seed = []
    for seed in seed_liste:
        print("pour la seed :", seed)
        previous_converted_seed_table = [seed]
        tableau_final = []
        for i in range(len(dico)):
            new_converted_seed_table = []
            for j in range(len(previous_converted_seed_table)):
                new_converted_seed_table = new_converted_seed_table + convert_one_seed(previous_converted_seed_table[j], dico[i])
            tableau_final.append(new_converted_seed_table)
            previous_converted_seed_table = new_converted_seed_table
        tableau_final_seed.append(tableau_final)
        print(tableau_final)
    return tableau_final_seed

#text = open("input.txt").readlines()
text = open("input.txt").readlines()


def convert_one_seed(seed, dico):
    converted_seed = []
    decompo_isnt_finished = True
    while decompo_isnt_finished:
        dico_change_rien = 0
        for j in range(len(dico)):
            if decompo_isnt_finished:
                if seed[0] in range(dico[j][1], dico[j][1]+dico[j][2]):
                    if seed[1] in range(dico[j][1], dico[j][1]+dico[j][2]):
                        converted_seed.append([dico[j][0] + seed[0] -dico[j][1], dico[j][0] + seed[1] -dico[j][1]]) 
                        decompo_isnt_finished = False
                    else:
                        converted_seed.append([dico[j][0] + seed[0] -dico[j][1], dico[j][0]+dico[j][2]])
                        seed[0] = dico[j][1]+dico[j][2]
                elif dico[j][1] in range(seed[0], seed[1]+1):
                    if dico[j][1]+dico[j][2]-1 in range(seed[0], seed[1]):
                        pass
                    else:
                        converted_seed.append([dico[j][0] , seed[1] + dico[j][0] -dico[j][1]])
                        seed[1] = dico[j][1]-1
                else:
                    dico_change_rien+=1
                    if(dico_change_rien == len(dico)):
                        converted_seed.append([seed[0] , seed[1]])
                        decompo_isnt_finished = False
    return converted_seed


def tri_table(table):
    min = table[0][0]
    for i in table:
        if i[0] < min:
            min = i[0]

    return min


seed = liste_seed_range(text)
dico1 = dico(text)

def analyse(seed, dico):
    converted_seed = [seed]
    for i in range(7):
        new_converted_seed = []
        for j in converted_seed:
            new_converted_seed += convert_one_seed(j,dico[i])
        converted_seed = new_converted_seed
    return converted_seed

def analyse_finale(seed_liste,dico):
    min = 10000000000
    for seed in seed_liste:
        if tri_table(analyse(seed,dico))<min:
            min = tri_table(analyse(seed,dico))
    return min


table = analyse(seed[0],dico1)
print(analyse(seed[0],dico1))
print(tri_table(table))
print(analyse_finale(seed, dico1))

