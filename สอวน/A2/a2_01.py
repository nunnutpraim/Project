def solve():
    n, m = map(int, input().split())
    red_input = list(map(int, input().split()))
    blue_input = list(map(int, input().split()))

    red_pos = [0] + red_input
    blue_pos = [0] + blue_input

    # สร้างจุดของเส้นแดง
    red_points = []
    y = 0
    for x in red_pos:
        red_points.append((x, y))
        y = 1 - y  # สลับขึ้นลง

    # สร้างจุดของเส้นน้ำเงิน
    blue_points = []
    y = 0
    for x in blue_pos:
        blue_points.append((x, y))
        y = 1 - y

    crossing_points = set()  # ใช้ set เพื่อป้องกันจุดซ้ำ

    # หาเส้นตัด
    for i in range(len(red_points) - 1):
        r_x1, r_y1 = red_points[i]
        r_x2, r_y2 = red_points[i+1]
        for j in range(len(blue_points) - 1):
            b_x1, b_y1 = blue_points[j]
            b_x2, b_y2 = blue_points[j+1]

            # เช็คว่าช่วง x ทับกัน
            if not (r_x2 < b_x1 or b_x2 < r_x1):
                dx_red = r_x2 - r_x1
                dy_red = r_y2 - r_y1
                dx_blue = b_x2 - b_x1
                dy_blue = b_y2 - b_y1

                if dx_red == 0 or dx_blue == 0:
                    continue

                slope_red = dy_red / dx_red
                slope_blue = dy_blue / dx_blue

                intercept_red = r_y1 - slope_red * r_x1
                intercept_blue = b_y1 - slope_blue * b_x1

                if slope_red == slope_blue:
                    continue  # เส้นขนาน

                x_cross = (intercept_blue - intercept_red) / (slope_red - slope_blue)
                y_cross = slope_red * x_cross + intercept_red

                if (min(r_x1, r_x2) <= x_cross <= max(r_x1, r_x2)) and (min(b_x1, b_x2) <= x_cross <= max(b_x1, b_x2)):
                    point = (round(x_cross, 8), round(y_cross, 8))
                    if point not in crossing_points:
                        crossing_points.add(point)
                        #print(f"Red: [{r_x1}, {r_x2}] ตัดกับ Blue: [{b_x1}, {b_x2}]")

    #print(f"จำนวนจุดตัดทั้งหมด: {len(crossing_points)}")
    print(len(crossing_points))
if __name__ == "__main__":
    solve()