import pandas
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

allStates = []
allMonths = []
allCities = []

def transformTypesIntoNumerical(df_injuries):
    for i, row in df_injuries.iterrows():
        state = row["State"].strip()
        if state not in allStates:
            allStates.append(state)
    numOfStates = len(allStates)
    
    for i, row in df_injuries.iterrows():
        city = row["City Or County"].strip()
        if city not in allCities:
            allCities.append(city)
    numOfCities = len(allCities)
    
    for i, row in df_injuries.iterrows():
        date = row["Incident Date"].strip()
        month = date.split(' ')[0]
        if month not in allMonths:
            allMonths.append(month)
    numOfMonths = len(allMonths)
    
    def createNewColumnnMonths(row):
        data = []
        k = allMonths.index(row["Incident Date"].strip().split(' ')[0])
        for i in range(numOfMonths):
            if i == k:
                data.append(1)
            else:
                data.append(0)
        return pandas.Series(data)
    
    def createNewColumnnCity(row):
        data = []
        k = allCities.index(row["City Or County"])
        for i in range(numOfCities):
            if i == k:
                data.append(1)
            else:
                data.append(0)
        return pandas.Series(data)
    
    def createNewColumnnStates(row):
        data = []
        k = allStates.index(row["State"])
        for i in range(numOfStates):
            if i == k:
                data.append(1)
            else:
                data.append(0)
        return pandas.Series(data)
    
    df_injuries[allMonths] = df_injuries.apply(createNewColumnnMonths, axis=1)
    df_injuries[allStates] = df_injuries.apply(createNewColumnnStates, axis=1)
    df_injuries[allCities] = df_injuries.apply(createNewColumnnCity, axis=1)
    df_injuries = df_injuries.drop(columns = ["Incident Date", "State", "City Or County", "Unnamed: 0"])
    return df_injuries

def main():
    df_injuries = pandas.read_csv("processed_injuries.csv")
    df_injuries = transformTypesIntoNumerical(df_injuries)
    
    def encode_units(x):
        if x <= 0:
            return 0
        if x >= 1:
            return 1

    df_injuries = df_injuries.applymap(encode_units)
    print df_injuries
    
    frequent_itemsets = apriori(df_injuries, min_support = 0.07, use_colnames = True)

    print frequent_itemsets
    
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    print rules
    
if __name__ == "__main__":
    main()
