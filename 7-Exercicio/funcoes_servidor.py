class FuncoesServidor:
    @staticmethod
    def calc_novo_valor_venda(x):
        # Recebe o total e calcula com o aumento (25% do valor)
        total = sum(x) + (sum(x) * 0.25)
        return total