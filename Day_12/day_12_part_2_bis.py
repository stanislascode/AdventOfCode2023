tab_hash = ['#','##','###','####','#####','######','#######','########','#########','##########','###########','############','#############','##############','###############','################','#################']

def parser(text):
    data = []
    for row in text:
        ligne = [[i for i in row.split(" ")[0]], [ int(i) for i in row.split(" ")[1].split("\n")[0].split(",")]]
        data.append(ligne)
    return data

def tri_row(row):
    i = 0
    tableau = []
    while i <len(row):
        while i <len(row) and (row[i] == '.'):
            i+=1
        tab = []
        while i <len(row) and (row[i] != '.'):
            tab.append(row[i])
            i+=1
        if tab != []:
            tableau.append(tab)
    return tableau
    
def reduire_probleme(row):
    bla = [list(i) for i in row[0]]
    blu = list(row[1])

    # print("bla", bla)
    # print("blu",blu)
    # print("row",row[0])
    # print("row1",row[1])

    if len(bla) > 0 and len(blu)>0 and len(bla[-1])==blu[-1]:
        del(bla[-1])
        del(blu[-1])
    if len(bla)>0 and len(blu)>0 and len(bla[0])==blu[0]:
        del(bla[0])
        del(blu[0])
    
    return [bla,blu]

def print_tab(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end = "")
        print("")

text = open("example.txt").readlines()
data = parser(text)

new_data = []
for row in data:
    row[0] = tri_row(row[0])
    for i in range(10):
        row = reduire_probleme(row)
    if row != [[],[]]:
        new_data.append(row)

print(new_data)