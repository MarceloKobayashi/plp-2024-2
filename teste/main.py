class Matriz:
    def __init__(self, n_linhas, n_colunas):
        self.n_linhas = n_linhas
        self.n_colunas = n_colunas
        self.matriz = []

    def leia_matriz(self):
        for l in range(self.n_linhas):
            linha = []
            for c in range(self.n_colunas):
                numero = int(input(f"Digite o número colocado em {l}, {c}: "))
                linha.append(numero)

            self.matriz.append(linha)

        return self.matriz

    def imprima_matriz(self):
        for l in range(self.n_linhas):
            linha = []
            for c in range(self.n_colunas):
                linha.append(self.matriz[l][c])

            print_linha = f'\t'.join(str(numero) for numero in linha)
            print(print_linha)

    def simetrica(self):
        if self.n_linhas != self.n_colunas:
            print("\nO número de linhas e de colunas é diferente, não simétrica.")
            return False

        for l in range(self.n_linhas):
            for c in range(self.n_colunas):
                if self.matriz[l][c] != self.matriz[c][l]:
                    print("\nNúmeros opostos não são iguais, não simétrica.")
                    return False

        print("\nA matriz é simétrica.")
        return True

    def multiplica_matriz(self, outra_matriz):
        if self.n_colunas != outra_matriz.n_linhas:
            print("Não é possível fazer a multiplicação.")
            return

        matriz_resultado = [[0] * outra_matriz.n_colunas for _ in range(self.n_linhas)]

        for i in range(self.n_linhas):
            for j in range(outra_matriz.n_colunas):
                soma = 0
                for k in range(self.n_colunas):
                    soma += self.matriz[i][k] * outra_matriz.matriz[k][j]
                matriz_resultado[i][j] = soma

        resultado = Matriz(self.n_linhas, outra_matriz.n_colunas)
        resultado.matriz = matriz_resultado

        return resultado


if __name__ == "__main__":
    linhas_a = int(input("Digite o número de linhas da sua matriz: "))
    colunas_a = int(input("Digite o número de colunas da sua matriz: "))

    a_mat = Matriz(linhas_a, colunas_a)
    a_mat.leia_matriz()
    a_mat.imprima_matriz()
    # a_mat.simetrica()

    linhas_b = int(input("\nDigite o número de linhas da sua matriz: "))
    colunas_b = int(input("Digite o número de colunas da sua matriz: "))
    b_mat = Matriz(linhas_b, colunas_b)
    b_mat.leia_matriz()
    b_mat.imprima_matriz()

    try:
        mult_matriz = a_mat.multiplica_matriz(b_mat)
        print("\n")
        mult_matriz.imprima_matriz()
    except ValueError as e:
        print(e)
