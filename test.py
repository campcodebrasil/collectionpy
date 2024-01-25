
from collectionpy.date import dtget
from datetime import datetime

agora = datetime.now()
print(agora) # RESULTADO: 2024-01-24

# Recupera o Último Dia Número
ultimo_dia = dtget.lastDay(agora)
print(ultimo_dia) # RESULTADO: 31

# Recupera o Último Dia em Data
ultimo_dia = dtget.lastDate(agora)
print(ultimo_dia) # RESULTADO: 2024-01-31

# Adiciona mês (Positivo e Negativo)
proximo_mes = dtget.addMonth(agora, 1)
mes_anterior = dtget.addMonth(agora, -1)
print(proximo_mes) # RESULTADO: 2024-02-24
print(mes_anterior) # RESULTADO: 2023-12-24



