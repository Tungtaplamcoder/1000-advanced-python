k = int(input("Nhập số bạn mong muốn: "))
tong = 0
tich = 1
if k==0:
    print("Vui lòng nhập số khác 0")
else:
    for i in range(1,k+1):
        tich = tich*i
        tong = tong + tich
    print("Kết quả là: ", tong)