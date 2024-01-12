class Livros:
    def __init__(self, titulo, autor, preco):
        ttitulo = titulo.lower()
        self.lista_livros_Proibidos = [
            'minha luta', 'ensaio sobre a desigualdade das raças humanas']
        if ttitulo in self.lista_livros_Proibidos:
            raise Exception('Favor evitar esse tipo de leitura')
        else:
            self.nomelivro = titulo
        aautor = autor.lower()
        self.lista_escritores_Proibidos = [
            'paulo coelho', 'blanka lipińska', 'erika leonard james', 'paulo vieira', 'mark manson']
        if aautor in self.lista_escritores_Proibidos:
            raise Exception('Favor escolher livro de um autor de verdade')
        else:
            self.escritor = autor
        self.valor = preco

    def comprarlivro(self, nome, autor):
        if nome not in self.lista_livros_Proibidos and autor not in self.lista_escritores_Proibidos:
            print(f'A compra foi feita com sucesso!')


books = Livros("Harry Potter e a câmara secreta", "j.k rowling", "R$55,00")
books2 = Livros("1984", "George Orwell", "R$30,00")
teste = Livros("não sei quantos principios inuteis e genericos",
               "Paulo Vieira", "FREE")
print(teste.escritor)
