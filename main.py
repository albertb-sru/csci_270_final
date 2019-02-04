#!/usr/bin/env python3
# Made by Albert
# main.py

import button;
import calendar;
import datetime;
import db_handler as dbh;
import dictionary;
import math;
import os;
import turtle;
import time;
import webpages as web;
import webbrowser;


# Text to show on turtle
turtleText= """
You have been alive %alive% days!
Your Chinese Animal: %chyr%
Your Zodiac: %zodiac%
Your personality: \n%personality%
""";

# Location in which the webpage results will be.
webLocation = "./web/results.html"

# Convert a number with two or more digits to one digit by summing its digits.
def sumNum(num):
    while num >= 10:
        num = sum( [ int(i) for i in str(num) ] );
    return num;

# Write text like an error, in red.
def writeError(text):
    turtle.color("red")
    turtle.write(text, False, align="center", font=('Arial', 24, 'bold'))

# Write text, c is the color of the text, s is the size, and b is the style, 'normal', 'bold'.
def writeText(text, c, s, b):
    turtle.color(c)
    turtle.write(text, False, align="center", font=('Arial', s, b))

# Write for logs
def writeLog(text, c, s, b):
    turtle.color(c)
    turtle.write(text, True, align="left", font=('Arial', s, b))

# Open the results web page.
def openWebpage():
    path = os.path.abspath("./web/results.html");
    webbrowser.open_new("file:///" + path);

# Move the pen on the X axis.
def movePenX(x):
    turtle.penup();
    turtle.setx(x);
    turtle.pendown();

# Move the pen on the Y axis.
def movePenY(y):
    turtle.penup();
    turtle.sety(y);
    turtle.pendown();

# Switch between screens
def switchScreen(fun):
    turtle.resetscreen();
    button.buttons.clear()
    for t in turtle.turtles():
        t.ht();
    fun();

# First scene in the app
def startUp():
    buttons = [];
    turtle.tracer(0,0);
    movePenY(75)
    writeText("Birth Test", "black", 18, 'bold');
    movePenY(50)
    writeText("By Albert", "black", 12, 'normal');

    start_button.draw();
    buttons.append(start_button);

    logs_button.draw();
    buttons.append(logs_button);

    button.setButtons(buttons);

    turtle.update();

def viewLogs():
    buttons = [];

    back_button.draw();

    buttons.append(back_button);

    movePenY(150);
    movePenX(0);
    
    writeText("Birth Test Logs", "black", 18, 'bold');

    y = 125;
    movePenY(y);
    writeText("Timestamp | Name | Birthdate | Days Alive | Personality ID | Chinese Year ID | Zodiac ID", "black", 12, "bold");
    y-=20;
    movePenY(y);
    movePenX(-200);
    logs = [tuple(arr) for arr in dbh.getLogs()];

    # Show a list of logs sorted by newest to oldest.
    for row in reversed(sorted(logs, key=lambda entry: entry[0])):
        writeLog(\
            datetime.datetime.fromtimestamp(row[0]).strftime("%m-%d-%Y %H:%M:%S"), "blue", 12, "normal");
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(\
            row[1], "red", 12, "normal");
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(\
            datetime.datetime.fromtimestamp(row[2]).strftime("%m-%d-%Y"), "green", 12, "normal");
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(row[3], "purple", 12, "normal")
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(row[4], "blue", 12, "normal")
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(row[5], "red", 12, "normal")
        writeLog(\
            " || ", "black", 12, "normal");
        writeLog(row[6], "green", 12, "normal")
        y-=20;
        movePenY(y)
        movePenX(-200)

    button.setButtons(buttons);
    turtle.update();

