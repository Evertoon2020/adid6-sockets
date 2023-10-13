import socket
import struct

try:
    # Abrir a conexão para cliente, na porta 1234
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 1234))

    # Enviar dados para o servidor
    despesas = float(input("Digite o total de despesas no restaurante: "))

    # Empacotar despesas como um número de ponto flutuante de 4 bytes (big-endian) e enviá-lo ao servidor
    dados_a_enviar = struct.pack('!f', despesas)
    cliente.sendall(dados_a_enviar)

    # Receber e mostrar o resultado do servidor
    total_bytes = cliente.recv(4) 
    total_a_pagar = struct.unpack('!f', total_bytes)[0]
    print("O total a ser pago com gorjeta é: R$", total_a_pagar)

    # Fechar conexão
    cliente.close()

except ConnectionRefusedError:
    print("Erro: Não foi possível conectar ao servidor.")
except ValueError:
    print("Erro: Entrada inválida.")
except Exception as e:
    print("Erro:", str(e))
