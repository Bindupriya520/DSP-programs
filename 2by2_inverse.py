p=input("enter row")
a=[[0 for i in range(0,p)] for j in range(0,p)]
c=[[0 for i in range(0,p)] for j in range(0,p)]
e=[[0 for i in range(0,p)] for j in range(0,p)]
for i in range(p):
	for j in range(p):
		a[i][j]=input("enter element")
b=len(a)
if(b==2):
	def det_matrix(a):
		det=(a[0][0]*a[1][1])-(a[1][0]*a[0][1])
		return det
	def inv_matrix(a):
		c[0][0]=a[1][1]
		c[0][1]=(-1*a[1][0])
		c[1][0]=(-1*a[0][1])
		c[1][1]=a[0][0]
		return c
k=det_matrix(a)
print ("det",k)
if(k!=0):
	for i in range(0,p):
		for j in range(0,p):
			inv_matrix(a)
			e[i][j]=((-1/k)*c[i][j])
			print (e[i][j])
			print("\n")


