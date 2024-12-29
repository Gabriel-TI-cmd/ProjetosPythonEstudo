n = float(input('Digite um valor em metros: '))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000
print('O valor {:.0f} metros em milímetros é: {:.0f} mm.\nO valor {:.0f} metros em centímetros é: {:.0f} cm.'.format(n, mm, n, cm))
print('O valor {:.0f} metros em decímetros é: {:.0f} dm.\nO valor {:.0f} metros em decâmetros é: {} dam.'.format(n, dm, n, dam))
print('O valor {:.0f} metros em hectômetros é: {} hm.\nO valor {:.0f} metros em quilômetros é: {} Km.'.format(n, hm, n, km))
