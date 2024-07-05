def calculaTempo(min):
    if min >= 15:
        if min >= 60:
            hrs = min // 60
            custo = (hrs - 1) * 1.50 + 9.00
            pis, coffins, icms = custo * 0.033, custo * 0.020, custo * 0.17
            imposto = pis + coffins + icms
    print("=" * 30)
    print(f"Tempo {hrs:.2f} horas\nPIS: R${pis:.2f}\nCOFFINS: R${coffins:.2f}\nICMS: R${icms:.2f}\nImpostos: R${imposto:.2f}\nCusto final: R${custo:.2f}")


calculaTempo(int(input("Digite tempo em minutos: ")))