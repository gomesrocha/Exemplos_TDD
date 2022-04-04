import array as arr
#Função para calculo de INSS
def calculo_inss(salario_bruto):
    if salario_bruto < 1693.73:
        inss = salario_bruto * 8 /100
    elif salario_bruto >= 1693.73 and salario_bruto < 2822.91:
        inss = salario_bruto * 9 / 100
    elif  salario_bruto > 2822.90 and salario_bruto < 5645.80:
        inss = salario_bruto * 11 / 100
    else:
        inss = 621.03
    return inss

#Função para calculo de imposto de renda retido na fonte
def calculo_irrf(salario_bruto):
    salario = salario_bruto - calculo_inss(salario_bruto)
    if salario >= 1903.99 and salario < 2826.66:
        irrf = (salario - 142.82) * 7.5 / 100
    elif salario >= 2826.66 and salario < 3751.06:
        irrf = (salario - 354.80) * 15 / 100
    elif salario >= 3751.05 and salario < 4664.69:
        irrf = (salario - 636.13) * 22.5 / 100
    elif salario >= 4664.69:
        irrf = (salario - 869.36) * 27.5 / 100
    return irrf
#Função para exibir folha de pagamento
def folha(salario_bruto):
    print("Folha de Pagamento")
    print("Salario Bruto")
    print(salario_bruto)
    print("Descontos")
    print("_______________________")
    print("INSS")
    print(calculo_inss(salario_bruto))
    print("IRRF")
    print(calculo_irrf(salario_bruto))
    print("Total de descontos")
    total = calculo_irrf(salario_bruto) + calculo_inss(salario_bruto)
    print(total)
    salario_liquido = salario_bruto - total
    print("_______________________")
    print("Salario líquido")
    print(salario_liquido)
    print("_______________________")