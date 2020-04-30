from .programs import Decode as d,Encrypt as e
from os import system as osys
from platform import system as psys
def func():
    print('''请选择：
0->“加密”
其他->“解密”''')
    choice=input()
    if psys()=="Windows":
        osys("cls")
    else:
        osys("clear")
    if choice=='0':
        e.func()
    else:
        d.func()

if __name__ == "__main__":
    print('''"解密"程序版本信息：
%s
"加密"程序版本信息：
%s'''%(d.intro,e.intro))
    try:
        func()
    except KeyboardInterrupt:
        print('')
    except Exception:
        print("程序出错！错误信息：",str(Exception))