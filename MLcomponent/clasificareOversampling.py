import numpy
import sklearn

from pandas import read_excel
# find your sheet name at the bottom left of your excel file and assign
# it to my_sheet
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import resample
import pandas as pd

from domain.Result import Result

my_sheet = 'Tari' # change it to your sheet name
#file_name = 'tariClasificate.xlsx' # change it to the name of your excel file
file_name = '../resources/tariClasificateAvgDateAntrenament.xlsx'  # change it to the name of your excel file
data = read_excel(file_name, sheet_name = my_sheet)

results = []

print("Count values: ")
print(data.Clasification.value_counts())

data_0 =  data[data.Clasification == 0]
data_1 =  data[data.Clasification == 1]
data_2 =  data[data.Clasification == 2]
data_3 =  data[data.Clasification == 3]
data_4 =  data[data.Clasification == 4]

print("________")
data_1_resampling = resample(data_1,replace=True, n_samples=93, random_state=45)
data_2_resampling = resample(data_2,replace=True, n_samples=93, random_state=45)
data_3_resampling = resample(data_3,replace=True, n_samples=93, random_state=45)
data_4_resampling = resample(data_4,replace=True, n_samples=93, random_state=45)

data = pd.concat([data_0, data_1_resampling,data_2_resampling,data_3_resampling,data_4_resampling])

print("Count values: ")
print(data.Clasification.value_counts())

X = data.iloc[:, 0:41]
y = data.iloc[:, 42:43]
print(X)


from sklearn.model_selection import train_test_split
for i in range (0,1):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)
        copy_X_test = X_test.copy();
        print("_________copy")
        print(copy_X_test)
        print(type(X_test))
        del X_test['Year']
        del X_train['Year']
        del X_train['Country']
        del X_test['Country']
        print(X_test)
        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaledX_train = scaler.fit_transform(X_train)
        rescaledY_train = scaler.fit_transform(y_train)
        rescaledX_test = scaler.fit_transform(X_test)
        rescaledY_test = scaler.fit_transform(y_test)
        # summarize transformed data
        numpy.set_printoptions(precision=3)
        print(rescaledX_test)

        from sklearn.neural_network import MLPClassifier
        mlp = MLPClassifier(hidden_layer_sizes=(20, 20, 20), max_iter=3000)
        mlp.fit(rescaledX_train, y_train.values.ravel())

        predictions = mlp.predict(rescaledX_test)
        print("rezultat_______________________")
        print(type(predictions))
        print(predictions)

        from sklearn.metrics import classification_report, confusion_matrix
        print("--------")
        print(type(confusion_matrix(y_test,predictions)))
        print(confusion_matrix(y_test,predictions))
        print("--------")
        print(type(classification_report(y_test,predictions, zero_division=1)))
        print(classification_report(y_test,predictions, zero_division=1))
        scr = mlp.score(X_test, y_test)
        print(scr)
        print(copy_X_test)
        years = copy_X_test['Year'].tolist()
        countries = copy_X_test['Country'].tolist()
        for i in range(0,len(years)):
                   results.append(Result(years[i], countries[i], predictions[i]))





