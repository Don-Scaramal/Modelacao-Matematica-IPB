import matplotlib.pyplot as plt
import numpy as np

# Dados experimentais ajustados
tensoes = np.array([0.5, 2.5, 4.8, 8.6])  # V
correntes = np.array([139, 130, 115, 80])  # mA

# Converter corrente para A (opcional, mas mantemos em mA para legibilidade)
correntes_ma = correntes

# Calcular potência (P = V * I) em mW
potencias = tensoes * correntes_ma

# Criar figura com dois subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico I x V
ax1.plot(tensoes, correntes_ma, 'bo-', linewidth=2, markersize=8)
ax1.set_xlabel('Tensão (V)', fontsize=12)
ax1.set_ylabel('Corrente (mA)', fontsize=12)
ax1.set_title('Curva I x V - Módulo Fotovoltaico', fontsize=14)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 160)

# Destacar o MPP no gráfico I x V
ax1.plot(8.6, 80, 'ro', markersize=10, label='MPP (8,6 V; 80 mA)')
ax1.legend()

# Gráfico P x V
ax2.plot(tensoes, potencias, 'gs-', linewidth=2, markersize=8)
ax2.set_xlabel('Tensão (V)', fontsize=12)
ax2.set_ylabel('Potência (mW)', fontsize=12)
ax2.set_title('Curva P x V - Ponto de Máxima Potência', fontsize=14)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 800)

# Destacar o MPP no gráfico P x V
ax2.plot(8.6, 688, 'ro', markersize=10, label=f'MPP: 688 mW')
ax2.legend()

# Adicionar anotações
ax2.annotate(f'MPP\n(8,6V; 688mW)', xy=(8.6, 688), xytext=(5, 600),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=10)

plt.tight_layout()
plt.show()

# Valores em tabela
print('='*50)
print('Tabela de valores medidos:')
print('='*50)
print(f"{'Tensão (V)':<12} {'Corrente (mA)':<15} {'Potência (mW)':<15}")
print('-'*42)
for v, i, p in zip(tensoes, correntes_ma, potencias):
    print(f"{v:<12} {i:<15} {p:<15.1f}")
print('='*50)
print(f'Ponto de Máxima Potência (MPP): 8,6 V / 80 mA → {potencias[3]:.0f} mW')
