import time
import numpy as np
import csv
import tracemalloc
from datetime import datetime
import os
from numba import njit

@njit
def ordenacao_cycle_sort(lista):
    n = len(lista)
    for inicio_ciclo in range(0, n - 1):
        item = lista[inicio_ciclo]
        pos = inicio_ciclo
        for i in range(inicio_ciclo + 1, n):
            if lista[i] < item:
                pos += 1
        if pos == inicio_ciclo:
            continue
        while item == lista[pos]:
            pos += 1
        lista[pos], item = item, lista[pos]
        while pos != inicio_ciclo:
            pos = inicio_ciclo
            for i in range(inicio_ciclo + 1, n):
                if lista[i] < item:
                    pos += 1
            while item == lista[pos]:
                pos += 1
            lista[pos], item = item, lista[pos]

def medir_tempo_memoria(funcao, lista):
    inicio = time.perf_counter()
    funcao(lista)
    fim = time.perf_counter()

    tempo_segundos = fim - inicio
    memoria_bytes = lista.nbytes  # Tamanho real da lista em bytes
    uso_memoria_mb = memoria_bytes / (1024 * 1024)

    return tempo_segundos, uso_memoria_mb

def gerar_melhor_caso(n):
    return np.arange(n)

def gerar_pior_caso(n):
    return np.arange(n - 1, -1, -1)

def gerar_caso_aleatorio(n):
    lista = np.arange(n)
    np.random.shuffle(lista)
    return lista

def salvar_resultados_csv(nome_algoritmo, n, tipo_caso, tempo, memoria):
    agora = datetime.now()
    data_str = agora.strftime("%Y-%m-%d")
    hora_str = agora.strftime("%H-%M-%S")

    nome_arquivo = 'cycle_sort.csv'
    escrever_cabecalho = not os.path.exists(nome_arquivo)
    with open(nome_arquivo, mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        if escrever_cabecalho:
            escritor.writerow(["Data", "Hora", "Algoritmo", "N", "Caso", "Tempo", "Memoria"])
        escritor.writerow([data_str, hora_str, nome_algoritmo, n, tipo_caso, f"{tempo:.6f}", f"{memoria:.6f}"])

def main():
    nome_algoritmo = "Cycle Sort"
    tamanhos_n = [100, 1000, 10000, 100000, 1000000, 10000000]

    for n in tamanhos_n:
        print(f"\nExecutando {nome_algoritmo} com N={n}")

        print("  Melhor caso...")
        melhor_caso = gerar_melhor_caso(n)
        tempo_melhor, memoria_melhor = medir_tempo_memoria(ordenacao_cycle_sort, melhor_caso.copy())
        salvar_resultados_csv(nome_algoritmo, n, "Melhor caso", tempo_melhor, memoria_melhor)

        print("  Pior caso...")
        pior_caso = gerar_pior_caso(n)
        tempo_pior, memoria_pior = medir_tempo_memoria(ordenacao_cycle_sort, pior_caso.copy())
        salvar_resultados_csv(nome_algoritmo, n, "Pior caso", tempo_pior, memoria_pior)

        print("  Caso médio (5 execuções aleatórias)...")
        tempos = []
        memorias = []
        for i in range(5):
            aleatorio = gerar_caso_aleatorio(n)
            tempo, memoria = medir_tempo_memoria(ordenacao_cycle_sort, aleatorio.copy())
            tempos.append(tempo)
            memorias.append(memoria)
            print(f"    Execução {i+1}: Tempo = {tempo:.6f}s, Memória = {memoria:.6f}MB")

        tempo_medio = sum(tempos) / len(tempos)
        memoria_media = sum(memorias) / len(memorias)
        salvar_resultados_csv(nome_algoritmo, n, "Caso medio", tempo_medio, memoria_media)

if __name__ == "__main__":
    main()
