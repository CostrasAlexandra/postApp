from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

from MLcomponent.Classification import Classification
from repository.PostDataRepository import PostDataRepository
from service.PredictionService import PredictionService
from service.Service import Service
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# file_name = './resources/tariClasificateAvgDateAntrenament.xlsx'
# sheet_name = 'Tari'
# post_data_repository = PostDataRepository(file_name,sheet_name)
# classification = Classification(post_data_repository.get_data())
# classification.classification()

service = Service()
classification_results = service.get_classification_names()
countries = service.get_countries()
years = service.get_years()
predictions = service.get_predictions()

sheet_name = 'Tari'


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
        filtered_list = service.filter_and_sort(country,year,prediction,sort_request)
        return render_template('results.html', classification_results=filtered_list, countries=countries,
                               years=years, predictions=predictions)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/your_data")
def your_data():
    return render_template('your_data.html',title='Your Data')

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["XLSX"]

def allowed_file(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/your_data", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            excel = request.files["excel"]
            if excel != '':
                if allowed_file(excel.filename):
                    filename = secure_filename(excel.filename)
                    print(filename)
                prediction_service1 = PredictionService(service.get_ml_compoment(), excel, sheet_name)
                return render_template("your_data.html",classification_results = prediction_service1.get_predictions())

    return render_template("your_data.html")


if __name__ == '__main__':
    app.run()
