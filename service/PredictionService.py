from repository.PostDataRepository import PostDataRepository
from utils.UtilsForServices import UtilsForServices


class PredictionService:
    def __init__(self,ml_component,file_name,sheet_name):
        self.__ml_component = ml_component
        self.repository = PostDataRepository(file_name,sheet_name)

    def get_predictions(self):
        result = self.__ml_component.predict(self.repository.get_data())
        for r in result:
            print(r)
        return  UtilsForServices.get_results_with_country_name(result)




