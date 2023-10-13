class FuncoesServidor:
    @staticmethod
    def calc_somatorio(x, y):
        soma = 0
        # Garantir que x seja menor ou igual a y para evitar loops infinitos
        # Loop para x
        for i in range(1, y + 1):
            if i % 2 == 0:
                soma += i
        
        # Loop para y
        for i in range(1, x + 1):
            if i % 2 == 0:
                soma += i
        
        return soma