Este projeto permite executar uma calculadora em Python através de scripts em Bash. Os arquivos execod.txt e comman.sh configuram e rodam a calculadora de maneira interativa.

Arquivos e Funções
comman.sh: É o script principal que interage com o usuário e executa a calculadora (calc.py). Primeiro, ele solicita o nome do usuário, exibe uma saudação e verifica se o arquivo calc.py está disponível no mesmo diretório.
Se o arquivo existe, ele o executa com python3 calc.py. Ao término, o script agradece o usuário. Se calc.py não for encontrado, exibe uma mensagem de erro.
execod.txt: Um script auxiliar que configura as permissões para comman.sh, tornando-o executável e permitindo gravação apenas para o usuário. Após a configuração, execod.txt automaticamente executa comman.sh.
Como Usar
Coloque os arquivos execod.txt, comman.sh e calc.py no mesmo diretório.
Certifique-se de que execod.txt e comman.sh têm permissão de execução usando: chmod +x execod.txt comman.sh
Para iniciar, execute o arquivo execod.txt use: ./execod.txt

