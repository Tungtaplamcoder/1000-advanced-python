k = int(input("Nhập số bạn mong muốn: "))
uoc = []
tong = 0
for i in range(1,k+1):
    if k%i==0 and i%2==0:
        uoc.append(i)
for i in uoc:
    tong += i
print("Tổng của tất cả các ước chẵn của số", k,"là:",tong)