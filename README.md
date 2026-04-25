
# 🎥 Tufos Video Scraper & Downloader

Este projeto é um scraper automatizado desenvolvido em Python com o objetivo de estudar como plataformas de streaming organizam e distribuem seus vídeos através de CDN (Content Delivery Network).

O sistema foi construído para:

- Extrair informações de episódios a partir de HTML local
- Identificar padrões de URLs de vídeos
- Reconstruir links de mídia hospedados em CDN
- Automatizar downloads em massa
- Organizar arquivos de forma estruturada

---

# 🧠 Objetivo do projeto

Este projeto não é apenas um downloader.

Ele foi desenvolvido como um estudo prático de:

- Engenharia reversa de URLs
- Estruturação de mídia em plataformas web
- Automação de scraping com Python
- Multithreading para otimização de performance
- Manipulação de HTML com BeautifulSoup

O foco principal é entender como sistemas reais entregam conteúdo de vídeo.

---

# ⚠️ Aviso importante

Este projeto é exclusivamente educacional.

Ele demonstra técnicas de análise de estrutura web e automação, sem incentivo ao uso indevido ou violação de termos de serviços externos.

---

# 🌐 Como os vídeos são estruturados

Os vídeos seguem um padrão baseado em CDN:

https://tufos-assinantes.b-cdn.net/arquivos/atracao/
[HASH_ATRACAO]/
[ID_EPISODIO]/
videos/
[SLUG_ATRACAO]-[NUMERO]-[SLUG_EPISODIO]-desktop-tufoscombr.mp4

---

# 🔍 Exemplo real analisado

https://tufos-assinantes.b-cdn.net/arquivos/atracao/
0f28b5d49b3020afeecd95b4009adf4c/
EP02-1773237967/
videos/
os-caipiras-filminho-014-carrapato-no-bumbum-desktop-tufoscombr.mp4

---

# 🧩 Como cada parte é obtida

## 📦 Hash da atração
Encontrado dentro da tag de imagem no HTML:

.../atracao/0f28b5d49b3020afeecd95b4009adf4c/EP02-1773237967/...

---

## 🆔 ID do episódio

EP02-1773237967

Também presente na URL da imagem.

---

## 🎬 Slug da atração

Exemplo:

os-caipiras-filminho

Encontrado no link da série dentro do HTML.

---

## 📺 Slug do episódio

Exemplo:

carrapato-no-bumbum

Encontrado na URL do episódio.

---

## 🔢 Número do vídeo

Este valor NÃO aparece no HTML.

Ele é descoberto através de tentativa controlada:

- 1
- 01
- 001

O sistema testa variações até encontrar a URL válida.

---

# ⚡ Funcionalidades do projeto

## 🔎 Scraper HTML
- Lê arquivos locais (pagina1.html até paginaN.html)
- Extrai episódios automaticamente
- Filtra dados relevantes do DOM

## 🧠 Reconstrução de URLs
- Identifica padrões da CDN
- Monta URLs dinamicamente
- Testa múltiplos formatos de numeração

## ⚡ Multithreading
- Acelera buscas e downloads
- Permite execução paralela
- Usuário define quantidade de threads

## ⬇️ Downloader automático
- Baixa vídeos diretamente da CDN
- Usa streaming para evitar sobrecarga de memória
- Renomeia arquivos automaticamente

## 📁 Organização inteligente
- Cria pastas por série
- Organiza episódios automaticamente
- Remove caracteres inválidos de nomes

---

# 📁 Estrutura final gerada

videos/
  Os Caipiras Filminho/
    Cachaca De Alambique.mp4
    Tirando Leite Da Mimosa.mp4
    Carrapato No Bumbum.mp4

---

# 📊 Tecnologias utilizadas

- Python 3
- Requests
- BeautifulSoup
- ThreadPoolExecutor
- Regex
- TQDM

---

# 🚀 Fluxo do sistema

1. Lê arquivos HTML locais
2. Extrai episódios
3. Monta possíveis URLs
4. Testa existência na CDN
5. Confirma vídeo válido
6. Baixa arquivo
7. Organiza em pastas

---

# 🧠 Conceitos aplicados

- Web scraping estruturado
- Engenharia reversa de URL
- Pattern matching em HTML
- Concurrency (threads)
- File system automation
- CDN behavior analysis

---

# 📌 Observações técnicas

- O sistema depende de padrões consistentes da CDN
- Pequenas mudanças no site podem quebrar a lógica
- O número do vídeo é inferido, não explicitamente fornecido
- Hashes e IDs são essenciais para reconstrução da URL

---

# ⚠️ Segurança e análise do site

A estrutura observada indica:

- Uso de CDN pública para distribuição de vídeos
- URLs parcialmente previsíveis
- Metadados expostos no HTML
- Dependência de hashes para ocultação de acesso direto

Isso sugere um sistema com:

- Segurança baseada em ofuscação de URL
- Controle moderado de acesso
- Dependência do backend para validação real

---

# 🧪 Finalidade do projeto

Este projeto serve como:

- Estudo de scraping avançado
- Análise de sistemas de streaming
- Demonstração de automação com Python
- Experimento de engenharia reversa de mídia

---

# ⚠️ Disclaimer

Este projeto é apenas para fins educacionais e de pesquisa técnica.

Qualquer uso indevido é de total responsabilidade do usuário.
