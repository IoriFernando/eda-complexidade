import time
import numpy as np
import csv
from datetime import datetime
import os
from numba import njit

# --- Algoritmos de ordenação ---

@njit
def ordenacao_cocktail_shaker(lista):
    n = len(lista)
    trocou = True
    inicio = 0
    fim = n - 1
    while trocou:
        trocou = False
        for i in range(inicio, fim):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True
        if not trocou:
            break
        trocou = False
        fim -= 1
        for i in range(fim - 1, inicio - 1, -1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                trocou = True
        inicio += 1


@njit
def ordenacao_comb_sort(lista):
    n = len(lista)
    intervalo = n
    reducao = 1.3
    ordenado = False
    while not ordenado:
        intervalo = int(intervalo / reducao)
        if intervalo <= 1:
            intervalo = 1
            ordenado = True
        i = 0
        while i + intervalo < n:
            if lista[i] > lista[i + intervalo]:
                lista[i], lista[i + intervalo] = lista[i + intervalo], lista[i]
                ordenado = False
            i += 1

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

    nome_arquivo = 'ResultadosObitidos.csv'
    escrever_cabecalho = not os.path.exists(nome_arquivo)

    with open(nome_arquivo, mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        if escrever_cabecalho:
            escritor.writerow(["Data", "Hora", "Algoritmo", "N", "Caso", "Tempo", "Memoria"])
        escritor.writerow([data_str, hora_str, nome_algoritmo, n, tipo_caso, f"{tempo:.6f}", f"{memoria:.6f}"])


def main():
    algoritmos = {
        "Cocktail Shaker Sort": ordenacao_cocktail_shaker,
        "Comb Sort": ordenacao_comb_sort,
        "Cycle Sort": ordenacao_cycle_sort
    }

    print("=== Benchmark de Algoritmos de Ordenação ===")

    try:
        n = int(input("1. Quantidade de números para ordenar (ex: 10000): "))
    except ValueError:
        print("Entrada inválida para N. Encerrando.")
        return

    print("\n2. Algoritmos disponíveis:")
    for i, nome in enumerate(algoritmos, start=1):
        print(f"   {i}. {nome}")

    escolha = input("Escolha o algoritmo pelo nome exato (copie/cole): ").strip()

    if escolha not in algoritmos:
        print("Algoritmo não reconhecido.")
        return

    nome_alg = escolha
    funcao_ordenacao = algoritmos[nome_alg]

    print(f"\nExecutando {nome_alg} com N={n}")

    print("  Melhor caso...")
    melhor_caso = gerar_melhor_caso(n)
    tempo_melhor, memoria_melhor = medir_tempo_memoria(funcao_ordenacao, melhor_caso.copy())
    salvar_resultados_csv(nome_alg, n, "Melhor caso", tempo_melhor, memoria_melhor)

    print("  Pior caso...")
    pior_caso = gerar_pior_caso(n)
    tempo_pior, memoria_pior = medir_tempo_memoria(funcao_ordenacao, pior_caso.copy())
    salvar_resultados_csv(nome_alg, n, "Pior caso", tempo_pior, memoria_pior)

    print("  Caso médio (5 execuções aleatórias)...")
    tempos = []
    memorias = []
    for i in range(5):
        aleatorio = gerar_caso_aleatorio(n)
        tempo, memoria = medir_tempo_memoria(funcao_ordenacao, aleatorio.copy())
        tempos.append(tempo)
        memorias.append(memoria)
        print(f"    Execução {i+1}: Tempo = {tempo:.6f}s, Memória = {memoria:.6f}MB")

    tempo_medio = sum(tempos) / len(tempos)
    memoria_media = sum(memorias) / len(memorias)
    salvar_resultados_csv(nome_alg, n, "Caso medio", tempo_medio, memoria_media)


if __name__ == "__main__":
    main()
