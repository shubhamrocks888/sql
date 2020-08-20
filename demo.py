## To truncate the file, you can open the file in append mode or write mode.

##with open("demo3.txt",'r') as file:
##    data = file.readlines()

l = ['\nname:shubham\n', '\nage:25\n', '\ncity:bangalore']

for i in l:
    if i.strip('\n')!='age:25':
        print (i)
