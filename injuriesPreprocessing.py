import pandas

def no_injuries():
    print('put Null values on zero injured rows')
    df_injuries = pandas.read_csv('./injuries.csv')

    for i, row in df_injuries.iterrows():
        number_injuries = row['# Injured']
        if(number_injuries == 0):
            df_injuries.set_value(i, '# Injured', None)

    return df_injuries


def remove_missing_values(df):
    print('[remove_missing_values] Function enter')
    #df_injuries = pandas.read_csv('./injuries.csv')
    df_injuries_tmp = df[pandas.notnull(df['# Injured'])]
    #df_injuries_tmp = df_injuries_tmp[pandas.notnull(df_injuries_tmp['type'])]
    #df_injuries_tmp = df_injuries_tmp[pandas.notnull(df_injuries_tmp['rating'])]
    print('[remove_missing_values] Function exit')
    return df_injuries_tmp

def main():
    df = no_injuries()
    df = remove_missing_values(df)

    #remove column Operations
    df = df[['Incident Date','State','City Or County','# Killed','# Injured']]

    print(df.describe())
    print(df.head())

    #export new csv file
    df.to_csv("processed_injuries.csv")

if __name__ == "__main__":
    main()