from turtle import *
from random import randint
import time
from time import sleep
import math

wordlist = ['abrasive', 'bilk', 'covert', 'engender', 'hangar', 'knotty', 'nuance', \
'plagiarism', 'renown', 'tangent', 'abasement', 'billowing', 'labyrinth', 'plaintiff',\
'enigma', 'absolution', 'creditable', 'laceration', 'enshroud']



s=getscreen()
sw=800
sh=900

s.setup(sw, sh)
s.bgcolor('#20f9f9')
t1=getturtle()

t1.speed(0)
t1.hideturtle()

twrite = Turtle()
twrite.hideturtle()

tbadletter = Turtle()
tbadletter.hideturtle()

alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterswrong =""
letterscorrect=""
secretword=""
displayWord=""
fails=6
gamedone = False

def secretword():
  global secretword
  secretword = wordlist[randint(0, len(wordlist)-1 )]
  print("This is the word:" + secretword )
  

def drawgallows():
  t1.width(5)
  t1.color('black')
  t1.penup()
  t1.goto(-int(sw/4), -int(sh/4))
  t1.pendown()
  t1.forward(int(sw/2))
  t1.left(180)
  t1.forward(80)
  t1.right(90)
  t1.forward(int(sh/2))
  t1.left(90)
  t1.forward(int(sh/7))
  t1.left(90)
  t1.forward(int(sh/10))
  t1.right(90)

def drawhead():

  t1.circle(20)
  t1.left(90)
  t1.penup()
  t1.forward(40)
  t1.pendown()
  
  
def drawtorso():
  
  t1.forward(int(sh/8))
  
def drawleg1():
  t1.right(45)
  t1.forward(int(sh/10))

def drawleg2():
  t1.backward(int(sh/10))
  t1.left(90)
  t1.forward(int(sh/10))
  
def drawarm1():
  t1.backward(int(sh/10))
  t1.right(45)
  t1.backward(int(sh/8))
  t1.left(35)
  t1.forward(int(sh/12))

def drawarm2():
  t1.backward(int(sh/12))
  t1.right(70)
  t1.forward(int(sh/12))
  
def dointro():
  twrite.penup()
  twrite.goto(-int(sw*0.4), -int(sh*0.4) )
  twrite.write("Guess a letter...", font=("Arial", 15, "bold"))
  
def makewordstring():
  global displayWord, alpha
  displayWord = ""
  for l in secretword:
    if str(l) in alpha:
        if str(l) in letterscorrect:
            displayWord += str(l) + " "
        else:
            displayWord += " _ " + " "
    else:
        displayWord += str(l) + " "

def displaytext(newtext):
    twrite.clear()
    twrite.penup()
    twrite.goto(-int(sw*0.40), -int(sh*0.40) )
    twrite.write( newtext, font=("Arial", 15, "bold") )

def displaybadletter(newtext):
    tbadletter.clear()
    tbadletter.penup()
    tbadletter.goto(-int(sw*0.40), int(sh*0.40) )
    tbadletter.write( newtext, font=("Arial", 15, "bold") )

def getguess():
  boxTitle="letters Used;" + letterswrong
  guess = s.textinput(boxTitle, "Enter a guess type $$ to guess a word" )
  return guess


    
def updatehangman():
  global fails

  print("in updatehangman fails is " + str(fails))
  if fails == 5:
    drawhead()
  if fails == 4:
    drawtorso()
  if fails == 3:
    drawleg1()
  if fails == 2:
    drawleg2()
  if fails == 1:
    drawarm1()
  if fails == 0:
    drawarm2()

def checkwordguess():
  global fails, gamedone
  boxTitle="Word Guess"
  theguess = s.textinput(boxTitle, "Ok Great ...Guess the word" )
  if theguess == secretword:
    displaytext("Yes! You got it.")
    gamedone = True
  else:
    displaytext("No the word is not: " + theguess)
    time.sleep(1)
    displaytext(displayWord)
    fails -= 1
    print(fails)
    updatehangman()

def restart():
    boxtitle="Want to play again"
    guess = s.textinput(boxtitle, 'Type in "y" to play again')

    if guess.lower()=='y':
        t1.clear()
        drawgallows()
        secretword()
        dointro()
        displaybadletter("Not in word: [" + letterswrong +"]")
        time.sleep(1)
        makewordstring()
        displaytext(displayWord)
        updatehangman()
        checkwordguess()
        fails = 6

def playgame():
  global gamedone, fails, alpha, letterscorrect, letterswrong
  while gamedone == False and fails > 0:
    theguess = getguess()
    print( "The guess is : " + theguess)
    if theguess == "$$":
      print("Let them guess word")
      checkwordguess()
    elif theguess == "" or len(theguess) > 1 :
        displaytext("Sorry I need a letter, guess again")
        time.sleep(1)
        displaytext(displayWord)
    elif theguess not in alpha:
        displaytext("Sorry I need a letter, guess again")
        time.sleep(1)
        displaytext(displayWord)
    elif theguess.lower() in secretword.lower():
        letterscorrect += theguess.lower()
        makewordstring()
        displaytext(displayWord)

    else:
        if theguess.lower() not in letterswrong:
            letterswrong += theguess.lower() + ", "
            fails -= 1
            displaytext(theguess + " is not in the word")
            time.sleep(1)
            updatehangman()
            displaytext(displayWord)
            displaybadletter("Not in word: [" + letterswrong +"]")
        else:
            displaytext(theguess + " was already guessed try again.")
            time.sleep(1)
            displaytext(displayWord)
        

    if "_" not in displayWord:
        displaytext("YES! You won, word is " + secretword)
        gamedone = True
    if fails <= 0:
        displaytext("Sorry out of guesses, the word was" + secretword)
        gamedone = True
    if gamedone == True:
        restart()
        


#secretword()
#drawgallows()
#makewordstring()
#drawhead()
#drawtorso()
#drawleg1()
#drawleg2()
#drawarm1()
#drawarm2()

time.sleep(1)
t1.clear()
drawgallows()
secretword()
dointro()
displaybadletter("Not in word: [" + letterswrong +"]")
time.sleep(1)
makewordstring()
displaytext(displayWord)
#updatehangman()
#checkwordguess()
playgame()
