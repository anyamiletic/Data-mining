import pandas

allDates = []

def transformTypesIntoNumerical(df_injuries):
    for i, row in df_injuries.iterrows():
        date = row["Incident Date"].strip()
        if date not in allDates:
            allDates.append(date)
    numOfDates = len(allDates)
    
    def createNewColumnn(row):
        data = []
        k = allDates.index(row["Incident Date"])
        for i in range(numOfDates):
            if i == k:
                data.append(1)
            else:
                data.append(0)
        return pandas.Series(data)
    
    df_injuries[allDates] = df_injuries.apply(createNewColumnn, axis=1)
    return df_injuries

def main():
    df_injuries = pandas.read_csv("processed_injuries.csv")
    df_injuries = transformTypesIntoNumerical(df_injuries)
    
    df_injuries = df_injuries.drop(columns = ["Incident Date"])
    print df_injuries
    
    with open("injuries_transformed_types_to_numerical.csv", "w") as newCsvFile:
        csv = df_injuries.to_csv(index = False)
        newCsvFile.write(csv)
    
    
if __name__ == "__main__":
    main()
    
    
