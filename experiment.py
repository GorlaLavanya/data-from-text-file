import re
print("enter how many contacts you want")
text=open("myfile.txt","a+")
n=int(raw_input())
if(n==1):
	text.write('\n')
	name=raw_input("enter the name")
	phoneno=raw_input("enter the phoneno")
	text.write(name+' ')
	text.write(phoneno)
elif(n==2):
	for i in range(1,n+1):
		text.write('\n')
		name=raw_input("enter the name")
		phoneno=raw_input("enter the phoneno")
		text.write(name+' ')
		text.write(phoneno)
else:
	print("maximum two contacts only")
text.close()
text=open("myfile.txt","r+")
for line in text:
	words=line.split()
	print(words)
text=open("myfile.txt","r+")
name=raw_input("enter the name")
for line in text:
	words=line.split()
	if name in words:
		print(line) 	
text.close()