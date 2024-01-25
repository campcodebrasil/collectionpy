def normalized_mean(max, min, mean, median, safety_factor=True):
    """
    PT-BR: Cálculo para Normalizar a Média de resultados
        1. Realiza a ponderação da média para cima
        2. Realiza a ponderação da média para baixo
        3. Realiza a média da ponderação
        4. Realiza a média do cálculo anterior com a mediana

        Fator de Segurança = Verdadeiro (Default = True)
        5. Realiza a Média do resultado anterior com a média da Média + a Mediana

    EN: Calculation to Normalize the Average of Results
        1. Weights the average upwards
        2. Weights from average down
        3. Performs the weighting average
        4. Performs the average of the previous calculation with the median
        
        Safety Factor = True (Default = True)
        5. Performs the Average of the previous result with the average of the Average + the Median
    """

    a, b, c, d = max, min, mean, median
    m1 = (a+c)/2
    m2 = (b+c)/2
    m3 = (m1+m2)/2
    m4 = (d+m3)/2
    if safety_factor:
        mmd = (c+d) / 2
        return (m4 + mmd) / 2
    else: return m4
