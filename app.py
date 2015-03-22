import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = './static/rtfounders.csv'
	csv_file = open(csv_path, 'rb')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list
	return render_template(template, object_list=object_list)


@app.route("/")
def index():
	template = 'index.html'
	return render_template(template)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
