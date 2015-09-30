import sys

for line in sys.stdin:
	line=line.split(',')
	x=line[2]
	y=line[3]
	var=float(line[1])-float(line[0])
	print '%s#_#_#%s' % (str([x,y]), str(var))
