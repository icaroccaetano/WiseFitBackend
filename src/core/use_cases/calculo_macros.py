def calculo_de_macros(calorias, peso, prot_factor=2.2, fat_factor=0.8):
    
    qtd_proteinas = peso * prot_factor
    qtd_gorduras = peso * fat_factor
    
    calorias_restantes = calorias - (qtd_proteinas * 4) - (qtd_gorduras * 9)
    qtd_carboidratos = calorias_restantes / 4
    
    if qtd_carboidratos < 0:
        qtd_carboidratos = 0
    
    return {
        "proteinas": round(qtd_proteinas, 1),
        "gorduras": round(qtd_gorduras, 1),
        "carboidratos": round(qtd_carboidratos, 1)
    }