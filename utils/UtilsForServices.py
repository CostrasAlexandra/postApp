from domain.ClassificationNames import ClassificationNames
from domain.Result import Result


class UtilsForServices:

    @staticmethod
    def get_results_with_country_name(classification_list):
        results_list = set()

        for result in classification_list:
            if result.get_prediction() == ClassificationNames.unsatisfactory.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.unsatisfactory.name))
            elif result.get_prediction() == ClassificationNames.satisfactory.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.satisfactory.name))
            elif result.get_prediction() == ClassificationNames.good.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.good.name))
            elif result.get_prediction() == ClassificationNames.very_good.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.very_good.name))
            else:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.excellent.name))
        return results_list
