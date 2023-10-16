#this file was created by: Jordan Rosas

import turtle

from turtle import *

import os

print("The current working directory is (getcwd): " + os.getcwd())

print("The current working directory is (path.dirname): " + os.path.dirname(__file__))
 
game_folder = os.path.dirname(__file__)

images_folder = os.path.join(game_folder, 'images') # where the images are drawn from in the graphics

WIDTH, HEIGHT = 1000, 400  # where the graphic pops up in the termanal

rock_w, rock_h = 256, 280 # with and hight of rock and were it sits in the termanal
paper_w, paper_h = 256, 204 # with and hight of paper and were it sits in the termanal
scissors_w, scissors_h = 256, 170 # with and hight of scissors and were it sits in the termanal


screen = turtle.Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)  

screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")

cv = screen.getcanvas()

cv._rootwindow.resizable(False, False)

 

rock_image = os.path.join(images_folder, 'rocky.gif')
rock_instance = turtle.Turtle()
paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()

def show_rock(x,y): # where rock pops up in termanal

    screen.addshape(rock_image)
    rock_instance.shape(rock_image)
    rock_instance.penup()
    rock_instance.setpos(x,y)

def show_paper(x,y): # where paper pops up in termanal

    screen.addshape(paper_image)  
    paper_instance.shape(paper_image)
    paper_instance.penup()  
    paper_instance.setpos(x,y)

def show_scissors(x,y): # where scissors pops up in termanal

    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

t = turtle.Turtle()
text = turtle.Turtle()
text.color('deep pink') # Color of the text in the termanal
t.penup()
text.hideturtle()

 

t.hideturtle()

show_rock(-300, 0)
show_paper(0,0)
show_scissors (300,0)

text.penup()
text.hideturtle()
text.setpos(-300,150)
text.write("choose rock, paper, or scissors", False, "left", ("Arial", 24, "normal"))

def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] - w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False
    t.penup()

def player(x, y):

    global text
    if (collide(x,y,rock_instance, rock_w, rock_h)):
        user_choice = "rock"

    elif(collide(x,y,paper_instance,rock_w,rock_h)):
        user_choice = "paper"

    elif(collide(x,y,scissors_instance,scissors_w,scissors_h)):
        user_choice = "scissors"

    text.penup()
    text.clear()  
    text.goto(-100, 150)
    text.write(f"You chose {user_choice}!", align="left", font=("Arial", 24, "normal"))

    from random import randint
    
    possible_choices = ["rock", "paper", "scissors"]
    computer_choices = possible_choices[randint(0, 2)] 
    message = f"Computer chooses... {computer_choices}!"
    
    x, y = -200, -200
    target_x, target_y = -200, -200
    text.penup()
    text.goto(x, y)
    text.write(message, align="left", font=("Arial", 24, "normal"))
    text.goto(target_x, target_y)

    import time

    time.sleep(2) 

    if user_choice == computer_choices:
        result = "It's a tie!"

    elif (user_choice == "rock" and computer_choices == "scissors") or \
      (user_choice == "paper" and computer_choices == "rock") or \
         (user_choice == "scissors" and computer_choices == "paper"):
        result = "You won!"

    else:
        result = "You lost!"

    text.clear()
    text.goto(-82, 151)
    text.write(result, align="left", font=("Arial", 24, "normal"))


playerchoice = screen.onclick(player)
playerchoice = screen.mainloop()