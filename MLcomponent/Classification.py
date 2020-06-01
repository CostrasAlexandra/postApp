from pandas import read_excel
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import resample
import pandas as pd

from domain.Result import Result


class Classification:
    data = any
    results = []
    n_samples_size = 93
    random_state_size = 45
    X_train = any
    X_test = any
    copy_X_test = any
    y_train = any
    y_test = any
    rescaledX_train = any
    rescaledY_train = any
    rescaledX_test = any
    rescaledY_test = any
    prediction = any

    def __init__(self, data):
        self.data = data
        self.__mlp = any

    def resample_data(self):
        data_0 = self.data[self.data.Clasification == 0]
        data_1 = self.data[self.data.Clasification == 1]
        data_2 = self.data[self.data.Clasification == 2]
        data_3 = self.data[self.data.Clasification == 3]
        data_4 = self.data[self.data.Clasification == 4]

        data_1_resample = resample(data_1, replace=True, n_samples=self.n_samples_size,
                                   random_state=self.random_state_size)
        data_2_resample = resample(data_2, replace=True, n_samples=self.n_samples_size,
                                   random_state=self.random_state_size)
        data_3_resample = resample(data_3, replace=True, n_samples=self.n_samples_size,
                                   random_state=self.random_state_size)
        data_4_resample = resample(data_4, replace=True, n_samples=self.n_samples_size,
                                   random_state=self.random_state_size)

        self.data = pd.concat([data_0, data_1_resample, data_2_resample, data_3_resample, data_4_resample])

    def separate_data(self):
        X = self.data.iloc[:, 0:41]
        y = self.data.iloc[:, 42:43]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.30)
        self.copy_X_test = self.X_test.copy();

        del self.X_test['Year']
        del self.X_train['Year']
        del self.X_train['Country']
        del self.X_test['Country']

    def prepare_data(self):
        scaler = MinMaxScaler(feature_range=(0, 1))
        self.rescaledX_train = scaler.fit_transform(self.X_train)
        self.rescaledY_train = scaler.fit_transform(self.y_train)
        self.rescaledX_test = scaler.fit_transform(self.X_test)
        self.rescaledY_test = scaler.fit_transform(self.y_test)

    def ann(self):
        self.__mlp = MLPClassifier(hidden_layer_sizes=(20, 20, 20), max_iter=3000)
        self.__mlp.fit(self.rescaledX_train, self.y_train.values.ravel())

    def test_ann(self):
        self.predictions = self.__mlp.predict(self.rescaledX_test)
        years = self.copy_X_test['Year'].tolist()
        countries = self.copy_X_test['Country'].tolist()
        self.results = self.create_result(years, countries, self.predictions)

    def classification(self):
        self.resample_data()
        self.separate_data()
        self.prepare_data()
        self.ann()
        self.test_ann()

    def get_results(self):
        return self.results

    def report(self):
        return classification_report(str(self.y_test), self.predictions, str(zero_division=1))

    def predict(self, list_of_data):
        x_input = list_of_data.iloc[:, 0:41]
        copy_x_input = list_of_data.iloc[:, 0:41]

        del x_input['Year']
        del x_input['Country']

        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaled_x_input = scaler.fit_transform(x_input)

        predict = self.__mlp.predict(rescaled_x_input)
        years = copy_x_input['Year'].tolist()
        countries = copy_x_input['Country'].tolist()

        return self.create_result(years, countries, predict)

    def create_result(self, years, countries, predictions):
        rez = []
        for i in range(0, len(years)):
            rez.append(Result(years[i], countries[i], predictions[i]))
        return rez
