from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

from service.PredictionService import PredictionService
from service.MainService import Service
from flask_bootstrap import Bootstrap

from utils.UtilsForServices import UtilsForServices

app = Flask(__name__)
Bootstrap(app)
service = Service()
classification_results = service.get_classification_names()
countries = service.get_countries()
years = service.get_years()
predictions = service.get_predictions()


@app.route('/performances')
def charts():
    return render_template('performance.html', predictions=list(service.get_predictions()),
                           predictions_numbers=UtilsForServices.get_list_of_numbers_of_predictions_of_same_type(
                               predictions, service.get_classification_names()),
                           expected_numbers=UtilsForServices.get_list_of_numbers_of_real_output_of_same_type(
                               predictions, service.get_test_data()),
                           accuracy=service.get_accuracy(), stability_statistics=service.get_stability_statistics())


@app.route('/results')
def results():
    return render_template('results.html', classification_results=classification_results, countries=countries,
                           years=years, predictions=predictions)


@app.route('/results', methods=['POST'])
def filter():
    if request.form["filter"] == "filter":
        print("filter")
        country = request.form['country']
        year = request.form['year']
        prediction = request.form['prediction']
        sort_request = request.form['sort_by']
        filtered_list = service.filter_and_sort(country, year, prediction, sort_request)
        return render_template('results.html', classification_results=filtered_list, countries=countries,
                               years=years, predictions=predictions)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/your_data")
def your_data():
    return render_template('your_data.html', title='Your Data')


sheet_name = 'Tari'


@app.route("/your_data", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            excel = request.files["excel"]
            if excel != "":
                if allowed_file(excel.filename):
                    filename = secure_filename(excel.filename)
                    print(filename)
                    prediction_service1 = PredictionService(service.get_ml_compoment(), excel, sheet_name)
                    return render_template("your_data.html", title='Your Data',
                                           classification_results=prediction_service1.get_predictions())
                else:
                    return render_template('your_data.html', title='Your Data', message="You can add only XLSX files", alert ="Error")



app.config["ALLOWED_FILE_EXTENSIONS"] = ["XLSX"]


def allowed_file(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
