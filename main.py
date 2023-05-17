import pandas as pd
import math

testCasesCount = 100

clickIncome = [math.log10(level) * level**2 / 32 for level in range(1, testCasesCount)]
passiveIncome = [math.sqrt(level) * level for level in range(1, testCasesCount)]

clickCost = [math.exp(level / 6) for level in range(1, testCasesCount)]
passiveCost = [math.exp(level / 6.2) for level in range(1, testCasesCount)]

dfDict = {"Click Income": clickIncome, "Click Upgrade Cost": clickCost, "Passive Income": passiveIncome, "Passive Upgrade Cost": passiveCost}
df = pd.DataFrame(dfDict)
clickTime = df['Click Upgrade Cost'] / (df['Click Income'] * 5.8)
passiveTime = df['Passive Upgrade Cost'] / df['Passive Income']
df['Click Progress Time'] = clickTime
df['Passive Progress Time'] = passiveTime

print(df)
