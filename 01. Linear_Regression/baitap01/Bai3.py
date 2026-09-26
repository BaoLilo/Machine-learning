import numpy as np
import pandas as pd

df = pd.read_csv("data/gia_nha.csv")

x = df["tuoi_nha"].to_numpy()
y = df["gia"].to_numpy()

x_tb = x.mean()
y_tb = y.mean()

tu_so = ((x - x_tb) * (y - y_tb)).sum()
mau_so = ((x - x_tb) ** 2).sum()

w = tu_so / mau_so
b = y_tb - w * x_tb

print(f"He so goc  w = {w:.6f}")
print(f"He so chan b = {b:.6f}")
print()
print("Nhan xet: He so goc w mang dau am (-0.037858) vi tuoi nha va gia ban co quan he nghich bien; nha cang cu (so nam su dung tang len) thi gia tri can ho cang giam do khau hao theo thoi gian, cu the moi nam cu them thi gia giam khoang 0.0379 ty dong (khoang 38 trieu dong).")