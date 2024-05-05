
import pandas as pd
import numpy as np
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE  # Örnekleme için SMOTE

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

# Hedef ve özellikler
target = 'PERSONALLOAN'
features = data.columns.drop(target)

# Veri setini eğitim ve test setleri olarak ayırma
X_train, X_test, y_train, y_test = train_test_split(
    data[features], data[target], test_size=0.2, random_state=42, stratify=data[target]
)

# SMOTE ile örnekleme yapma
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

# TPOTClassifier ayarları
tpot = TPOTClassifier(
    generations=5,
    population_size=50,
    verbosity=2,
    random_state=42,
    scoring='balanced_accuracy',
    config_dict='TPOT light'
)

# Modelin eğitilmesi
tpot.fit(X_train_res, y_train_res)

# Test seti üzerinde modelin değerlendirilmesi
print("En iyi pipeline'ın test skoru: ", tpot.score(X_test, y_test))

# En iyi pipeline'ın kaydedilmesi
tpot.export('best_pipeline.py')



