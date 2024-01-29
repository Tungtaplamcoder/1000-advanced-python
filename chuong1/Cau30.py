k = int(input("Nhập số bạn mong muốn: "))
uoc = []
tong = 0
for i in range(1,k+1):
    if k%i==0 and i<k:
        uoc.append(i)
for i in uoc:
    tong += i
if tong == k:
    print(k,"là số hoàn thiện")
else:
    print(k,"không là số hoàn thiện")