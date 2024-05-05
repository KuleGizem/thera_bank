import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import MaxAbsScaler
from sklearn.tree import DecisionTreeClassifier
from tpot.builtins import StackingEstimator
from tpot.export_utils import set_param_recursive
import joblib
# NOTE: Make sure that the outcome column is labeled 'target' in the data file
# Veri setini yükleme
data_path = 'credit/bank_loan.csv'
data = pd.read_csv(data_path)

# Sütun isimlerini düzenleme ve veri temizleme
data.columns = data.columns.str.replace(' ', '').str.upper()

# 'CCAvg' sütununu işleme
def convert_fraction_to_float(fraction_str):
    if fraction_str.endswith("/00"):
        return float(fraction_str.replace("/00", ""))
    else:
        numerator, denominator = fraction_str.split('/')
        return float(numerator) / float(denominator)

data['CCAVG'] = data['CCAVG'].apply(convert_fraction_to_float)
data['CCAVG'] = data['CCAVG'] * 1000 * 12
data['INCOME'] = data['INCOME'] * 1000
data['MORTGAGE'] = data['MORTGAGE'] * 1000
data['EXPERIENCE'] = data['EXPERIENCE'].apply(lambda x: max(x, 0))
data = data.drop(['ID', 'ZIPCODE'], axis=1)

tpot_data = data

features = tpot_data.drop('PERSONALLOAN', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['PERSONALLOAN'], random_state=42)

# Average CV score on the training set was: 0.9492551370517258
exported_pipeline = make_pipeline(
    MaxAbsScaler(),
    StackingEstimator(estimator=DecisionTreeClassifier(criterion="entropy", max_depth=10, min_samples_leaf=7, min_samples_split=19)),
    DecisionTreeClassifier(criterion="gini", max_depth=1, min_samples_leaf=14, min_samples_split=5)
)
# Fix random state for all the steps in exported pipeline
set_param_recursive(exported_pipeline.steps, 'random_state', 42)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

joblib.dump(exported_pipeline, 'finalized_model.joblib')

##