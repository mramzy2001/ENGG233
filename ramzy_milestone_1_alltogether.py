import numpy as np
import matplotlib.pyplot as pyplot

class FileIO:
    def __init__(self, filePath):
        self.filePath = filePath
    
    def get_dataTable(self):
        dataTable = np.loadtxt(self.filePath , delimiter=',', skiprows=1, usecols=(0,1,2,3,4), dtype=np.float)
        return dataTable

class Date:
    def __init__(self, month, year):
        self.month = month
        self.year = year

class TemperatureData:
    def __init__(self, date, maxTemperature, minTemperature, snowFall):
        self.date = date
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature
        self.snowFall = snowFall

class Chart:
    def __init__(self, x, y, title, xlabel, ylabel):
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def drawLineChart(self):

        pyplot.title(self.title)
        pyplot.ylabel(self.ylabel)
        pyplot.xlabel(self.xlabel)

        pyplot.plot(self.x, self.y, marker = "o")
        pyplot.show()

    def drawBarChart(self):
        ypos = np.arange(len(self.x))

        pyplot.bar(ypos, self.y, align = 'center', alpha = 0.5)
        pyplot.xticks(ypos, self.x)
        pyplot.xlabel(self.xlabel)
        pyplot.ylabel(self.ylabel)
        pyplot.title(self.title)

        pyplot.show
