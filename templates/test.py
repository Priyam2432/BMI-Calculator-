l=[7,9,4 ]
k=[[]]
for i in  l:
    k+=[j+[i] for j in k]
for i in range (0,len (k)):
    for j in range(i+1,len(k)):
        if (len(k[i])>len(k[j])):
            t=k[i]
            k[i]=k[j]
            k[j]=t
for i  in k:
    print(i)