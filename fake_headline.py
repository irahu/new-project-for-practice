#import random for random number
import random
subjects=[
    "Sharuk",
    "virat",
    "nirmala",
    "modi",
    "mickale"   
]

action=[
    "launches",
    "cancels",
    "dance",
    "eat",
    "order"
] 
places_or_things=[
    "gandha",
    "bandar",
    "tatti",
    "bhagi",
    "dimag kahrab" 
]

#start the randm genrationn of loop
while True:
    subjects =random.choice(subjects)
    action =random.choice(action)
    places_or_things=random.choice(places_or_things)
    
    headline =(f"Breaking News: {subjects} {action} {places_or_things}")
    print("\n"+ headline)
    
    
    user= input(("\n do you want a spicy news yes/no: ").strip())
    if user=="no":
        break
    
#print good bye
print("\n thank you for your specious time")