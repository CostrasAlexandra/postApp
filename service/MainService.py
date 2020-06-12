import pickle

from sklearn.metrics import accuracy_score

from repository.PostDataRepository import PostDataRepository
from utils.SortAndFilterResults import SortAndFilterResults
from domain.ClassificationNames import ClassificationNames
from domain.Result import Result
from utils.UtilsForServices import UtilsForServices


class Service:
    def __init__(self):
        self.__file_name = './resources/tariClasificateAvgDateAntrenament.xlsx'
        self.__sheet_name = 'Tari'
        self.__post_data_repository = PostDataRepository(self.__file_name,self.__sheet_name)
        self.__path_name = './MLcomponent/'
        self.__model = pickle.load((open(self.__path_name+'finalized_model.sav', 'rb')))
        self.__input_data = pickle.load((open(self.__path_name+'x_test_data.pkl', 'rb')))
        self.__output_data = pickle.load((open(self.__path_name+'y_test_data.pkl', 'rb')))

        self.__classification_list = []
        self.__classification_with_names_list = set()

    def refresh_classification(self):
        self.__classification_list = pickle.load(open(self.__path_name+'create_result.pkl', 'rb'))

    def get_classification(self):
        self.refresh_classification()
        return self.__classification_list

    def get_ml_compoment(self):
        return self.__model

    def find_classification_by_value(self):
        self.__classification_with_names_list.clear()
        self.__classification_with_names_list = UtilsForServices.get_results_with_country_name(
            self.__classification_list)

    def get_classification_names(self):
        self.get_classification()
        self.find_classification_by_value()
        return sorted(self.__classification_with_names_list, key=lambda x: x.get_year(), reverse=False)

    def get_countries(self):
        list_of_countries = set()
        self.find_classification_by_value()
        for result in self.__classification_with_names_list:
            list_of_countries.add(result.get_country())
        return sorted(list_of_countries)

    def get_years(self):
        list_of_years = set()
        self.find_classification_by_value()
        for result in self.__classification_with_names_list:
            list_of_years.add(result.get_year())
        return sorted(list_of_years)

    def get_predictions(self):
        list_of_predictions = []
        for name, member in ClassificationNames.__members__.items():
            list_of_predictions.append(member.name)
        return list_of_predictions

    def filter_and_sort(self, country, year, prediction, sort_request):
        sort_and_filter = SortAndFilterResults(self.__classification_with_names_list)
        filtered_list = sort_and_filter.filter(country, year, prediction)
        if len(filtered_list) == 0:
            return sort_and_filter.sort(sort_request, self.__classification_with_names_list)
        return sort_and_filter.sort(sort_request, filtered_list)

    def get_test_data(self):
        rez = set()
        for data in UtilsForServices.get_results_with_country_name(pickle.load(open(self.__path_name+'get_test_data.pkl','rb'))):
            rez.add(data)
        return rez

    def get_accuracy(self):
        return UtilsForServices.truncate(accuracy_score(self.__output_data, self.__model.predict(self.__input_data)))*100

    def get_stability_statistics(self):
        stability_list = []
        for number in pickle.load(open(self.__path_name+'stability_statistic.pkl','rb')):
            stability_list.append(UtilsForServices.truncate(number)*100)
        return stability_list

