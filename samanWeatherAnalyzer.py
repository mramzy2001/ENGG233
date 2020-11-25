class WeatherAnalyzer:
    
    def __init__(self, minTemp, maxTemp, snowFall):

        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.snowFall = snowFall
    
    def getMinTemp(self):

        minTempList = self.minTemp
        minAnnually = []

        for i in range(0, len(minTempList)):

            min_year_i = np.min(minTempList[i])

            minAnnually.append(min_year_i)

        return np.min(minAnnually)

    def getMinTempAnnually(self):
        
        minTempList = self.minTemp
        minAnnually = []

        for i in range(0, len(minTempList)):

            min_year_i = np.min(minTempList[i])

            minAnnually.append(min_year_i)
        
        return minAnnually

    def getMaxTemp(self):

        maxTempList = self.maxTemp
        maxAnnually = []

        for i in range(0, len(maxTempList)):

            max_year_i = np.max(maxTempList[i])

            maxAnnually.append(max_year_i)
        
        return np.max(maxAnnually)

    def getMaxTempAnnually(self):
        
        maxTempList = self.maxTemp
        maxAnnually = []

        for i in range(0, len(maxTempList)):

            max_year_i = np.max(maxTempList[i])

            maxAnnually.append(max_year_i)
        
        return maxAnnually

    def getAvgSnowFallAnnually(self):
        
        snowFall = self.snowFall
        avgSnowFallAnnually = []

        for i in range(0, len(snowFall)):

            avg_year_i = np.average(snowFall[i])

            avgSnowFallAnnually.append(avg_year_i)

        return avgSnowFallAnnually

    def getAvgTempAnnually(self):
        
        maxTemp = self.maxTemp
        minTemp = self.minTemp
        avgTempAnnually = []

        if len(maxTemp) == len(minTemp):

            for i in range(0, len(maxTemp)):
                
                avgMax_i = np.average(maxTemp[i])
                avgMin_i = np.average(minTemp[i])

                avg_i = np.average([avgMax_i, avgMin_i])

                avgTempAnnually.append(avg_i)
        
        return avgTempAnnually
