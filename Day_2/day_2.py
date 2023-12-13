def parser_texte(file):
    file = open(file)
    text = file.readlines()
    nb_game = 0
    allgame = []
    for row in text:
        tableau = []
        nb_manches = row.count(";")
        print("Game ",nb_game+1,": ",end = " ")
        for i in range(nb_manches+1):
            tableau.append([0,0,0])
        posgreen = 0
        posblue = 0
        posred = 0
        possep = 0
        newpossep = 0
        for i in range(nb_manches+1):
            if i < nb_manches:
                possep = newpossep
                newpossep = row.find(";", possep+1)
                posgreen = row.find("green", possep, newpossep)
                posred = row.find("red", possep, newpossep)
                posblue = row.find("blue",possep,newpossep)
            else:
                posgreen = row.find("green", newpossep)
                posred = row.find("red", newpossep)
                posblue = row.find("blue",newpossep)

            if posgreen != -1:
                cpt = 0
                while row[posgreen-2-cpt].isdigit():
                    cpt+=1
                print(row[posgreen-1-cpt:posgreen-1], " vert," , end=" ")
                tableau[i][0] = int(row[posgreen-1-cpt:posgreen-1])
            if posblue != -1:
                cpt = 0
                while row[posblue-2-cpt].isdigit():
                    cpt+=1
                print(row[posblue-1-cpt:posblue-1], " bleu," , end=" ")
                tableau[i][1] = int(row[posblue-1-cpt:posblue-1])
            if posred != -1:
                cpt = 0
                while row[posred-2-cpt].isdigit():
                    cpt+=1
                print(row[posred-1-cpt:posred-1], " red," , end=" ")
                tableau[i][2] = int(row[posred-1-cpt:posred-1])
            print(";", end= "")
        print("")
        nb_game+=1
        allgame.append(tableau)
    
    return allgame
def is_it_possible(tableau, green, blue, red):
    s = 0
    for nb_game in range(len(tableau)):
        game_is_possible = True
        for manche in tableau[nb_game]:
            if manche[0] > green:
                game_is_possible = False
            if manche[1]>blue:
                game_is_possible = False
            if manche[2] > red:
                game_is_possible = False
        if game_is_possible:
            s+= nb_game+1
    return s

def sum_of_power(tableau):
    s = 0
    for nb_game in range(len(tableau)):
        red = 0
        blue = 0
        green = 0
        for manche in tableau[nb_game]:
            green = max(manche[0], green)
            blue = max(manche[1],blue)
            red = max(manche[2], red)
        s+=green*blue*red
    return s

table = parser_texte("liste_game.txt")
print(is_it_possible(table,13,14,12))
print(sum_of_power(table))