# for a given input. the program should find the previous numbers upto and including itself their squares all in a dictionary

# it should return the output

#num = int(input())
num = 8

dict = dict()

for i in range(num+1):
    dict[i] = i*i

print(dict)


