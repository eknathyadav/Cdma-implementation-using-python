#Code Division multiple access
n = int(input("Enter number of channels : "))
Chl = []
DB = []
# Channels[for ex "-1 0 -1 0"]and databits[for ex "-1"] inputs
for i in range(n):
    l = input("Enter sequence of channel "+str(i+1)+": ")
    d = input("Enter databits of channel "+str(i+1)+": ")
    temp = l.split()
    Chl.append(temp)
    DB.append(d)
cseq = []
##Multiplication C*D[for ex : [ -1 0 -1 0]*-1]
for i in range(len(DB)):
    r = []
    for j in range(len(Chl)):
        if(i==j):##Note : dont use .index() 
            t = Chl[j]
            for k in t:
                eseq = int(DB[i])*int(k)
                r.append(eseq)
    cseq.append(r)
rseq = []
##finding resultant sequence C1*D1+C2*D2+CN*DN
for i in range(len(temp)):
    col_sum = 0 
    for j in cseq:
        col_sum = col_sum + j[i]
    rseq.append(col_sum)
print("----------------------------------------------------------------")
print("Resultant channel sequence = "+str(rseq))
V = input("Enter sequence of channel : ")
Vc = V.split()
## Finding inner product i.e resultant sequence*channel
s=0
for i in range(len(rseq)):
    for j in range(len(Vc)):
        if(i==j):
            f = int(rseq[i])*int(Vc[j])  
            s = s + f
print("----------------------------------------------------------------")            
print("Inner product = " + str(s))
print("----------------------------------------------------------------")
print("Data bit that was sent = " + str(round(s/n)))-1



            
            



    
        
    
        
        
        
            

        

            
            
            
        
        
    



        
