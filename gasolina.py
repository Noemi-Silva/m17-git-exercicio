import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("gasolina.csv")

plt.figure(figsize=(10, 6))
sns.lineplot(x="dia", y="venda", data=df, marker="o")
plt.title("Preço médio da gasolina em São Paulo - Julho/2021")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.savefig("gasolina.png")
plt.close()
