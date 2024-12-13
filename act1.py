#readd its content
file=open('sample.txt','r')
print(file.read())
file.close()
#read only first  8  chracters
file=open('sample.txt','r')
print(file.read(8))
file.close()

#append name to the file
file=open('sample.txt','a')
file.write('\nDivisha')
file.close()

file=open('sample.txt','r')
print(file.read())
file.close()