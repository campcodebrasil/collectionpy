
from collectionpy.date.dtmath import add, dateDiff
from datetime import datetime 

atual = datetime(2024, 1, 5)

proximo_dia = add(atual, day=1)
dia_anterior = add(atual, day=-1)

proximo_mes = add(atual, month=1)
mes_anterior = add(atual, month=-1)

proximo_ano = add(atual, year=1)
ano_anterior = add(atual, year=1)


print(atual)
print(proximo_dia)
print(dia_anterior)
print(proximo_mes)
print(mes_anterior)
print(proximo_ano)
print(ano_anterior)

