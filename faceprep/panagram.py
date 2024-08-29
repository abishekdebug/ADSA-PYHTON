n=input()
k=n.split()
h=len(k)
c=0
for i in range (97,123):
    for j in range (h):
        if chr(i) in k[j]:
            c+=1
if c>=26:
    print("True")
else:
    print("false")


            


