import socket
import struct

try:
    # Abrir a conexão para cliente, na porta 1234
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 1234))

    # Enviar dados para o servidor
    valor = float(input("Digite o valor total do produto: "))

    # Empacotar valor como um número de ponto flutuante de 4 bytes (big-endian) e enviá-lo ao servidor
    dados_a_enviar = struct.pack('!f', valor)
    cliente.sendall(dados_a_enviar)

    # Receber e mostrar o resultado do servidor
    total_bytes = cliente.recv(4) 
    novo_valor_total = struct.unpack('!f', total_bytes)[0]
    print("O novo valor total da venda a ser pago com acrescimo de 25% é: R$", novo_valor_total)

    # Fechar conexão
    cliente.close()

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor.")
except ValueError:
    print("Erro: Entrada inválida.")
except Exception as e:
    print("Erro:", str(e))
