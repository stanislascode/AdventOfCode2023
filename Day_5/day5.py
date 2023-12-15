def liste_seed(text):
    return text[0].split(":")[1].split("\n")[0].split(" ")[1::]

def dico_seed_to_soil(text):
    dico ={}
    debut = find(text, "soil")
    fin = find(text, "fertilizer")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

def dico_soil_to_fertilizer(text):
    dico ={}
    debut = find(text, "fertilizer")
    fin = find(text, "water")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

def dico_fertilizer_to_water(text):
    dico ={}
    debut = find(text, "water")
    fin = find(text, "light")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico 

def dico_water_to_light(text):
    dico ={}
    debut = find(text, "light")
    fin = find(text, "temperature")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

def dico_light_to_temperature(text):
    dico ={}
    debut = find(text, "temperature")
    fin = find(text, "humidity")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

def dico_temperature_to_humidity(text):
    dico ={}
    debut = find(text, "humidity")
    fin = find(text, "location")-2
    for row in text[debut:fin]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

def dico_humidity_to_location(text):
    dico ={}
    debut = find(text, "location")
    for row in text[debut::]:
        convertisseur = row.split("\n")[0].split(" ")
        for i in range(int(convertisseur[2])):
            dico[int(convertisseur[1])+i] = int(convertisseur[0])+i
    return dico

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

text = open("input.txt").readlines()
#text = open("example.txt").readlines()

seed = liste_seed(text)
dico1 = dico_seed_to_soil(text)
dico2 = dico_soil_to_fertilizer(text)
dico3 = dico_fertilizer_to_water(text)
dico4 = dico_water_to_light(text)
dico5 = dico_light_to_temperature(text)
dico6 = dico_temperature_to_humidity(text)
dico7 = dico_humidity_to_location(text)

def searchvalue(dico, seed):
    try:
        to = dico[seed]
    except:
        to = seed
    return to

result = 10000
for i in range(len(seed)):
    result = min(result, searchvalue(dico7,searchvalue(dico6,searchvalue(dico5,searchvalue(dico4,searchvalue(dico3,searchvalue(dico2,searchvalue(dico1, int(seed[i])))))))))

print(result)