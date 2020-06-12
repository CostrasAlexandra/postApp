class Result:
    def __init__(self, year, country, prediction, real_output):
        self.__year = year
        self.__country = country
        self.__prediction = prediction
        self.__real_output = real_output

    def get_year(self):
        return self.__year

    def get_country(self):
        return self.__country

    def get_prediction(self):
        return self.__prediction

    def get_real_output(self):
        return self.__real_output

    def to_string(self):
        return str(self.__year) + ' ' + self.__country + ' ' + str(self.__prediction) + ' ' + str(self.__real_output)

    def year_and_country_to_string(self):
        return str(self.__year) + ' ' + self.__country

    def __str__(self):
        return str(self.__year) + ' ' + self.__country + ' ' + str(self.__prediction) + str(self.__real_output)

    def __eq__(self, other):
        return self.__country == other.__country and self.__year == other.__year and self.__prediction == other.__prediction and self.__real_output == other.__real_output

    def __hash__(self):
        return hash((self.__country, self.__year, self.__prediction, self.__real_output))
