import pandas

def sumIncidentsPerCityAndState(df):
    df = df.drop(columns = ["Unnamed: 0", "Incident Date"])
    
    incidents = {}
    for i, row in df.iterrows():
        state = row["State"].strip()
        city = row["City Or County"].strip()
        if state + ":" + city not in incidents:
            incidents[state + ":" + city] = int(row["# Injured"]) + int(row["# Killed"])
        else:
            incidents[state + ":" + city] += int(row["# Injured"]) + int(row["# Killed"])
        df = df.drop([i])
    
    df = df.drop(columns = ["# Killed", "# Injured"])
    for k, v in incidents.iteritems():
        key = k.split(':')
        city = key[1]
        state = key[0]
        numberOfDeaths = v
        df = df.append({"State" : state, "City Or County" : city, "# Incidents" : int(numberOfDeaths)}, ignore_index = True)
    
    return df

def main():
    df = pandas.read_csv("../processed_injuries.csv")
    df2 = pandas.read_csv("../processed_deaths.csv")
    for i, row in df2.iterrows():
        df = df.append(row, ignore_index = True)
    
    df = sumIncidentsPerCityAndState(df)
    
    with open("summedIncidents.csv", "w") as csv_file:
        csv = df.to_csv(index = False)
        csv_file.write(csv)

if __name__ == "__main__":
    main()
