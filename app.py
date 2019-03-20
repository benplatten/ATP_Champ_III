import os 


from flask import Flask, render_template, request

from creative_builder_test import head_to_head, set_score, match_winner, post_match_card


ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    PORT = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    PORT = 5000


DEBUG = True
HOST = '127.0.0.1'


app = Flask(__name__)

@app.route("/")
def home():   

    return render_template("home.html")

@app.route('/receivedata', methods=['POST'])
def receive_data():
    template_type = request.form['template_type']
    if template_type == '1':
        player1Name = request.form['player1Name']
        player2Name = request.form['player2Name']
        match_date = request.form['match_date']

        data = head_to_head(player1Name,player2Name,match_date)
        return render_template("receivedata.html", data=data)

    if template_type == '2':
        player1Name = request.form['player1Name']
        player2Name = request.form['player2Name']
        set_scores_string = request.form['set_scores']


        data = set_score(player1Name,player2Name,set_scores_string)
        return render_template("receivedata.html", data=data)

    if template_type == '3':
        player1Name = request.form['player1Name']
        player2Name = request.form['player2Name']
        winner_name = request.form['winner']
        set_scores_string = request.form['set_scores']
        aces = request.form['aces']
        unforced_errors = request.form['unforced_errors']        


        data = match_winner(player1Name,player2Name,winner_name,set_scores_string,aces,unforced_errors)
        return render_template("receivedata.html", data=data)

    if template_type == '4':
        player1Name = request.form['player1Name']
        player2Name = request.form['player2Name']
        winner = request.form['winner']
        set_scores = request.form['set_scores']
        match_duration = request.form['match_duration']
        player1_aces = request.form['player1_aces']
        player2_aces = request.form['player2_aces']
        player1_first_serve_winners = request.form['player1_first_serve_winners']
        player2_first_serve_winners = request.form['player2_first_serve_winners']
        player1_break_points_served = request.form['player1_break_points_served']
        player2_break_points_served = request.form['player2_break_points_served']
        player1_break_points_converted = request.form['player1_break_points_converted']
        player2_break_points_converted = request.form['player2_break_points_converted']
        player1_total_points_won = request.form['player1_total_points_won']
        player2_total_points_won = request.form['player2_total_points_won']
        winner_faces = request.form['player3Name']


        data = post_match_card(player1Name,player2Name,winner,set_scores,match_duration,player1_aces,player2_aces,player1_first_serve_winners,
        	player2_first_serve_winners,player1_break_points_served,player2_break_points_served,player1_break_points_converted
        	,player2_break_points_converted,player1_total_points_won,player2_total_points_won,winner_faces)
        return render_template("receivedata.html", data=data)

    else:
        return render_template("receivedata.html", data='error')
   


if __name__ == "__main__":
    app.run(debug=DEBUG,host=HOST,port=PORT)
