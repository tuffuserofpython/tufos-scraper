import os
import re
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

ARQUIVO = "videos_encontrados.txt"
PASTA_BASE = "videos"

lock = Lock()


# ---------------- LIMPEZA DE NOMES ----------------
def limpar_nome(nome):
    nome = nome.replace("-", " ").replace("_", " ")
    nome = re.sub(r"\s+", " ", nome).strip()
    return nome.title()


# ---------------- EXTRAIR INFO DA URL ----------------
def extrair_info(url):
    parts = urlparse(url).path.split("/")

    # pega nome da série pelo slug da atração
    try:
        serie_slug = parts[4]  # ex: os-caipiras-filminho
    except:
        serie_slug = "Desconhecido"

    serie = limpar_nome(serie_slug.split("-filminho")[0])

    # nome do arquivo
    filename = parts[-1].replace("-desktop-tufoscombr.mp4", "")
    episodio_nome = limpar_nome(filename.split(serie_slug)[0])

    return serie, episodio_nome


# ---------------- DOWNLOAD ----------------
def baixar(url):
    try:
        serie, episodio = extrair_info(url)

        pasta = os.path.join(PASTA_BASE, serie)
        os.makedirs(pasta, exist_ok=True)

        caminho = os.path.join(pasta, f"{episodio}.mp4")

        if os.path.exists(caminho):
            with lock:
                print(f"⏩ Já existe: {episodio}")
            return

        r = requests.get(url, stream=True, timeout=15)

        if r.status_code != 200:
            with lock:
                print(f"❌ FALHA: {episodio}")
            return

        with open(caminho, "wb") as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)

        with lock:
            print(f"✔ BAIXADO: {serie} -> {episodio}")

    except Exception as e:
        with lock:
            print(f"❌ ERRO: {url} | {e}")


# ---------------- MAIN ----------------
def main():
    if not os.path.exists(ARQUIVO):
        print("Arquivo videos_encontrados.txt não encontrado")
        return

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    threads = int(input("⚡ Quantos threads quer usar? "))

    print(f"\n🚀 Baixando {len(urls)} vídeos...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(baixar, urls)

    print("\n🎉 Finalizado!")


if __name__ == "__main__":
    main()