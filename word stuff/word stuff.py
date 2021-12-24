#loading things i believe
#so like if you're reading this hi
#this is literally just "is this a real word"
enableallgamemodes = True #this is literally just for testing purposes, you cheaters
import pygame
from pygame import rect
from pygame import key
from pygame.constants import MOUSEBUTTONDOWN
pygame.font.init()
import os
import sys
import random
print("whats up martians")
lm = 1
(width, height) = (1920, 1080)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
running = True
titlefont = pygame.font.SysFont('sans', 80)
font = pygame.font.SysFont('sans', 50)
smallfont = pygame.font.SysFont('sans', 32)
tinyfont = pygame.font.SysFont('sans', 16)
intitle = 1
questions = 0
#opens the files that have the answers
#real words
realfile = open("textdependencies\\\\real.txt", "r")
realcontent = realfile.read()
real_list = realcontent.split(",")
realfile.close()
print(real_list)
#fakes
fakefile = open("textdependencies\\\\fakes.txt", "r")
fakecontent = fakefile.read()
fake_list = fakecontent.split(",")
fakefile.close()
green = (0,255,0)
red = (255,0,0)
print(fake_list)
background_color = (20,20,20)
darkgrey = (40,40,40)
framerate = 60
timerstart = 0
frame_count = 0
hasgamemodesenabled = 0
jb = False
backnotifier = font.render("go back", True, green, background_color)
backnotifierrect = backnotifier.get_rect()
backnotifierrect.center = (width // 2, height // 2 + 150)
#the game freaks the hell out if i don't predefine buttons for some reason so i'm just copypasting them.
#not efficient, i don't care
realbutton = font.render("this is real", True, green, background_color)
realbuttonrect = realbutton.get_rect()
realbuttonrect.center = (width // 2 - 300, height // 2 + 50)
background_color = (20,20,20)
fakebutton = font.render("this is fake", True, green, background_color)
fakebuttonrect = fakebutton.get_rect()
fakebuttonrect.center = (width // 2 - 300, height // 2 + 50)
yellow = (255,255,0)
blue = (150,255,255)
checkbutton = font.render("click to see correct / incorrect", True, blue, background_color)
checkbuttonrect = checkbutton.get_rect()
aistartbutton = font.render("ai word guesser", True, green, background_color)
aistartbuttonrect = aistartbutton.get_rect()
aistartbuttonrect.center = (width // 2 , height // 2 - 200)
grey = (125, 125, 125)
clock = pygame.time.Clock()
quizstartbutton = font.render("word writer", True, green, background_color)
quizstartbuttonrect = quizstartbutton.get_rect()
quizstartbuttonrect.center = (width // 2 , height // 2 - 100)
konamicounter = 0
user_text = ""
#runs the damn program
while running:
  mousepos = pygame.mouse.get_pos()
  #looks for events (button presses) and acts accordingly
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN and playbuttonrect.collidepoint(pygame.mouse.get_pos()) and intitle == 1:
      intitle = 4
      print("game start")
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_l and intitle == 1 or event.key == pygame.K_l and intitle == 4 or event.key == pygame.K_l and intitle == 3:
            if lm < 2:
                lm += 1
                user_text = ""
            else:
                lm = 1
                user_text = ""
        #keyboard input grabber (for text sections in games like word writer)
        if event.key == pygame.K_BACKSPACE:
            user_text = user_text[:-1]
        else:
            user_text += event.unicode
    #check button
    if event.type == pygame.MOUSEBUTTONDOWN and checkbuttonrect.collidepoint(pygame.mouse.get_pos()) and intitle == 3:
        intitle = 1
    if event.type == pygame.MOUSEBUTTONDOWN and aistartbuttonrect.collidepoint(pygame.mouse.get_pos()) and intitle == 4:
        intitle = 2
    if event.type == pygame.MOUSEBUTTONDOWN and backnotifierrect.collidepoint(pygame.mouse.get_pos()) and intitle == 6:
        intitle = 1
    if event.type == pygame.MOUSEBUTTONDOWN and quizstartbuttonrect.collidepoint(pygame.mouse.get_pos()) and intitle == 4 and hasgamemodesenabled >= 1:
        intitle = 5
    #registers player input with the real/fake buttons
    if event.type == pygame.MOUSEBUTTONDOWN and realbuttonrect.collidepoint(pygame.mouse.get_pos()):
        nextquestion = True
        if questions == 1:
            qg1 = True
            nextquestion = True
            if rf == 1:
                q1word = fake_list[i]
            else:
                q1word = real_list[i]
        elif questions == 2:
            qg2 = True
            if rf == 1:
                q2word = fake_list[i]
            else:
                q2word = real_list[i]
        elif questions == 3:
            qg3 = True
            if rf == 1:
                q3word = fake_list[i]
            else:
                q3word = real_list[i]
        elif questions == 4:
            qg4 = True
            if rf == 1:
                q4word = fake_list[i]
            else:
                q4word = real_list[i]
        elif questions == 5:
            qg5 = True
            if rf == 1:
                q5word = fake_list[i]
            else:
                q5word = real_list[i]
        elif questions == 6:
            qg6 = True
            if rf == 1:
                q6word = fake_list[i]
            else:
                q6word = real_list[i]
        elif questions == 7:
            qg7 = True
            if rf == 1:
                q7word = fake_list[i]
            else:
                q7word = real_list[i]
        elif questions == 8:
            qg8 = True
            if rf == 1:
                q8word = fake_list[i]
            else:
                q8word = real_list[i]
        elif questions == 9:
            qg9 = True
            if rf == 1:
                q9word = fake_list[i]
            else:
                q9word = real_list[i]
        elif questions == 10:
            qg10 = True
            if rf == 1:
                q10word = fake_list[i]
            else:
                q10word = real_list[i]
            pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONDOWN and fakebuttonrect.collidepoint(pygame.mouse.get_pos()):
        nextquestion = True
        if questions == 1:
            qg1 = False
            nextquestion = True
            if rf == 1:
                q1word = fake_list[i]
            else:
                q1word = real_list[i]
        elif questions == 2:
            qg2 = False
            if rf == 1:
                q2word = fake_list[i]
            else:
                q2word = real_list[i]
        elif questions == 3:
            qg3 = False
            if rf == 1:
                q3word = fake_list[i]
            else:
                q3word = real_list[i]
        elif questions == 4:
            qg4 = False
            if rf == 1:
                q4word = fake_list[i]
            else:
                q4word = real_list[i]
        elif questions == 5:
            qg5 = False
            if rf == 1:
                q5word = fake_list[i]
            else:
                q5word = real_list[i]
        elif questions == 6:
            qg6 = False
            if rf == 1:
                q6word = fake_list[i]
            else:
                q6word = real_list[i]
        elif questions == 7:
            qg7 = False
            if rf == 1:
                q7word = fake_list[i]
            else:
                q7word = real_list[i]
        elif questions == 8:
            qg8 = False
            if rf == 1:
                q8word = fake_list[i]
            else:
                q8word = real_list[i]
        elif questions == 9:
            qg9 = False
            if rf == 1:
                q9word = fake_list[i]
            else:
                q9word = real_list[i]
        elif questions == 10:
            qg10 = False
            if rf == 1:
                q10word = fake_list[i]
            else:
                q10word = real_list[i]
            pygame.display.flip()
        pygame.display.flip()
    pygame.display.set_caption('is this a real word')
    #checks pallete
    if lm == 2:
        background_color = (20,20,20)
        text_color = (255, 255, 255)
    elif lm == 1:
        background_color = (20,20,20)
        text_color = (255, 255, 255)
    else:
        background_color = (20,20,20)
        text_color = (255, 255, 255)
  screen.fill(background_color)
  #checks if title is active, if not then checks if game is active, if not crashes or something i don't know
  #adds title
  if intitle == 1:
    title = titlefont.render("random text projects", True, text_color, background_color)
    titlerect = title.get_rect()
    titlerect.center = (width // 2, height // 2 - height // 6)
    screen.blit(title, titlerect)
    #adds credits
    madeby = smallfont.render('made by ssadie', True, text_color, background_color)
    madebyrect = madeby.get_rect()
    madebyrect.center = (width // 2, 930)
    screen.blit(madeby, madebyrect)
    #makes play button
    playbutton = font.render('play', True, text_color, background_color)
    playbuttonrect = playbutton.get_rect()
    playbuttonrect.center = (width // 2, height // 2)
    screen.blit(playbutton, playbuttonrect)
    nextquestion = True
    justbegin = True
    onecheck = True
  #actual game and not the title screen
  if intitle == 2:
    #set 0 at begin of each round
    if justbegin == True:
        questions = 0 - 1
        justbegin = False
    #set next question at beginning of each round
    if nextquestion == True:
        #generates a random number, and figures out question number, and if it's real or fake. generates accordingly
        rf = random.randint(1,2)
        if rf == 1:
            for i in [random.randint(1,39)]:
                word = fake_list[i]
            if questions == 1:
                q1 = False
            elif questions == 2:
                q2 = False
            elif questions == 3:
                q3 = False
            elif questions == 4:
                q4 = False
            elif questions == 5:
                q5 = False
            elif questions == 6:
                q6 = False
            elif questions == 7:
                q7 = False
            elif questions == 8:
                q8 = False
            elif questions == 9:
                q9 = False
            elif questions == 10:
                q10 = False
            print("question false")
        else:
            for i in [random.randint(1,39)]:
                word = real_list[i]
            if questions == 1:
                q1 = True
            elif questions == 2:
                q2 = True
            elif questions == 3:
                q3 = True
            elif questions == 4:
                q4 = True
            elif questions == 5:
                q5 = True
            elif questions == 6:
                q6 = True
            elif questions == 7:
                q7 = True
            elif questions == 8:
                q8 = True
            elif questions == 9:
                q9 = True
            elif questions == 10:
                q10 = True
            print("question true")
        nextquestion = False
        questions += 1
    else:
        #begin writing the real/fake words
        rfword = titlefont.render("word " + str(questions) + ": " + word, True, text_color, background_color)
        rfwordrect = rfword.get_rect()
        rfwordrect.center = (width // 2, height // 2 - 50)
        screen.blit(rfword, rfwordrect)
        #is this real button
        realbutton = font.render("this is real", True, green, background_color)
        realbuttonrect = realbutton.get_rect()
        realbuttonrect.center = (width // 2 - 300, height // 2 + 50)
        screen.blit(realbutton,realbuttonrect)
        #is this fake button
        fakebutton = font.render("this is fake", True, red, background_color)
        fakebuttonrect = fakebutton.get_rect()
        fakebuttonrect.center = (width // 2 + 300, height // 2 + 50)
        screen.blit(fakebutton,fakebuttonrect)
        if questions > 10:
            intitle = 3
            final = True
    #total screen, basically just checks if question answer is equal to player answer and if so, increments "total"
  elif intitle == 3:
    if final == True:
        final = False
        total = 0
        if qg1 == q1:
            total += 1
            c1 = True
        else:
            c1 = False
        if qg2 == q2:
            c2 = True
        else:
            c2 = False
        if qg3 == q3:
            total += 1
            c3 = True
        else:
            c3 = False
        if qg4 == q4:
            total += 1
            c4 = True
        else:
            c4 = False
        if qg5 == q5:
            total += 1
            c5 = True
        else:
            c5 = False
        if qg6 == q6:
            total += 1
            c6 = True
        else:
            c6 = False
        if qg7 == q7:
            total += 1
            c7 = True
        else:
            c7 = False
        if qg8 == q8:
            total += 1
            c8 = True
        else:
            c8 = False
        if qg9 == q9:
            total += 1
            c9 = True
        else:
            c9 = False
        if qg10 == q10:
            total += 1
            c10 = True
        else:
            c10 = False
    #rating score
        if total >= 0 and total <= 3:
            score = "bad"
        if total >= 4 and total <= 7:
            score = "eh"
        elif total >= 8 and total <= 10:
            score = "good"
    else:
        totalshow = titlefont.render("you got: " + str(total) + "/10", True, text_color, background_color)
        totalshowrect = totalshow.get_rect()
        totalshowrect.center = (width // 2, height // 2 - 100 - 20)
        screen.blit(totalshow, totalshowrect)
        if score == "bad":
            scoreshow = smallfont.render("thats bad lmao, 1-3", True, grey, background_color)
            scoreshowrect = scoreshow.get_rect()
            scoreshowrect.center = (width // 2, height // 2 - 20)
            screen.blit(scoreshow, scoreshowrect)
        if score == "eh":
            scoreshow = smallfont.render("that was okay, i guess, 4-7", True, grey, background_color)
            scoreshowrect = scoreshow.get_rect()
            scoreshowrect.center = (width // 2, height // 2 - 20)
            screen.blit(scoreshow, scoreshowrect)
        if score == "good":
            scoreshow = smallfont.render("you did well, 8+", True, grey, background_color)
            scoreshowrect = scoreshow.get_rect()
            scoreshowrect.center = (width // 2, height // 2)
            screen.blit(scoreshow, scoreshowrect)
        checkbutton = font.render("back to title", True, text_color, background_color)
        checkbuttonrect = checkbutton.get_rect()
        checkbuttonrect.center = (width // 2, height // 2 + 75)
        screen.blit(checkbutton, checkbuttonrect)
        if total >= 7:
            codeshow1 = smallfont.render("word writer unlocked, 7+", True, text_color, background_color)
            codeshow1rect = codeshow1.get_rect()
            codeshow1rect.center = (width // 2, height // 2 + 200)
            screen.blit(codeshow1, codeshow1rect)
            if onecheck == True:
                hasgamemodesenabled += 1
                onecheck = False
  #gamemode selector
  if intitle == 4:
      gamemodenotifier = titlefont.render("please select your gamemode or something", True, text_color, background_color)
      gamemodenotifierrect = gamemodenotifier.get_rect()
      gamemodenotifierrect.center = (width // 2, height // 2 - 400)
      screen.blit(gamemodenotifier,gamemodenotifierrect)
#simple selecting buttons
      aistartbutton = font.render("ai word guesser", True, text_color, background_color)
      aistartbuttonrect = aistartbutton.get_rect()
      aistartbuttonrect.center = (width // 2 , height // 2 - 200)
      screen.blit(aistartbutton, aistartbuttonrect)
      #simple selecting buttons
      if hasgamemodesenabled >= 1:
        quizstartbutton = font.render("word writer", True, text_color, background_color)
        quizstartbuttonrect = quizstartbutton.get_rect()
        quizstartbuttonrect.center = (width // 2 , height // 2 - 100)
        screen.blit(quizstartbutton, quizstartbuttonrect)
      else:
        quizstartbutton = font.render("???", True, darkgrey, background_color)
        quizstartbuttonrect = quizstartbutton.get_rect()
        quizstartbuttonrect.center = (width // 2 , height // 2 - 100)
        screen.blit(quizstartbutton, quizstartbuttonrect)
        jb = True
      if hasgamemodesenabled >= 2:
          storystartbutton = font.render("more stuff coming soon", True, darkgrey, background_color)
          storystartbuttonrect = storystartbutton.get_rect()
          storystartbuttonrect.center = (width // 2, height // 2)
          screen.blit(storystartbutton, storystartbuttonrect)
      else:
          storystartbutton = font.render("???", True, darkgrey, background_color)
          storystartbuttonrect = storystartbutton.get_rect()
          storystartbuttonrect.center = (width // 2, height // 2)
          screen.blit(storystartbutton, storystartbuttonrect)
  #setup of word list
  if intitle == 5:
    if jb == True:
        print("start quiz")
        jb = False
        questions = 0
    #grabs a random word
    if nextquestion == True:
        r2 = random.randint(1,2)
        if r2 == 1:
            for i in [random.randint(1,39)]:
                word = real_list[i]
        elif r2 == 2:
            for i in [random.randint(1,39)]:
                word = fake_list[i]
        nextquestion = False
    #throwing text at a wall and hoping it works
    inputrect = pygame.Rect(width // 4 - 9000, height // 2 + 50, 80000, 90)
    pygame.draw.rect(screen, darkgrey, inputrect)
    wordwritenotifier = titlefont.render("write \"" + word + "\"", True, text_color, background_color)
    wordwritenotifierrect = wordwritenotifier.get_rect()
    wordwritenotifierrect.center = (width // 2, height // 2 - 100)
    screen.blit(wordwritenotifier,wordwritenotifierrect)
    inputnotifier = font.render(user_text, True, text_color, darkgrey)
    inputnotifierrect = inputnotifier.get_rect()
    inputnotifierrect.center = (width // 2, height // 2 + 90)
    screen.blit(inputnotifier,inputnotifierrect)
    total_seconds = frame_count // framerate
    #makesa a tally of how many done
    tallynotifier = smallfont.render(str(questions) + "/20", True, text_color, background_color)
    tallynotifierrect = tallynotifier.get_rect()
    tallynotifierrect.center = (width // 2, height // 2 + 200)
    screen.blit(tallynotifier,tallynotifierrect)
    #go to results screen
    if word == user_text:
        user_text = ""
        questions += 1
        nextquestion = True
    if questions == 21:
        intitle = 6
  if intitle == 6:
    writenotifier = titlefont.render("you win", True, text_color, background_color)
    writenotifierrect = writenotifier.get_rect()
    writenotifierrect.center = (width // 2, height // 2 - 50)
    screen.blit(writenotifier,writenotifierrect)
    tallynotifier = smallfont.render("tip: timing yourself for this is kinda fun i think", True, grey, background_color)
    tallynotifierrect = tallynotifier.get_rect()
    tallynotifierrect.center = (width // 2, height // 2 + 50)
    screen.blit(tallynotifier,tallynotifierrect)
    backnotifier = font.render("go back", True, text_color, background_color)
    backnotifierrect = backnotifier.get_rect()
    backnotifierrect.center = (width // 2, height // 2 + 150)
    screen.blit(backnotifier,backnotifierrect)
    ngnotifier = smallfont.render("oh yeah you unlocked a new gamemode", True, grey, background_color)
    ngnotifierrect = ngnotifier.get_rect()
    ngnotifierrect.center = (width // 2, height // 2 - 150)
    screen.blit(ngnotifier,ngnotifierrect)
    hasgamemodesenabled = 2
  if intitle == 7:
    print("placeholder")
  betastart = tinyfont.render("v0.17, alpha prerelease", True, grey, background_color)
  betastartrect = betastart.get_rect()
  betastartrect.center = (width // 2 , height // 2 + 500)
  screen.blit(betastart, betastartrect)
  pygame.display.flip()
