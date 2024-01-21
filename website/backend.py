import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__, template_folder=".")

@app.route('/',methods=['GET','POST'])
def my_maps():
	mapbox_access_token = 'pk.eyJ1IjoiamVyZW1pYXMyMTMiLCJhIjoiY2xybWY1OTN6MTBpMjJrcDc0c3Z1Z3RzbiJ9.JAmfJcUFTUBaoVPQ7fvTyQ'

	return render_template('gpt.html',
		mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
	app.run(debug=True)
