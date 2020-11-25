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

class WeatherAnalyzer:
    def __init__(self, temp_list):
        self.temp_list = temp_list

    def getMinTemp(self):
        min_list = []
        for i in range(len(self.temp_list)):
            min_list.append(self.temp_list[i].minTemperature)
        
        return print(min(min_list))

    def getMinTempAnnually(self):
        monthly_mintemp = [ ]
        annual_mintemp = [ ]

        for i in range(len(self.temp_list)):
            if i == len(self.temp_list) - 1:
                monthly_mintemp.append(self.temp_list[i].minTemperature)
                annual_mintemp.append(min(monthly_mintemp))

            elif self.temp_list[i].date.year == self.temp_list[i+1].date.year:
                monthly_mintemp.append(self.temp_list[i].minTemperature)
            
            else:
                monthly_mintemp.append(self.temp_list[i].minTemperature)
                annual_mintemp.append(min(monthly_mintemp))
                monthly_mintemp = [ ]
        return print(annual_mintemp)

    def getMaxTemp(self):
        max_list = []
        for i in range(len(self.temp_list)):
            max_list.append(self.temp_list[i].maxTemperature)
        
        return print(max(max_list))

    def getMaxTempAnnually(self):
            monthly_maxtemp = [ ]
            annual_maxtemp = [ ]

            for i in range(len(self.temp_list)):
                if i == len(self.temp_list) - 1:
                    monthly_maxtemp.append(self.temp_list[i].maxTemperature)
                    annual_maxtemp.append(max(monthly_maxtemp))

                elif self.temp_list[i].date.year == self.temp_list[i+1].date.year:
                    monthly_maxtemp.append(self.temp_list[i].maxTemperature)
                
                else:
                    monthly_maxtemp.append(self.temp_list[i].maxTemperature)
                    annual_maxtemp.append(max(monthly_maxtemp))
                    monthly_maxtemp = [ ]
            return print(annual_maxtemp)

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

def main():
    filepath = FileIO("ProjectMilestone1/CalgaryWeather.csv")

    array = filepath.get_dataTable()
    
    dates = []
    temp_data = []

    for i in range(len(array)):
        dates.append(Date(array[i][1], array[i][0]))
        temp_data.append(TemperatureData(dates[i], array[i][2], array[i][3], array[i][4]))
    
    temp_analyzer = WeatherAnalyzer(temp_data)
    print(temp_data[0].snowFall)

    
main()