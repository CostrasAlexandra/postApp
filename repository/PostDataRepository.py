from pandas import read_excel


class PostDataRepository:

    def __init__(self, file_name, sheet_name):
        self.__file_name = file_name
        self.__sheet_name = sheet_name

    def read_data(self):
        return read_excel(self.__file_name, sheet_name=self.__sheet_name)

    def get_data(self):
        return self.read_data()