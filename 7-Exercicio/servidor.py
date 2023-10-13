import socket
import struct

from funcoes_servidor import FuncoesServidor

try:
    # Definir o socket do servidor (abrir porta de conexão)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 1234))
    servidor.listen(1)
    print("Servidor esperando conexão na porta 1234")

    # Aguardar solicitação de conexão do cliente
    conexao, endereco_cliente = servidor.accept()
    print("Cliente", endereco_cliente, "conectado")

    # Definir stream de entrada de dados no servidor
    dados_entrada = conexao.recv(4)  # Receber dados do cliente (4 bytes para float)
    valor = struct.unpack('!f', dados_entrada)[0]  # Interpretar dados como um número de ponto flutuante

    #Calcular a somatória do novo valor da venda
    novo_valor  = FuncoesServidor.calc_novo_valor_venda([valor])

    # Definir stream de saída de dados do servidor
    conexao.sendall(struct.pack('!f', novo_valor))  # Enviar novo valor total da venda de volta ao cliente

    # Fechar a conexão
    conexao.close()

except ConnectionRefusedError:
    print("Erro: Não foi possível estabelecer a conexão.")
except Exception as e:
    print("Erro:", str(e))