import os
import time
import random
import r

#   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#  → UF means unfinished.                                                       ←
#  → Still to do the actual program order, creating functions/routines.         ←
#  → To figure out transfer of variables between functions.                     ←
#  → Clutter to be cleaned when functions finsihed.                             ←
#   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

print("Welcome to Wordle but with scoring!")
time.wait(2)


count = 1
words = r.get_random_words(100)
guesslist = [""]


# Intro UF
print("You will Get the first letters of the word and characters. The amount of attempts is x3 the lenght of the word!")
time.sleep(2)
print(".")
time.sleep(2)
# Intro!

# Try to get while loop for each letter.



def words(currentword, score, wordscorrect):
  os.clear('cls')
  time.sleep(0.5)
  currentword = words[random.randint(1,100)]
  currentcharacters = list(currentword)
  time.sleep(2)
  print("")
  print("Guess the character")
  

  return currentcharacters

def guesser(currentcharacters, count, guesslist, score):

  countcorrect = 0
  currentattempts = 0  # Sets variable
  attempts = len(currentcharacters)*3

  while count != len(currentcharacters):  # Loops guessing for a whole word
    import UI
    guess = input()
    if guess == currentcharacters[count]:
      count += 1
      countcorrect += 1
      score += 2
      time.sleep(0.5)
      print("Correct letter!")
      os.clear('cls')
      time.sleep(0.4)
      print("Next letter --")
      
    
    else:
      print("Wrong letter!")
      time.sleep(0.5)

      if guess in currentcharacters:
        score += 1
        print("However " + "\033[1;32;40m " + guess + "  \n" + " is in the word!")
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
            print("All attempts used!")
            time.sleep(1)
            print("You lose.")
            break
      
        
      else:
        currentattempts += 1
        time.sleep(0.5)
      
        if currentattempts == attempts: #Losing
          print("All attempts used!")
          time.sleep(1)
          print("You lose.")
          break
      
      #Ideas: UI?
            # coloured 