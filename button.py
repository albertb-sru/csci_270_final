#!/usr/bin/env python3
# Made by Albert Brandt
# button.py

import turtle;

# Store button instances here.
buttons = [];

canvas = turtle.getcanvas();

turtle.hideturtle()
# Button Class.
# x = the x position of the center of the button,
# y = the y position of the center of the button,
# w = width of the button,
# h = height of the button,
# text = text label for the button,
# action = the function for the button to execute on button click,
# args = the arguments passed to the action
class Button:

    # Runs when a button is created.
    def __init__(self, x, y, w, h, text):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.text = text;
        self.fun = {};
        self.hovered = False;
        self.bTurtle = turtle.Turtle();
        self.bTurtle.hideturtle();

    # Draw the actual button graphic on the screen
    def draw(self):
        turtle.tracer(0, 0)
        self.bTurtle.hideturtle();
        self.bTurtle.penup();
        self.bTurtle.goto(self.x-(self.w/2),self.y-(self.h/2));
        self.bTurtle.pendown();

        if self.hovered == True:
            self.bTurtle.color("#a6a6a6");
        else:
            self.bTurtle.color("gray");
            
        self.bTurtle.begin_fill();
        for i in range(2):
            self.bTurtle.forward(self.w);
            self.bTurtle.left(90);
            self.bTurtle.forward(self.h);
            self.bTurtle.left(90);

        self.bTurtle.end_fill();
        
        self.bTurtle.penup();
        self.bTurtle.goto(self.x,self.y-(self.h/4));
        self.bTurtle.color("white");
        self.bTurtle.write(self.text, False, align="center", font=('Arial', 10, "bold"));
        self.bTurtle.color("gray");

        turtle.update();

    # Runs all click functions when the button is clicked.
    def onClick(self):
        for f, a in self.fun.items():
            if a == None:
                f();
            else:
                f(a);

    # Add a function to execute when button is clicked.
    def addClick(self, fun, args):
        self.fun[fun] = args;

    # When the button is hovered
    def onHover(self):
        self.bTurtle.reset();
        turtle.hideturtle();
        self.draw();

    # When the button is unhovered
    def unHover(self):
        self.bTurtle.reset();
        turtle.hideturtle();
        self.draw();

    # Set if the button is being hovered by mouse.
    def setHover(self, bo):
        self.hovered = bo;

    # Delete the button in its entirety.
    def delete(self):
        buttons.remove(self);

# Create a button with a function.
# Returns the instance of the button created.
def createButton(x, y, w, h, text):
    return Button(x, y, w, h, text);

# x = the x coordinates of where the click event happened,
# y = the y coordinates of where the click event happened.
# Loop through all the buttons that exist and check whether or not the click happens within the buttons area, if so then execute code.
def clickScreen(x, y):
    for b in buttons:
        if x > (b.x-(b.w/2)) and x < (b.x+(b.w/2)) and y > (b.y-(b.h/2)) and y < (b.y+(b.h/2)):
            if not b.fun == None:
                b.onClick();

def mouseMotion(event):
    # Convert coordinates to turtle coordinates
    x, y = (canvas.winfo_pointerx() - (turtle.window_width()/2) - canvas.winfo_rootx()) - 3, -(canvas.winfo_pointery() - (turtle.window_height()/2) - canvas.winfo_rooty() - 3)

    for b in buttons:
        if x > (b.x-(b.w/2)) and x < (b.x+(b.w/2)) and y > (b.y-(b.h/2)) and y < (b.y+(b.h/2)):
            if b.hovered == False:
                b.setHover(True);
                b.onHover();
        else:
            if b.hovered == True:
                b.setHover(False);
                b.unHover();
                
# Set the current buttons
def setButtons(b):
    buttons.clear();
    buttons.extend(b);
    
# On motion
canvas.bind('<Motion>', mouseMotion);         

# On click event.
turtle.onscreenclick(clickScreen, 1);
turtle.listen()

