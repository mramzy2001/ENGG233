# import fileIO
import matplotlib as pyplot
import numpy as np


# import Date
# import chart


def menu():
    choices = [
        '1- Get Minimum Temperature of 1990-2019',
        '2- Get Maximum Temperature of 1990-2019',
        '3- Get Minimum Temperature of 1990-2019 Annually',
        '4- Get Maximum Temperature of 1990-2019 Annually',
        '5- Get Average Snowfall between 1990-2019 Annually'
    ]

    for i in range(0, len(choices)):
        print(choices[i] + '\n')


def commandName(commandNumber):
    if commandNumber == 1:
        return 'getMinTemp'
    if commandNumber == 2:
        return 'getMaxTemp'
    if commandNumber == 3:
        return 'getMinTempAnnually'
    if commandNumber == 4:
        return 'getMaxTempAnnually'
    if commandNumber == 5:
        return 'getAvgSnowFallAnnually'


def runFunction(TheObject, command_Name):

    date = TemperatureData.TemperatureData().dateObject()
    years = date.years()

    if command_Name == 'getMinTemp':
        result = TheObject.getMinTemp()
        print(f'The minimum temperature between 1990-2019 is {result}')

    if command_Name == 'getMaxTemp':
        result = TheObject.getMaxTemp()
        print(f'The maximum temperature between 1990-2019 is {result}')

    if command_Name == 'getMinTempAnnually':
        result = TheObject.getMinTempAnnually()

        for i in range(len(result)):
            year = int(years[i])
            print(f'The minimum temperature in year {year} is {result[i]}')

    if command_Name == 'getMaxTempAnnually':
        result = TheObject.getMaxTempAnnually()

        for i in range(len(result)):
            year = int(years[i])
            print(f'The maximum temperature in year {year} is {result[i]}')

    if command_Name == 'getAvgSnowFallAnnually':
        result = TheObject.getAvgSnowFallAnnually()

        for i in range(len(result)):
            year = int(years[i])
            print(f'The snowfall in year {year} is {result[i]}')


def main():
    menu()

    commandNUmber = int(input('Please choose on option: '))

    if commandNUmber < 1 or commandNUmber > 5:
        print('Command out of range')
    else:
        command_Name = commandName(commandNUmber)

        Data = TemperatureData.TemperatureData()
        minTempList = Data.minTemp()
        maxTempList = Data.maxTemp()
        snowFallList = Data.snowFall()

        Weather_Analyzer = WeatherAnalyzer.WeatherAnalyzer(minTempList, maxTempList, snowFallList)
        runFunction(Weather_Analyzer, command_Name)


if __name__ == '__main__':
    main()
