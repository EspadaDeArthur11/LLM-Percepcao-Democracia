import pyreadstat

# Ler os dados da pesquisa
df, meta = pyreadstat.read_sav("04832.SAV")

print(df)
print(meta)
