import os 


from flask import Flask, render_template, request

from creative_builder_test import head_to_head


ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    PORT = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    PORT = 3000


DEBUG = True
HOST = '0.0.0.0'


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
    	data = head_to_head(player1Name,player2Name)
    	return render_template("receivedata.html", data=data)

    else:
    	return render_template("receivedata.html", data='error')


    #if template_type == 2:
    #	do this
    #if template_type == 3:
   # 	do this
    #if template_type == 4:
    #	do this


    


if __name__ == "__main__":
    app.run(debug=DEBUG,host=HOST,port=PORT)