# Second scene in the app
def mainApp():
    # Draw the main part of the application
    def drawResults():
        buttons = [];
        turtle.reset();

        # Move the turtle pen
        movePenY(75);

        turtle.tracer(0, 0);

        # Write to turtle
        writeText("Hello " + firstName.capitalize() + " I see you were born on " + calendar.month_name[bMon] + " " + str(bDay) + " in the year " + str(bYear) + " on a " + calendarBday, "black", 18, 'bold');

        # Move the turtle pen
        movePenY(-215);

        # Write the text to turtle
        writeText(turtleText.replace("%alive%", str(daysAlive.days))\
                  .replace("%chyr%", dictionary.chyr[chyr])\
                  .replace("%zodiac%", dictionary.getZodiacName(zodiac))\
                  .replace("%personality%", dictionary.paragraphs[personality]), "gray", 12, 'normal');

        v_web.draw();
        buttons.append(v_web);
        z_info.draw();
        buttons.append(z_info);
        ex.draw();
        buttons.append(ex);

        button.setButtons(buttons);

        turtle.update();
    
    # Get the users first name
    firstName = turtle.textinput("", "What is your name?");

    # If the user does not put their birthdate in the correct format
    # then the error is caught and makes them reinput their birthdate correctly.
    while True:
        try:
            t = time.strptime(turtle.textinput("", "What date were you born? (Format mm-dd-yyyy) "), "%m-%d-%Y");
            turtle.reset();
            break;
        except ValueError:
           writeError("Oops! You did not use the correct birthdate format! (mm-dd-yyyy)");

    # Set Variables to make it a bit simpler.
    bDay = t.tm_mday;
    bYear = t.tm_year;
    bMon = t.tm_mon;

    # Calculate the birth sum number for personality paragraphs.
    personality = sumNum(bDay + bYear + bMon);

    # Calculate Chineses yr number
    chyr = ((bYear-1900) % 12) + 1;

    # Get the day the person was born on. Ex. Tuesday.
    calendarBday = calendar.day_name[datetime.datetime(bYear, bMon, bDay).weekday()];

    # Get the persons zodiac sign.
    zodiac = dictionary.getZodiac(bMon, bDay);

    # Calculate days alive.
    now = datetime.date.today();
    age = datetime.date(bYear, bMon, bDay);
    daysAlive = now-age;

    # Equation to calculate biorhythm
    gen_eq = lambda t, x: round(math.sin((2*math.pi*t)/x)*100);

    # Calculate each of the main three biorhythm
    bio_phys = gen_eq(daysAlive.days, 23);
    bio_emot = gen_eq(daysAlive.days, 28);
    bio_inte = gen_eq(daysAlive.days, 33);

    # Set the addClick to open webpage on click.
    z_info.addClick(lambda z: webbrowser.open_new(z), dictionary.getZodiacURL(zodiac));

    # Open the webpage file to write to it.
    webPage = open(webLocation, "wt");

    # Gather the html and replace each placeholder with its content.
    html = web.getHTML()\
        .replace("%firstname%", firstName)\
        .replace("%chyr%", dictionary.chyr[chyr])\
        .replace("%days_alive%", str(daysAlive.days))\
        .replace("%personality%", dictionary.paragraphs[personality])\
        .replace("%zodiac%", dictionary.getZodiacName(zodiac))\
        .replace("%z_url%", dictionary.getZodiacURL(zodiac))\
        .replace("%bio_phys%", str(bio_phys))\
        .replace("%bio_emot%", str(bio_emot))\
        .replace("%bio_inte%", str(bio_inte));

    # Write to the webpage file and close it.
    webPage.write(html);
    webPage.close();

    # Draw the results on turtle.
    drawResults();

    # Log info to logs.db
    dbh.addLog(firstName, datetime.datetime(bYear, bMon, bDay).timestamp(), daysAlive.days, personality, chyr, zodiac);

# Create all instances of buttons.
start_button = button.createButton(0, 0, 100, 30, "Begin");
start_button.addClick(switchScreen, mainApp);

logs_button = button.createButton(0, -50, 100, 30, "View Logs");
logs_button.addClick(switchScreen, viewLogs);

back_button = button.createButton(-125, 165, 50, 25, "Back");
back_button.addClick(switchScreen, startUp);

v_web = button.createButton(0, -235, 100, 40, "View Webpage");
# Set the button to open web version on click.
v_web.addClick(openWebpage, None);

z_info = button.createButton(125, -235, 100, 40, "Zodiac Info");

ex = button.createButton(-125, -235, 100, 40, "Exit");
ex.addClick(turtle.bye, None);

startUp();
