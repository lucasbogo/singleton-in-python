# Professor, não consegui resolver isso em python. 
# Seria interessante fazer um 'code-along' em sala de aula com a correção desse exercício. 
# Só para obtenção de conhecimento mesmo, não precisa dar nota sobre a solução


class SiteConfiguration:

    _instance = None

    def __init__(self):
        self.titulo = 'Titulo'
        self.subtitulo = 'Sub Titulo'
        self.email = 'user@email.com'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == '__main__':

    titulo = SiteConfiguration()
    subtitulo = SiteConfiguration()
    email = SiteConfiguration()

    print(titulo.titulo)
    print(subtitulo.subtitulo)
    print(email.email)


class Visitor():

    counter = 0

    def __init__(self):

        Visitor.counter += 1


x = Visitor()
print(x.counter)

# y = Visitor()
# print(y.counter)
