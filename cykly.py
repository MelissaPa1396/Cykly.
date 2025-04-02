import random                       #3*100 = 30 - ondra matyáš, 2.4. 2025
#im thinking miku miku ooeeeoo im thinking miku miku ooeeoo im thinking miku miku ooeeoo im thinking miku miku ooeeoo im on top of the world because of you
for x in range(30): 
    a = random.randint(0,10)  
    b = random.randint(0,10) 
    znamenko = random.randint(1,2)

    if znamenko == 1:
        print(f"{a} * {b} = ")    
    else:   
        print(f"{a} / {b} = ")
        print(f"{a} + {b} = ")
        print(f"{a} - {b} = ")
    
    
