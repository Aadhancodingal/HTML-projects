import random
attempts_list = []
def show_score():
 if len(attempts_list) <=0:
  print("There is no current highscore.It's yours for the taking")
 else:
  print("The current high score is {}".format(min(attempts_list)))
  
def start_game():
 random_number = int(random.randint(1,10))
 print("Hey there welcome to the game of guesses")
 player_name = input("Enter your name")
 wanna_play = input("Hi {}, would you like to play the game of guesses? (Enter Yes/No)".format(player_name))
 attempts = 0
 show_score()
 while wanna_play.lower() == "yes":
  try:
    guess = input("Pick a number from 1 to 10")
    if int(guess) < 1 or int(guess) > 10:
     raise ValueError("Please guess a number within the given range")
    if int(guess)==random_number:
     print("Congrats! You guessed it right")
     attempts += 1
     attempts_list.append(attempts)
     print("It took you {} attempts".format(attempts))
     play_again =input("Wolud you like to play again")
     if play_again.lower() == "no":
      print("That's cool. Have a nice day")
      break
    elif int(guess) < random_number:
     print("It is lower")
     attempts += 1
    elif int(guess) > random_number:
     print("it is higher")
     attempts += 1
  except ValueError as err:
   print("Oh!, that is not a vaild value. Try again.....")
   print("({})".format(err))
 else:  
   print("That's cool.Have a nice day")
if __name__ == '__main__':
  start_game()  