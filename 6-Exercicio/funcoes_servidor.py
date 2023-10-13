class FuncoesServidor:
    @staticmethod
    def calc_com_gorjeta(x):
        # Recebe o total e calcula a gorjeta (10% do valor)
        total = sum(x) + (sum(x) * 0.1)
        return total