import os
from unicodedata import numeric

print(os.getcwd())

f = open("01/input.txt")
string = f.read()

finalResult = 0

spelledDigits = [["one",1], ["two",2], ["three",3], ["four",4], ["five",5],[ "six",6], ["seven",7], ["eight",8], ["nine",9]]

for line in string.split('\n'):
    tab = []
    tab = [-1 for i in range(len(line))]
    for digit in spelledDigits:
        for i in range(len(line)):
            index = line.find(digit[0],i);
            if index != -1:
                tab[index] = digit[1]
            if line[i].isnumeric():
                tab[i] = numeric(line[i])
               
    tab = list(filter((-1).__ne__, tab))
    lineResult = (10*tab[0]) + tab[len(tab)-1]
    finalResult += lineResult
    print(line+":"+str(tab)+":"+str(lineResult)+"=>"+str(finalResult))

print(finalResult)
        



