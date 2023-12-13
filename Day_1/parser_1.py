def premier_dernier_number(file):
    texte = open(file)
    tab = texte.readlines()
    s=0
    for row in tab:
        digit_in_row =[]
        for number in ["0","1","2","3","4","5","6","7","8","9","zero","one","two","three","four","five","six","seven","eight","nine"]:
            poscar = row.find(number)
            if poscar == -1:
                digit_in_row.append([-1])
            else:
                tabposcar = []
                while poscar != -1:
                    tabposcar.append(poscar)
                    poscar = row.find(number, poscar+1)
                digit_in_row.append(tabposcar)
        posmax = -1
        posmin = len(row)
        min = 0
        max = 0
        for i in range(len(digit_in_row)):
            if digit_in_row[i][0] < posmin and digit_in_row[i][0]!=-1:
                min = i%10
                posmin = digit_in_row[i][0]
            if digit_in_row[i][-1] > posmax and digit_in_row[i][0]!=-1:
                max = i%10
                posmax = digit_in_row[i][-1]
        print(min,max)
        s+= min*10 + max
    return s

# print(premier_dernier_digit("texte_test.txt"))
# print(premier_dernier_digit("texte.txt"))
print(premier_dernier_number("texte.txt"))