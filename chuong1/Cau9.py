k = int(input("Nhập số bạn mong muốn: "))
tong = 1

if k==0:
    print("Vui lòng nhập số khác 0")
else:
    for i in range(1,k+1):
        tong = tong*i
    print("Kết quả là: ", tong)