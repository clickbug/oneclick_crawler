# OneClick Crawler

O OneClick Crawler é uma ferramenta de linha de comando para rastrear links internos e externos em uma página da web, permitindo que você especifique a profundidade desejada para a coleta de links. O script usa BeautifulSoup para analisar o HTML da página e identificar os links.

## Requisitos

Antes de usar o OneClick Crawler, certifique-se de ter o Python 3 instalado em seu sistema e de ter instalado as seguintes bibliotecas:

- requests
- beautifulsoup4
- lxml

Você pode instalar as bibliotecas usando o gerenciador de pacotes pip:

~~~
pip install requests beautifulsoup4 lxml
~~~

## Como usar
1 - Clone este repositório ou baixe o arquivo "oneclick_crawler.py".
2 - Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo "oneclick_crawler.py" está localizado.
3 - Execute o script fornecendo a URL de entrada, a profundidade desejada e a opção de saída (opcional) para salvar os links em arquivos. Você também pode especificar o caminho e o nome do arquivo de saída usando o parâmetro -f ou --file.

##Exemplo:
~~~
python oneclick_crawler.py https://exemplo.com/ 2 -o both -f caminho_do_arquivo.txt
~~~

Isso rastreará a página https://exemplo.com/ até a profundidade 2 e salvará os links internos e externos em um arquivo chamado caminho_do_arquivo.txt. Se você não fornecer o parâmetro -f, os links serão salvos nos arquivos padrão (links_intern.txt, links_extern.txt ou all_links.txt).

Para interromper o processo de rastreamento manualmente, pressione Ctrl + C.

## Opções de saída
-o intern: Salva os links internos em um arquivo chamado links_intern.txt.
-o extern: Salva os links externos em um arquivo chamado links_extern.txt.
-o both (ou -o all): Salva todos os links (internos e externos) em um arquivo chamado all_links.txt.
Se você não especificar nenhuma opção de saída, os links não serão salvos em nenhum arquivo.

## Nota importante

Esta ferramenta foi desenvolvida apenas para fins educacionais e para uso por pessoas que participam de programas de bug bounty ou outros programas de segurança. O uso desta ferramenta em ambientes de produção ou em sistemas sem o consentimento prévio da empresa ou proprietário dos recursos é estritamente proibido. O autor não assume qualquer responsabilidade pelo uso indevido desta ferramenta.


## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.
