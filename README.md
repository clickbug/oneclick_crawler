# OneClick Crawler

O OneClick Crawler é uma ferramenta de linha de comando para rastrear links internos e externos em uma página da web, permitindo que você especifique a profundidade desejada para a coleta de links. O script usa BeautifulSoup para analisar o HTML da página e identificar os links.

## Requisitos

Antes de usar o OneClick Crawler, certifique-se de ter o Python 3 instalado em seu sistema e de ter instalado as seguintes bibliotecas:

- requests
- beautifulsoup4
- lxml

Você pode instalar as bibliotecas usando o gerenciador de pacotes pip:

```bash
pip install requests beautifulsoup4 lxml
bash´´´

Como usar

1. Clone este repositório ou baixe o arquivo "oneclick_crawler.py".
2. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo "oneclick_crawler.py" está localizado.
3. Execute o script fornecendo a URL de entrada, a profundidade desejada e a opção de saída (opcional) para salvar os links em arquivos.

Exemplo:

python oneclick_crawler.py https://exemplo.com/ 2 -o both


Isso rastreará a página https://exemplo.com/ até a profundidade 2 e salvará os links internos e externos em dois arquivos separados chamados links_intern.txt e links_extern.txt.

Para interromper o processo de rastreamento manualmente, pressione Ctrl + C.


Opções de saída
-o intern: Salva os links internos em um arquivo chamado links_intern.txt.
-o extern: Salva os links externos em um arquivo chamado links_extern.txt.
-o both (ou -o all): Salva todos os links (internos e externos) em um arquivo chamado all_links.txt.
Se você não especificar nenhuma opção de saída, os links não serão salvos em nenhum arquivo.

Licença
Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.



Certifique-se de substituir "https://exemplo.com/" pelo URL que você deseja rastrear em seus próprios exemplos.

Espero que este README.md seja útil para fornecer informações sobre o seu script OneClick Crawler e facilitar o uso e colaboração em seu projeto!
