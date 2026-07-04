import random

numofstreak=0
for exnum in range(10000):
    flip=[]

    for i in range(100):
        flip.append(random.randint(0,1))
    
    streak=1
    for i in range(1,len(flip)):
        if flip[i]==flip[i-1]:
            streak+=1
        else:
            streak=1
        if streak >= 6:
            numofstreak+=1
            break

print(f"Change of streak={numofstreak/10000}")
    

