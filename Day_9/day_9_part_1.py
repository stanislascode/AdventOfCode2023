text = open("input.txt").readlines()

def parser(text):
    tableau = []
    for row in text:
        tableau.append([int(i) for i in cleaning_list(row.split(" "))])
    return tableau

def continu_story(story):
    if len(story) == 1:
        return 0
    new_story = []
    for i in range(len(story)-1):
        new_story.append(story[i+1]-story[i])
    return story[-1] + continu_story(new_story) 
         

def cleaning_list(liste):
    while 1:
            try:
                liste.remove( '')
            except:
                return liste

data = parser(text)
sum = sum([continu_story(story) for story in data])
print(sum)