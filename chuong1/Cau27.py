k = int(input("Nhập số bạn mong muốn: "))
uoc = []
for i in range(1,k+1):
    if k%i==0 and i%2==0:
        uoc.append(i)
print("Số ước của số", k,"là:",len(uoc))