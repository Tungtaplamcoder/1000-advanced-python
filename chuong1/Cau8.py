k = int(input("Nhập số bạn mong muốn: "))
tong = 0

for i in range(1,k+1):
    tong = tong + ((2*i+1)/(2*i+2))
print("Kết quả là: ", tong)