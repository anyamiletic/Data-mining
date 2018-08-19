import pandas

print("**************\n*deaths.csv*\n**************\n")
df_deaths = pandas.read_csv("deaths.csv")
print
print(df_deaths.head())
print
print(df_deaths.count())
print
print(df_deaths.describe())
print
for col in df_deaths.columns:
    print("count values in column " + col)
    print(df_deaths[col].value_counts(dropna = False))
    # opet se najvise slucajeva desava u teksasu i tenesiju
    # od gradova i mesta su gradovi u teksasu i tenesiju
    # uzoracka sredina za ubistva je (1.006),
    # dok je za povrede (0.038), sto znaci da je uglavnom 
    # ubijena samo jedna osoba i da niko nije povredjen
