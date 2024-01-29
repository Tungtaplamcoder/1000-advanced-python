k = int(input("Nhập số bạn mong muốn: "))
uoc = []
for i in range(1,k+1):
    if k%i==0 and i%2!=0:
        uoc.append(i)
print("Các ước của số lẻ", k,"là: " )
for i in uoc:
    print(i, end=' ')