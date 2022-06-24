import os
import time
import random
import sys

clear = lambda: os.system('cls')

# Globals
global currentword
global currentcharacters
global words
global count
global guess
global guesslist
global guessC
global score
global countcorrect
global attempts
global currentattempts
# Globals!

# Pre-pre define
count = 1
guesslist = [""]
guessC = 0
currentcharacters = [""]
score = 0
countcorrect = 0
currentattempts = 0
attempts = 0
# Pre-pre define!

#   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#  → UF means unfinished.                                                       ←
#  → Make a full successful Run                                                 ←
#  → To figure out transfer of variables between functions.                     ←
#  → To work out variable optimising.                                           ←
#   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

print("Welcome to Wordle but with scoring!")
time.sleep(2)
print("")




# ORDER AND LINKING OF CODE IS WIP
# Will get raw code and logic before finallising order


  

def intro():
  # Intro UF
  print("You will Get the first letters of the word and characters. The  amount of attempts is 1.5x the length of the word!")
  time.sleep(2)
  print(".")
  time.sleep(2)
  clear()
  # Intro!

  currentword = word[random.randint(0,500)]
  time.sleep(0.5)
  currentcharacters = list(currentword)
  time.sleep(2)
  print("")
  print("Guess the character")
  attempts = len(currentcharacters)*1.5

 

def lossing():
  print("All attempts used!")
  time.sleep(1)
  print("You lose.")
  time.sleep(1)
  print("Your score was " + score)
  sys.exit("Too bad.")


          

def main():
  while count != len(currentcharacters):  # Loops guessing for a whole word

    currentattempts += 1 # Attempt count
    print("Guess a letter!")
    guess = input() # Input 

    if isinstance(guess, int) == True: # If letter
      time.sleep(0.2)
      print("No letters...")
      clear()
    
    if guess == currentcharacters[count]: # If correct guess
      count += 1
      countcorrect += 1
      score += 2
      time.sleep(0.5)
      print("Correct letter!")
      clear()
      time.sleep(0.4)
      print("Next letter --")

    elif isinstance(guess, int) == True: # If numbers
      time.sleep(0.2)
      print("No numbers...")
      clear()
    
    else: # Wrong guess
      print("Wrong letter!")
      time.sleep(0.5)

    if guess in currentcharacters [count:-1]:
      if len(guess) != 1:
        print("Please refrain from typing more then a single letter.")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")

      else:
        score += 1
        print("However " + guess + " is in the word!")
        time.sleep(0.5)

      # Remove outdated guesses - 
        LGLx = 1
        LGL = 0
        while LGL != count - 1:

          if guesslist[LGLx] in currentcharacters[0:count - 1]:
            if guesslist[LGLx] in currentcharacters[count - 1: len(currentcharacters)]:
              LGLx += 1
              LGL += 1

            else:
              guesslist.pop(LGLx)
              break
              
        # Remove outdated guesses -
        # Add appropriate guess to list -
        if guess not in guesslist:
          guesslist.append(guess)
        
        
        else:  
          print("")
          
        # Add appropriate guess to list -
          

        
        currentattempts += 1
        time.sleep(0.5)
      
        if currentattempts == attempts: #Losing
          lossing()
        
    else:
      time.sleep(0.5)
      import UI
      # End of if int guess but not there
      
      if currentattempts == attempts: #Losing
        lossing()

      else:
        clear()
        import UI
      
    #Ideas: UI?
          # coloured 

x = 1
while x == 1:

  # Word list
  my_file = open("words.txt", "r")
  data = my_file.read()
  data_into_list = data.split("\n")
  word = data_into_list
  my_file.close()
  random.shuffle(word)
  # Word list!

  # Pre define
  count = 1
  guesslist = [""]
  guessC = 0
  currentcharacters = [""]
  score = 0
  countcorrect = 0
  currentattempts = 0
  attempts = 0
  # Pre define!
  
  intro()

  main()