# -*- coding: utf-8 -*-
"""Bài tập 1: Lọc ra nhóm căn hộ lớn có diện tích > 100 m2."""

import pandas as pd

df = pd.read_csv("data/gia_nha.csv")

nhom_lon = df[df["dien_tich"] > 100]

so_can = len(nhom_lon)
gia_tb = nhom_lon["gia"].mean()

print("So can co dien tich lon hon 100 m2:", so_can)
print(f"Gia trung binh cua nhom can lon: {gia_tb:.3f} ty dong")
# Nhận xét: Nhóm căn hộ lớn hơn 100 m² chiếm 10 trên 60 căn,
# có giá trung bình đạt 8.962 tỷ đồng, cao hơn đáng kể so với
# mức giá trung bình 6.493 tỷ đồng của toàn bộ dữ liệu, phù hợp
# với xu hướng diện tích càng lớn thì giá bán càng cao