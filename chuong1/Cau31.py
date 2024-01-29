k = int(input("Nhập số bạn mong muốn: "))
uoc = []
for i in range(1,k+1):
    if k%i==0:
        uoc.append(i)
if len(uoc)== 2:
    print(k,"là số nguyên tố")
else:
    print(k,"không là số nguyên tố")