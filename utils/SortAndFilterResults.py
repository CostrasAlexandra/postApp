from domain.Result import Result


class SortAndFilterResults:

    def __init__(self,classification_list):
        self.classification_with_names_list = classification_list

    def __filter_by_country(self, country):
        list_of_results = list()

        for result in self.classification_with_names_list:
            if result.get_country() == country:
                list_of_results.append(result)
        return list_of_results

    def __filter_by_year(self, year):
        list_of_results = list()
        for result in self.classification_with_names_list:
            if result.get_year() == year:
                list_of_results.append(result)
        return list_of_results

    def __filter_by_country_and_year(self, country, year):
        for result in self.classification_with_names_list:
            if result.get_year() == year and result.get_country() == country:
                return [result]
        return [Result(0, "Not Found", "Not Found")]

    def __filter_by_country_and_prediction(self, country, prediction):
        list_of_results = list()
        for result in self.classification_with_names_list:
            if result.get_prediction() == prediction and result.get_country() == country:
                list_of_results.append(result)
        if len(list_of_results) == 0:
            return [Result(0, "Not Found", "Not Found")]
        else:
            return list_of_results

    def __filter_by_year_and_prediction(self, year, prediction):
        list_of_results = list()
        for result in self.classification_with_names_list:
            if result.get_prediction() == prediction and result.get_year() == year:
                list_of_results.append(result)
        if len(list_of_results) == 0:
            return [Result(0, "Not Found", "Not Found")]
        else:
            return list_of_results

    def __sort_by_year(self, list_to_sort):
        return sorted(list_to_sort, key=lambda x: x.get_year(), reverse=False)

    def __sort_by_country(self, list_to_sort):
        return sorted(list_to_sort, key=lambda x: x.get_country(), reverse=False)

    def __filter_by_prediction(self, prediction_name):
        list_of_results = list()
        for result in self.classification_with_names_list:
            if result.get_prediction() == prediction_name:
                list_of_results.append(result)
        return list_of_results

    def __filter_by_country_year_prediction(self, country, year, prediction):
        for result in self.classification_with_names_list:
            if result.get_year() == year and result.get_country() == country and result.get_prediction() == prediction:
                return [result]
        return [Result(0, "Not Found", "Not Found")]

    def filter(self, country, year, prediction):
        filtered_list = set()
        if country != 'Country':
            if prediction != 'Prediction':
                if year != 'Year':
                    year = int(year)
                    filtered_list = self.__filter_by_country_year_prediction(country, year, prediction)
                else:
                    filtered_list = self.__filter_by_country_and_prediction(country, prediction)
            else:
                if year != 'Year':
                    year = int(year)
                    filtered_list = self.__filter_by_country_and_year(country, year)
                else:
                    filtered_list = self.__filter_by_country(country)
        else:
            if prediction != 'Prediction':
                if year != 'Year':
                    year = int(year)
                    filtered_list = self.__filter_by_year_and_prediction(year, prediction)
                else:
                    filtered_list = self.__filter_by_prediction(prediction)
            else:
                if year != 'Year':
                    year = int(year)
                    filtered_list = self.__filter_by_year(year)
        return filtered_list

    def sort(self, sort_request, list_to_sort):
        if sort_request == 'Year':
            return self.__sort_by_year(list_to_sort)
        else:
            return self.__sort_by_country(list_to_sort)
