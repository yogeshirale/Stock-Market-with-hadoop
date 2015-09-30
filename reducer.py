import sys

dict1={}
max_row=0
for line in sys.stdin:
	line=line.strip('\n')
	line=line.split('#_#_#',1)
	key=line[0]
	var=line[1]
	key=key.strip("[").strip("]")	
	x,y=key.split(',')
	x=x.strip('\'')
	y=y.strip('\'').strip("\n").strip("\r")
	if(x not in dict1):
		dict1[x]=[]
		dict1[x].append([y,var])
	else:
		dict1[x].append([y,var])
	if(int(x)>max_row):
		max_row=int(x)
max_row+=1	
for x in range(max_row):
	value=dict1[str(x)]
	value=sorted(value,key=lambda l:l[0])
	l=[]
	for item in value:
		l.append(item[1])
	print l
	
	
