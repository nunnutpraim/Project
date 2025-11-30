W, H, M, N = map(int, input().split())

# รับตำแหน่งมีดแนวตั้ง
X = list(map(int, input().split()))

# รับตำแหน่งมีดแนวนอน
Y = list(map(int, input().split()))

# เพิ่มขอบของขนมปังเข้าไป (ซ้าย = 0, ขวา = W)
X.insert(0, 0)
X.append(W)

# เพิ่มขอบของขนมปังเข้าไป (ล่าง = 0, บน = H)
Y.insert(0, 0)
Y.append(H)

# คำนวณความกว้างของแต่ละชิ้น
widths = []
for i in range(len(X) - 1):
    width = X[i+1] - X[i]
    widths.append(width)

# คำนวณความสูงของแต่ละชิ้น
heights = []
for i in range(len(Y) - 1):
    height = Y[i+1] - Y[i]
    heights.append(height)

# คำนวณพื้นที่ของทุกชิ้น
areas = []
for w in widths:
    for h in heights:
        area = w * h
        areas.append(area)

# เรียงพื้นที่จากมากไปน้อย
areas.sort(reverse=True)

# แสดงพื้นที่มากที่สุด 2 ชิ้น
print(areas[0], areas[1])