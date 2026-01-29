import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv("gasolina.csv")

# Estilo do gráfico atualizado
sns.set_style("darkgrid")
plt.figure(figsize=(10,6))

sns.lineplot(x="dia", y="venda", data=df, marker="o", color="green")
plt.title("Preço médio da gasolina em São Paulo - Julho/2021 (Atualizado)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

plt.savefig("gasolina.png")
plt.close()

# Comentário final
# Gráfico atualizado salvo em "gasolina.png" na branch develop
