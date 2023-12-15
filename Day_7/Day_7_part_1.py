from collections import Counter
possibilities = "AKQT98765432J"

def parser(text):
    liste_main_bet = []
    for row in text:
        main = row.split("\n")[0].split(" ")
        liste_main_bet.append([main[0],int(main[1])])
    return liste_main_bet

def classement_main(liste_main_bet):
    #search of pairs
    liste_carre = []
    liste_pair = []
    liste_brelan = []
    liste_full = []
    liste_rien = []
    liste_double_pair = []
    liste_cinq = []
    for main in liste_main_bet:
        dico = Counter(main[0])
        combinaison = [0]*6
        nb_jocker=0
        for i in main[0]:
            if i == "J":
                nb_jocker+=1
            else:
                combinaison[dico[i]]+=1/dico[i]
        combinaison = combinaison[2::]
        for i in range(4):
            if combinaison[3-i] != 0 and nb_jocker != 0:
                combinaison[3-i]-=1
                combinaison[3-i+nb_jocker] +=1
                nb_jocker = 0
        if nb_jocker != 0 and nb_jocker != 5:
            combinaison[nb_jocker-1]=1
        if nb_jocker == 5:
            combinaison = [0,0,0,1]
        if int(combinaison[0]) == 1 and combinaison[1] == 0:
            pos=0
            car = 0
            if len(liste_pair)!= 0:
                while pos != len(liste_pair) and possibilities.find(liste_pair[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_pair[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_pair[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_pair.insert(pos,main)
        elif int(combinaison[0]) == 2:
            pos=0
            car = 0
            if len(liste_double_pair)!= 0:
                while pos != len(liste_double_pair) and possibilities.find(liste_double_pair[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_double_pair[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_double_pair[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_double_pair.insert(pos,main)
            
        elif int(combinaison[1]) == 1 and int(combinaison[0]) == 0:
            pos=0
            car = 0
            if len(liste_brelan)!= 0:
                while pos != len(liste_brelan) and possibilities.find(liste_brelan[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_brelan[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_brelan[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_brelan.insert(pos,main)

        elif int(combinaison[0]) == 1 and combinaison[1] == 1:
            pos=0
            car = 0
            if len(liste_full)!= 0:
                while pos != len(liste_full) and possibilities.find(liste_full[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_full[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_full[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_full.insert(pos,main)
        elif int(combinaison[2]) ==1:
            pos=0
            car = 0
            if len(liste_carre)!= 0:
                while pos != len(liste_carre) and possibilities.find(liste_carre[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_carre[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_carre[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_carre.insert(pos,main)
        elif int(combinaison[3]) == 1:
            pos=0
            car = 0
            if len(liste_cinq)!= 0:
                while pos != len(liste_cinq) and possibilities.find(liste_cinq[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_cinq[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_cinq[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
            liste_cinq.insert(pos,main)
        else:
            pos=0
            car = 0
            if len(liste_rien)!= 0:
                while possibilities.find(liste_rien[pos][0][car]) >= possibilities.find(main[0][car]):
                    while car != 4 and possibilities.find(liste_rien[pos][0][car]) == possibilities.find(main[0][car]):
                        car+=1
                    if possibilities.find(liste_rien[pos][0][car]) < possibilities.find(main[0][car]):
                        break
                    pos+=1
                    car = 0
                    if pos == len(liste_rien):
                        break
            liste_rien.insert(pos,main)
    classement = liste_rien+liste_pair+liste_double_pair+liste_brelan+liste_full+liste_carre+liste_cinq
    print(liste_pair)
    s=0
    for i in range(len(classement)):
        s+=(i+1)*classement[i][1]
    return s




text = open("input.txt").readlines()
liste_main_bet = parser(text)
classement = classement_main(liste_main_bet)
print(classement)
