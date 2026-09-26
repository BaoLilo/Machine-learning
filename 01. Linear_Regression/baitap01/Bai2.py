import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/gia_nha.csv")

plt.scatter(df["so_phong"], df["gia"])
plt.xlabel("So phong")
plt.ylabel("Gia (ty dong)")
plt.title("Gia nha theo so phong")

plt.savefig("bai2.png", dpi=150)
plt.show()

print("Nhan xet: So phong va gia nha co quan he dong bien, so phong cang nhieu thi mat bang gia ban can ho cang cao.")