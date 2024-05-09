import numpy as np

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

class SimpleLinearRegression:
    def __init__(self, x:list, y:list):
        self.xi = np.array(x)
        self.yi = np.array(y)

        n = len(self.xi)
        sum_xi = np.sum(self.xi)
        sum_yi = np.sum(self.yi)
        sum_xi_yi = np.sum(self.xi * self.yi)
        sum_xi_squared = np.sum(self.xi ** 2)

        self.b = (n * sum_xi_yi - sum_xi * sum_yi) / (n * sum_xi_squared - sum_xi ** 2)
        self.a = (sum_yi - self.b * sum_xi) / n

        if len(x) != len(y): raise Exception('As Listas X e Y devem conter a mesma quantidade de itens')

    def expression(self): return "Equação da linha de regressão: y =", self.a, "+", self.b, "* x"

    def calcular(self, x): return  self.a + self.b * x
