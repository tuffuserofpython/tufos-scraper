import os
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- CONFIG ---
NOME_ARQUIVO_SAIDA = "videos_encontrados.txt"
PASTA_VIDEOS = "videos"
ARQUIVOS_HTML = [f"pagina{i}.html" for i in range(1, 8)]
RANGE_TENTATIVAS = (1, 101)

BASE_CDN = "https://tufos-assinantes.b-cdn.net/arquivos/atracao/"
SUFIXO_VIDEO = "-desktop-tufoscombr.mp4"


# ---------------- UTIL ----------------
def nome_seguro(nome):
    return re.sub(r'[\\/*?:"<>|]', "", nome)


# ---------------- HTML ----------------
def extrair_dados_dos_html(arquivos):
    episodios = []
    print("🔎 Lendo HTML...")

    for arq in arquivos:
        if not os.path.exists(arq):
            continue

        with open(arq, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        for item in soup.find_all("li", class_="itemEpisodio"):
            link_ep = item.select_one("a.titulo")
            img = item.select_one("img.lazy")
            link_atr = item.select_one("a.linkAtracao")

            if not all([link_ep, img, link_atr]):
                continue

            m1 = re.search(r"/episodio/([^/]+)/", link_ep["href"])
            m2 = re.search(r"/atracoes/([^/]+)/", link_atr["href"])
            m3 = re.search(r"/atracao/([a-f0-9]+)/([A-Z0-9\-]+)/", img.get("data-original", "") or img.get("src", ""))

            if not (m1 and m2 and m3):
                continue

            episodios.append({
                "titulo": link_ep.get("title", "Sem Título"),
                "slug_episodio": m1.group(1),
                "slug_atracao": m2.group(1),
                "hash_atracao": m3.group(1),
                "id_ep_com_hash": m3.group(2)
            })

    print(f"✅ Episódios encontrados: {len(episodios)}")
    return episodios


# ---------------- BUSCA URL COM PROGRESSO ----------------
def encontrar_url(episodio, lock_print):
    titulo = episodio["titulo"]

    for i in range(RANGE_TENTATIVAS[0], RANGE_TENTATIVAS[1]):
        formatos = [str(i), f"{i:02d}", f"{i:03d}"]

        for num in formatos:
            nome_video = f"{episodio['slug_atracao']}-{num}-{episodio['slug_episodio']}{SUFIXO_VIDEO}"
            url = f"{BASE_CDN}{episodio['hash_atracao']}/{episodio['id_ep_com_hash']}/videos/{nome_video}"

            with lock_print:
                print(f"🔄 [{titulo}] tentando: {num}")

            try:
                r = requests.head(url, timeout=5)
                if r.status_code == 200:
                    with lock_print:
                        print(f"✔ ENCONTRADO: {titulo}")
                    return url, titulo

            except:
                pass

    with lock_print:
        print(f"❌ FALHA AO ENCONTRAR: {titulo}")

    return None


# ---------------- DOWNLOAD ----------------
def baixar_video(item, lock_print):
    if not item:
        return

    url, titulo = item
    nome = nome_seguro(titulo) + ".mp4"
    caminho = os.path.join(PASTA_VIDEOS, nome)

    if os.path.exists(caminho):
        return

    try:
        r = requests.get(url, stream=True, timeout=10)
        total = int(r.headers.get("content-length", 0))

        with open(caminho, "wb") as f, tqdm(
            desc=f"⬇ {nome}",
            total=total,
            unit="B",
            unit_scale=True,
            leave=False
        ) as bar:

            for chunk in r.iter_content(1024):
                f.write(chunk)
                bar.update(len(chunk))

        with lock_print:
            print(f"✔ DOWNLOAD OK: {nome}")

    except Exception as e:
        with lock_print:
            print(f"❌ ERRO DOWNLOAD {nome}: {e}")


# ---------------- MAIN ----------------
def main(episodios):
    os.makedirs(PASTA_VIDEOS, exist_ok=True)

    threads = int(input("⚡ Quantos threads quer usar? "))

    from threading import Lock
    lock_print = Lock()

    resultados = []

    print("\n🚀 INICIANDO BUSCA...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(encontrar_url, ep, lock_print): ep for ep in episodios}

        for f in tqdm(as_completed(futures), total=len(futures), desc="Progresso geral"):
            res = f.result()
            if res:
                resultados.append(res)

                with open(NOME_ARQUIVO_SAIDA, "a", encoding="utf-8") as arq:
                    arq.write(res[0] + "\n")

    print("\n⬇ INICIANDO DOWNLOADS...\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        list(tqdm(
            executor.map(lambda x: baixar_video(x, lock_print), resultados),
            total=len(resultados),
            desc="Downloads"
        ))

    print("\n🎉 FINALIZADO!")


# ---------------- RUN ----------------
if __name__ == "__main__":
    dados = extrair_dados_dos_html(ARQUIVOS_HTML)
    main(dados)