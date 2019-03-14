from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os




def head_to_head(player1Name,player2Name):

    template = Image.open('static/ATP_Static_V2.png')
    player1image = Image.open('static/players/' + str(player1Name) + '.jpg')
    player2image = Image.open('static/players/' + str(player2Name) + '.jpg')
    r_al = 1080 - len(player2Name)
    template.paste(player1image, (100, 238))
    template.paste(player2image, (r_al, 238))
    # will the images include name?
    location = 'static/new_creative/'+'h2h'+'_'+player1Name+'_'+player2Name+'.png'
    template.save(location)
    return location




def set_score():
    template = Image.open('static/ATP_Static_Stats.png')
    set_number = "Set " + input("Enter set number: ") +" score"
    home_score = input("Enter home set score: ")
    away_score = input("Enter away set score: ")


    #format

    fontsFolder = 'C:\Windows\Fonts'
    font_format = ImageFont.truetype(os.path.join(fontsFolder, 'CHILLER.ttf'), 80)


    #paste in location

    draw = ImageDraw.Draw(template)
    draw.text((500,100), set_number, fill="red",font=font_format)
    draw.text((400,300), home_score, fill="red",font=font_format)
    draw.text((800,300), away_score, fill="red",font=font_format)

    #right align test
    name = "Nadal"
    r_al = 1080 - len(name)
    igr = Image.open('static/RepriseBlack.jpg')
    template.paste(igr, (r_al, 238))


    #save / return output
    template.show()

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

    


#head_to_head('Rafael Nadal','Roger Federer')
#select_template()


#input control
#regex selection
#html form input to python variable


