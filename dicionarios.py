
serie1 = {
    'nome': 'The Big Bang Theory',
    'genero': 'Comédia'
}

serie2 = {
    'nome': 'Rick and Morty',
    'genero': 'ficção científica'
}

print(serie1.get('nome'))

videoteca = []

videoteca.append(serie1)
videoteca.append(serie2)

item = videoteca[0]
print(videoteca[0].get('nome'))
print(videoteca[0]['nome'])