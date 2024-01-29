k = int(input("Nhập số bạn và lũy thừa mong muốn: "))
z = int(input("Nhập số mong muốn: "))
tong = 0
for i in range(k):
    tong = tong + ((z**(i+1))/(2*i+1))
print("Kết quả là: ", tong)