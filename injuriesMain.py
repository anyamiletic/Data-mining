import pandas

print("**************\n*injuries.csv*\n**************\n")
df_injuries = pandas.read_csv("injuries.csv")
print
print(df_injuries.head())
print
print(df_injuries.count())
print
print(df_injuries.describe())
print
for col in df_injuries.columns:
    print("count values in column " + col)
    print(df_injuries[col].value_counts(dropna = False))
    # najvise incidenata za praznike poput dana nezavisnosti (4. jul) 
    # i meksickog praznika (5. maj)
    # najvise slucajeva se desava u teksasu
    # od gradova i mesta ubedljivo najvise se desava u cikagu
    # uzoracka sredina za ubistva je jako mala (0.03),
    # dok je za povrede (1.08), sto znaci da je uglavnom 
    # povredjena samo jedna osoba i da niko nije umro
