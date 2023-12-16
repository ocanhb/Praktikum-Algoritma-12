import pandas as pd

df = pd.read_csv("negara.csv", index_col=0)
mean = df.groupby(['Benua']).mean(numeric_only=True)
std = df.groupby(["Benua"]).std(numeric_only=True)

print("berikut data framenya : ")
print(df, '\n')

print("berikut data meannya: ")
print(mean, '\n')

print("berikut data standar deviasinya")
print(std, '\n')