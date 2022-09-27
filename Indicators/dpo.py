import numpy as np 

class DPO:
    def __init__(self,dataset:list,period:int=4) -> None: #gereken inputlar: dataset(array),period(int)
        self.dataset = dataset
        self.period = period

    def moving_average(self):              # Calculates the MA 
        n = self.period                    # for a period by using Index Slicers
        ret = np.cumsum(self.dataset)      
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n-1:] / n
    
    def closes(self):      # Getting (n/2)+1th close price
        n = self.period    # to calculate DPO
        tempArr = []
        for i in range(n-2,((n-2)+2*len(self.moving_average())),2):
            tempArr.append(self.dataset[(i//2)+1])
        return np.array(tempArr)

    def print(self): #liste döndürecek yazdirma fonksiyonu, bu çağırılacak.
        dpoFinalize = np.subtract(self.closes(),self.moving_average())
        return dpoFinalize