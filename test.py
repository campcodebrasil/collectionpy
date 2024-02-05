
from collectionpy.chart.googlecharts import GTable

cols = ['Periodo', 'Orçado', 'Realizado']
rows = [
    ['2023-01', 25000, 20000], 
    ['2023-02', 24500, 25000], 
    ['2023-03', 25300, 26000], 
    ['2023-04', 25700, 27000], 
]

gchart = GTable(id='Table', rows=rows, cols=cols)

print(gchart.render())
print(gchart.js_loader)

