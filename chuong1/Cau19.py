# x là z, n là k
k = int(input("Nhập số bạn và lũy thừa mong muốn(Yêu cầu số chẵn): "))
z = int(input("Nhập số mong muốn: "))
tong = 1
giaithua = 1
if k%2==0:
    print("Vui lòng chọn số lẻ")
else:
    hsk = int((k-1)/2)
    for i in range(hsk+1):
        for m in range(1,2*i+2):
            giaithua = giaithua*m
        giaithua = int(giaithua)
        tong += ((z**(2*i))/giaithua)
    print("Kết quả là: ", tong)
