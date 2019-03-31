class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    Luciano = Pessoa(renzo,nome ='Luciano')
    print(Pessoa.cumprimentar(Luciano))
    print(id(Luciano))
    print(Luciano.cumprimentar())
    print(Luciano.nome)
    print(Luciano.idade)
    for filho in  Luciano.filhos:
        print(filho.nome)
    Luciano.sobrenome = 'Ramalho'
    del Luciano.filhos
#dict só mostra os atributos de instância e não de classe

    print(Luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(Luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(Luciano.olhos),id(renzo.olhos))
    Luciano.olhos = 1
    Pessoa.olhos = 3

    print(Luciano.__dict__)
    print(Pessoa.olhos)
    del Luciano.olhos
    print(Luciano.__dict__)

