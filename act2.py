#read 1st line of file
file=open('sample.txt','r')
print(file.readline())
file.close()


#read first 3 lines i n file
file=open('sample.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('sample.txt','r')
for line in file:
    print(line)

file.close()