k = int(input("Nhập số bạn mong muốn: "))
uoc = []
tich = 1
for i in range(1,k+1):
    if k%i==0:
        uoc.append(i)
for i in uoc:
    tich *= i
print("Tích của tất cả các ước của số", k,"là:",tich)