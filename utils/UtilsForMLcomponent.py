import pickle

from domain.Result import Result


class UtilsForMLcomponent:

    @staticmethod
    def create_result(years, countries, predictions, real_ouputs):
        rez = []
        for i in range(0, len(years)):
            rez.append(Result(years[i], countries[i], predictions[i], real_ouputs[i]))
        pickle.dump(rez, open("create_result.pkl", 'wb'))
        return rez
