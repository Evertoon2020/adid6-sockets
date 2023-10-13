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
    dados_entrada = conexao.recv(8)  # 8 bytes para dois inteiros de 4 bytes cada
    peso_atual, peso_desejado = int.from_bytes(dados_entrada[:4], byteorder='big'), int.from_bytes(dados_entrada[4:], byteorder='big')

    # Calcular o percentual dos pesos recebidos
    percentual = FuncoesServidor.calc_percentual(peso_atual, peso_desejado)

    # Definir stream de saída de dados do servidor
    conexao.sendall(struct.pack('!f',percentual))

    # Fechar a conexão
    conexao.close()

except ConnectionRefusedError:
    print("Erro: Não foi possível estabelecer a conexão.")
except Exception as e:
    print("Erro:", str(e))