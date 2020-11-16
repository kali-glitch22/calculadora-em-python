import math
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from os import system
from platform import system as ss
def stri(self):
    h = str(self)
    l = h.replace('[', '')
    b = l.replace(']', '')
    k = b.replace(',', '')
    global j
    j = k.replace("'", '')
cac = 1
if cac == 1:
    class calc:
        try:
            print("\033[0:31m", """ 
                            ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ 
                            ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
                            ██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║
                            ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
                            ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
                             ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝""", "\033[0m")
            sleep(0.8)
            print("""
        [ 0 ] ADIÇÃO 
        [ 1 ] SUBTRAÇÃO 
        [ 2 ] MUTIPLICAÇÃO
        [ 3 ] DIVISÃO 
        [ 4 ] EXPONCIACÃO 
        [ 5 ] RAIZ
        [ 6 ] SENO
        [ 7 ] COSSENO 
        [ 8 ] TANGENTE
        [ 9 ] ARCO SENO 
        [ 10 ] ARCO COSSENO 
        [ 11 ] ARCO TANGENTE
        [ 12 ] FATORIAL
        [ 13 ] PRIMOS
        [ 14 ] LIMPAR
        [ 15 ] LOGARITIMO
        [ 16 ] SAIR
        aperte uma letre e enter para sair do loop no meio da operação""")


            def soma():
                global c
                cs = 0
                o = 1

                a = list()
                while True:
                    try:
                        n = float(input(f'digite seu {o} numero: '.capitalize()))
                        if o == 1:
                            a.insert(1, '+')
                    except:
                        if a.pop() == '+' and o > 1:
                            a.remove('+')
                        a.append('=')
                        break

                    o += 1
                    cs += n
                    a.append(n)
                    c = len(a)
                    if a[:c:2]:
                        a.append('+')

                stri(a)

                return print(f'\n{j}'.center(12), (str(cs).rjust(1)))

            def menos():
                cs = 0
                o = 1
                global c
                global n
                global n1
                global a
                a = list()
                while True:
                    if o == 1:
                        try:
                            global n1
                            n1 = float(input(f'digite seu 1 numero: '.capitalize()))
                            a.append(n1)
                            a.insert(1, '-')
                        except:

                            a.append('=')
                            break
                    elif o != 1:
                        try:
                            n = float(input(f'digite seu {o} numero: '.capitalize()))
                            a.append(n)
                        except:
                            if a.pop() == '-' and o > 1:
                                a.remove('-')
                            a.append('=')
                            break

                    c = len(a)
                    if a[:c:2]:
                        a.append('-')
                    k = n1
                    if o == 2:
                        cs = k - n
                    if o >= 3:
                        cs -= n
                    o += 1

                stri(a)

                return print(f'\n{j}'.center(12), (str(cs).rjust(1)))

            def mutiplica():
                global c
                cs = 0
                a = list()
                cx = 1
                o = 1
                while True:
                    global c
                    cs = 1
                    o = 1

                    a = list()
                    while True:
                        try:
                            n = float(input(f'digite seu {o} numero: '.capitalize()))
                            if o == 1:
                                a.insert(1, 'x')
                        except:
                            if a.pop() == 'x' and o > 1:
                                a.remove('x')
                            a.append('=')
                            break

                        o += 1
                        cs *= n
                        a.append(n)
                        c = len(a)
                        if a[:c:2]:
                            a.append('x')

                    stri(a)

                    return print(f'\n{j}'.center(12), (str(cs).rjust(1)))

            def fracao():
                cs = 1
                o = 1
                global c
                global n
                global n1
                global a
                a = list()
                while True:
                    if o == 1:
                        try:
                            global n1
                            n1 = float(input(f'digite seu 1 numero: '.capitalize()))
                            a.append(n1)
                            a.insert(1, '÷')
                        except:

                            a.append('=')
                            break
                    elif o != 1:
                        try:
                            n = float(input(f'digite seu {o} numero: '.capitalize()))
                            a.append(n)
                        except:
                            if a.pop() == '÷' and o > 1:
                                a.remove('÷')
                            a.append('=')
                            break

                    c = len(a)
                    if a[:c:2]:
                        a.append('÷')
                    k = n1
                    if o == 2:
                        cs = k / n
                    if o >= 3:
                        cs /= n
                    o += 1

                stri(a)

                return print(f'\n{j}'.center(12), (str(cs).rjust(1)))

            def expo():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                    v = int(input('digite seu exponencial: '.capitalize()))
                except:
                    print('*-*')
                cx = o ** v
                return print('\n', f'{o} ^ {v} ='.center(12), str(cx).rjust(1))

            def raiz():
                global o, v
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                    v = float((input('digite sua raiz: '.capitalize())))
                except:
                    print('*-*')
                cx = o ** (1 / v)
                return print('\n', f'√{o} ='.center(12), str(cx).rjust(1))


            def sen():
                global o
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.sin(o)
                return print('\n', f'sen({o}) ='.center(12), str(cx).rjust(1))

            def cos():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.cos(o)
                return print('\n', f'cos({o}) ='.center(12), str(cx).rjust(1))

            def tan():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.tan(o)
                return print('\n', f'tan({o}) ='.center(12), str(cx).rjust(1))

            def arccos():

                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.cos(o) ** -1
                return print('\n', f'arcsen({o}) ='.center(12), str(cx).rjust(1))

            def arcsen():

                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.sin(o) ** -1
                return print('\n', f'arccos({o}) ='.center(12), str(cx).rjust(1))

            def arctan():

                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.tan(o) ** -1
                return print('\n', f'arctan({o}) ='.center(12), str(cx).rjust(1))

            def fact():
                n = int(input('digite um numero: '.capitalize()))
                cx = math.factorial(n)
                print(f'{n}! = ', end='')
                for l in range(1, n + 1, 1):
                    if l == n:
                        print(f'{l}', f'= {cx}'.rjust(1))
                        break
                    print(f'{l}', 'x ', end='')
                return
            def primos():
                n = int(input('digite um numero inicial: '.capitalize()))
                n1 = int(input('digite um numero final: '.capitalize()))
                for c in range(n, n1 + 1):
                        if c != 1:
                            if c % 2 != 0 and c % 3 != 0 and c % 4 != 0 and c % 5 != 0 and c % 6 != 0 and c % 7 != 0 and c % 8 != 0 and c % 9 != 0 or c == 2 or c == 3 or c == 5 or c == 7:
                                print(c)
                return
            def limpar():
                if ss() == 'Windows':
                    system("cls")
                if ss() == 'Linux':
                    system("clear")
                return print("""    [ 0 ] ADIÇÃO
    [ 1 ] SUBTRAÇÃO 
    [ 2 ] MUTIPLICAÇÃO
    [ 3 ] DIVISÃO 
    [ 4 ] EXPONCIACÃO 
    [ 5 ] RAIZ
    [ 6 ] SENO
    [ 7 ] COSSENO 
    [ 8 ] TANGENTE
    [ 9 ] ARCO SENO 
    [ 10 ] ARCO COSSENO 
    [ 11 ] ARCO TANGENTE
    [ 12 ] FATORIAL
    [ 13 ] PRIMOS
    [ 14 ] LIMPAR
    [ 15 ] LOGARITIMO
    [ 16 ] SAIR
    aperte uma letre e enter para sair do loop no meio da operação""")
            def log():
                n = float(input('digite o numero: '.capitalize()))
                b = int(input('digite a base: '.capitalize()))
                result = math.log(n, b)
                return print('\n', f'log({n}) ='.center(12), str(result).rjust(1))
            while True:
                r = int(input("opção: ".capitalize()))
                if r >= 16:
                    break
                if r == 0:
                    soma()
                if r == 1:
                    menos()
                if r == 2:
                    mutiplica()
                if r == 3:
                    fracao()
                if r == 4:
                    expo()
                if r == 5:
                    raiz()
                if r == 6:
                    sen()
                if r == 7:
                    cos()
                if r == 8:
                    tan()
                if r == 9:
                    arcsen()
                if r == 10:
                    arccos()
                if r == 11:
                    arctan()
                if r == 12:
                    fact()
                if r == 13:
                    primos()
                if r == 14:
                    limpar()
                if r == 15:
                    log()
        except:
            print('algo deu errado')

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(calc)
