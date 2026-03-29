Este projeto consiste em:

sender.py: Criptografa o arquivo e envia para o servidor.
receiver.py: Recebe o arquivo criptografado, descriptografa e salva localmente.
generate_key.py: Script auxiliar para teste de criptografia e descriptografia AES.

É necessário ter instaladas as bibliotecas pycryptodome (para criptografia AES) e tqdm (para exibir a barra de progresso).

Uso:

1-Execute primeiro o receiver: ele ficará escutando em localhost:9998.

2-Em outro terminal, execute o sender: ele envia o arquivo chamado “file” criptografado. O receiver o descriptografa e o salva localmente como “file.txt”.

Observação: utilize chaves aleatórias para aumentar a segurança.
