def tempo(h, m, s):
    hm = h * 60
    ms = hm + m
    ss = s + (ms * 60)
    print(f"{ss} segundos.")

hora, minuto, segundos = map(int, input("Digite tempo (hh:mm:ss): ").split(":"))
tempo(hora, minuto, segundos)