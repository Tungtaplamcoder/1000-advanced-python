k = int(input("Nhập số bạn mong muốn: "))
tong = 0

if k==0:
    print("Vui lòng nhập số khác 0")
else:
    for i in range(1,k+1):
        tong = tong + (1/(i*(i+1)))
    print("Kết quả là: ", tong)