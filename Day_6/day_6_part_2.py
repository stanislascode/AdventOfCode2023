def parser(text):
    Time = ""
    Distance = ""
    Time_list = cleaning_list(text[0].split(":")[1].split("\n")[0].split(" "))
    Distance_list =cleaning_list(text[1].split(":")[1].split("\n")[0].split(" "))
    for i in range(len(Time_list)):
        Time += Time_list[i]
        Distance += Distance_list[i]
    return [int(Time), int(Distance)] 

def traitement(Time, Distance):
    time_spent_push = 0
    while time_spent_push * (Time - time_spent_push) < Distance:
        print(time_spent_push)
        time_spent_push+=100
    time_spent_push -= 100
    while time_spent_push * (Time - time_spent_push) < Distance:
        print(time_spent_push)
        time_spent_push+=1
    return Time -2*(time_spent_push)+1

def cleaning_list(liste):
    while 1:
            try:
                liste.remove( '')
            except:
                return liste
    

text = open("input.txt").readlines()
data = parser(text)
print(traitement(data[0], data[1]))