text = open("input.txt").readlines()

def parser(text):
    instruction = text[0].split("\n")[0]
    dico = {}
    for row in text[2::]:
        treated_row = row.split("\n")[0].split("=")
        index = row.split("\n")[0].split("=")[0].split(" ")[0]
        guide = treated_row
        guide = [row.split("\n")[0].split("=")[1].split(" ")[1].split("(")[1].split(",")[0],row.split("\n")[0].split("=")[1].split("(")[1].split(")")[0].split(",")[1].split(" ")[1]]
        dico[index] = guide
    return [instruction, dico]

def parcours(instruction, dico):
    result = 'AAA'
    liste_deja_vu = ['ZZZ']
    i = 0
    while result != 'ZZZ':
        print("je suis a la ligne ", result, " j'ai l'instruction ", instruction[i%len(instruction)], " donc je vais vers ")
        if instruction[i%len(instruction)] == 'R':
            result = dico[result][1]
        else:
            result = dico[result][0]

        liste_deja_vu.append(result)
        print(result)
        i+=1
    print(i)


data = parser(text)

parcours(data[0], data[1])