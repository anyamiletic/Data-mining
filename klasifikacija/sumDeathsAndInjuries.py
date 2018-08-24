import pandas

def changeDateFormat(df):
    for i, row in df.iterrows():
        month = row["Incident Date"].strip().split(' ')[0].split(',')[0]
        df.set_value(i, "Incident Date", month)
    
    df = df.drop(columns = ["Unnamed: 0"])
    
    injuriesMonths = {}
    for i, row in df.iterrows():
        month = row["Incident Date"].strip()
        state = row["State"].strip()
        city = row["City Or County"].strip()
        if month + ":" + state not in injuriesMonths:
            injuriesMonths[month + ":" + state + ":" + city] = int(row["# Injured"]) + int(row["# Killed"])
        else:
            injuriesMonths[month + ":" + state + ":" + city] += int(row["# Injured"]) + int(row["# Killed"])
        df = df.drop([i])
        #print i
    
    df = df.drop(columns = ["# Killed", "# Injured"])
    for k, v in injuriesMonths.iteritems():
        key = k.split(':')
        city = key[2]
        state = key[1]
        month = key[0]
        numberOfDeaths = v
        df = df.append({"Incident Date" : month, "State" : state, "City Or County" : city, "# Incidents" : int(numberOfDeaths)}, ignore_index = True)
    
    return df

def main():
    df = pandas.read_csv("processed_injuries.csv")
    df2 = pandas.read_csv("processed_deaths.csv")
    for i, row in df2.iterrows():
        df = df.append(row, ignore_index = True)
    
    df = changeDateFormat(df)
    
    with open("processed_changed_date_injuries.csv", "w") as csv_file:
        csv = df.to_csv(index = False)
        csv_file.write(csv)

if __name__ == "__main__":
    main()
