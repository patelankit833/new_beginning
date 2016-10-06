#Exercise 10
print 'Exercise 1'

count=0
lst=list()
daysdict=dict()
emaildict=dict()
hourdict=dict()
tuplelst=list()
hrslst=list()
filename=raw_input('Enter file name:')
try:
	fhandle=open(filename)
except:
	print 'File name is incorrect'
	exit()

for line in fhandle:
	lst=line.split()
	if ((len(lst)!=0) and (lst[0]=='From')):
		email=lst[1]
		emaildict[email]=emaildict.get(email,0)+1
		time=lst[5]
		septime=time.split(':')
		hour=septime[0]
		hourdict[hour]=hourdict.get(hour,0)+1

for key,val in emaildict.items():
	tuplelst.append( (val,key))
tuplelst.sort(reverse=True)

for hrs,total in hourdict.items():
	hrslst.append((total,hrs))
hrslst.sort(reverse=True)

print max(emaildict), emaildict[max(emaildict)]
print tuplelst[0]
print hourdict.sort()

