file1=open('sample.txt','r')
file2=open('updatedsample.txt','w')

for line in file1:
    if not(line.startswith('coding')):
        file2.write(line)

file1.close()
file2.close()

file2=open('updatedsample.txt','r')
print(file2.read())
file2.close()


