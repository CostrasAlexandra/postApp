# from flask import Blueprint, render_template, request,g
# from service.Service import Service
#
# results_blueprint = Blueprint('results_blueprint', __name__, template_folder='templates',
#     static_folder='static')
#
#
# classification_results = g.service.get_classification_names()
# countries = g.service.get_countries()
# years = g.service.get_years()
# predictions = g.service.get_predictions()
#
# sheet_name = 'Tari'
#
# @results_blueprint.route('/results')
# def results():
#     return render_template('results.html', classification_results=classification_results, countries=countries,
#                            years=years, predictions=predictions)
#
#
# @results_blueprint.route('/results', methods=['POST'])
# def filter():
#     if request.form["filter"] == "filter":
#         print("filter")
#         country = request.form['country']
#         year = request.form['year']
#         prediction = request.form['prediction']
#         sort_request = request.form['sort_by']
#         filtered_list = service.filter_and_sort(country,year,prediction,sort_request)
#         return render_template('results.html', classification_results=filtered_list, countries=countries,
#                                years=years, predictions=predictions)
