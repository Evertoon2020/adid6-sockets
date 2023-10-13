import socket
import struct

try:
    # Abrir a conexão para cliente, na porta 1234
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 1234))

    # Enviar dados para o servidor
    peso_atual = int(input("Digite seu peso atual em kg: "))
    peso_desejado = int(input("Digite o peso dejado em kg: "))

    # Empacotar os números como inteiros de 4 bytes (big-endian) e enviá-los ao servidor
    dados_a_enviar = struct.pack('>II', peso_atual, peso_desejado)
    cliente.sendall(dados_a_enviar)

    # Receber e mostrar o resultado do servidor
    resultado_bytes = cliente.recv(4)
    resultado = struct.unpack('!f', resultado_bytes)[0]
    print("O percentual de peso a ser perdido é de: {:.0f}%".format(resultado))

    # Fechar conexão
    cliente.close()

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor.")
except ValueError:
    print("Erro: Entrada inválida.")
except Exception as e:
    print("Erro:", str(e))
