w = 0.078367
b = 0.401752

def du_doan_gia(dien_tich):
    if dien_tich < 35.5 or dien_tich > 117.5:
        print(f"Canh bao: Dien tich {dien_tich} m2 nam ngoai vung du lieu (35.5 toi 117.5 m2)")
    return w * dien_tich + b

for dt in [60, 80, 200]:
    gia = du_doan_gia(dt)
    print(f"Can {dt} m2 duoc du doan: {gia:.3f} ty dong")