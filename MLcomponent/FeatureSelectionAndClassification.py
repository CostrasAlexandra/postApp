from pandas import read_excel
from sklearn.feature_selection import RFE
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
import pandas as pd
import numpy as np

class FeatureSelectionAndClassification:
    def __init__(self):
        self.__my_sheet = 'Tari'  # change it to your sheet name
        self.__file_name = '../resources/resources/set1.xlsx'  # change it to the name of your excel file
        self.__X = any
        self__y = any
        self.__X_train= any
        self.__X_test = any

    def __read_data(self):
        self.__data = read_excel(self.__file_name, sheet_name=self.__my_sheet)
        print(self.__data.head())  # shows headers with top 5 rows
        self.__X = self.__data.iloc[:, 2:41]
        self.__y = self.__data.iloc[:, 42:43]

    def __feature_selection(self):

        m = XGBClassifier(
            max_depth=2,
            gamma=2,
            eta=0.8,
            reg_alpha=0.5,
            reg_lambda=0.5
        )
        rfe = RFE(XGBClassifier(n_jobs=-1, random_state=1))

        rfe.fit(self.__X, self.__y.values.ravel())
        columns = list(self.__X)

        count = 0

        newX = []
        for r in rfe.support_:
            if (r == True):
                newX.append(columns[count])
            count = count + 1

        from imblearn.over_sampling import SMOTE

        smote = SMOTE(sampling_strategy='all', n_jobs=-1)
        X_sm, y_sm = smote.fit_resample(self.__X, self.__y)
        X_sm = X_sm[newX]

        df = pd.DataFrame(X_sm, columns=newX)
        df['Clasification'] = y_sm

        self.__X = df.iloc[:, 0:19]
        self.__y = df.iloc[:, 19:20]

    def separate_and_normalize_data(self):
        self.__X_train, self.__X_test, self.__y_train, self.__y_test = train_test_split(self.__X, self.__y, test_size=0.20, random_state=90)
        scaler = MinMaxScaler(feature_range=(0, 1))
        self.__rescaledX_train = scaler.fit_transform(self.__X_train)
        self.__rescaledX_test = scaler.fit_transform(self.__X_test)

    def train_and_test(self):
        np.set_printoptions(precision=3)
        mlp = MLPClassifier(hidden_layer_sizes=(128, 512, 32), max_iter=2000)
        mlp.fit(self.__rescaledX_train, self.__y_train.values.ravel())

        predictions = mlp.predict(self.__rescaledX_test)

        print(classification_report(self.__y_test, predictions, zero_division=1))
        scr = mlp.score(self.__X_test, self.__y_test)
        print(scr)

    def ann(self):
        self.__read_data()
        self.__feature_selection()

f = FeatureSelectionAndClassification()
f.ann()
for i in range (0,5):
    f.separate_and_normalize_data()
    f.train_and_test()