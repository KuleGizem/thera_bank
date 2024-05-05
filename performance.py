import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Veri setini yükle
data = pd.read_csv('credit/bank_loan.csv')

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


# Bağımsız değişkenler ve hedef değişken
X = data.drop('PERSONALLOAN', axis=1)
y = data['PERSONALLOAN']

# Veri setini eğitim ve test seti olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli yükle
model = joblib.load('credit/finalized_model.joblib')

# Eğitim setinde tahminler
train_preds = model.predict(X_train)
# Test setinde tahminler
test_preds = model.predict(X_test)

# Performans metriklerini hesapla ve yazdır
print("Eğitim Seti Performansı:")
print(classification_report(y_train, train_preds))

print("Test Seti Performansı:")
print(classification_report(y_test, test_preds))

# Opsiyonel olarak doğruluk skorları
print("Eğitim seti doğruluk:", accuracy_score(y_train, train_preds))
print("Test seti doğruluk:", accuracy_score(y_test, test_preds))
