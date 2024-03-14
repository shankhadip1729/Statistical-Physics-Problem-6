import pandas as pd
df=pd.read_html("https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_other_languages")
table=df[3]
t=table.to_numpy()
import numpy as np

def good(x):
    s = ""
    for j in range(0,len(x)):
        if ((x[j]=='0')or(x[j]=='1')or(x[j]=='2')or(x[j]=='3')or(x[j]=='4')or(x[j]=='5')or(x[j]=='6')or(x[j]=='7')or(x[j]=='8')or(x[j]=='9')or(x[j]=='.')) :
            s = s+x[j]
    return(s)
A = []
for i in range (0,86):
    A.append(t[i,0])
print(A)
E= []
for i in range (0,86):
    E.append(np.float64(float(good(t[i,1]))/100))
print(E)
T= []
for i in range (0,86):
    T.append(np.float64(float(good(t[i,7]))/100))
print(T)
T_ord = []
for i in range(0,86):
    if T[i]!= 0:
        T_ord.append((i,A[i],T[i]))
print(T_ord)
Tf26 = []
for i in range(0,26):
    Tf26.append(T[i])
Emod = []
for i in range(0,26):
    if E[i]!=0:
        Emod.append(E[i])
Tmod1 = Tf26
for i in range (0,26):
    if i == 2:
        Tmod1[i]+=T[35]
    elif i == 6:
        Tmod1[i]+=T[48]
    elif i == 8:
        Tmod1[i]+=T[54]
    elif i == 14:
        Tmod1[i]+=T[62]
    elif i == 18:
        Tmod1[i]+=T[70]
    elif i == 20:
        Tmod1[i]+=T[80]
Tmod = []
for i in range(0,26):
    if Tmod1[i]!=0:
        Tmod.append(Tmod1[i])
print(Tmod)
def S(x):
    S = 0
    for i in range(0,len(x)):
        S-=x[i]*np.log(x[i])
    return(S)
print(S(Emod),S(Tmod))
