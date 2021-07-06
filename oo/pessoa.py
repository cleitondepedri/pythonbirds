class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    cleiton = Pessoa(nome='Cleiton')
    felipe = Pessoa(cleiton, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(id(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
        print(filho.nome)
    felipe.sobrenome = 'Pedri'
    del felipe.filhos
    felipe.olhos = 1
    del felipe.olhos
    print(felipe.__dict__)
    print(cleiton.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(felipe.olhos)
    print(cleiton.olhos)
    print(id(Pessoa.olhos), id(felipe.olhos), id(cleiton.olhos))












