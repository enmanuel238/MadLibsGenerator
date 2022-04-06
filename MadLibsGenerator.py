from random import randint
import copy

STORY = (
    "Érase una vez un joven {} que llevaba un cubo de leche en la {}, camino al {} para {}. " +
    "Durante el camino, el {} joven iba imaginando lo que podría lograr conseguir con la leche. " +
    "Pensó que en primer lugar y con el dinero de la venta compraría un canasto de huevos, los cuales una vez eclosionaran le permitiría {} una pequeña granja de pollos. " +
    "Una vez estos crecieran podría {}, lo que le daría dinero para comprarse un lechon."
)

words_dict = {
    'adj': ['alado', 'grande', 'juvenil', 'dulce','pequeño', 'comunista', 'amargo', 'diminuto', 'infantil', 'ácido', 'seco', 'capitalista', 'rojo', 'caro', 'renacentista', 'verde', 'inteligente', 'fotográfico', 'rubio', 'divertido','mucho', 'fuerte', 'fiel','poco', 'débil', 'agradable','demasiado', 'flexible', 'sucio','suficiente', 'tostado', 'limpio','todo', 'ronco', 'amable','varios', 'nítido', 'nuevo','más', 'áspero', 'valiente','menos', 'suave', 'hermoso', 'unos', 'cuantos', 'rugoso', 'largo','algún', 'esponjoso', 'cruel','ningún', 'flojo', 'perfecto','cierto', 'redondo', 'culto','ninguno', 'cuadrado', 'ancho','otro', 'universitario', 'musical','semejante', 'institucional', 'democrático','tal', 'artístico', 'individual','cada', 'religioso', 'nacional','sendos', 'cultural', 'regional','cualquier', 'estructural', 'mundial','bastante', 'policial', 'económico','ese', 'mensual', 'político','aquel', 'diario', 'histórico','aquellas', 'solar', 'civil','este', 'militar', 'familiar','nuestro', 'navideño', 'industrial','tu', 'laboral', 'naval','vuestra', 'mercantil', 'agrícola','mi', 'vanguardista', 'colombiano','cuál', 'dental', 'energética','cuánto', 'quirúrgico', 'petrolero','qué', 'un', 'segundo','cuánta', 'dos', 'triple','cuanto', 'primer', 'ambos','cuyo'],
    'part_of_body':['cabeza', 'mano', 'pie', 'ojos', 'nariz', 'dedos'],
    'name': ['Hugo','Martín','Lucas','Mateo','Leo','Daniel','Alejandro','Pablo','Manuel','Álvaro','Adrián','David','Mario','Enzo','Diego','Marcos','Iza','Javier','Marco','Álex','Bruno','Oliver','Miguel','Thiago','Antonio','Marc','Carlos','Ángel','Juan','Gonzalo','Gael','Sergio','Nicolás','Dylan','Gabriel','Jorge','José','Adam','Liam','Eric','Samuel','Darío','Héctor','Luca','Iker','Amir','Rodrigo','Saúl','Víctor','Francisco','Iván','Jesús','Jaime','Aarón','Rubén','Ian','Guillermo','Erik','Mohamed','Julen','Luis','Pau','Unai','Rafael','Joel','Alberto','Pedro','Raúl','Aitor','Santiago','Rayan','Pol','Nil','Noah','Jan','Asier','Fernando','Alonso','Matías','Biel','Andrés','Axel','Ismael','Martí','Arnau','Imran','Luka','Ignacio','Aleix','Alan','Elías','Omar','Isaac','Youssef','Jon','Teo','Mauro','Óscar','Cristian','Leonard','Abel','Adrián','Alejandro','Ángel','Carlos','César','Bruno','Daniel','Darío','David','Diego','Emilio','Fabián','Felipe','Gabriel','Héctor','Hugo','Jacobo','Jaime','Joaquín'],
    'last_name': ['García','González','Rodríguez','Fernández','López','Martínez','Sánchez','Pérez','Gómez','Martin','Jiménez','Ruiz','Hernández','Diaz','Moreno','Muñoz','Álvarez','Romero','Alonso','Gutiérrez','Navarro','Torres','Domínguez','Vázquez','Ramos','Gil','Ramírez','Serrano','Blanco','Molina','Morales','Suarez','Ortega','Delgado','Castro','Ortiz','Rubio','Marín','Sanz','Núñez','Iglesias','Medina','Garrido','Cortes','Castillo','Santos','Lozano','Guerrero','Cano','Prieto','Méndez','Cruz','Calvo','Gallego','Vidal','León','Márquez','Herrera','Peña','Flores','Cabrera','Campos','Vega','Fuentes','Carrasco','Diez','Caballero','Reyes','Nieto','Aguilar','Pascual','Santana','Herrero','Lorenzo','Montero','Hidalgo','Giménez','Ibáñez','Ferrer','Duran','Santiago','Benítez','Mora','Vicente','Vargas','Arias','Carmona','Crespo','Román','Pastor','Soto','Sáez','Velasco','Moya','Soler','Parra','Esteban','Bravo','Gallardo','Rojas'],
    'place':['apartamento','avenida','puente','edificios',' parada de autobús','catedral','cementerio, panteón','iglesia','centro de la ciudad','embajada','fábrica','casa','biblioteca','monumento','vecindario, barrio',' quiosco de periódicos, puesto de periódicos','palacio',' estacionamiento','cárcel, prisión','escuela, colegio','rascacielos','estadio','estatua','calle','universidad','galería de arte','centro de artes','circo','sala de conciertos','cine','museo','parque','campo de juegos','parque infantil','teatro','zoológico','panadería','librería','pastelería','dulceria','tienda de ropas','tienda departamental, grandes almacenes','farmacia','frutería','mueblería','joyería','centro comercial','mercado','tienda de música','tienda de animales','zapatería','tienda','centro comercial','centro comercial','tienda de deportes','tienda','supermercado','juguetería','aeropuerto','banco','estación de autobuses','cafeteria','gasolinera','hospital','hotel','lavaderia','biblioteca','residencia para ancianos','home','asilo de ancianos','orfanato','estación de policía, comisaría','oficina de correos, oficina postal','estación de ferrocarril','restaurante','estación del metro','estación del subterráneo','agencia de viajes'],
    'verb': ['abrir', 'acabar', 'acercar', 'aconsejar', 'acordar','amar', 'andar', 'apoyar', 'aprender', 'armar','asesinar', 'atacar', 'ayudar', 'bailar', 'bajar','bastar', 'bañar', 'beber', 'buscar', 'caer','callar', 'calmar', 'cambiar', 'caminar', 'campar','cantar', 'cazar', 'cenar', 'centrar', 'cercar','cerrar', 'citar', 'cocinar', 'coger', 'comenzar','comer', 'comparar', 'comprar', 'conducir', 'conocer','conseguir', 'contar', 'continuar', 'correr', 'cortar','coser', 'costar', 'crear', 'creer', 'cuidar','culpar', 'dar', 'dañar', 'deber', 'decidir','decir', 'dejar', 'descansar', 'describir', 'desear','destruir', 'disculpar', 'divertir', 'doler', 'dormir','durar', 'elegir', 'empezar', 'empujar', 'encantar','encontrar', 'enseñar', 'entender', 'entrar', 'equipar','esconder', 'escribir', 'escuchar', 'esperar', 'esposar','estar', 'estudiar', 'existir', 'explicar', 'extrañar','faltar', 'forzar', 'funcionar', 'ganar', 'gritar','gustar', 'haber', 'hablar', 'hacer', 'importar','intentar', 'ir', 'jugar', 'jurar', 'lamentar','lanzar', 'largar', 'lavar', 'leer', 'limpiar','llamar', 'llegar', 'llenar', 'llevar', 'llorar','luchar', 'mandar', 'matar', 'mejor', 'mejorar','mentir', 'mirar', 'morir', 'mostrar', 'mover','necesitar', 'negociar', 'nombrar', 'ocurrir', 'odiar','ofrecer', 'olvidar', 'orar', 'oír', 'pagar','parar', 'parecer', 'partir', 'pasar', 'pelar','pelear', 'peligrar', 'penar', 'pensar', 'perder','perdonar', 'permitir', 'pisar', 'poder', 'poner','preferir', 'preguntar', 'preocupar', 'preparar', 'probar','prometer', 'pulsar', 'quedar', 'quemar', 'querer','recibir', 'reconocer', 'recordar', 'regalar', 'regresar','repetir', 'responder', 'reír', 'saber', 'sacar','salir', 'saltar', 'salvar', 'seguir', 'sentar','sentir', 'ser', 'significar', 'sonar', 'sonreír','soñar', 'suceder', 'suponer', 'tardar', 'temer','tener', 'terminar', 'tirar', 'tocar', 'tomar','trabajar', 'traer', 'tratar', 'usar', 'valer','vender', 'venir', 'ver', 'viajar', 'visitar','vivir', 'volver']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words) - 1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(words_dict)
    return STORY.format(
        get_word('adj', local_dict),
        get_word('part_of_body', local_dict),
        get_word('place', local_dict),
        get_word('verb', local_dict),
        get_word('adj', local_dict),
        get_word('verb', local_dict),
        get_word('verb', local_dict)
    )


def main():
    print(create_story())


if __name__ == '__main__':
    main()
