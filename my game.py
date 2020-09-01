a = 58
print("lets play a game of guessing number" ) 
print ("Guess the no.:")
while(True):
    b = int(input())
    if b==a:
        print("CONGRATS YOU GOT THE NUMBER")
        break
    elif b<0 or b>100:
        print("enter a number in range of 1-100")
        continue
    elif b<5 or b>95:
        print("you are not even close")
        continue
    elif b<10 or b>90:
        print("you are not even close") 
        continue
    elif b<15 or b>85:
        print("you are not even close") 
        continue          
    elif b<20 or b>80:
        print("you are not even close")
        continue     
    elif b<25 or b>75:
        print("you are not even close")
        continue  
    elif b<30 or b>70:
        print("you are not even close")
        continue     
    elif b<35 or b>65:
        print("you are close")
        continue     
    elif b<40 or b>60:
        print("you are close")  
        continue
    elif b<45 or b>60:
        print("you are a little far from the number")
        continue
    elif b<50 or b>60:
        print("you are very close")
        continue      
    elif b<55 or b>60:
        print("you are very very close") 
        continue       
    elif b<57 or b>60:
        print("you are very near")
        continue


