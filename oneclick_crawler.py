import signal
import sys
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
import argparse

links_intern = set()
links_extern = set()

def is_valid_url(url):
    """
    Verifica se a URL é válida, não vazia e contém apenas caracteres válidos.
    """
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc) and bool(parsed_url.path)

def level_crawler(input_url, current_depth, max_depth):
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc

    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml"
    )

    for anchor in beautiful_soup_object.find_all("a"):
        href = anchor.attrs.get("href")
        if href and is_valid_url(href):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            if current_url_domain not in href and href not in links_extern:
                print("Extern - {}".format(href))
                links_extern.add(href)

            if current_url_domain in href and href not in links_intern:
                print("Intern - {}".format(href))
                links_intern.add(href)
                temp_urls.add(href)

    if current_depth < max_depth:
        for url in temp_urls:
            level_crawler(url, current_depth + 1, max_depth)

def save_links_to_file(links, file_path):
    with open(file_path, "w") as file:
        for link in links:
            file.write(link + "\n")

def signal_handler(signal, frame):
    print("Rastreamento interrompido manualmente.")
    if links_intern or links_extern:
        save_links_to_file(links_intern, "url_intern.txt")
        save_links_to_file(links_extern, "url_extern.txt")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description="Ferramenta de rastreamento de links.")
    parser.add_argument("url", help="URL de entrada para iniciar o rastreamento.")
    parser.add_argument("depth", type=int, help="Profundidade desejada para o rastreamento.")
    parser.add_argument("-o", "--output", default=None,
                        help="Salvar links internos, externos ou ambos em um unico arquivo ou arquivos diferentes. "
                             "Escolha 'intern', 'extern', 'all', 'both' ou não especifique para não salvar.")
    parser.add_argument("-f", "--file", default=None,
                        help="Caminho e nome do arquivo para salvar os links (opcional).")

    args = parser.parse_args()

    input_url = args.url
    depth = args.depth

    if depth < 0:
        print("Profundidade inválida. Deve ser maior ou igual a 0.")
    else:
        level_crawler(input_url, 1, depth)

        if args.output:
            if args.output == "intern":
                save_links_to_file(links_intern, args.file or "url_intern.txt")
            elif args.output == "extern":
                save_links_to_file(links_extern, args.file or "url_extern.txt")
            elif args.output == "all":
                all_url = links_intern.union(links_extern)
                save_links_to_file(all_url, args.file or "all_url.txt")
            elif args.output == "both":
                save_links_to_file(links_intern, "intern_" + args.file or "url_intern.txt")
                save_links_to_file(links_extern, "extern_" + args.file or "url_extern.txt")
