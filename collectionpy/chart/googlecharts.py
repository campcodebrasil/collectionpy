class GChart:
    """Documentação Oficial Google Charts: https://developers.google.com/chart/interactive/docs?hl=pt-br

    Tipos de Gráficos:
    - LineChart (Default)
    - ColumnChart (Primeira Coluna é o Label do Eixo x)
    - BarChart  (Primeira Coluna é o Label do Eixo y)
    - PieChart (Usar Apenas Duas Colunas no atribuito Cols)
    - ScatterChart
    """
    def __init__(self, rows=[], cols=[], id='gChart', chartType='LineChart', divClass=''):
        self.js_loader = '<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>'        
        self.loader = "google.charts.load('current',{packages:['corechart']});"
        self.data = ''
        self.rows = rows
        self.cols = cols
        self.options = {'width': '100%', 'height': '100%'}
        self.id = id
        self.chartType = chartType
        self.divClass = divClass
        
    def addCol(self, col): 
        """['C1', 'C2', ... {'role': 'style'} (opcional) ]"""
        self.cols.append(col)

    def addRow(self, row): 
        """['C1', 'C2', ... 'role: value, role: value, ...' (Adicionar Regras somente se for adicionado o role na coluna) ]"""
        self.rows.append(row)

    def getData(self):
        listRows = []
        listRows.append(self.cols)
        max_cols = len(self.cols)
        for r in self.rows:
            row = []
            for i in range(0, max_cols):
                try: value = r[i]
                except: value = ''
                row.append(value)
            listRows.append(row)
        return listRows

    def render(self):
        id = self.id.title()
        return f"""
<script type="text/javascript">
    {self.loader}
    google.charts.setOnLoadCallback({id});

    function {self.id.title()}() {{
        var data = google.visualization.arrayToDataTable({self.getData()});
        var chart  = new google.visualization.{self.chartType}(document.getElementById('{id}'));
        chart.draw(data, {self.options});
    }}
</script>
<div id="{id}" class="{self.divClass}"></div>
"""


class GTable(GChart):
    """Documentação Oficial Google Charts: https://developers.google.com/chart/interactive/docs/gallery/table?hl=pt-br"""
    def __init__(self, rows=[], cols=[], id='gTable', divClass=''):
        super().__init__(rows, cols, id, 'Table', divClass)
        self.loader = "google.charts.load('current', {'packages':['table']});"
        self.options = {'showRowNumber': 'true', 'width': '100%', 'height': '100%'}    


class GComboChart(GChart):
    """Documentação Oficial Google Charts: https://developers.google.com/chart/interactive/docs/gallery/combochart?hl=pt-br"""
    def __init__(self, rows=[], cols=[], lines=[0,], id='gComboChart', divClass=''):
        super().__init__(rows, cols, id, 'ComboChart', divClass)
        self.loader = "google.charts.load('current', {'packages':['table']});"
        self.options = {'showRowNumber': 'true', 'width': '100%', 'height': '100%'}
        self.lines = lines

    def get_series(self):
        series = {}
        if len(self.lines) == 0: self.lines = [0,]
        self.options['seriesType'] = 'bars'
        max_cols = len(self.cols)
        for l in self.lines:
            indice = l
            if indice < max_cols: series[indice] = {'type': 'line', 'colors': 'black'}
        self.options['series'] = series


    def render(self):
        self.get_series()
        return super().render()


    
