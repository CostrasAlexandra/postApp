from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import resample
import pandas as pd
import pickle

from domain.Result import Result
from utils.UtilsForMLcomponent import UtilsForMLcomponent


class Classification:

    def __init__(self, data):
        self.__data = data
        self.__mlp = any
        self.__statistics = []
        self.__results = []
        self.__n_samples_size = 93
        self.__random_state_size = 45
        self.__X_train = any
        self.__X_test = any
        self.__copy_X_test = any
        self.__y_train = any
        self.__y_test = any
        self.__rescaledX_train = any
        self.__rescaledY_train = any
        self.__rescaledX_test = any
        self.__rescaledY_test = any
        self.__predictions = any
        self.__copy_Y_test = []

    def __resample_data(self):
        data_0 = self.__data[self.__data.Clasification == 0]
        data_1 = self.__data[self.__data.Clasification == 1]
        data_2 = self.__data[self.__data.Clasification == 2]
        data_3 = self.__data[self.__data.Clasification == 3]
        data_4 = self.__data[self.__data.Clasification == 4]

        data_1_resample = resample(data_1, replace=True, n_samples=self.__n_samples_size,
                                   random_state=self.__random_state_size)
        data_2_resample = resample(data_2, replace=True, n_samples=self.__n_samples_size,
                                   random_state=self.__random_state_size)
        data_3_resample = resample(data_3, replace=True, n_samples=self.__n_samples_size,
                                   random_state=self.__random_state_size)
        data_4_resample = resample(data_4, replace=True, n_samples=self.__n_samples_size,
                                   random_state=self.__random_state_size)

        self.__data = pd.concat([data_0, data_1_resample, data_2_resample, data_3_resample, data_4_resample])

    # separates data in train data and test data
    def __separate_data(self):
        x = self.__data.iloc[:, 0:41]
        y = self.__data.iloc[:, 42:43]

        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(x, y, test_size=0.30)
        self.__copy_X_test = self.__X_test.copy()
        self.__copy_Y_test = self.__y_test.copy()

        del self.__X_test['Year']
        del self.__X_train['Year']
        del self.__X_train['Country']
        del self.__X_test['Country']

    # normalize data
    def __prepare_data(self):
        scaler = MinMaxScaler(feature_range=(0, 1))

        self.__rescaledX_train = scaler.fit_transform(self.__X_train)
        self.__rescaledY_train = scaler.fit_transform(self.__y_train)
        self.__rescaledX_test = scaler.fit_transform(self.__X_test)
        self.__rescaledY_test = scaler.fit_transform(self.__y_test)

    # train
    def __ann(self):
        self.__mlp = MLPClassifier(hidden_layer_sizes=(20, 20, 20), max_iter=3000)
        self.__mlp.fit(self.__rescaledX_train, self.__y_train.values.ravel())

    # test the ann saves the result
    def __test_ann(self):
        self.__predictions = self.__mlp.predict(self.__rescaledX_test)
        self.__save_result()

    def classification(self):
        self.__resample_data()
        self.__separate_data()
        self.__prepare_data()
        self.__find_stability_statistics()
        self.__ann()
        self.__test_ann()

    def save_model(self):
        self.classification()

        filename_model = 'finalized_model.sav'
        filename_x = 'x_test_data.pkl'
        filename_y = 'y_test_data.pkl'

        pickle.dump(self.__mlp, open(filename_model, 'wb'))
        pickle.dump(self.__rescaledX_test, open(filename_x, 'wb'))
        pickle.dump(self.__y_test, open(filename_y, 'wb'))
        self.__get_test_data()

    def __save_result(self):
        years = self.__copy_X_test['Year'].tolist()
        countries = self.__copy_X_test['Country'].tolist()
        real_output = self.__copy_Y_test['Clasification'].tolist()
        self.__results = UtilsForMLcomponent.create_result(years, countries, self.__predictions, real_output)

        filename_results = 'results.pkl'
        pickle.dump(self.__rescaledX_test, open(filename_results, 'wb'))

    def __get_accuracy(self):
        return accuracy_score(self.__y_test, self.__predictions)

    # saves the dataset used for testing
    def __get_test_data(self):
        test_data_list = []
        years = self.__copy_X_test['Year'].tolist()
        countries = self.__copy_X_test['Country'].tolist()
        expected_classification = self.__copy_Y_test['Clasification'].tolist()

        for i in range(0, len(years)):
            test_data_list.append(Result(years[i], countries[i],[], expected_classification[i]))

        filename_test_data ="get_test_data.pkl"
        pickle.dump(test_data_list, open(filename_test_data, 'wb'))

    # saves the accuracies for 10 trainings
    def __find_stability_statistics(self):
        statistics = []

        for i in range(0, 10):
            self.__separate_data()
            self.__prepare_data()
            self.__ann()
            self.__test_ann()
            statistics.append(self.__get_accuracy())
        self.__statistics = statistics

        filename_stability_statistics ="stability_statistic.pkl"
        pickle.dump(self.__statistics, open(filename_stability_statistics, 'wb'))








