# -*- coding: utf-8 -*-
# Buri by Sinbing
import base64



def Il1():
    global _, __________
    _ = input('请输入食用进去的代码文件路径（相对路径/绝对路径都OK）')
    try:
        ___________ = _.split('\\')
        ____________ = ___________[-1]
        __________ = ____________[:____________.index('.py')]
        return _
    except:
        print('Bug Bug Bug Bug Bug Bug Bug Bug Bug Bug')


def l1I(__):
    global ____
    with open (__,'r', encoding = 'utf-8') as ___:
        ____ = str(___.read())
    ___.close()
    return ____


def i1l(_________, _____):
    ______ = base64.b64encode(str(_____).encode('utf-8'))
    ________ = ('import base64;exec(base64.b64decode({0}))'.format(______))
    with open('./shit_{0}.py'.format(__________), mode="w", encoding="utf-8") as _______:
        _______.write (________)
    _______.close()


if __name__ == '__main__':
    Il1()
    l1I(_)
    i1l(_, ____)
