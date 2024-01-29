k = int(input("Nhập số bạn mong muốn: "))
z = int(input("Nhập số lũy thừa mong muốn: "))
tong = 0
if z<=0 :
    print("Vui lòng nhập số lũy thừa là số khác 0")
else:
    for i in range(1,z+1):
        tong = tong + (k**i)
    print("Kết quả là: ", tong)

