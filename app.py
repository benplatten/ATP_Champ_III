import os 


from flask import Flask, render_template, request

from creative_builder_test import head_to_head, set_score


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
        match_date = request.form['']

        data = head_to_head(player1Name,player2Name,match_date)
        return render_template("receivedata.html", data=data)

    if template_type == '2':
        player1Name = request.form['player1Name']
        player2Name = request.form['player2Name']
        set_scores = request.form['set_scores']


        data = set_score(player1Name,player2Name,set_scores_string)
        return render_template("receivedata.html", data=data)

    if template_type == '3':
        winner = request.form['winner']
        set_scores = request.form['set_scores']
        aces = request.form['aces']
        unforced_errors = request.form['unforced_errors']        


        data = winner(player1Name,player2Name,winner,set_scores,aces,unforced_errors)
        return render_template("receivedata.html", data=data)

    if template_type == '4':
        winner = request.form['']
        player1_set_scores = request.form['']
        player2_set_scores = request.form['']
        player1_match_duration = request.form['']
        player2_match_duration = request.form['']
        player1_aces = request.form['']
        player2_aces = request.form['']
        player1_first_serve_winners = request.form['']
        player2_first_serve_winners = request.form['']
        player1_break_points_served = request.form['']
        player2_break_points_served = request.form['']
        player1_break_points_converted = request.form['']
        player2_break_points_converted = request.form['']
        player1_total_points_won = request.form['']
        player2_total_points_won = request.form['']
        winner_faces = request.form['']


        data = winner(winner,winner_set_scores,aces,unforced_errors)
        return render_template("receivedata.html", data=data)

    else:
        return render_template("receivedata.html", data='error')


    #if template_type == 2:
    #    do this
    #if template_type == 3:
   #     do this
    #if template_type == 4:
    #    do this


    


if __name__ == "__main__":
    app.run(debug=DEBUG,host=HOST,port=PORT)
