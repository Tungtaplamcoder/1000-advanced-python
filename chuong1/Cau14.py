k = int(input("Nhập số bạn mong muốn: "))
z = int(input("Nhập số lũy thừa mong muốn(Yêu cầu số lẻ): "))
tong = 0
if z<=0 or z%2==0:
    print("Vui lòng nhập số lũy thừa là số lẻ")
else:
    n = (z-1)/2
    n = int(n)
    for i in range(n+1):
        tong = tong + (k**(2*n+1))
    print("Kết quả là: ", tong)

