class calc:
    try:
        print("\033[0:31m" + """ 
                        ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ 
                        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
                        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║
                        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║
                        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║
                         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                  """ + "\033[0m")
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
    [ 13 ] SAIR""")
        def soma():
            cs = 0
            o = 1
            while True:
                try:
                    n = float(input(f'digite seu {o} numero: '))
                except:
                    break
                cs += n
                o += 1
            print(cs)

        def menos():
            cs = 0
            o = 1
            while True:
                if o == 1:
                    try:
                        global n1
                        n1 = float(input(f'digite seu 1 numero: '))
                    except:
                        break
                elif o != 1:
                    try:
                        n = float(input(f'digite seu {o} numero: '))
                    except:
                        break
                k = n1
                if o == 2:
                    cs = k - n
                if o >= 3:
                    cs -= n
                o += 1
            print(cs)

        def mutiplica():
            cx = 1
            o = 1
            while True:
                try:
                    n = float(input(f'digite seu {o} numero: '))
                except:
                    break
                cx *= n
                o += 1
            print(cx)

        def fracao():
            cx = 1
            o = 1
            while True:
                if o == 1:
                    try:
                        global n1
                        n1 = float(input(f'digite seu 1 numero: '))
                    except:
                        break
                elif o != 1:
                    try:
                        n = float(input(f'digite seu {o} numero: '))
                    except:
                        break
                k = n1
                if o == 2:
                    cs = k / n
                if o >= 3:
                    cs /= n
                o += 1
            print(cs)

        def expo():
            try:
                o = float(input('digite seu numero: '))
                v = int(input('digite seu exponencial: '))
            except:
                print('*-*')
            cx = o ** v
            print(cx)

        def raiz():
            try:
                o = float(input('digite seu numero: '))
                v = float((input('digite sua raiz: ')))
            except:
                print('*-*')
            cx = o ** (1/v)
            print(cx)

        def sen():
            try:
                o = float(input('digite seu numero: '))
            except:
                print('*-*')
            cx = math.sin(o)
            print(cx)

        def cos():
            try:
                o = float(input('digite seu numero: '))
            except:
                print('*-*')
            cx = math.cos(o)
            print(cx)

        def tan():
            try:
                o = float(input('digite seu numero: '))
            except:
                print('*-*')
            cx = math.tan(o)
            print(cx)

        def arccos():

                try:
                    o = float(input('digite seu numero: '))
                except:
                    print('*-*')
                cx = math.cos(o) ** -1
                print(cx)

        def arcsen():

                try:
                    o = float(input('digite seu numero: '))
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
            n = int(input('digite um numero: '))
            cx = math.factorial(n)
            print(cx)

        while True:
            r = int(input("opção: "))
            if r >= 13:
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
    except:
        print('algo deu errado')
calc()
