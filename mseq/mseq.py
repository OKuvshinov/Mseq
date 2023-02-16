import matplotlib.pyplot as plt
import numpy

print("Программа для расчета М-последовательности\n\nДля выхода введите \"0\"\n\n")

d1 = []

def find_M(start):
    n = int(input("Введите показатель n: "))  
    if n == 0:
        return 0
    N = 2**n - 1
    c = []
    d = []
    print('\n')
    for i in range(n):
        c.append(int(input("c" + str(i + 1) + ": ")))
    print('\n')
    for i in range(n):
        d.append(int(input("d" + str(i + 1) + ": ")))
    for i in range(n, N):
        sum = c[0] * d[i - 1]
        for j in range(1, n):
            sum ^= c[j] * d[i - j - 1]
        d.append(sum)
    if start == 0:
        start = 1
        for i in range(N):
            d1.append(d[i])
    else:
        sum = 0
        for i in range(N):
            sum += d1[i] * d[i] 
        print('\n')
        print(sum)
        print('\n')
        
    print('\n')
    print(d)
    pack = [d, N]
    return pack

def apply_filter(pack):
    N = pack[1]
    fltr1 = []
    out1 = numpy.zeros((N, N * 2), dtype=int)
    for i in range(N):
        reversed_d = list(reversed(pack[0]))
        for j in range(N):
            if reversed_d[j] == 0:
                reversed_d[j] = -1
        if reversed_d[N - i - 1] == -1:
            for j in range(N):
                if reversed_d[j] == -1:
                    reversed_d[j] = 1
                else:
                    reversed_d[j] = -1
        for j in range(i, i + N):
            out1[i][j] = reversed_d[j - i]
    print('\n')
    if N <= 7:
        print(out1)
    else:
        for i in range(N):
            print(*out1[i])
    for i in range(N * 2):
        sum = 0
        for j in range(N):
            sum += out1[j][i]
        fltr1.append(sum)
    print('\n')
    print(fltr1)
    reversed_d = list(reversed(pack[0]))
    for j in range(N):
        if reversed_d[j] == 0:
            reversed_d[j] = -1
    pack2 = (reversed_d, N)
    print('\n')
    title1 = "Последовательность импульсов на выходе сумматора"
    title2 = "Сигнал на выходе СФ информационной последовательности\n при действии информационного сигнала"
    draw_res(fltr1, N, title1, title2)
    return pack2

def end_filter(pack2):
    N = pack2[1]
    prev = pack2[0]
    fltr2 = []
    out2 = numpy.zeros((N, N * 2), dtype=int)
    start = 1

    d = find_M(start)
    for i in range(N):
        reversed_d = list(reversed(d[0]))
        for j in range(N):
            if reversed_d[j] == 0:
                reversed_d[j] = -1
        if prev[N - i - 1] == -1:
            for j in range(N):
                if reversed_d[j] == -1:
                    reversed_d[j] = 1
                else:
                    reversed_d[j] = -1
        for j in range(i, i + N):
            out2[i][j] = reversed_d[j - i]
    print('\n')
    if N <= 7:
        print(out2)
    else:
        for i in range(N):
            print(*out2[i])
    for i in range(N * 2):
        sum = 0
        for j in range(N):
            sum += out2[j][i]
        fltr2.append(sum)
    print('\n')
    print(fltr2)
    print('\n')
    title1 = "Процесс на выходе сумматора при действии синхронизирующего сигнала"
    title2 = "Сигнал на выходе СФ информационной последовательности\n при действии синхронихирующего сигнала"
    draw_res(fltr2, N, title1, title2)

def draw_res(epur, N, title1, title2):
    x = [0]
    y = []
    y_shifted = [0]
    for i in range(1, N*2):
        x.append(i)
        x.append(i)
    for i in range(0, N*2):
        y.append(epur[i])
        y.append(epur[i])
        y_shifted.append(epur[i])
        y_shifted.append(epur[i])
    x.append(N*2)
    fig, axs = plt.subplots(2)
    axs[0].set_title(title1)
    axs[0].grid()
    axs[0].plot(x, y)
    x.append(N*2)
    axs[1].set_title(title2)
    axs[1].grid()
    axs[1].plot(x, y_shifted)

start = 0
print('\nФормирование СФ с информационной последовательностью\n')
pack = find_M(start)
if pack != 0:
    pack2 = apply_filter(pack)
    print('\nФормирование СФ с сигналом синхронизации\n')
    end_filter(pack2)
    plt.show()

