import pickle

from MLcomponent.Classification import Classification
from repository.PostDataRepository import PostDataRepository


def retrain_model():
    file_name = '../resources/resources/set1.xlsx'
    sheet_name = 'Tari'
    r = PostDataRepository(file_name, sheet_name)
    cl = Classification(r.get_data())
    cl.save_model()
    m = pickle.load((open('finalized_model.sav', 'rb')))
    x = pickle.load((open('x_test_data.pkl', 'rb')))
    y = pickle.load((open('y_test_data.pkl', 'rb')))

retrain_model()