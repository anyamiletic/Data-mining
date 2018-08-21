import pandas

def no_deaths():
    print('put Null values on zero death rows')
    df_deaths = pandas.read_csv('./deaths.csv')

    for i, row in df_deaths.iterrows():
        number_deaths = row['# Killed']
        if(number_deaths == 0):
            df_deaths.set_value(i, '# Killed', None)

    return df_deaths


def remove_missing_values(df):
    print('[remove_missing_values] Function enter')
    #df_deaths = pandas.read_csv('./deaths.csv')
    df_deaths_tmp = df[pandas.notnull(df['# Killed'])]
    #df_deaths_tmp = df_deaths_tmp[pandas.notnull(df_deaths_tmp['type'])]
    #df_deaths_tmp = df_deaths_tmp[pandas.notnull(df_deaths_tmp['rating'])]
    print('[remove_missing_values] Function exit')
    return df_deaths_tmp

def main():
    df = no_deaths()
    df = remove_missing_values(df)

    #remove column Operations
    df = df[['Incident Date','State','City Or County','# Killed','# Injured']]

    print(df.describe())
    print(df.head())

    #export new csv file
    df.to_csv("processed_deaths.csv")

if __name__ == "__main__":
    main()