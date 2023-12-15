def parser(text):
    Time_list = [int(i) for i in cleaning_list(text[0].split(":")[1].split("\n")[0].split(" "))]
    Distance_list = [int(i) for i in cleaning_list(text[1].split(":")[1].split("\n")[0].split(" "))]
    return [Time_list, Distance_list] 

def traitement(Time_list, Distance_list):
    s = 1
    for index in range(len(Time_list)):
        distance_beat = 0
        for time_spent_push in range(1,Time_list[index]):
          #print("en appuyant ",time_spent_push ," milisecondes on avance de ",time_spent_push * (Time_list[index] - time_spent_push) ," milimetre")
          if time_spent_push * (Time_list[index] - time_spent_push) > Distance_list[index]:
              distance_beat +=1
        s = s*distance_beat
    return s


def cleaning_list(liste):
    while 1:
            try:
                liste.remove( '')
            except:
                return liste

text = open("input.txt").readlines()
data = parser(text)
print(traitement(data[0], data[1]))