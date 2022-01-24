#mcandrew

import sys
import numpy as np
import pandas as pd

class postprocess(object):
    def __init__(self):
        self.forecast_date = self.getForecastDate()
        self.boundBelowByZero()
        self.writeOut()

    def getForecastDate(self):
        from epiweeks import Week
        import datetime

        from datetime import datetime as dt

        today = dt.today()
        dayofweek = today.weekday()

        thisWeek = Week.thisweek()
        if dayofweek in {6,0}: # a SUNDAY or MONDAY
            thisWeek = thisWeek-1
        else:
            pass
        self.thisWeek = thisWeek
        
        forecastDate = ((thisWeek+1).startdate() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.forecast_date = forecastDate
        return forecastDate

    def boundBelowByZero(self):
        import pandas as pd
        d = pd.read_csv("{:s}-LUcompUncertLab-TEVA-preprocess.csv".format(self.forecast_date))
        d["value"] = [ np.max([0,x]) for x in d["value"]] # if negative make 0

        self.d = d
        return d

    def writeOut(self):
        self.d.to_csv("{:s}-LUcompUncertLab-TEVA.csv".format(self.forecast_date),index=False)
    

if __name__ == "__main__":

    PP = postprocess()
