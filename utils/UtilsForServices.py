import math

from domain.ClassificationNames import ClassificationNames
from domain.Result import Result


class UtilsForServices:

    @staticmethod
    def __get_number_of_predictions_of_same_type(type,input_list):
        count = 0
        for result in input_list:
            if result.get_prediction() == type:
                count = count + 1
        return count

    @staticmethod
    def get_list_of_numbers_of_predictions_of_same_type(type_list,input_list):
        rez = []
        for type in type_list:
            rez.append(UtilsForServices.__get_number_of_predictions_of_same_type(type,input_list))
        return rez

    @staticmethod
    def __get_number_of_real_output_of_same_type(type, input_list):
        count = 0
        for result in input_list:
            if result.get_real_output() == type:
                count = count + 1
        return count

    @staticmethod
    def get_list_of_numbers_of_real_output_of_same_type(type_list, input_list):
        rez = []
        for type in type_list:
            rez.append(UtilsForServices.__get_number_of_real_output_of_same_type(type, input_list))
        return rez

    @staticmethod
    def truncate(number):
        stepper = 10.0 ** 3
        return float(math.trunc(stepper * number) / stepper)

    @staticmethod
    def get_classification_name_for_real_output(result_real_output):
        if result_real_output == ClassificationNames.unsatisfactory.value:
            return ClassificationNames.unsatisfactory.name
        elif result_real_output == ClassificationNames.satisfactory.value:
            return ClassificationNames.satisfactory.name
        elif result_real_output == ClassificationNames.good.value:
            return ClassificationNames.good.name
        elif result_real_output == ClassificationNames.very_good.value:
            return ClassificationNames.very_good.name
        return ClassificationNames.excellent.name

    @staticmethod
    def get_results_with_country_name(classification_list):
        results_list = set()

        for result in classification_list:
            if result.get_prediction() == ClassificationNames.unsatisfactory.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.unsatisfactory.name,
                           UtilsForServices.get_classification_name_for_real_output(result.get_real_output())))
            elif result.get_prediction() == ClassificationNames.satisfactory.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.satisfactory.name,
                           UtilsForServices.get_classification_name_for_real_output(result.get_real_output())))
            elif result.get_prediction() == ClassificationNames.good.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.good.name,
                           UtilsForServices.get_classification_name_for_real_output(result.get_real_output())))
            elif result.get_prediction() == ClassificationNames.very_good.value:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.very_good.name,
                           UtilsForServices.get_classification_name_for_real_output(result.get_real_output())))
            else:
                results_list.add(
                    Result(result.get_year(), result.get_country(), ClassificationNames.excellent.name,
                           UtilsForServices.get_classification_name_for_real_output(result.get_real_output())))
        return results_list
