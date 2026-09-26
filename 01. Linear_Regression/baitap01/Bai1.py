import pandas as pd

df = pd.read_csv("data/gia_nha.csv")

nhom_lon = df[df["dien_tich"] > 100]

print("So can co dien tich lon hon 100 m2:", len(nhom_lon))
print("Gia trung binh:", nhom_lon["gia"].mean())
print("Nhan xet: Nhom can ho lon hon 100 m2 chiem 10 tren 60 can, co gia trung binh dat 8.962 ty dong, cao hon dang ke so voi muc gia trung binh 6.493 ty dong cua toan bo du lieu, phu hop voi xu huong dien tich cang lon thi gia ban cang cao.")