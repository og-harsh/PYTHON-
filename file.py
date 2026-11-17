file = open('sample.txt','w')
file.write("here we write a command ")
file.write("Hello user of JAVATPOINT")
file.close()

f = open("sample.txt", "r")
r = f.read()
print(r)
f.close()
