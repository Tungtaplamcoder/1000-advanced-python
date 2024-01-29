k = int(input("Nhập số bạn mong muốn: "))
tong = 0
for i in range(k):
    tong = tong + (1/(2*i+1))
print("Kết quả là: ", tong)