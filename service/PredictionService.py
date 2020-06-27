from sklearn.preprocessing import MinMaxScaler

from domain.Result import Result
from repository.PostDataRepository import PostDataRepository
from utils.SortAndFilterResults import SortAndFilterResults
from utils.UtilsForServices import UtilsForServices


class PredictionService:

    def __init__(self,ml_component,file_name,sheet_name):
        self.__ml_component = ml_component
        self.repository = PostDataRepository(file_name,sheet_name)
        self.list_of_results = []

    #applies the model on a dataset
    def get_predictions(self):

        data = self.repository.get_data()
        years = data['Year'].tolist()
        countries = data['Country'].tolist()
        real_output = data['Clasification'].tolist()
        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaled_data = scaler.fit_transform(data.iloc[:, 2:41])

        prediction = self.__ml_component.predict(rescaled_data)

        results = []
        for i in range(0,len(prediction)):
            results.append(Result(years[i],countries[i],prediction[i],real_output[i]))
        self.list_of_results = UtilsForServices.get_results_with_country_name(results)
        return self.list_of_results;

    def get_countries(self):
        list_of_countries = set()
        for result in self.list_of_results:
            list_of_countries.add(result.get_country())
        return sorted(list_of_countries)

    def get_years(self):
        list_of_years = set()
        for result in self.list_of_results:
            list_of_years.add(result.get_year())
        return sorted(list_of_years)

    def get_predictions_names(self):
        list_of_predictions = set()
        for result in self.list_of_results:
            list_of_predictions.add(result.get_prediction())
        return sorted(list_of_predictions)

    def filter_and_sort(self, country, year, prediction, sort_request):
        sort_and_filter = SortAndFilterResults(self.list_of_results)
        filtered_list = sort_and_filter.filter(country, year, prediction)
        if len(filtered_list) == 0:
            return sort_and_filter.sort(sort_request, self.list_of_results)
        return sort_and_filter.sort(sort_request, filtered_list)