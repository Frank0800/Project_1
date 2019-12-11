w = int(input())  # 活動總票數
v = int(input())  # 會員等級分界
m = int(input())  # 登記人數
b = []
ID = []
IDblist = []  # 包含登記人數＆票數（取票數與最大可取票數的最小值）
I = []

#預設一個累積票數的變數
EstOrder = 0
#預設一個票數差
minus = 0

# b輸入各等級取票張數上限
blist = input().split(',')
for h in blist:
    b.append(int(h))

# "m > 0" 成立才有第五第六行
if m > 0:
    # ID輸入ID列表
    IDlist = input().split(',')
    for i in IDlist:
        ID.append(int(i))
    # 各ID希望取票數量
    ilist = input().split(',')
    for j in ilist:
        I.append(int(j))

    for k in ID:
        if 0 < k < v:
            IDblist.append(k)
            Loc = ID.index(k)
            IDblist.append(min(b[0], I[Loc]))
    for k in ID:
        if k >= v:
            IDblist.append(k)
            Loc = ID.index(k)
            IDblist.append(min(b[1], I[Loc]))
    for k in ID:
        if k < 0:
            IDblist.append(k)
            Loc = ID.index(k)
            IDblist.append(min(b[2], I[Loc]))
else:
    print(w)
for r in range(m):
    EstOrder += IDblist[2 * r + 1]
    if EstOrder < w:
        minus = w - EstOrder
    elif EstOrder >= w:
        minus = EstOrder - w
    if EstOrder > w:
        count = r
        break

if EstOrder < w:
    print(minus)
    for i in range(m):
        print(str(IDblist[2 * i]) + ':' + str(IDblist[2 * i + 1]))
elif EstOrder == 0:
    print(0)
    for i in range(r):
        print(str(IDblist[2 * (i - 1)]) + ':' + str(IDblist[2 * (i - 1) + 1]))
    if IDblist[2 * i + 1] != 0:
        print(str(IDblist[2 * i]) + ':' + str(IDblist[2 * i + 1]))
else:
        print(0)
        for i in range(r):
            print(str(IDblist[2 * i]) + ':' + str(IDblist[2 * i + 1]))
        if w - (EstOrder - IDblist[2 * r + 1]) != 0:
            print(str(IDblist[2 * count]) + ':' + str(w - (EstOrder - IDblist[2 * r + 1])))