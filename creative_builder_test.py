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

    location = 'static/new_creative/'+'setscore'+'_'+player1Name+'_'+player2Name+'_'+set_scores_string+'_'+'.png'
    template.save(location)
    return location


def match_winner(player1Name,player2Name,winner,set_scores_string,aces,unforced_errors):
    player1Name = player1Name.upper()
    player2Name = player2Name.upper()
    set_scores_string = set_scores_string.upper()

    if winner == "1":
        winner = player1Name
        loser = "VS. " + player2Name
    if winner == "2":
        winner = player2Name
        loser = "VS. " + player1Name



    template = Image.open('static/03 Winner.png')

    font_format_winner = ImageFont.truetype("static/Gilroy/Gilroy-ExtraBoldItalic.otf", 52)
    font_format_loser = ImageFont.truetype("static/Gilroy/Gilroy-ExtraBoldItalic.otf", 18)
    font_format_rest = ImageFont.truetype("static/Gilroy/Gilroy-Bold.otf", 16)

    draw = ImageDraw.Draw(template)
    wwidth, wheight = draw.textsize(winner, font=font_format_winner)
    swidth, sheight = draw.textsize(set_scores_string, font=font_format_rest)
    awidth, aheight = draw.textsize(aces, font=font_format_rest)
    uewidth, ueheight = draw.textsize(unforced_errors, font=font_format_rest)   


    ## factor in white space
   
    draw.text((372-wwidth,199), winner, fill="#000000",font=font_format_winner)
    draw.text((197,258), loser, fill="#FFFFFF",font=font_format_loser)
    draw.text((788-swidth,180), set_scores_string, fill="#FFFFFF",font=font_format_rest)
    draw.text((788-awidth,225), aces, fill="#FFFFFF",font=font_format_rest)
    draw.text((788-uewidth,268), unforced_errors, fill="#FFFFFF",font=font_format_rest)

    location = 'static/new_creative/'+'winner'+'_'+player1Name+'_'+player2Name+'_'+set_scores_string+'_'+'.png'
    template.save(location)
    return location


def post_match_card(player1Name,player2Name,winner,set_scores,match_duration,player1_aces,player2_aces,player1_first_serve_winners,
            player2_first_serve_winners,player1_break_points_served,player2_break_points_served,player1_break_points_converted
            ,player2_break_points_converted,player1_total_points_won,player2_total_points_won,winner_faces):

            player1Name = player1Name.upper()
            player2Name = player2Name.upper()
            winner_faces = winner_faces.upper()
            set_scores = set_scores.upper()

            template = Image.open('static/04 Stats.png')
            trophy = Image.open('static/Winner (White).png')

            font_format = ImageFont.truetype("static/Gilroy/GilroyBlack.otf", 27)
            font_format_p3 = ImageFont.truetype("static/Gilroy/GilroyBlack.otf", 36)      

            draw = ImageDraw.Draw(template)
            p1width, p1height = draw.textsize(player1Name, font=font_format)
            swidth, sheight = draw.textsize(set_scores, font=font_format)
            mdwidth, mdheight = draw.textsize(match_duration, font=font_format)
            p1awidth, p1aheight = draw.textsize(player1_aces, font=font_format)
            p1fswwidth, p1fswaheight = draw.textsize(player1_first_serve_winners, font=font_format)
            p1bpswidth, p1bpsheight = draw.textsize(player1_break_points_served, font=font_format)
            p1bpcwidth, p1bpcheight = draw.textsize(player1_break_points_converted, font=font_format)
            p1tpwwidth, p1tpwheight = draw.textsize(player1_total_points_won, font=font_format)

            if winner == "1":
                template.paste(trophy,(284,46), mask=trophy)
                
            if winner == "2":
                template.paste(trophy,(692,46), mask=trophy)

            ## factor in white space
           
            draw.text((511-p1width,1), player1Name, fill="#290045",font=font_format)
            draw.text((552,1), player2Name, fill="#290045",font=font_format)
            draw.text((532-(swidth/2),64), set_scores, fill="#FFFFFF",font=font_format)
            draw.text((522-p1awidth,151), player1_aces, fill="#FFFFFF",font=font_format)
            draw.text((542,151), player2_aces, fill="#FFFFFF",font=font_format)
            draw.text((522-p1fswwidth,196), player1_first_serve_winners, fill="#FFFFFF",font=font_format)
            draw.text((542,196), player2_first_serve_winners, fill="#FFFFFF",font=font_format)
            draw.text((522-p1bpswidth,242), player1_break_points_served, fill="#FFFFFF",font=font_format)
            draw.text((542,242), player2_break_points_served, fill="#FFFFFF",font=font_format)
            draw.text((522-p1bpcwidth,287), player1_break_points_converted, fill="#FFFFFF",font=font_format)
            draw.text((542,287), player2_break_points_converted, fill="#FFFFFF",font=font_format)
            draw.text((522-p1tpwwidth,333), player1_total_points_won, fill="#FFFFFF",font=font_format)
            draw.text((542,333), player2_total_points_won, fill="#FFFFFF",font=font_format)
            draw.text((533-(mdwidth/2),108), match_duration, fill="#FFFFFF",font=font_format)
            draw.text((421,374), winner_faces, fill="#290045",font=font_format_p3)


            location = 'static/new_creative/'+'stats'+'_'+player1Name+'_'+player2Name+'_'+set_scores+'_'+'.png'
            template.save(location)
            return location


    
#match_winner("Nadal","Federer","1","6-2","2","2")

#
#head_to_head('Rafael Nadal','Roger Federer','tomorrow')
#select_template()


#input control
#regex selection
#html form input to python variable


