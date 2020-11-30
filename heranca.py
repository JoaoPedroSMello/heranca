class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprime(self):
        print(self.codigo, self.nome, self.matricula)


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprime(self):
        print(self.codigo, self.nome, self.matricula, self.ano)


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprime(self):
        print(self.codigo, self.nome, self.matricula, self.ano)


alunoGraduacao = AlunoGraduacao(1, "Joao", "ADS", 3)
alunoEnsinoMedio = AlunoEnsinoMedio(1, "Joao", "ADS", 3)
aluno = Aluno(1, "Joao", "ADS")
alunoGraduacao.imprime()
alunoEnsinoMedio.imprime()
aluno.imprime()