import Examen1_1 as P
'''
Funcionamiento de las clases Pelicula y Catalogo

En resumen la clase catalogo cuenta con un atributo llamado "lista"
que contiene todas las peliculas creadas, tengo el metodo "pelicula"
que ayuda a crear instancias y almacenarlas en el atributo lista
'''
#Se crea la instancia
catalogo_peliculas = P.Catalogo()
#Se crean las peliculas
catalogo_peliculas.pelicula('Star Wars: Episodio IV - Una Nueva Esperanza', 1977, 121 , 'PG', 'George Lucas', 'Mark Hamill,  Harrison Ford, Carrie Fisher', 'La película sigue a un joven granjero llamado Luke Skywalker mientras se une a un grupo de rebeldes para luchar contra el malvado Imperio Galáctico. Con la ayuda de Jedi como Obi-Wan Kenobi y Han Solo, Luke se embarca en un viaje para rescatar a la Princesa Leia y enfrentar al temible Darth Vader')
catalogo_peliculas.pelicula('Star Trek II: La ira de Khan', 1982, 113  , 'PG', 'Nicholas Meyer', ' William Shatner,  Leonard Nimoy, Ricardo Montalbán', 'En la película, el Capitán Kirk y su tripulación se enfrentan a Khan Noonien Singh, un antiguo enemigo que busca venganza. La película es conocida por su acción emocionante y por explorar temas de la amistad y el sacrificio.')
catalogo_peliculas.pelicula('Forrest Gump', 1994, 142, 'PG-13', 'Robert Zemeckis', ' Tom Hanks, Robin Wright, Gary Sinise', 'Es un drama que narra la vida de un hombre con discapacidad intelectual llamado Forrest Gump. A lo largo de varias décadas, Forrest se convierte en parte de momentos clave de la historia de Estados Unidos mientras busca a su amor de la infancia, Jenny.')
#Impresion de las peliculas creadas
catalogo_peliculas.impresion()

