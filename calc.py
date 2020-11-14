import math
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from os import system
from platform import system as ss
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
        [ 15 ] SAIR
        Aperte uma letra para sair do loop no meio das contas""")

            def soma():
                cs = 0
                o = 1
                while True:
                    try:
                        n = float(input(f'digite seu {o} numero: '.capitalize()))
                    except:
                        break
                    cs += n
                    o += 1
                return print(str(cs).rjust(10))

            def menos():
                cs = 0
                o = 1
                while True:
                    if o == 1:
                        try:
                            global n1
                            n1 = float(input(f'digite seu 1 numero: '.capitalize()))
                        except:
                            break
                    elif o != 1:
                        try:
                            n = float(input(f'digite seu {o} numero: '.capitalize()))
                        except:
                            break
                    k = n1
                    if o == 2:
                        cs = k - n
                    if o >= 3:
                        cs -= n
                    o += 1
                return print(str(cs).rjust(10))

            def mutiplica():
                cx = 1
                o = 1
                while True:
                    try:
                        n = float(input(f'digite seu {o} numero: '.capitalize()))
                    except:
                        break
                    cx *= n
                    o += 1
                return print(str(cx).rjust(10))

            def fracao():
                cx = 1
                o = 1
                while True:
                    if o == 1:
                        try:
                            global n1
                            n1 = float(input(f'digite seu 1 numero: '.capitalize()))
                        except:
                            break
                    elif o != 1:
                        try:
                            n = float(input(f'digite seu {o} numero: '.capitalize()))
                        except:
                            break
                    k = n1
                    if o == 2:
                        cs = k / n
                    if o >= 3:
                        cs /= n
                    o += 1
                print(str(cs).rjust(10))

            def expo():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                    v = int(input('digite seu exponencial: '.capitalize()))
                except:
                    print('*-*')
                cx = o ** v
                return print(str(cx).rjust(10))

            def raiz():
                try:
                    o = float(input('digite seu numero: '))
                    v = float((input('digite sua raiz: '.capitalize())))
                except:
                    print('*-*')
                cx = o ** (1 / v)
                print(cx)

            def sen():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.sin(o)
                print(cx)

            def cos():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.cos(o)
                print(cx)

            def tan():
                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.tan(o)
                print(cx)

            def arccos():

                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.cos(o) ** -1
                print(cx)

            def arcsen():

                try:
                    o = float(input('digite seu numero: '.capitalize()))
                except:
                    print('*-*')
                cx = math.sin(o) ** -1
                print(cx)

            def arctan():

                try:
                    o = float(input('digite seu numero: '))
                except:
                    print('*-*')
                cx = math.tan(o) ** -1
                print(cx)

            def fact():
                n = int(input('digite um numero: '.capitalize()))
                cx = math.factorial(n)
                print(cx)
            def primos():
                n = int(input('digite um numero inicial: '))
                n1 = int(input('digite um numero final: '))
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
    [ 15 ] SAIR""")

            while True:
                r = int(input("opção: ".capitalize()))
                if r >= 15:
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
        except:
            print('algo deu errado')

    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(calc)
