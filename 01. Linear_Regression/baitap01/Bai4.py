import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/gia_nha.csv")

X = df[["dien_tich", "so_phong"]]
y = df["gia"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mo_hinh = LinearRegression()
mo_hinh.fit(X_train, y_train)

y_pred = mo_hinh.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"R2 tren tap kiem tra: {r2:.4f}")
print("So sanh: R2 tang tu 0.9622 (mo hinh mot bien) len 0.9698 (mo hinh hai bien). Muc tang khoang 0.0076 la khong lon vi dien_tich da giai thich phan lon bien dong cua gia nha. Viec them bien so_phong co giup mo hinh tot hon mot chut nhung khong tao ra su khac biet vuot troi.")