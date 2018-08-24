import pandas

def changeDateFormat(df):
    for i, row in df.iterrows():
        month = row["Incident Date"].strip().split(' ')[0].split(',')[0]
        df.set_value(i, "Incident Date", month)
    
    df = df.drop(columns = ["Unnamed: 0", "Incident Date", "City Or County"])
    
    allIncidents = {}
    allStates = []
    for i, row in df.iterrows():
        state = row["State"].strip()
        if state not in allStates:
            allStates.append(state)
            allIncidents[state] = int(row["# Injured"]) + int(row["# Killed"])
        else:
            allIncidents[state] += int(row["# Injured"]) + int(row["# Killed"])
        df = df.drop([i])
    
    df = df.drop(columns = ["# Killed", "# Injured"])
    for k, v in allIncidents.iteritems():
        state = k
        numberOfDeaths = v
        df = df.append({"State" : state, "# Incidents" : int(numberOfDeaths)}, ignore_index = True)
    
    return df

def main():
    df = pandas.read_csv("processed_injuries.csv")
    df2 = pandas.read_csv("processed_deaths.csv")
    for i, row in df2.iterrows():
        df = df.append(row, ignore_index = True)
    
    df = changeDateFormat(df)
    
    with open("summedIncidentsPerState.csv", "w") as csv_file:
        csv = df.to_csv(index = False)
        csv_file.write(csv)

if __name__ == "__main__":
    main()
