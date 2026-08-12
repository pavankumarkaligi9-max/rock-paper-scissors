import random
rule=["r","p","s"]
print('''  for choosing you can select the numbers    rock='r'
                 paper='p'
                 scissor='s'
                 exit=999  ''')
                 
 # function  if player chosses rock  
               
def rock():
    global choose
    global bot
    global bot_win
    global player_win
    if bot=="r":
        print(f"bot choosen : {bot}")
        print("no one won the round")
    elif bot=="s":
        print(f"bot choosen : {bot} ")
        print("player won the round ")
        player_win+=1
        print(f"score : player={player_win}                           bot={bot_win}")
    elif bot=="p":
        print(f"bot choosen : { bot} ")
        print("bot won the round ")
        bot_win+=1
        print(f" score : player={player_win}                          bot={bot_win}")
#function if player chooses paper        
        
def paper():
        global player_win
        global bot_win
        if bot=="p":
            print(f"bot choosen : {bot}")
            print("no one won the round")
        elif bot=="r":
            print(f"bot choosen :{bot} ")
            print("player won the round")
            player_win+=1
            print(f" score : player={player_win}                          bot={bot_win}")
        elif bot=="s":
            print(f"bot choosen : {bot}")
            print("bot won the round") 
            bot_win+=1
            print(f"score: player={player_win}                            bot={bot_win}")

#function if player chooses scissors

def scissors():
        global player_win
        global bot_win
        if bot=="s":
            print(f"bot choosen :{bot}")
            print(" no one won the round ")
        elif bot=="p":
            print(f"bot choosen :{bot}")
            print("player won the round ")
            player_win+=1
            print(f"score: player={player_win}                            bot={bot_win}")
        elif bot=="r":
            print(f"bot choosen :{bot}")
            print("botbwon the round")
            bot_win+=1
            print(f"score: player={player_win}                            bot={bot_win}")   
#start of the game
player_win=0
bot_win=0        
while True:
    bot=random.choice(rule)
    choose=input("enter your choice : ")
    if choose==str(999):
        break
    elif choose=="r":
       rock()
    elif choose=="p":
       paper()
    elif choose=="s":
       scissors()
    else :
        print(" please choose between r,p,s  only ")
#final scores 
print(f"your final scores : player={player_win}    bot={bot_win}")                                               bot={bot_win}")
if bot_win>player_win:
       print("bot won the game ")
elif bot_win<player_win:
       print("player won the game ")
elif bot_win==player_win:
       print("both have equale score in the game")
print(" THANK YOU FOR PLAYING THE GAME ")