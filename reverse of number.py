#homework
a="1","2","3","4","5","6","7","8","9","10"
rev=''

for i in range (len(a)-1,-1,-1):
    print(a[i])
    rev=rev+a[i]
print(rev)
