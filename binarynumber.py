def decimalToBinary(n):  
    return bin(n).replace("0b", "")  

if __name__ == '__main__':
    n = int(input())
    rem,counter,maxcount = (0,0,0)
    n1 = int(decimalToBinary(n))
    
    while(n1>0):
        rem = n1%10
        if(rem == 1):
            counter = counter +1
            if(counter >= maxcount):
              maxcount = counter
        else: counter = 0
        n1 = n1//10
    print(maxcount)

