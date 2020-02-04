from random import randint

''' In this monster attack game
1. a player can harm a monster
2. a player can heal itself thereby increasing its health level
3. a player has a health status bar which shows whether the player is alive or dead

The moster can also:
1. harm a player
2. has a health status bar which shows whether the monster is alive or dead
'''
print("Developer: Solomon Yaw Adeklo")
print("This is my first Python Program")
print()
print ("In this monster attack game")
print()
print ("1. a player can harm a monster")
print ("2. a player can heal itself thereby increasing its health level")
print ("3. a player has a health status bar which shows whether the player is alive or dead")
print()
print ("The moster can also:")
print ("1. harm a player")
print ("2. has a health status bar which shows whether the monster is alive or dead")

     


game_running = True;

game_results=[]

def calculate_monster_attack():
   return randint(monster["attack_min"],monster["attack_max"])

def game_ends(winner_name):
    print(f'{winner_name} won the game')


while game_running == True:
  counter = 0

  new_round=True
  player = {"name":"Solomon","attack":13,"heal":16,"health":100}

  monster = {"name":"Monster","attack_min":12,"attack_max":20,"health":100}   

  print("----"*7)
  print("Enter player name")
  player["name"]= input()
  print(player["name"]+" has "+str(player["health"]) + " health")
  print(monster["name"]+" has "+str(monster["health"]) + " health")

  while new_round ==True:
        
        counter = counter + 1
        player_won=False
        monster_won=False
        
        print("----"*7)
        print("Please select action")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit")
        print("4) Show Results")

        player_choice = input()

        if player_choice == "1":

            monster["health"] = monster["health"]-player["attack"]#player attacks the monster
            if monster["health"]<=0:
                player_won = True
            else :
               
                player["health"] = player["health"]-calculate_monster_attack()  #monster attacks the player
            if player["health"]<=0:
                monster_won = True;

        elif player_choice == "2":
             player["health"]= player["health"] + player["heal"]
             player["health"] = player["health"]-calculate_monster_attack()  #monster attacks the player
             if player["health"]<=0:
                 monster_won = True
          

        elif player_choice =="3":
            game_running=False
            new_round=False

        elif player_choice=="4":
            print("Below are the game results")
            print("----"*7)
            for player_stats in game_results:
                print(player_stats)

        else:
            print("Invalid Input")

        if player_won==False and monster_won==False:
           print(player["name"]+" has " +str(player["health"])+" health left")
           print(monster["name"]+" has " +str(monster["health"])+" health left")

        elif player_won==True:
            game_ends(player["name"])
            round_result ={"name":player["name"],"health":player["health","rounds":counter]}
            game_results.append(round_result)
            new_round= False

        elif monster_won==True:
            game_ends(monster["name"])
            round_result ={"name":player["name"],"health":player["health"],"rounds":counter}
            game_results.append(round_result)
            new_round= False;
        
        

def calculate_monster_attack():
   return randint(monster["attack_min"],monster["attack_max"])