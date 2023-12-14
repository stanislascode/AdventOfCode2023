def scratchgame(file):
    file = open(file)
    text = file.readlines()
    s=0
    for row in text:
        pow = -1
        winning_number = cleaning_list(row.split(":")[1].split("|")[1].split("\n")[0].split(" "))
        my_number = cleaning_list(row.split(":")[1].split("|")[0].split(" "))
        for i in my_number:
            if i in winning_number:
                pow+=1
        s+=round(2**pow)
    print(s)

def addiction(file):
    file = open(file)
    text = file.readlines()
    nb_scratchcard=1
    nb_win = [1]*(len(text))
    current_ticket = 0
    s=0
    for row in text:
        win = 0 
        winning_number = cleaning_list(row.split(":")[1].split("|")[1].split("\n")[0].split(" "))
        my_number = cleaning_list(row.split(":")[1].split("|")[0].split(" "))
        for i in my_number:
            if i in winning_number:
                win+=1
                if(current_ticket == len(nb_win)-1):
                    win = 0
                nb_win[current_ticket+win]+=nb_win[current_ticket]
        current_ticket+=1
    for i in nb_win:
        s+=i
    print(s)

def cleaning_list(liste):
    while 1:
            try:
                liste.remove( '')
            except:
                return liste
            
scratchgame("input.txt")
addiction("input.txt")
        
