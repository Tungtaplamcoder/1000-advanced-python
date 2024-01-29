k = int(input("Nhập số bạn mong muốn: "))
z = int(input("Nhập số lũy thừa mong muốn(Yêu cầu số chẵn): "))
tong = 0
if z<=0 or z%2!=0:
    print("Vui lòng nhập số lỹ thừa chẵn")
else:
    for i in range(1,int((z/2)+1)):
        tong = tong + (k**(2*i))
    print("Kết quả là: ", tong)