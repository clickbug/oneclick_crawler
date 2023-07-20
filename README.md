
</head>
<body>
    <h1>OneClick Crawler</h1>
    <p>
        O OneClick Crawler é uma ferramenta de linha de comando para rastrear links internos e externos em uma página da web, permitindo que você especifique a profundidade desejada para a coleta de links. 
        O script usa BeautifulSoup para analisar o HTML da página e identificar os links.
    </p>
</body>
<body>
    <h2>Requisitos</h2>
    <p>
        Antes de usar o OneClick Crawler, certifique-se de ter o Python 3 instalado em seu sistema e de ter instalado as seguintes bibliotecas:
    </p>
    <ul>
        <li>requests</li>
        <li>beautifulsoup4</li>
        <li>lxml</li>
    </ul>
    <p>
        Você pode instalar as bibliotecas usando o gerenciador de pacotes pip:
    </p>
    <pre><code>pip install requests beautifulsoup4 lxml</code></pre>
</body>
<body>
    <h2>Como usar</h2>
    <ol>
        <li>Clone este repositório ou baixe o arquivo "oneclick_crawler.py".</li>        
          <li>Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo "oneclick_crawler.py" está localizado.</li>
          <li>Execute o script fornecendo a URL de entrada, a profundidade desejada e a opção de saída (opcional) para salvar os links em arquivos.</li>      
    </ol>
    <p>Obs: Você também pode especificar o caminho e o nome do arquivo de saída usando o parâmetro -f ou --file.</p>
</body>
<body>
    <h2>Exemplo:</h2>
    <p>Ex: <code>python oneclick_crawler.py https://exemplo.com/  2  -o all -f caminho_do_arquivo.txt</code></p>
    <p>
        Isso rastreará a página https://exemplo.com/ até a profundidade 2 e salvará os links internos e externos em um arquivo chamado caminho_do_arquivo.txt.
        Se você não fornecer o parâmetro -f, os links serão salvos nos arquivos padrão (url_intern.txt, url_extern.txt ou all_url.txt).
    </p>
    <p>Para interromper o processo de rastreamento manualmente, pressione Ctrl + C.</p>
</body>
<body>
    <h2>Opções de saída</h2>
    <ul>
        <li>-o intern: Salva os links internos em um arquivo chamado url_intern.txt.</li>
        <li>-o extern: Salva os links externos em um arquivo chamado url_extern.txt.</li>
        <li>-o all: Salva todos os links (internos e externos) em um arquivo chamado all_url.txt.</li>
			  <li>-o both: Salva todos os links (internos e externos) em um arquivo diferentes.</li> <br>
					<p>
						Sem o parâmetro -f será salvo como:<br>
							-> url_intern.txt <br>
							-> url_extern.txt <br><br>
						Com parâmetro -f savará com o nome informado + (intern_ e extern_ ).<br><br>
								EX:  python oneclick_crawler.py https://exemplo.com/  2  -o both -f arquivo.txt <br>
								-> intern_arquivo.txt <br>
								-> extern_arquivo.txt
					</p>
        <li>Se você não especificar nenhuma opção de saída, os links não serão salvos em nenhum arquivo.</li>
    </ul>
</body>
<body>
    <h2>Nota importante</h2>
    <p>
        Esta ferramenta foi desenvolvida apenas para fins educacionais e para uso por pessoas que participam de programas de bug bounty ou outros programas de segurança.
        O uso desta ferramenta em ambientes de produção ou em sistemas sem o consentimento prévio da empresa ou proprietário dos recursos é estritamente proibido.
        O autor não assume qualquer responsabilidade pelo uso indevido desta ferramenta.
    </p>
</body>
    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter mais detalhes.</p>
</body>
</html>
