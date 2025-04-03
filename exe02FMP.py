qtdnumLidos = int(input("Quantos números devem ser lidos? "))
faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0 
for i in range(0, qtdnumLidos): 
    num = int(input('Informe um valor entre 0 e 100: '))

    if num >= 0 and num <= 25:
        faixa1 = faixa1 + 1
        
    elif num >= 26 and num <= 50:
        faixa2 = faixa2 + 1
    
    elif num >= 51 and num <=75:
        faixa3 = faixa3 + 1
        
    elif num >= 76 and num <= 100:
        faixa4 = faixa4 + 1
      
    else:
        print('Valor informado não está dentro da faixa solicitada')
        
        
print("Na faixa 1 tem {} números ".format(faixa1))
print("Na faixa 2 tem {} números ".format(faixa2))
print("Na faixa 3 tem {} números ".format(faixa3))
print("Na faixa 4 tem {} números ".format(faixa4))

        
