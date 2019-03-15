from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os
import urllib.parse




def head_to_head(player1Name,player2Name,match_date):
    
    player1Name = player1Name.upper()
    player2Name = player2Name.upper()
    match_date = match_date.upper()

    template = Image.open('static/01 PvP.png')

    font_format = ImageFont.truetype("static/Gilroy/GilroyBlack.otf", 41)
    font_format_date = ImageFont.truetype("static/Gilroy/Gilroy-Bold.otf", 23)

    draw = ImageDraw.Draw(template)
    p1width, p1height = draw.textsize(player1Name, font=font_format)
    mdwidth, mdheight = draw.textsize(match_date, font=font_format_date)

    ## factor in white space
   
    draw.text((368-p1width,333), player1Name, fill="#290045",font=font_format)
    draw.text((430,333), player2Name, fill="#290045",font=font_format)
    draw.text((791-mdwidth,390), match_date, fill="#290045",font=font_format_date)

    location = 'static/new_creative/'+'h2h'+'_'+player1Name+'_'+player2Name+'_'+match_date+'_'+'.png'
    template.save(location)
    return location





#
def set_score(player1Name,player2Name,set_scores_string):

    player1Name = player1Name.upper()
    player2Name = player2Name.upper()
    set_scores_string = set_scores_string.upper()

    template = Image.open('static/02 Set Scores.png')

    font_format = ImageFont.truetype("static/Gilroy/GilroyBlack.otf", 41)
    font_format_scores = ImageFont.truetype("static/Gilroy/Gilroy-Bold.otf", 23)

    draw = ImageDraw.Draw(template)
    p1width, p1height = draw.textsize(player1Name, font=font_format)
    swidth, sheight = draw.textsize(set_scores_string, font=font_format_scores)

    ## factor in white space
   
    draw.text((368-p1width,333), player1Name, fill="#290045",font=font_format)
    draw.text((430,333), player2Name, fill="#290045",font=font_format)
    draw.text((400-(swidth/2),390), set_scores_string, fill="#FFFFFF",font=font_format_scores)

    location = 'static/new_creative/'+'h2h'+'_'+player1Name+'_'+player2Name+'_'+set_scores_string+'_'+'.png'
    template.save(location)
    return location




#def winner():


def post_match_card():

    template2 = Image.open('creative/ATP_Static_Stats.png')
    sets = input("Enter number of sets: ")
    home_set_scores = input("Enter score of games of sets won by home player (e.g 6-4,6-2): ")
    away_set_scores = input("Enter score of games of sets won by away player (e.g 6-4,6-2): ")
    match_duration = input("Enter match duration in -units-: ")
    aces = input("Enter number of aces: ")

    draw = ImageDraw.Draw(template)
    draw.text((500, 100), sets, fill="red", font=font_format)
    draw.text((400, 300), home_set_scores, fill="red", font=font_format)
    draw.text((800, 300), away_set_scores, fill="red", font=font_format)

    template.show()


def select_template():
    while True:
        accepted = ['1','2','End']
        creative = input("""Which creative template do you require? \n Choose from: 
                \n Enter '1' for POST SET SCORE CARD 
                \n Enter '2' for POST MATCH SCORE CARD
                \n (Enter 'End' if no template is required) 
                \n -: """)

        if creative == '1':
            print ("You have selected POST SET SCORE CARD. Excellent choice, m'lord.")

            set_score()
        elif creative == '2':
            post_match_card()

        elif creative == 'End':
            break
        
        elif creative not in accepted:
            print ("That is not an option. Please try again.")

    


#head_to_head('Rafael Nadal','Roger Federer','tomorrow')
#select_template()


#input control
#regex selection
#html form input to python variable


