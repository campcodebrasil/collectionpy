from datetime import datetime
from collectionpy.date import dtmath, dtget


class RelativeDate:
    """OBJETO RelativeDate

    Cria um objeto com o atributo datetime, podendo ter todas as funcionalidades do pacote datetime nesse atributo e possui métodos de datas relativas dentro do objeto RelativeDate
    """
    def __init__(self, dt=None):
        if dt is None:
            self.datetime = datetime.now()
        else:
            self.datetime = dt

        self.initial_date = dt
    
    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d')
    
    ### PROPRIEDADES DATE ###
    def second(self):
        return self.datetime.second
    
    def minute(self):
        return self.datetime.minute
    
    def hour(self):
        return self.datetime.hour
    
    def day(self):
        return self.datetime.day
    
    def month(self):
        return self.datetime.month
    
    def year(self):
        return self.datetime.year

    ### DATE MATH ###
    def addDay(self, relative_day):
        self.datetime = dtmath.addDay(self.datetime, relative_day)

    def addMonth(self, relative_month):
        self.datetime = dtmath.addMonth(self.datetime, relative_month)

    def addYear(self, relative_year):
        self.datetime = dtmath.addYear(self.datetime, relative_year)

    def add(self, year=0, month=0, day=0, hour=0, minute=0, second=0):        
        self.datetime = dtmath.add(dt=self.datetime,year=year, month=month, day=day, hour=hour, minute=minute, second=second)

    def dateDiff(self, dt, on='month'):
        return dtmath.dateDiff(self.datetime, dt, on)
    
    ### DATE GET ###
    def lastDay(self):
        return dtget.lastDay(self.datetime)
    
    def lastDate(self):
        return dtget.lastDate(self.datetime)
    
    def getUtilDay(self, util_day, disregard=[], last_day=False):
        return dtget.getUtilDay(self.datetime, util_day, disregard, last_day)

    def utilDays(self, disregard=[]):
        return dtget.utilDays(self.datetime, disregard)