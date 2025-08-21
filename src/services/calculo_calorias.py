def calculo_de_calorias(peso, altura, idade, sexo, nivel_atividade, deficit):
    if sexo == "feminino":
        metabolismo_basal = 10 * peso + 6.25 * altura - 5 * idade - 161
    elif sexo == "masculino": # masculino
        metabolismo_basal = 10 * peso + 6.25 * altura - 5 * idade + 5
    
    fatores_ativ = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'intenso': 1.725,
        'muito_intenso': 1.9
    }
    fator = fatores_ativ.get(nivel_atividade, 1.2)  # padrão sedentário

    gasto_total = metabolismo_basal * fator

    gasto_cutting = gasto_total * (1-(deficit/100))

    return round(gasto_cutting, 0)