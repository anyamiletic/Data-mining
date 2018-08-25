import pandas
import datetime as dt

def addDayOfTheWeek(df):
    months = {
        "December": 12,
        "November": 11,
        "October": 10,
        "September": 9,
        "August": 8,
        "July": 7,
        "June": 6,
        "May": 5,
        "April": 4,
        "March": 3,
        "February": 2,
        "January": 1
    }
    dayMonthMap = {}
    for i, row in df.iterrows():
        date = row["Incident Date"]
        year_sep = date.split(',')
        date_sep = year_sep[0].split(' ')

        month = months[date_sep[0].strip()]
        day = int(date_sep[1].strip())
        year = int(year_sep[1].strip())

        readable_date = dt.date(year, month, day)
        
        dayOfTheWeek = readable_date.weekday()
        dayOfTheWeek = list(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])[dayOfTheWeek]
        month = date_sep[0]
        
        if dayOfTheWeek + ":" + month not in dayMonthMap:
            dayMonthMap[dayOfTheWeek + ":" + month] = row["# Incidents"]
        else:
            dayMonthMap[dayOfTheWeek + ":" + month] += row["# Incidents"]
    
    
    df2 = pandas.DataFrame(data = {"Month" : [], "Day Of The Week" : [], "# Incidents" : []})
    
    for k, v in dayMonthMap.iteritems():
        day = k.split(':')
        month = day[1]
        day = day[0]
        df2 = df2.append({"Month" : month, "Day Of The Week" : day, "# Incidents" : v}, ignore_index = True)
    
    return df2

def main():
    df = pandas.read_csv("processed_injuries.csv")    
    df = df.append(pandas.read_csv("processed_deaths.csv"))

    data = []
    for i, row in df.iterrows():
        data.append(row["# Killed"] + row["# Injured"])
    
    df["# Incidents"] = pandas.Series(data, index = df.index)
    #print df
    df = addDayOfTheWeek(df)
    
    with open("dayOfTheWeekPerMonth.csv", "w") as csvFile:
        csv = df.to_csv(index = True)
        csvFile.write(csv)
    
if __name__ == "__main__":
    main()
