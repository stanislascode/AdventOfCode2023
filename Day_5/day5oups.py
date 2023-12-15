def liste_seed(text):
    return [int(i) for i in text[0].split(":")[1].split("\n")[0].split(" ")[1::]]

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
    result = 10000000000000
    for seed in seed_liste:
        converted_seed = seed
        for i in range(len(dico)):
            for j in range(len(dico[i])):
                if seed in range(dico[i][j][1], dico[i][j][1]+dico[i][j][2]):
                    converted_seed = dico[i][j][0] + seed -dico[i][j][1]
            seed = converted_seed
        result = min(result, seed)
    return result

#text = open("input.txt").readlines()
text = open("example.txt").readlines()

seed = liste_seed(text)
dico1 = dico(text)
print(searchvalue(dico1,seed))