from MLcomponent.Classification import Classification
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
        self.__classification = Classification(self.__post_data_repository.get_data())
        self.__classification.classification()

        self.__classification_list = []
        self.__classification_with_names_list = set()

    def refresh_classification(self):
        self.__classification_list = self.__classification.get_results()

    def get_classification(self):
        self.refresh_classification()
        return self.__classification_list

    def get_ml_compoment(self):
        return self.__classification

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
        list_of_predictions = set()
        self.find_classification_by_value()
        for result in self.__classification_with_names_list:
            list_of_predictions.add(result.get_prediction())
        return sorted(list_of_predictions)

    def filter_and_sort(self, country, year, prediction, sort_request):
        sort_and_filter = SortAndFilterResults(self.__classification_with_names_list)
        filtered_list = sort_and_filter.filter(country, year, prediction)
        if len(filtered_list) == 0:
            return sort_and_filter.sort(sort_request, self.__classification_with_names_list)
        return sort_and_filter.sort(sort_request, filtered_list)
