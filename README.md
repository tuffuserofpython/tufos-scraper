```md
# 🎥 Tufos Video Scraper & Downloader

Este projeto é um **scraper automatizado de vídeos da plataforma Tufos**, desenvolvido em Python, que permite extrair, localizar e baixar vídeos hospedados em uma CDN a partir de arquivos HTML locais.

Ele foi criado com foco em estudo de:

- Web scraping
- Engenharia reversa de URLs
- Automação com Python
- Multithreading
- Processamento de HTML

---

# ⚠️ Aviso importante

Este projeto é **apenas para fins educacionais e de pesquisa técnica**.

Ele demonstra como estruturas de sites podem ser analisadas e automatizadas, sem qualquer intenção de uso comercial ou violação de termos de serviço.

---

# 🧠 Como o sistema funciona

O scraper analisa páginas HTML salvas localmente e extrai informações dos episódios, como:

- Nome da atração (série)
- Nome do episódio
- Hash da atração
- ID interno do episódio
- Slugs de URL

Com esses dados, ele tenta reconstruir URLs de vídeos hospedados em uma CDN.

---

# 🔗 Estrutura da URL analisada

Os vídeos seguem um padrão semelhante a:

```

[https://tufos-assinantes.b-cdn.net/arquivos/atracao/](https://tufos-assinantes.b-cdn.net/arquivos/atracao/)
[HASH_DA_ATRACAO]/
[ID_EPISODIO]/
videos/
[SLUG_ATRACAO]-[NUMERO]-[SLUG_EPISODIO]-desktop-tufoscombr.mp4

```

---

# 🔍 Exemplo real de vídeo

```

[https://tufos-assinantes.b-cdn.net/arquivos/atracao/](https://tufos-assinantes.b-cdn.net/arquivos/atracao/)
0f28b5d49b3020afeecd95b4009adf4c/
EP02-1773237967/
videos/
os-caipiras-filminho-014-carrapato-no-bumbum-desktop-tufoscombr.mp4

```

---

# 🧩 Como os dados são obtidos

## 📌 Hash da atração
Encontrado na tag `<img>`:

```

.../atracao/0f28b5d49b3020afeecd95b4009adf4c/EP02-1773237967/...

```

---

## 📌 ID do episódio

Também presente na URL da imagem:

```

EP02-1773237967

```

---

## 📌 Slug da atração

Encontrado no link da série:

```

/atracoes/os-caipiras-filminho/141/

```

---

## 📌 Slug do episódio

Encontrado no link do episódio:

```

/episodio/carrapato-no-bumbum/2412/

```

---

## 📌 Número do vídeo

Este valor não aparece diretamente no HTML.

Ele é descoberto por tentativa (ex: 1, 01, 001).

---

# ⚙️ Funcionalidades

- 🔎 Leitura de HTML local
- 🧠 Construção dinâmica de URLs
- ⚡ Multithreading (busca e download)
- ⬇️ Download automático de vídeos
- 📁 Organização por série e episódio
- 📊 Logs de status (ENCONTRADO / FALHA)

---

# 📁 Estrutura final dos arquivos

```

videos/
Os Caipiras Filminho/
Carrapato No Bumbum.mp4
Cachaca De Alambique.mp4
Tirando Leite Da Mimosa.mp4

```

---

# 🌐 O Tufos é seguro?

Com base na análise técnica das URLs e da arquitetura observada, alguns pontos podem ser considerados:

### 📌 1. Uso de CDN pública
Os vídeos são entregues via CDN (`b-cdn.net`), o que indica:

- Distribuição de conteúdo em servidores externos
- Possível uso de links diretos acessíveis via URL

---

### 📌 2. URLs previsíveis
As URLs seguem um padrão estruturado e parcialmente previsível, o que sugere:

- Ausência de proteção forte contra enumeração de arquivos
- Possível dependência de ofuscação por IDs e hashes

---

### 📌 3. Exposição de metadados no HTML
O HTML contém informações como:

- Slugs
- IDs internos
- Estrutura de episódios

Isso facilita automação e scraping.

---

### 📌 4. Controle de acesso não visível neste contexto
Não é possível afirmar autenticação interna apenas pela análise da CDN.

---

## ⚠️ Conclusão sobre segurança

Com base apenas na engenharia reversa observada:

- O sistema parece ter **proteção moderada baseada em URL e hashes**
- A estrutura permite automação se padrões forem descobertos
- Não há evidência suficiente para classificar como “inseguro” ou “seguro” de forma absoluta

👉 Portanto, a segurança depende mais da camada de autenticação do site principal do que da CDN em si.

---

# 🧠 Tecnologias usadas

- Python
- Requests
- BeautifulSoup
- ThreadPoolExecutor
- TQDM

---

# 🚀 Objetivo do projeto

Este projeto foi criado para demonstrar:

- Como sites estruturam entrega de mídia
- Como URLs podem ser analisadas e reconstruídas
- Como automação pode acelerar downloads em lote
- Como scraping pode ser otimizado com multithreading

---

# ⚠️ Disclaimer

Este projeto é apenas para fins educacionais e de estudo técnico.

O uso indevido pode violar termos de serviços de terceiros.
```
