# x là z, n là k
k = int(input("Nhập số bạn và lũy thừa mong muốn: "))
z = int(input("Nhập số mong muốn: "))
tong = 0
giaithua = 1
for i in range(1,k+1):
    for m in range(1,i+1):
        giaithua = giaithua*m
    giaithua = int(giaithua)
    tong = tong + ((z**(i))/giaithua)
print("Kết quả là: ", tong)