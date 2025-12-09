print("---BỘ CHUYỂN ĐỔI ĐƠN VỊ MỸ---")
print("\nCHỌN CHỨC NĂNG:")
print("1. Đổi Cân nặng (Lbs <-> Kg)")
print("2. Đổi Độ dài (Hệ Inch/Ft <-> Hệ Mét)")
chon_menu = input("Nhập số (1 hoặc 2): ")
if chon_menu == "1":
    print("\n---ỔI CÂN NẶNG---")
    print("a. Pounds (lbs) -> Kilogram (kg)")
    print("b. Kilogram (kg) -> Pounds (lbs)")
    chon = input("Bạn chọn (a/b): ")
    if chon == 'a':
        so_lbs = float(input("Nhập số Pounds (lbs): "))
        ket_qua = so_lbs * 0.453592
        print(f"{so_lbs} lbs = {ket_qua:.2f} kg")
    elif chon == 'b':
        so_kg = float(input("Nhập số Kg: "))
        ket_qua = so_kg * 2.20462
        print(f"{so_kg} kg = {ket_qua:.2f} lbs")
    else:
        print(" Chọn sai rồi!")
elif chon_menu == "2":
    print("\n---ĐỔI ĐỘ DÀI---")
    print("a. Inch -> Cm và Mét")
    print("b. Feet (ft) -> Cm và Mét")
    print("c. Cm -> Inch và Feet")
    print("d. Mét (m) -> Inch và Feet")
    chon = input("Bạn chọn hướng nào (a/b/c/d): ")
    if chon == 'a':
        val = float(input("Nhập số Inch: "))
        print(f"{val} inch = {val * 2.54:.2f} cm")
        print(f"{val} inch = {(val * 2.54) / 100:.4f} m")
    elif chon == 'b':
        val = float(input("Nhập số Feet (ft): "))
        print(f"{val} ft = {val * 30.48:.2f} cm")
        print(f"{val} ft = {(val * 30.48) / 100:.4f} m")
    elif chon == 'c':
        val = float(input("Nhập số Cm: "))
        print(f"{val} cm = {val / 2.54:.2f} inch")
        print(f"{val} cm = {val / 30.48:.2f} ft")
    elif chon == 'd':
        val = float(input("Nhập số Mét (m): "))
        cm = val * 100
        print(f"{val} m = {cm / 2.54:.2f} inch")
        print(f"{val} m = {cm / 30.48:.2f} ft")
    else:
        print("Chọn sai rồi!")

else:
    print("Vui lòng chỉ nhập số 1 hoặc 2.")
input("\nBấm Enter để thoát chương trình...")