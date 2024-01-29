k = int(input("Nhập số bạn mong muốn: "))
uoc = []
for i in range(1,k+1):
    if i**2==k:
        uoc.append(i)
if len(uoc)== 1:
    print(k,"là số chính phương")
else:
    print(k,"không là số chính phương")