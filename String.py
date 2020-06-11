T = int(input())
if(T<=10 and T>=1):
    for i in range(T):
        S = input()
        if(len(S)>= 2 and len(S)<=10000):
            Evenstr = str()
            Oddstr = str()
       
            for i in range(len(S)):
                if(i%2==0):
                    Evenstr = Evenstr + S[i]
                else:
                    Oddstr = Oddstr + S[i]
            print(Evenstr+" "+Oddstr)
        else: exit()
else: exit()
    
