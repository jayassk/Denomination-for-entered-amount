#Denomination for entered amount in different notes
a=int(input("enter amount"))
b=a//2000 
c=a%2000
d=c//500
e=c%500
f=e//200
g=e%200
h=g//100
i=g%100
j=i//50
k=i%50
l=k//20
m=k%20
n=m//10
o=m%10
p=o//5
q=o%5
r=q//2
s=q%2
t=s//1
u=s%1
print('₹2000=',b,'₹500=',d,'₹200=',f,'₹100=',h,'₹50=',j,'₹20=',l,'₹10=',n,'₹5=',p,'₹2=',r,'₹1=',t)
