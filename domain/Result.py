class Result:
    def __init__(self, year, country, prediction):
        self.__year = year
        self.__country = country
        self.__prediction = prediction

    def get_year(self):
        return self.__year

    def get_country(self):
        return self.__country

    def get_prediction(self):
        return self.__prediction

    def to_string(self):
        return str(self.__year) + ' ' + self.__country + ' ' + str(self.__prediction)

    def year_and_country_to_string(self):
        return str(self.__year) + ' ' + self.__country

    def __str__(self):
        return str(self.__year) + ' ' + self.__country + ' ' + str(self.__prediction)

    def __eq__(self, other):
        return self.__country == other.__country and self.__year == other.__year and self.__prediction == other.__prediction

    def __hash__(self):
        return hash((self.__country, self.__year, self.__prediction))