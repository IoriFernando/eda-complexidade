# Análise e Comparação de Algoritmos de Ordenação

Este projeto tem como objetivo realizar uma análise teórica e prática de três algoritmos de ordenação: **Cocktail Shaker Sort**, **Comb Sort** e **Cycle Sort**, destacando suas diferenças em **tempo de execução**, **consumo de memória** e **complexidade computacional**.

## 📌 Algoritmos Analisados

1. **Cocktail Shaker Sort**  
   - Variação do Bubble Sort com varreduras bidirecionais.
   - Melhora o desempenho em listas parcialmente ordenadas.
   - Complexidade:  
     - Melhor caso: `O(n)`  
     - Caso médio: `O(n²)`  
     - Pior caso: `O(n²)`

2. **Comb Sort**  
   - Baseado no Bubble Sort, mas usa gaps para comparar elementos distantes.
   - Reduz a quantidade de comparações nas fases iniciais.
   - Complexidade:  
     - Melhor caso: `O(n log n)`  
     - Caso médio: `O(n log n)`  
     - Pior caso: `O(n²)`

3. **Cycle Sort**  
   - Minimiza o número de movimentações.
   - Ideal quando escrita em memória tem custo elevado.
   - Complexidade:  
     - Melhor caso: `O(n²)`  
     - Caso médio: `O(n²)`  
     - Pior caso: `O(n²)`

## ⚙️ Critérios para Escolha dos Algoritmos

- Algoritmos com **complexidades diferentes** (pelo menos no melhor caso).
- Algoritmos com **diferenças significativas no consumo de memória e movimentação**.
- Abordagens variadas (gap, permutação cíclica, varredura dupla).
- Comparações baseadas em:
  - Tempo de execução.
  - Uso de memória.
  - Melhores, piores e casos médios.
  - Crescimento assintótico.

## 🧪 Estrutura dos Testes

### Entradas
- **N**: Quantidade de elementos a serem ordenados.
- **Algoritmo**: Um dos três algoritmos selecionados.

#### Valores de N utilizados:
100, 1.000, 10.000, 100.000, 1.000.000, 10.000.000

markdown
Copiar
Editar

### Casos testados para cada N
- ✅ **Melhor caso**: Lista já ordenada.
- ✅ **Pior caso**: Lista ordenada em ordem inversa.
- ✅ **Caso médio**: 5 execuções com listas aleatórias. Média dos resultados computada.

### Medidas coletadas
- ⏱ **Tempo de execução** (em segundos): Medido excluindo inicializações e I/O.
- 🧠 **Consumo de memória** (em MB): Medição do uso total durante a execução.

## 📁 Formato dos Arquivos

### Entrada
Arquivo contendo:
linha 1: N
linha 2: algoritmo

makefile
Copiar
Editar

Exemplo:
10000
Comb Sort

makefile
Copiar
Editar

### Saída (CSV)
Estrutura:
Data, Hora, Algoritmo, N, Caso, Tempo, Memória

makefile
Copiar
Editar

Exemplo:
2025-06-09, 17:50:13, Comb Sort, 10000, Caso médio, 112.134, 1024

mathematica
Copiar
Editar

## 📊 Comparação Final

| Algoritmo            | Melhor Caso | Pior Caso | Caso Médio | Memória |
|----------------------|-------------|-----------|------------|---------|
| Cocktail Shaker Sort | O(n)        | O(n²)     | O(n²)      | O(1)    |
| Comb Sort            | O(n log n)  | O(n²)     | O(n log n) | O(1)    |
| Cycle Sort           | O(n²)       | O(n²)     | O(n²)      | O(1)    |

## 📈 Complexidade (Linha a Linha)

Para cada algoritmo, foi realizada uma análise detalhada:

### Exemplo — Cocktail Shaker Sort

```python
while trocou:                  # Executado até não haver trocas → até O(n)
  for i in range(inicio, fim): # Laço de ida → O(n)
    if lista[i] > lista[i+1]:  # Comparação simples → O(1)
      troca(lista[i], lista[i+1]) # Troca condicional → O(1)
Resultado final: T(n) = n(n - 1) = O(n²)

Análises semelhantes foram feitas para o Comb Sort (com fator de redução do gap) e Cycle Sort (com permutação e controle de posição).
```

# 🖥️ Como Executar o Projeto
## ✅ Opção 1: Executar o script .py no PowerShell com Bypass e ambiente virtual
Abra o PowerShell como administrador e navegue até a pasta do projeto:

Permita execução com política Bypass (sem precisar alterar o sistema permanentemente):
```
powershell -ExecutionPolicy Bypass -File .\main.py
```
🔐 Obs.: isso evita erros como running scripts is disabled on this system.

### (Recomendado) Use um ambiente virtual:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Instale as dependências necessárias:
```
pip install numpy numba
```
## ✅ Opção 2: Executar a versão compilada .exe

Se preferir, você pode compilar o script para .exe e executá-lo diretamente, sem precisar de Python instalado.

Gere o .exe com PyInstaller:
```
pip install pyinstaller
pyinstaller --onefile main.py
```
O executável será criado na pasta dist/: <br>
Execute diretamente no PowerShell ou com duplo clique.

# 📦 Bibliotecas Utilizadas
O script depende das seguintes bibliotecas Python:
```python
import time
import numpy as np
import csv
from datetime import datetime
import os
from numba import njit
```
# 🔎 Conclusão
Este projeto apresenta uma visão abrangente dos algoritmos de ordenação em termos teóricos e práticos. A escolha do algoritmo ideal depende diretamente do contexto de uso — seja performance, memória ou número de escritas. Comb Sort mostrou-se o mais eficiente em casos médios; Cycle Sort, o que menos movimenta dados; e Cocktail Shaker, uma alternativa simples para listas quase ordenadas.
