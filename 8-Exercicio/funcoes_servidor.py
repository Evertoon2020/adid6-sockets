import sys

class FuncoesServidor:
    @staticmethod
    def calc_percentual(peso_atual, peso_desejado):
        try:
            if peso_atual <= 0 or peso_desejado <= 0:
                print("Os pesos devem ser valores positivos.")
                sys.exit()
            elif peso_atual <= peso_desejado:
                print("Você já atingiu ou está abaixo do peso desejado.")
                sys.exit()
            else:
                peso_a_eliminar = peso_atual - peso_desejado
                percentual = (peso_a_eliminar / peso_atual) * 100
                return percentual
        except Exception as e:
            print("Erro:", str(e))