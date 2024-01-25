CND_SRC = "https://cdn.jsdelivr.net/npm/apexcharts"

class Chart:
    def __init__(self, x:[], y:[], y_label=[], plot_type='bar',
                chartId='darkpyChart',
                foreColor='343E59',
                background= 'fff',    
                fontFamily= "Crimson Text",
                fontSize = 12,
                width = None,
                height = None,
                dropShadowTop = -7,
                dropShadowLeft = 7,
                dropShadowBlur = -10,
                borderRadius = 5,
                borderColor = '6e7eaa',
                borderRight = 25,
                borserLeft = 15,
                palette = 2
        ):
        """
        x:list => ['x1', 'x2', 'x3', ...]

        y:list[list] => [
            [1, 2, 3, ...],
            [1, 2, 3, ...],
            ...
        ]

        y_label:list => ['Orçado', 'Realizado', 'Desvio', ...]

        ApexCharts DOC: https://apexcharts.com/docs/installation/
        """

        self.chartId = chartId
        self.plot_type = plot_type
        self.x = x
        self.y = y
        self.y_label = y_label
        self.foreColor = foreColor.replace('#', '')
        self.background = background.replace('#', '')
        self.fontFamily = fontFamily
        self.fontSize = fontSize
        self.width = width
        self.height = height
        self.dropShadowTop = dropShadowTop
        self.dropShadowLeft = dropShadowLeft
        self.dropShadowBlur = dropShadowBlur
        self.borderRadius = borderRadius
        self.borderColor = borderColor.replace('#', '')
        self.borderRight = borderRight
        self.borserLeft = borserLeft
        self.palette = f"palette{palette}"
        

    def __str__(self) -> str:
        return str(self.options())
    
    def series(self):        
        dataset = []
        max_y_label = len(self.y_label)
        i_label = 0
        for values in self.y:
            i = 0
            data = []
            max_data = len(values)
            y_label = self.y_label[i_label] if i_label < max_y_label else f'{i_label}'
            for label in self.x:
                valor = {'x': label, 'y': values[i]} if i < max_data else {'x': label}
                data.append(valor)
                i += 1
            dataset.append({'name': y_label, 'data': data})
            i_label += 1
        
        return dataset
    
    def chart(self): 
        chart = {
                "id": self.chartId,
                "type": self.plot_type,
                "foreColor": f"#{self.foreColor}",
                "background": f"#{self.background}",    
                "fontFamily": self.fontFamily, 
                "dropShadow": {
                    "enabled": "true",
                    "top": self.dropShadowTop,
                    "left": self.dropShadowLeft,
                    "blur": self.dropShadowLeft
                },  
            }
        if self.width is not None: chart["width"] = self.width
        if self.height is not None: chart["height"] = self.height

        return chart

    def plotOptions(self):
        return {
                "bar": {
                    "borderRadius": self.borderRadius,
                    "borderRadiusApplication": "end",
                    "borderRadiusWhenStacked": "last",            
                },
                "treemap": {
                    "borderRadius": 4,
                    "dataLabels": {
                        "format": "scale"
                    }
                },
                "radialBar": {
                    "hollow": {
                        "background": "#fff"
                    },
                    "dataLabels": {
                        "name": {},
                        "value": {},
                        "total": {}
                    },
                    "barLabels": {
                        "margin": 5,
                        "fontWeight": 600,
                        "fontSize": "16px"
                    }
                },
                "pie": {
                    "donut": {
                        "labels": {
                            "name": {},
                            "value": {},
                            "total": {}
                        }
                    }
                }
            }

    def grid(self):
        return {
                "borderColor": f"#{self.borderColor}",
                "padding": {
                    "right": self.borderRight,
                    "left": self.borserLeft
                }
            }

    def legend(self):
        return {
                "position": "top",
                "fontSize": self.fontSize,
                "offsetX": 0,
                "offsetY": 13,
                "markers": {
                    "shape": "square",
                    "size": 8
                },
                "itemMargin": {
                    "vertical": 0
                }
            }

    def theme(self):
        return {"palette": self.palette}

    def options(self):
        return {
            "chart": self.chart(),
            "plotOptions": self.plotOptions(),
            "grid": self.grid(),
            "legend": self.legend(),            
            "series": self.series(),
            "theme": self.theme()
        }


def ChartExemple():

    x = ['Piracicaba', 'Americana', 'São Paulo']
    y = [
        [8, 2, 15, 24],
        [12,5]
    ]

    y_label = ['Orçado', 'Realizado']

    chart = Chart(x, y, y_label)

    return chart
