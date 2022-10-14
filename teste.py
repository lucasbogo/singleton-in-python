# Singleton/SingletonPattern.py

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val
    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


titulo = OnlyOne('titulo')
subtitulo = OnlyOne('subtitulo')
email = OnlyOne('email@email.com')
print(titulo)
print(subtitulo)
print(email)
