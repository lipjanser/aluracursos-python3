class Programa:

    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'


class Filme(Programa):

    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self._likes} - Duração: {self.duracao} '


class Serie(Programa):

    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self._likes} - Temporadas: {self.temporadas} '


class Playlist:

    def __init__(self, nome, programas) -> None:
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


diehard = Filme('duro de matar', 1988, 96)
diehard.dar_like()

diehard2 = Filme('duro de matar 2', 1990, 96)
diehard2.dar_like()

diehard3 = Filme('duro de matar 3', 1992, 96)
diehard3.dar_like()

diehard4 = Filme('duro de matar 4', 2000, 96)
diehard4.dar_like()

serie = Serie('brooklin 99', 2016, 7)
serie.dar_like()
serie.dar_like()
serie.nome = 'brooklyn 99'
serie.dar_like()

odat = Serie('one day at time', 2019, 3)
odat.dar_like()
odat.dar_like()

filmes_e_series = [diehard, diehard2, diehard3, serie, diehard4]
playlist_fim_de_semana = Playlist('Weekend', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho: {len(playlist_fim_de_semana)}')
