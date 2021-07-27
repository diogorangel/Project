from typing import Text

import re 

name = Text(input("Hello! What is your name? "))
print(f"Welcome {name}, for this athletic different game. My name is Diogo, and I will lead you"
"by this different game. ")
print()

#story
#Story = re.IGNORECASE(str)
Story = Text(input(f"{name}, You are playing soccer and is on the counterattack, "
    "you have just one more defenser of "
    "other team and goalkeeper for pass, and you have on teammate " 
    "that are ready for receive the ball for do the goal if you pass the ball to him." 
    "What you will choose?  "
f"PASS THE BALL SMILLING, PASS THE BALL SAD  or DRIBLLE THE DEFENSER? "))
#Story = Story.upper()
Story = re.IGNORECASE(Text)


if Story:
    #re.IGNORECASE = {Story}
    if Story == "PASS THE BALL SMILLING":     
        print(f"{name}, When you do this, your teammate do the GOAL! And after, he pay for you a lunch "
            "Congratilations for your job =)")

    elif Story == "PASS THE BALL SAD":
        print(f'{name}, You lost the ball for the defenser!')

    elif Story == "DRIBLLE THE DEFENSER":
        print(f"{name}, When you driblle the defenser, you driblle the goalkeeper to, and do a beautiful goal ." 
        "Congratilations!"
        "After this, you have a good opportunity to be the best of match!")
    else:
        print(f"{name}, Ok! This action is of other situation, Let's try create a story again ?")
    
    