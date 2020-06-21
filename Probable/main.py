from random import choice
import math

_l=eval("[%s]"%input('数据(list) >>> ').strip())
_var=input('变量 >>> ').split(',')
for _name in _var:
    exec("%s=0"%_name)
_exp=input('条件 >>> ')
_c=eval(input('次数(int) >>> '))
_a=eval(input('重复(bool) >>> '))
_count=0
for _i in range(_c):
    _tl=_l[:]
    for _name in _var:
        exec("{}={}".format(_name,choice(_tl)))
        if not _a:
            _tl.remove(eval(_name))
    if eval(_exp):
        _count+=1
print('%d/%d=%f'%(_count,_c,_count/_c))