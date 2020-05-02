from platform import system as psys
from os import system as osys

def getChoice(hint):
    while True:
        choice=input(hint+'(T或F，不填默认为F，不区分大小写)')
        if choice=='':
            choice='F'
        choice=choice.upper()
        if choice in ['T','F']:
            break
    return True if choice=='T' else False

def getTable(base):
    table=list()
    cur=base
    times=1
    while cur<64:
        table+=list(range(cur,cur+base))
        times+=2
        cur=base*times
    return table

def getError(rn,num):
    diff=rn^num
    brn,num,diff=str(bin(rn))[2:][::-1],str(bin(num))[2:][::-1],str(bin(diff))[2:][::-1]
    for i in range(len(diff)):
        ch=diff[i]
        if ch=='1':
            if brn[i]=='1':
                print(str(getTable(2**i))+'中有个%d呢。'%rn)
            else:
                print(str(getTable(2**i))+'中没有%d呢。'%rn)

num=0
i=0
print('随便想一个数字(0-63)...')
if psys()=='Windows':
    osys('pause')
else:
    input('按下Enter以继续...')
for i in range(6):
    osys('cls' if psys()=='Windows' else 'clear')
    print(getTable(2**i))
    if getChoice('这里面有你想的数字吗？'):
        num+=2**i
osys('cls' if psys()=='Windows' else 'clear')
print('你想的数字是：%d'%num) 
if not getChoice('是否准确？'):
    rn=int(input('你想的数字是？'))
    getError(rn,num)
if psys()=='Windows':
    osys('pause')