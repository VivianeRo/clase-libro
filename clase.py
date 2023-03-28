class Libro :

    def __init__(self,titulo,autor,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas =cantidad_paginas

libro1 = Libro('Mujercitas', 'lOUISE May', 360)

print(libro1.titulo)
print(libro1.autor)
print(libro1.cantidad_paginas)
print('Estoy modificando')