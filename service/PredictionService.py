from sklearn.preprocessing import MinMaxScaler

from domain.Result import Result
from repository.PostDataRepository import PostDataRepository
from utils.UtilsForServices import UtilsForServices


class PredictionService:

    def __init__(self,ml_component,file_name,sheet_name):
        self.__ml_component = ml_component
        self.repository = PostDataRepository(file_name,sheet_name)

    #applies the model on a dataset
    def get_predictions(self):

        data = self.repository.get_data()
        years = data['Year'].tolist()
        countries = data['Country'].tolist()
        real_output = data['Clasification'].tolist()
        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaled_data = scaler.fit_transform(data.iloc[:, 2:41])

        prediction = self.__ml_component.predict(rescaled_data)

        results = []
        for i in range(0,len(prediction)):
            results.append(Result(years[i],countries[i],prediction[i],real_output[i]))
        return UtilsForServices.get_results_with_country_name(results)

