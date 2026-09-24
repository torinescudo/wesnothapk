"""Las mareas sin nombre — Nerea Vado. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='nerea',
    title='Las mareas sin nombre',
    hero='Nerea Vado',
    companion='Luar',
    companion_type='Merman Hunter',
    race='human',
    recruit='Merman Fighter,Merman Hunter,Mermaid Initiate,Footpad,Bowman,Mage',
    enemy='nagas',
    length='Muy larga · 12 escenarios · 8–12 horas',
    premise=(
        'Una capitana de puerto libre y un cazador del arrecife siguen una corriente que borra los '
        'nombres de las islas. Doce travesías los enfrentarán a contrabandistas, custodios naga y una '
        'máquina que transforma la memoria en mareas.'),
    ending=(
        'Las islas recuperaron nombres elegidos por sus habitantes. Nerea fundó una escuela de '
        'navegación donde el primer mapa se dibujaba escuchando a otro. Luar escribió el suyo bajo el '
        'agua, para que nadie pudiera llevárselo sin aprender a bucear.'),
    chapters=[
        dict(
            title='El puerto sin cartas',
            goal='rescue',
            biome='harbor',
            antagonist='Recaudadora Vaska',
            opening=(
                'Todos los nombres desaparecieron de las cartas del puerto. Nerea Vado es capitana de '
                'puerto libre: gana la vida metiendo barcos dentro del paso cuando la marea los '
                'deja a media mar, y quiere una sola cosa hoy: firmar el registro de salida con '
                'el nombre de su calle todavía escrito. Vaska arrestó al único '
                'piloto que aún recordaba la salida y vendió permisos de navegación imposibles de '
                'usar. En el registro de la aduana cada isla figura como «sin designar» y cada barco '
                'como carga de valor variable. Ciro está en la celda del muelle con las manos atadas '
                'y una tablilla de precios colgada del cuello, sin una sola letra de su calle. Desde '
                'la torre, la marea sube con una calma que no le corresponde. La barca de Nerea también '
                'está en ese libro, tasada por lo que rinde, y a cada marea tranquila se le caen '
                'letras de la carta de navegación. Zarpar sin permiso sellado significa dejar la '
                'barca en prenda, y sin barca se le acaba el oficio.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', (
                    'Objetivo: llega a la prisión del muelle, saca al piloto y llévalo hasta la '
                    'bandera antes de la pleamar.')),
                ('companion', 'La corriente recuerda rutas que vuestra tinta ha olvidado.'),
                ('hero', (
                    'Entonces llevaremos al piloto hasta tu corriente y cobraremos la ayuda en '
                    'respuestas.')),
                ('Recaudadora Vaska', 'Nadie navega sin permiso sellado. Yo firmo los permisos, y hoy no firmo nada.'),
                ('hero', 'Los permisos se venden. Los nombres no deberían.'),
                ('Recaudadora Vaska', 'El nombre es la parte cara del permiso. El resto lo pongo yo.'),
                ('narrator', (
                    'En el libro de Vaska hay una etiqueta con un precio junto a cada renglón. '
                    'Ninguna etiqueta lleva nombre.')),
                ('companion', (
                    'A Ciro le colgaron la tablilla con la letra de su calle ya tachada. Lleva tres '
                    'días con ella al cuello.')),
                ('hero', 'Cortamos la cuerda y la tablilla cae al agua con su precio. Sin nombre no vale nada.'),
                ('companion', 'La puerta de servicio baja directa al canal. Si entramos por el agua, salimos por la misma escalera.'),
                ('hero', 'Yo abro, tú llevas al piloto. Nadie se queda atrás discutiendo precios.'),
                ('narrator', 'Vaska ha puesto dos hombres en la puerta principal y uno solo en la escalera de servicio.'),
                ('Recaudadora Vaska', 'Si rompéis esa puerta, cada tablón lo pagará la familia que espera detrás.'),
                ('hero', 'Entonces no rompemos nada. Entramos por donde el agua ya entró.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Recaudadora Vaska', 'Sin mi libro, este puerto es una fila de barcos que nadie sabe cobrar. Firmad el precio y os firmo la salida antes de que cierre la pleamar.'),
                    ('narrator', 'La aduana da a un canal de una sola boca y Vaska ha tendido una cadena al ras del agua para que la pleamar haga de carcelero. Decide si cortas la cadena por dentro o sacas a Ciro por el tejado.'),
                ]),
                ('turn 4', [
                    ('narrator', 'El agua cubre el primer escalón de la celda. Alguien ha abierto las compuertas del arrecife.'),
                    ('Recaudadora Vaska', 'No he sido yo. La máquina mantiene el mar quieto y cobra lo que nadie usa.'),
                ]),
                ('half strength', [
                    ('protected', 'No puedo correr. Dejadme con la tablilla y salid vosotros.'),
                    ('hero', 'La tablilla pesa menos que tú. Camina y no discutas con quien te saca de una celda.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Vaska solo tiene que esperar: en un turno la escalera de servicio queda inundada y solo quedará la puerta encadenada. Decide el paso ahora, que el agua sube más rápido que tus hombres.'),
                    ('Recaudadora Vaska', 'Detrás de cada precio hay un nombre guardado. Quitadme el libro y esos nombres se los come el canal, no yo.'),
                    ('hero', 'Los nombres viven en las calles, no en tus renglones.'),
                ]),
                ('turn 8', [
                    ('Recaudadora Vaska', (
                        'La máquina solo pide nombres viejos. Los guardo en el libro para que no se '
                        'pierdan.')),
                    ('hero', 'Quien decide qué nombre está viejo eres tú. Eso no es una máquina, es una aduana.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El libro de cuentas queda abierto en el suelo mojado del muelle.'),
                    ('companion', 'Mirad el último renglón. El precio está escrito y el nombre está raspado.'),
                ]),
            ],
            victory=[
                ('protected', 'La marea entró por el canal mientras Vaska contaba tablones.'),
                ('companion', 'Ese hombre vende lo que no construyó. Ahora sabe cuánto pesa un permiso mojado.'),
                ('hero', 'Ciro, marca la ruta sobre el agua. Ya la escribiremos con calma.'),
                ('protected', 'Necesito ver la salida desde la torre. Dadme un remo y os la dibujo.'),
                ('narrator', 'La tablilla del precio se quedó flotando en el canal, sin cuello al que colgarse.'),
            ],
            protected=('Ciro, piloto del puerto', 'Peasant'),
            resolution=(
                'El piloto recordó una isla que había desaparecido de los registros tres años antes '
                'de hundirse. La dibujó con brea en la puerta de la aduana y escribió debajo el '
                'nombre de su calle, que nadie le había devuelto. Vaska pagó la multa de su propio '
                'libro y se marchó del puerto sin que nadie le pidiera el permiso. Nerea firmó el registro con el nombre '
                'de su calle, y la marea le devolvió dos letras de su carta. Al amanecer, la '
                'corriente sin nombre tiraba hacia el paso exterior, donde dos filas de lanzas '
                'guardaban la única salida del archipiélago.'),
        ),
        dict(
            title='Los dientes del arrecife',
            goal='escape',
            biome='coast',
            antagonist='Naga Kess',
            opening=(
                'El paso exterior estaba custodiado por guerreros naga. Sus lanzas señalaban hacia el '
                'puerto, como si quisieran impedir que algo saliera de él. Kess no grita órdenes: '
                'golpea un caracol tres veces y las filas se cierran. En el cordel de cada lanza hay '
                'nudos atados por manos que ya no recuerdan a quién los ataron. La corriente que '
                'buscamos pasa por debajo de esas líneas. Solo hay una salida y está al otro lado, '
                'marcada con una bandera. El hueco entre las dos filas se abre con la resaca '
                'y se cierra cuando el agua se calma, y esta resaca dura lo que dura la luz. Cada '
                'paso que Nerea abre por una corriente sin nombre le borra una letra de su carta; '
                'quedarse en la orilla le borra el paso entero.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: cruza el arrecife y alcanza la bandera del paso exterior antes de que cierre la marea.'),
                ('companion', 'No protegen un tesoro. Están cerrando una herida.'),
                ('hero', 'Crucemos sin quedarnos atrapados entre sus lanzas y la marea.'),
                ('Naga Kess', 'Ley del arrecife: quien nombra una cosa la posee. Nosotros no poseemos nada, solo guardamos.'),
                ('hero', '¿Y qué guardáis aquí?'),
                ('Naga Kess', 'El paso que vuestros barcos usaron para pescar hasta el último banco. Ahora está en cuarentena.'),
                ('companion', 'El cordel de su lanza lleva siete nudos y el séptimo está deshecho.'),
                ('Naga Kess', 'Era de mi hermana. La máquina la tomó la primera. Los primeros borrados siempre somos nosotros.'),
                ('hero', 'Entonces no luchamos contra vosotros. Luchamos contra la corriente.'),
                ('Naga Kess', 'La corriente no se lucha, se atraviesa. Y se paga.'),
                ('companion', 'Hay dos filas de lanzas y un hueco en el centro. Con la resaca el hueco se ensancha.'),
                ('hero', 'Pasamos por el hueco, no por las lanzas. Nadie tiene que morir por una bandera.'),
                ('narrator', 'Los nagas retroceden con la marea. Alcanza la bandera y no te entretengas en la orilla.'),
                ('Naga Kess', (
                    'Si llegáis al agua dulce, decid que el arrecife sigue abierto. Es lo único que '
                    'aún podemos ofrecer.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Naga Kess', 'Nuestra ley dice que quien nombra una cosa la posee. Vosotros nombráis bancos y calas y por eso os parece que el mar os debe algo.'),
                    ('narrator', 'Dos filas de lanzas flanquean el hueco del arrecife y la resaca lo ensancha a cada ronda. Kess lo cierra en cuanto se calma el agua: decide si pasas ahora por el centro o rodeas por la poza honda, que cuesta dos turnos.'),
                ]),
                ('turn 4', [
                    ('companion', 'Sus lanzas se mueven con la resaca, no contra ella. Están dejando pasar el agua.'),
                    ('hero', 'Aprovecha el hueco. Cuenta hasta tres y corre.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la cala hay una pizarra de pescadores con seis nombres y un séptimo borrado a mano.'),
                    ('companion', 'El séptimo nudo. Aquí también les falta alguien.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Cuando baje la resaca, las filas cerrarán el hueco como una boca. Decide si empujas por el centro con todos o mandas delante a los rápidos para que marquen el paso desde el otro lado.'),
                    ('Naga Kess', 'Yo no poseo este paso, solo lo guardo, y mañana volveré a custodiarlo entero. Para eso estamos las de siempre: las primeras borradas.'),
                    ('hero', 'Entonces lo cruzamos con nombre. Le pondremos el de tu hermana, si me lo dices.'),
                ]),
                ('turn 8', [
                    ('Naga Kess', 'Mi ley dice que un nombre robado vuelve al agua con quien lo robó.'),
                    ('hero', 'Pues devolvamos el agua que falta y quedémonos con la ley.'),
                ]),
                ('time limit', [
                    ('narrator', 'La resaca baja. El hueco entre las filas se cierra a cada ronda.'),
                    ('companion', 'Si esperamos una marea más, tendremos que abrirnos paso.'),
                ]),
                ('enemy leader defeated', [
                    ('Naga Kess', 'No os he detenido. Tampoco os he dejado pasar. Recordad la diferencia.'),
                ]),
            ],
            victory=[
                ('companion', 'Han dejado pasar a los nuestros antes que a los suyos. Entre naga, eso es una deuda.'),
                ('hero', 'La anotamos. Sin precio.'),
                ('Naga Kess', 'Guardaos la lanza pequeña del paso. Es vuestra, y con ella la obligación de devolverla.'),
                ('hero', 'Volveremos a traerla cuando el paso vuelva a tener nombre.'),
                ('narrator', 'Detrás de las filas, el fondo del mar estaba sembrado de anclas sin barco.'),
            ],
            protected=None,
            resolution=(
                'Al otro lado del arrecife, el mar tenía el sabor del agua de lluvia. Luar nadó hasta '
                'una roca y ató en su cordel un nudo nuevo con el nombre del paso que acababan de '
                'cruzar. Kess lo vio desde lejos y no lo deshizo: era la primera vez en veinte años '
                'que alguien ataba un nombre en lugar de cortarlo. Aquel sabor venía de '
                'tres fuentes que manaban bajo la mar, y cada chorro bajaba con un nombre menos '
                'para las islas del borde. Nerea guardó el rumbo de las luces que las señalaban, '
                'sabiendo que encenderlas costaba apellidos ajenos.'),
        ),
        dict(
            title='Agua dulce en mar abierto',
            goal='beacons',
            biome='islands',
            antagonist='Custodio Issar',
            opening=(
                'Tres fuentes sumergidas vertían agua dulce desde una isla invisible. Activar sus '
                'balizas antiguas mostraría el camino, pero Issar había prohibido tocar los '
                'mecanismos. El custodio no defiende un secreto: administra una deuda. Cada chorro '
                'que mana descuenta años de memoria a las islas del borde, y él lleva la cuenta en '
                'tres piedras. Los nombres grabados en la calzada están tachados con sal, no con '
                'tinta, y alguno tiene la marca de un pulgar reciente. La tercera piedra, la de '
                'los nombres que nadie reclamó, está tibia debajo del agua. Nerea sabe lo que '
                'cuesta accionar estas balizas: cada luz encendida le ha costado hasta ahora una '
                'letra de su carta, y delante quedan tres luces y tres apellidos de más.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: activa las tres balizas sumergidas llevando una unidad a cada una.'),
                ('companion', 'Mi abuela hablaba de manantiales que pagaban su caudal con recuerdos.'),
                ('hero', 'Hoy solo les pediremos una dirección.'),
                ('Custodio Issar', 'Por cada baliza que encendéis, una familia del norte pierde su apellido. Elegid cuál.'),
                ('hero', 'Ninguna. Enciendo la baliza y devuelvo el nombre por donde vino.'),
                ('Custodio Issar', 'La máquina no funciona así. Recibe y devuelve. Ahora mismo está recibiendo.'),
                ('companion', 'En las piedras hay nombres raspados. Alguien quitó la sal con la mano antes que nosotros.'),
                ('Custodio Issar', 'Los custodios raspamos para poder leer. Es nuestra ley: un nombre raspado sigue siendo un nombre.'),
                ('narrator', 'La calzada está a media agua. Las balizas marcan su trazado y solo una unidad puede activar cada una.'),
                ('companion', 'Los peces evitan el agua dulce. No está sucia, está nueva.'),
                ('hero', 'Subimos por la calzada y encendemos las tres. Si Issar quiere cobrar, que cobre en preguntas.'),
                ('Custodio Issar', 'Mi gente bebió aquí primero. También fuimos los primeros en ser borrados.'),
                ('hero', 'Entonces grabaremos los vuestros antes que los nuestros.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Custodio Issar', 'Mi gente bebió de esta agua antes que nadie y la máquina nos pidió los nombres como fianza. Todavía los estamos pagando.'),
                    ('narrator', 'La calzada queda a media agua y solo se pasa por sus tres tramos de piedra. Los guardias de Issar cortan el tramo central: decide si repartes una unidad por baliza o abres el tramo de en medio primero.'),
                ]),
                ('beacon lit 1', [
                    ('narrator', 'Primera baliza encendida. El agua dulce se enturbia un instante y vuelve a estar clara.'),
                    ('companion', 'Ha pasado algo por debajo. No era un pez.'),
                ]),
                ('beacon lit 2', [
                    ('Custodio Issar', 'Dos luces. En el norte ya hay una aldea que no recuerda cómo llamaba a su cala.'),
                    ('hero', 'Anota la aldea. La escribiremos otra vez cuando volvamos.'),
                ]),
                ('beacon lit 3', [
                    ('narrator', 'La tercera baliza abre la calzada. En el centro hay una piedra con un nombre a medio raspar.'),
                    ('companion', 'Está empezado por la mitad. Alguien se arrepintió.'),
                ]),
                ('turn 6', [
                    ('narrator', 'El chorro dulce empuja hacia el norte y resbala a quien nada contra él, y los de Issar atacan a favor de corriente. Decide si usas el chorro para ganarles la espalda o aguantas la calzada sin moverte.'),
                    ('Custodio Issar', 'No guardo estas balizas por gusto: las guardo porque fuimos los primeros en pagarlas. Si encendéis las tres, mi deuda crece, y una deuda sin nombre se cobra en la primera casa que encuentre.'),
                    ('hero', 'Tu deuda la apuntamos con nosotros. Pero hoy encendemos las tres.'),
                ]),
                ('turn 8', [
                    ('narrator', 'Un bote sin remos aparece a la deriva con dos isleños dentro y ninguna carta a bordo.'),
                    ('hero', 'Súbelos a nuestro barco y tomamos el bote a remolque. Ya preguntaremos cómo se llaman.'),
                ]),
                ('time limit', [
                    ('Custodio Issar', 'El mar no espera a los que dudan. Yo tampoco.'),
                    ('companion', 'La calzada se está cubriendo. Nos queda una marea de luz.'),
                ]),
            ],
            victory=[
                ('companion', 'Las tres luces ya no apuntan al norte. Apuntan a la isla que falta.'),
                ('hero', 'Escribe el rumbo. Pondremos el nombre cuando lleguemos.'),
                ('Custodio Issar', 'Habéis pagado con vuestro tiempo lo que otros pagan con su casa. No os lo agradeceré.'),
                ('hero', 'No te lo he pedido.'),
                ('narrator', 'El agua dulce se mezcló con la sal y nadie perdió nada esa noche.'),
            ],
            protected=None,
            resolution=(
                'Las balizas revelaron una calzada bajo la superficie. Sobre sus piedras estaban '
                'grabados nombres tachados. Nerea raspó la sal con la uña en uno de ellos y encontró '
                'una letra debajo. Luar la copió en su cordel con un nudo, antes de que la marea '
                'volviera a cubrirla; Issar lo miró hacerlo y no lo impidió. Alguien había '
                'empezado a raspar aquellos nombres y no llegó a terminar la faena. Del último '
                'tramo de calzada partía un surco de anclas hacia una isla que no figuraba en '
                'carta alguna, y hacia allí tiraba la corriente.'),
        ),
        dict(
            title='La isla borrada',
            goal='conquer',
            biome='ruins',
            antagonist='Almirante Serkos',
            opening=(
                'Serkos utilizaba la isla sin nombre para ocultar barcos confiscados. Entre sus '
                'prisioneros había familias que el resto del mundo había olvidado por completo. No '
                'esconde la isla: la ha sacado de todos los mapas para que nadie reclame a los suyos. '
                'En los almacenes hay baúles con etiqueta de destino y sin remitente, y en la pared '
                'del faro alguien escribió el nombre de cada preso y raspó el suyo propio hasta '
                'levantar la cal. La marea entra por la '
                'calzada del este dos veces al día y deja el almacén aislado un rato: es el único '
                'momento en que sus guardias no se oyen entre sí. Nerea ataca esa franja sabiendo '
                'que cada hora de asalto es un flete que no cobrará nunca, porque las islas sin '
                'nombre no pagan rescates.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: derrota al almirante Serkos y abre los almacenes del fuerte.'),
                ('companion', 'Si regresan y nadie los reconoce, ¿adónde podrán ir?'),
                ('hero', 'Primero abrimos las puertas. Luego haremos sitio.'),
                ('Almirante Serkos', 'Esta isla no figura en ningún registro. Por eso nadie vendrá a quitármela.'),
                ('hero', 'Eso lo decidirán quienes están dentro.'),
                ('Almirante Serkos', 'Están dentro precisamente porque nadie los busca. Aquí comen todos los días.'),
                ('companion', 'Sus baúles llevan destino y no llevan dueño. Igual que sus presos.'),
                ('hero', 'Abrimos los baúles y devolvemos el nombre a quien lo reclame.'),
                ('narrator', 'El fuerte tiene dos puertas y una torre. Dos unidades por puerta fijan a sus hombres.'),
                ('Almirante Serkos', 'La máquina me paga por guardar gente que el mar ya no recuerda. Yo solo cobro.'),
                ('hero', 'Cobras por guardar lo que tú mismo borraste de las cartas.'),
                ('companion', 'Sobre la puerta hay una lista. El último renglón está raspado y reescrito tres veces.'),
                ('hero', 'Averigua de quién es. Yo voy a por el almirante.'),
                ('Almirante Serkos', 'Mi nombre también está en esa lista. El renglón raspado lo borré yo: sin nombre escrito no hay isla que reclamar.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Almirante Serkos', 'Cada preso que guardo come y duerme. Fuera, nadie los buscaba ni para enterrarlos: aquí tienen lista, tejado y número de baúl.'),
                    ('narrator', 'El fuerte tiene dos puertas y una torre entre las dos. Serkos refuerza la torre a cada turno: decide si cierras las puertas a la vez o la primera se te llena de heridos.'),
                ]),
                ('turn 4', [
                    ('narrator', 'Refuerzos por el embarcadero. Serkos ha mandado abrir el almacén de armas.'),
                    ('companion', 'Dos barcas con gente armada. Cuento veinte remos.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la caseta del muelle hay una etiqueta de equipaje con un precio y ninguna letra de nombre.'),
                    ('hero', 'La guardamos. Servirá de prueba cuando alguien pregunte por los baúles.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Al caer la tarde el agua cubre la calzada del este y corta la retirada, y Serkos juntará sus hombres en la torre. Decide qué puerta cierras antes: la del almacén de armas o la de la torre.'),
                    ('Almirante Serkos', 'No borré esta isla para quedármela: la borré para que no vinieran a repartirla. Mañana firmaré su nombre de nuevo, y será el que yo elija.'),
                    ('hero', 'Mañana firmará quien la habite. Y ya somos demasiados para tu firma.'),
                ]),
                ('turn 8', [
                    ('Almirante Serkos', 'Podéis llevaros a los presos. Los barcos os los quedaréis también. Solo quiero la isla sin nombre.'),
                    ('hero', 'La isla tiene el nombre que le dieron sus vecinos. Pregúntales a ellos.'),
                ]),
                ('time limit', [
                    ('narrator', 'La marea cubre la calzada del fuerte. Queda una ronda para cruzar.'),
                    ('companion', 'Los almacenes están abiertos. Falta desalojarlos antes del agua.'),
                ]),
                ('enemy leader defeated', [
                    ('Almirante Serkos', 'Guardadme en la lista. Con nombre. Es lo único que os pido.'),
                    ('hero', 'Ya estás. Con tu nombre y con el de la isla.'),
                ]),
            ],
            victory=[
                ('companion', 'La lista de la puerta tenía cuarenta y un renglones. El raspado era el nombre de la isla.'),
                ('hero', 'Pues la isla se llama así, como estaba escrito antes de que él lo borrara.'),
                ('companion', 'Los baúles vuelven a sus dueños. Cuarenta y uno, y falta uno por abrir.'),
                ('hero', 'Ese lo abrimos en el puerto, delante de testigos.'),
                ('narrator', 'Al alba, la isla volvió a los mapas con el nombre que una niña dijo en voz alta.'),
            ],
            protected=None,
            resolution=(
                'Una niña reconoció a Nerea en un retrato viejo. La capitana no recordaba haber '
                'visitado aquella isla. En la imagen salía junto a su madre, con un cuaderno bajo el '
                'brazo, delante del mismo almacén que acababa de cruzar. La niña le preguntó si el '
                'cuaderno seguía existiendo; Nerea tardó en contestar. La niña '
                'llevaba atada a la cintura una bolsa de cuero con un nudo que nadie sabía '
                'deshacer. Dentro esperaba un cuaderno escrito por su madre, y con él el camino '
                'hasta la única lectora que aún descifraba la tinta que aparece al anochecer.'),
        ),
        dict(
            title='El cuaderno de otra vida',
            goal='escort',
            biome='forest',
            antagonist='Rastreadora Olss',
            opening=(
                'La niña conservaba un cuaderno escrito por la madre de Nerea. Debían llevarlo a la '
                'casa de mareas, donde una lectora ciega podía descifrar la tinta que solo aparecía '
                'al anochecer. Olss rastrea por el olor del papel mojado y ha marcado los árboles del '
                'camino con brea. Cada vez que el cuaderno se abre, alguien de la comarca pierde el '
                'nombre de un árbol. Talia lo lleva en una bolsa de cuero atada con un nudo que no '
                'sabe deshacer. Para Nerea, abrir el '
                'cuaderno cuesta a la comarca un nombre; no abrirlo, no volver a leer a su madre. '
                'El anochecer cae dentro de dos jornadas, y la bolsa de Talia no puede caerse ni '
                'una vez por el camino.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: escolta a Talia y el cuaderno hasta la bandera, al final del bosque.'),
                ('companion', 'Puedes abrirlo ahora. Nadie te culparía.'),
                ('hero', 'Si la tinta se borra al sol, mi impaciencia volverá a dejarla sin voz.'),
                ('protected', 'Mi abuela me enseñó este nudo. Dice que mientras esté atado, el cuaderno es de casa.'),
                ('Rastreadora Olss', 'Devolved el cuaderno y os doy una jornada de ventaja. La máquina paga bien por lo que no debe leerse.'),
                ('hero', '¿Cuánto paga por un nombre raspado? Porque eso es todo lo que llevas contando.'),
                ('Rastreadora Olss', 'Paga por el orden. Sin nombres no hay deudas, y sin deudas no hay deudores.'),
                ('hero', 'Y sin deudores tampoco hay acreedores. Diles que vas a quedarte sin oficio.'),
                ('companion', 'Huele a resina quemada. Ha señalado los árboles con brea para que no salgamos del camino.'),
                ('protected', 'Los árboles tienen nombre. Al de la derecha lo llamo alto, y al otro también. Los llamo así desde pequeña.'),
                ('hero', 'Entonces no vamos por el camino. Vamos por el arroyo.'),
                ('narrator', 'El camino tiene dos puestos de brea y una ciénaga. La ciénaga es lenta, pero no está vigilada.'),
                ('Rastreadora Olss', 'En esta comarca ya nadie recuerda cómo se llamaba el río. Yo tampoco. Eso es lo que llevo en la mano.'),
                ('protected', 'Se llamaba Sombra. Mi madre lo decía así.'),
                ('hero', 'Escríbelo en la bolsa con carbón. Antes de que se nos olvide a los dos.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Rastreadora Olss', 'No persigo a la niña: persigo el papel. Un papel que solo se lee al anochecer ya ha borrado a más gente que yo, y alguien tiene que cerrarlo.'),
                    ('narrator', 'Olss ha marcado los árboles con brea para que el camino se estreche a cada tramo. Decide si sigues el arroyo, más lento pero sin marcas, o cortas por el soto y aguantas la emboscada.'),
                ]),
                ('turn 4', [
                    ('protected', 'El nudo de la bolsa sigue apretado. Si se afloja, avisadme.'),
                    ('companion', 'Yo llevo el extremo de la cuerda. Si tiras, lo noto.'),
                ]),
                ('half strength', [
                    ('protected', 'La bolsa sigue cerrada. El nudo aguanta.'),
                    ('hero', 'Tú también vas a aguantar. Luar, cárgala del lado bueno y sigue andando.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la carbonera hay una pizarra con los nombres de los árboles del término. Dos están borrados.'),
                    ('protected', 'El del sauce está borrado. Yo lo recuerdo: sauce.'),
                ]),
                ('turn 6', [
                    ('narrator', 'La ciénaga frena a quien carga peso y derriba a quien corre, y Olss ataca justo donde carga el peso. Decide quién abre paso y quién cierra la fila con Talia.'),
                    ('Rastreadora Olss', 'Detrás de mí hay una comarca que duerme sin nombres, y esa calma también es orden. Si antes de la noche no soltáis el papel, quemaré el soto entero.'),
                    ('hero', 'Luego el soto se quedará sin árboles y tú sin encargo. Escoge.'),
                ]),
                ('turn 8', [
                    ('Rastreadora Olss', 'Habéis llegado lejos para gente que no lleva mapa.'),
                    ('companion', 'Llevamos dos. Uno escrito y otro en la cabeza de la niña.'),
                ]),
                ('time limit', [
                    ('narrator', 'La casa de mareas está al final del arroyo. Queda una ronda de luz.'),
                    ('hero', 'Talia delante, el cuaderno en medio y nadie se para a discutir.'),
                ]),
            ],
            victory=[
                ('protected', 'El nudo sigue atado. Podéis abrirlo cuando ella lo abra.'),
                ('companion', 'La lectora vive detrás de esa puerta. Nadie ha entrado en veinte años sin traerle agua.'),
                ('hero', 'Llevamos cuaderno y agua.'),
                ('narrator', 'La tinta del cuaderno solo aparece al anochecer. La lectora lo leyó con los dedos, despacio, dos veces.'),
                ('protected', 'Dice que la letra es de una mujer que firmaba con dos nombres. Uno de ellos es el tuyo.'),
            ],
            protected=('Talia', 'Peasant'),
            resolution=(
                'La lectora encontró una orden de emergencia: la madre de Nerea había borrado una '
                'ruta para detener una invasión. Debajo de la orden había una cuenta de lo que la '
                'máquina cobraba por cada isla, un año de memoria por cada marea tranquila. En la '
                'última página, Aldara Vado había repetido su propio nombre siete veces, como si '
                'temiera perderlo antes de terminar de escribir. Antes '
                'del alba apareció en la puerta un caracol con muescas, una de ellas borrada: el '
                'arrecife venía a cobrar el cuaderno en nombre de todos los que faltaban. Y con '
                'el caracol llegaba la primera lanza, que no venía a discutir el precio, sino a '
                'fijarlo.'),
        ),
        dict(
            title='Quienes pagan la calma',
            goal='survive',
            biome='islands',
            antagonist='Primera Lanza Uss',
            opening=(
                'Los custodios naga exigieron entregar el cuaderno. Cada noche que la máquina '
                'mantenía tranquilas las aguas borraba un recuerdo de las islas periféricas. La madre '
                'de Nerea había intentado detenerla. Uss viene a cobrar en nombre del arrecife: el '
                'cuaderno es la prueba de la deuda. En las islas del borde los pescadores ya salen a '
                'la mar sin recordar su cala y vuelven guiándose por las estrellas. La aldea tiene '
                'hasta el alba para embarcar a todos. Uss viene con '
                'la ley del arrecife anudada en el brazo, un nudo por cada generación que la '
                'calma del puerto costó a los nagas. Aguantar una noche más cuesta otra tanda de '
                'nombres en las islas del borde; entregar el cuaderno cuesta la única letra que '
                'Nerea conserva de su madre. Con el alba zarpan todas las barcas.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: mantén a Nerea con vida hasta el comienzo del turno doce. A esa hora las barcas estarán cargadas.'),
                ('companion', 'La calma de vuestro puerto nos ha costado generaciones enteras.'),
                ('hero', (
                    'No pediré que nos perdonéis. Dame esta noche para sacar a la gente de su '
                    'alcance.')),
                ('Primera Lanza Uss', 'La ley del arrecife exige que quien rompe un pacto pague con lo que más guarda. Vosotros guardáis nombres.'),
                ('hero', 'Guardamos gente. Los nombres van con ellos.'),
                ('Primera Lanza Uss', 'Entregad el cuaderno y la marea queda quieta una luna más. Es un buen precio.'),
                ('companion', 'Es un precio de mercado. El mismo que cobra vuestro enemigo.'),
                ('Primera Lanza Uss', 'Mi enemiga construyó la máquina. Yo solo cobro lo que ella dejó firmado. Un custodio también obedece.'),
                ('narrator', 'Las barcas cargan de una en una. Cada turno que pasa, una familia sube a bordo.'),
                ('companion', 'En la cala del este hay una mujer que repite la canción de su aldea para no perderla.'),
                ('hero', 'Pon a la hija a cantar la respuesta. Así la canción tendrá dos voces y no se borrará.'),
                ('Primera Lanza Uss', 'Puedo esperar. Tengo más paciencia que vuestras barcas.'),
                ('narrator', 'Uss atacará por el muelle y por el agua. Deja dos unidades en el embarcadero.'),
                ('hero', 'Esta noche nadie duerme. El que no rema, vigila.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Primera Lanza Uss', 'El arrecife lleva veinte años pagando vuestras mareas quietas. Yo cobro lo firmado: un cuaderno por cada generación que nos falta.'),
                    ('narrator', 'Uss ataca por el muelle y por el agua, y las redes del embarcadero aguantan a los nadadores un turno. Decide si cierras el muelle con dos unidades o dejas que la cala se cubra sola.'),
                ]),
                ('turn 4', [
                    ('narrator', 'Tres familias a bordo y la cala ya huele a humo. Uss ha cortado las redes del muelle.'),
                    ('companion', 'Sin redes no hay excusa para quedarse. Empujad las barcas.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Uss corta la rompiente para dejar las barcas cargadas a tiro, y cada barca tarda un turno entero en salir. Decide cuántas escoltas se quedan en tierra: las que acompañen esta noche no nadarán.'),
                    ('Primera Lanza Uss', 'No quiero vuestra gente: quiero el papel que dejó firmado quien construyó la máquina. Si me lo dais, me marcho contando a los vuestros uno por uno y sin tachar ninguno.'),
                    ('hero', 'El papel se queda donde está. Cuenta a los que se van, que hoy suman más.'),
                ]),
                ('turn 8', [
                    ('companion', 'La mujer de la canción lleva en la mano un caracol con muescas. Una está borrada.'),
                    ('hero', 'Una muesca es una casa. Que su hija la vuelva a marcar con un clavo.'),
                ]),
                ('turn 10', [
                    ('Primera Lanza Uss', 'Queda una barca en el muelle. La mía también tiene nombre, aunque nadie lo recuerde.'),
                    ('hero', 'Entonces dilo tú, y lo apuntamos.'),
                ]),
                ('time limit', [
                    ('narrator', 'Última barca. Si cedéis el muelle, se llevan a quien no sabe nadar.'),
                    ('companion', 'Los viejos van dentro y los jóvenes al agua. Yo cierro la fila.'),
                ]),
            ],
            victory=[
                ('companion', 'Todas las barcas están fuera de la rompiente.'),
                ('hero', 'Contad cabezas otra vez. Quiero el número exacto.'),
                ('Primera Lanza Uss', 'Habéis salvado a los vuestros. Nosotros no tenemos barcas.'),
                ('hero', 'Por eso os dejo el muelle, el agua dulce y una copia del cuaderno. Nada más.'),
                ('narrator', 'Uss se quedó en el embarcadero contando las barcas que se alejaban hasta que la niebla tapó la última.'),
            ],
            protected=None,
            resolution=(
                'Los isleños huyeron con canciones repetidas en voz alta para no olvidar a quienes '
                'viajaban en la barca de al lado. Uss apuntó en el brazo la lista de los que se '
                'quedaban y se ató un nudo por cada uno. Llevaba cinco nudos cuando amaneció, y '
                'ninguno tenía nombre, porque ya nadie recordaba cómo se llamaba la cala. En el '
                'puerto al que remaban ya había puestos que vendían lo que la marea robaba: '
                'recuerdos en tablillas y nombres con precio. Nerea miró el cuaderno de su madre '
                'y pensó en lo que alguien estaría dispuesto a pagarlo.'),
        ),
        dict(
            title='El mercado de los nombres',
            goal='rescue',
            biome='harbor',
            antagonist='Mercader Dorven',
            opening=(
                'Dorven comerciaba con tablillas capaces de conservar recuerdos. Una buceadora '
                'cautiva conocía la entrada de la máquina; el mercader la vendía junto con el nombre '
                'de su familia. Las tablillas guardan un recuerdo durante un año y un nombre durante '
                'tres, y se pagan en objetos: una carta náutica, un diente de ballena, la letra de '
                'una canción. El puesto ocupa el muelle viejo, entre cajas de sal y unos grilletes '
                'que él llama fianzas. Yara lleva seis '
                'años pagando una fianza que nadie firmó, y Dorven conserva su apellido como '
                'garantía. Llevarse la buceadora sin pagar cuesta la carta de navegación que el '
                'mercader ya ha pedido ver; pagarla cuesta firmar que hasta un apellido tiene '
                'precio. Con el alba, Dorven cierra trato y la jaula cambia de puerto.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: llega a la jaula del muelle, libera a la buceadora y escóltala hasta la bandera.'),
                ('companion', 'Podemos pagar. Llevas oro suficiente.'),
                ('hero', 'Y mañana venderá a otra. Hoy se termina su negocio.'),
                ('Mercader Dorven', 'El precio de la buceadora ya está puesto. Lo que no tiene precio es su apellido.'),
                ('hero', 'Pues lo compro yo, y después lo rompo.'),
                ('Mercader Dorven', 'Podéis romper la tablilla. El recuerdo ya está copiado. De eso vive el negocio.'),
                ('companion', 'En la tablilla de al lado hay un precio grabado encima de otro. Tres nombres raspados para hacer sitio a las cifras.'),
                ('Mercader Dorven', 'Los nombres ocupan sitio. Las cifras caben todas.'),
                ('hero', 'La buceadora conoce las cámaras inundadas. La necesitamos viva y con memoria.'),
                ('companion', 'La jaula tiene fondo de rejilla y debajo pasa un canal de dos palmos.'),
                ('hero', 'Entra por el canal y yo distraigo al mercader con una compra.'),
                ('narrator', 'Dorven tiene dos guardias y un perro. La jaula es de hierro, pero el fondo da al agua.'),
                ('Mercader Dorven', 'Si os lleváis a la buceadora os llevaréis su deuda. La firmé con el puerto.'),
                ('hero', 'Enséñame esa firma. Si es del puerto, la pagará el puerto.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Mercader Dorven', 'Una tablilla guarda un recuerdo un año y un nombre tres. Yo no robo nada: lo cuido hasta que alguien paga lo que vale cuidarlo.'),
                    ('narrator', 'La jaula de Yara da al canal por un fondo de rejilla, y Dorven ha dejado al perro en el muelle seco. Decide si entras por el agua con una unidad o lo distraes fingiendo una compra en el puesto.'),
                ]),
                ('turn 4', [
                    ('Mercader Dorven', 'El precio ha subido. Ahora quiero también la carta de navegación que lleváis.'),
                    ('hero', 'La carta es nuestra. Sube lo que quieras, pero no te la voy a enseñar.'),
                ]),
                ('village captured', [
                    ('narrator', 'En las cajas de sal hay tablillas envueltas en tela. Cada una lleva escrito un precio en el canto.'),
                    ('companion', 'Ninguna lleva nombre. Eso quiere decir que ya está borrado.'),
                ]),
                ('half strength', [
                    ('protected', 'No puedo correr. Dadme la mano y salimos juntas.'),
                    ('hero', 'La mano y el hombro. Tú marca el paso.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Los cajones de sal estrechan el paso hasta la larga de una lanza, y el perro huele el canal por dentro. Decide si abres la jaula por la rejilla o la rompes por el canto con el perro encima.'),
                    ('Mercader Dorven', 'La familia de la buceadora lleva seis años pagando una fianza que nadie firmó. Si os la lleváis sin pagar, esos seis años valen nada, y mañana media ciudad vendrá a por lo suyo.'),
                    ('hero', 'Mañana media ciudad tendrá lo suyo. Ese es el trato.'),
                ]),
                ('turn 8', [
                    ('companion', 'El perro no ladra a quien huele a sal. Eso nos deja una puerta abierta.'),
                    ('hero', 'Úsala. Y si vuelve el mercader, dile que estoy comprando.'),
                ]),
                ('enemy leader defeated', [
                    ('Mercader Dorven', 'Sin tablillas no hay recuerdos. Ahora tendréis que acordaros de todo vosotros solos.'),
                    ('hero', 'Es lo que hacíamos antes de conocerte.'),
                ]),
            ],
            victory=[
                ('protected', 'Mi nombre está en la tercera tablilla. La pagó un hombre que no me conoce.'),
                ('hero', 'Dámela. La leo en voz alta una vez y la quemo.'),
                ('companion', 'Las demás tablillas son de gente que aún duerme en el puerto. Las devolvemos mañana.'),
                ('protected', 'Mi familia paga la fianza desde hace seis años. Solo habían comprado el nombre, no la deuda.'),
                ('narrator', 'El puesto quedó cerrado con las tablillas dentro, y el perro se fue con la buceadora.'),
            ],
            protected=('Yara, buceadora', 'Mermaid Initiate'),
            resolution=(
                'La buceadora enseñó a Luar una ruta por las cámaras inundadas. A cambio pidió que '
                'nadie volviera a escribir un precio junto a su nombre. Antes de bajar marcó con '
                'brea la entrada del canal en la pared del muelle y escribió debajo una sola '
                'palabra: libre. La palabra duró hasta la siguiente pleamar. La ruta '
                'de Yara terminaba bajo la roca, ante tres compuertas que repartían la memoria '
                'robada del mar. Detrás de ellas aguardaban los centinelas que la máquina '
                'alimentaba, y abrirlas devolvería los nombres mezclados como sal.'),
        ),
        dict(
            title='Las compuertas del olvido',
            goal='beacons',
            biome='cave',
            antagonist='Guardián de la Sal',
            opening=(
                'Las tres compuertas distribuían la memoria robada. Abrirlas a la vez devolvería '
                'parte de ella, pero también liberaría a los centinelas que la máquina alimentaba. '
                'Están talladas en la roca y se abren con palancas de hueso. La primera guarda los '
                'nombres de los vivos, la segunda los de los muertos recientes y la tercera los que '
                'nadie reclamó. Los centinelas no atacan por orden: atacan porque la máquina los '
                'alimenta con lo que las compuertas sueltan. La primera '
                'palanca está al alcance de una mano; la tercera se abre desde el fondo de un pozo '
                'que se llena con la marea. Luar lleva el cordel todavía liso, sin un nudo puesto, '
                'y copiar los nombres cuesta tiempo de marea: abrir sin copiar cuesta perderlos '
                'todos, mezclados.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: abre las tres compuertas llevando una unidad a cada palanca.'),
                ('companion', 'Si escuchas a tu madre, no sigas su voz. Será un recuerdo buscando salida.'),
                ('hero', 'La escucharé. Y seguiré andando.'),
                ('Guardián de la Sal', 'Estas compuertas no se cierran para castigar. Se cierran para que el mar no se lleve todo de golpe.'),
                ('hero', '¿Y quién decide cuánto se lleva?'),
                ('Guardián de la Sal', 'La ley de la sal: lo que se suelta vuelve mezclado. Nadie recupera un nombre limpio.'),
                ('companion', 'Entonces los devolveremos despacio, uno por uno, con su dueño delante.'),
                ('Guardián de la Sal', 'Nadie tiene tiempo para eso. Tenéis una marea.'),
                ('narrator', 'En las paredes hay listas de nombres escritos con sal. Algunos están borrados con el pulgar.'),
                ('companion', 'Aquí abajo hay cordeles colgados. Manos que aprendieron a hacer nudos antes que a escribir.'),
                ('hero', 'Un cordel, un nombre. Si abrimos las compuertas, el agua se los lleva.'),
                ('Guardián de la Sal', 'Por eso no las abro yo. También son mi archivo.'),
                ('hero', 'Copiamos los nudos antes de abrir. Dos unidades por palanca y una copiando. Ese es el plan.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Guardián de la Sal', 'Detrás de estas compuertas no hay tesoros: hay nombres que nadie reclamó. Yo soy el último que los recuerda sin cuerda y sin nudos.'),
                    ('narrator', 'La cueva se inunda por el túnel de entrada y las tres palancas están en salas distintas; los centinelas saldrán con la primera compuerta. Decide si mandas una unidad por palanca o abres camino con todo el grupo.'),
                ]),
                ('beacon lit 1', [
                    ('narrator', 'La primera compuerta cede. El agua sube un palmo y arrastra una lista escrita con sal.'),
                    ('companion', 'Esa era la lista de los vivos. Ahora está en el suelo.'),
                ]),
                ('beacon lit 2', [
                    ('companion', 'Se me ha deshecho un nudo en la mano. Solo queda la cuerda lisa.'),
                    ('hero', 'Anota cuántos has copiado. Los que falten los preguntaremos en tierra.'),
                ]),
                ('beacon lit 3', [
                    ('narrator', 'La tercera compuerta se abre y miles de nombres salen con el agua hacia el túnel.'),
                    ('Guardián de la Sal', 'Ya no puedo cerrarlas. Ahora decide el mar.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Los centinelas empujan hacia el túnel que se inunda y el agua salada ya moja las listas de la pared. Decide si copias antes de abrir o abres antes de que suba.'),
                    ('Guardián de la Sal', 'Abrir las tres de golpe devuelve los nombres mezclados, y un nombre mezclado es como no tenerlo. Prefiero guardarlos mojados y a salvo a devolverlos perdidos.'),
                    ('hero', 'Los mezclados los ordenamos juntos. Primero los tuyos.'),
                ]),
                ('turn 8', [
                    ('Guardián de la Sal', 'Vuestra madre bajó aquí tres veces. La última traía un cuaderno y una cuerda.'),
                    ('hero', 'Entonces sabía lo que hacía. Nosotros también.'),
                ]),
                ('time limit', [
                    ('narrator', 'La marea entra por el túnel. Queda una ronda antes de que el agua cubra las palancas.'),
                    ('companion', 'Las compuertas aguantan abiertas. Salgamos por donde bajamos.'),
                ]),
            ],
            victory=[
                ('companion', 'He copiado noventa y cuatro nudos. El resto se han deshecho en mi mano.'),
                ('hero', 'Noventa y cuatro más de los que teníamos esta mañana.'),
                ('Guardián de la Sal', 'Habéis abierto mi archivo y no habéis robado nada. Eso no lo había visto nunca.'),
                ('hero', 'Volveremos con cuerdas nuevas. Guárdanos los nombres que puedas.'),
                ('narrator', 'Miles de nombres salieron con el agua y el túnel quedó en silencio por primera vez en cuarenta años.'),
            ],
            protected=None,
            resolution=(
                'Miles de nombres salieron con el agua. Nerea recordó unas manos enseñándole a hacer '
                'un nudo. Las manos estaban bajo la superficie y el nudo era el mismo que llevaba el '
                'cuaderno. Comprendió que su madre había bajado hasta allí más de una vez y que había '
                'dejado cordeles en las paredes para que alguien, algún día, pudiera deshacerlos. Arriba, sobre esa misma '
                'agua que ya devolvía nombres, Serkos amarraba los barcos que el mundo daba por '
                'perdidos. La única bandera que decía algo en todo el estrecho era la suya, y '
                'navegaba hacia el paso antes de que la marea cambiara.'),
        ),
        dict(
            title='La flota de nadie',
            goal='conquer',
            biome='coast',
            antagonist='Serkos, sin bandera',
            opening=(
                'Serkos reunió los barcos abandonados para apoderarse del mecanismo. Prometía mares '
                'tranquilos a quienes aceptaran olvidar la guerra que él mismo había iniciado. En '
                'cada casco ha mandado rascar el nombre y pintar encima una promesa: agua quieta, '
                'marea obediente, ninguna pérdida que recordar. Sus capitanes aceptan porque están '
                'cansados, no porque le crean, y la única bandera que aún dice algo en toda la flota '
                'es la suya. Su promesa pesa porque es '
                'verdad: la máquina todavía regala mares sin funerales, y cada nombre que se '
                'rasca de un casco se queda sin reclamar. Deshacer la flota cuesta el último '
                'trato del puerto con los barcos sin pasado. El estrecho se cierra con la marea, '
                'y la segunda línea ya acorta por el bajo.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: derrota a Serkos y deshaz su flota antes de que cruce el estrecho.'),
                ('companion', 'Hay capitanes dispuestos a creerle. Están cansados.'),
                ('hero', 'Les ofreceremos un puerto al que volver sin entregar su pasado.'),
                ('Serkos, sin bandera', 'Os di el mar en calma y me llamasteis ladrón. Ahora vengo a cobrarlo con barcos.'),
                ('hero', 'Un mar en calma que borra a su gente no es un mar. Es una bodega.'),
                ('Serkos, sin bandera', 'En mi flota nadie pregunta quién eras. Eso es libertad.'),
                ('companion', 'En los cascos habéis raspado los nombres. El nuestro sigue escrito, y por eso nos encontráis.'),
                ('hero', 'Ofreced a cada capitán un nombre para su barco. Es lo único que quieren.'),
                ('Serkos, sin bandera', 'Les ofrezco no perder a nadie más. Vosotros no podéis ofrecer eso.'),
                ('companion', 'Podemos ofrecer recordar a quien se pierda. Es distinto y es más.'),
                ('narrator', 'La flota avanza en dos líneas: delante los barcos sin nombre, detrás los que aún recuerdan.'),
                ('hero', 'Atacamos la segunda línea. Si los que recuerdan se rinden, los viejos no tendrán a quién seguir.'),
                ('Serkos, sin bandera', 'Mirad bien esa bandera. Es la única de la flota que dice algo, y dice mi nombre.'),
                ('hero', 'Entonces arriarla será lo primero que caiga.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Serkos, sin bandera', 'Cada nombre que rascamos de un casco es un duelo que no volverá a hacer falta. Yo vendo barcos sin historial y mares sin funerales.'),
                    ('narrator', 'La flota avanza en dos líneas y la delantera abre la rompiente para la otra. Decide si cortas la primera línea sobre el bajo o la dejas desviarse hacia los bajos del este.'),
                ]),
                ('turn 4', [
                    ('companion', 'En la campana del barco viejos han limado el nombre. La campana sigue sonando igual.'),
                    ('hero', 'Que la toquen ellos cuando quieran rendirse. Así la oímos todos.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Los barcos sin nombre navegan pegados a la estela del almirante, y los que aún recuerdan dudan en la segunda. Decide si divides tu flota en dos lances o embistes la línea de los que recuerdan.'),
                    ('Serkos, sin bandera', 'A mis capitanes les prometí un mar donde no haya que despedir a nadie. Vosotros ofrecéis recuerdos, y recordar es justo lo que a ellos ya no les cabe.'),
                    ('hero', 'Les ofrecemos nombres para sus barcos. Un duelo nombrado pesa menos que un duelo mudo.'),
                ]),
                ('turn 8', [
                    ('Serkos, sin bandera', 'Mis capitanes no luchan por mí. Luchan por no acordarse.'),
                    ('hero', 'Pues dales algo mejor que el olvido. Un puerto y un nombre en el registro.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la casa del práctico hay una tablilla con los nombres de los barcos del puerto. Cinco están raspados.'),
                    ('companion', 'Los apuntamos todos. Alguno volverá a flotar con su nombre puesto.'),
                ]),
                ('time limit', [
                    ('narrator', 'La segunda línea se repliega hacia el estrecho. Queda una ronda para cortarle el paso.'),
                    ('hero', 'Todas las velas al centro. No dejamos que cruce.'),
                ]),
                ('enemy leader defeated', [
                    ('Serkos, sin bandera', 'Sin bandera no hay almirante. Sin almirante no hay flota. Lo habéis entendido, ¿verdad?'),
                    ('hero', 'Lo hemos entendido. Y aun así te dejamos la bandera.'),
                ]),
            ],
            victory=[
                ('companion', 'Los barcos de la segunda línea han arriado velas.'),
                ('hero', 'Que cada capitán escriba el nombre de su barco antes de atracar.'),
                ('narrator', 'Un capitán tardó una hora en recordar el suyo. Los demás le esperaron sin decir nada.'),
                ('companion', 'Serkos está en la cubierta del barco sin nombre. Pide hablar contigo.'),
                ('hero', 'Que suba. Y que traiga la bandera, para devolvérsela a quien la cosió.'),
            ],
            protected=None,
            resolution=(
                'La flota se rindió cuando sus tripulantes recordaron quién había confiscado sus '
                'barcos. Serkos entregó su bandera sin discutir y pidió que se la devolvieran a la '
                'sastra del puerto, que la había cosido veinte años atrás. Nerea la colgó en la sala '
                'de cartas del puerto con el nombre del barco debajo, para que nadie tuviera que '
                'preguntar de quién era. Pero el camino hasta la máquina seguía '
                'pasando por un canal que los nagas habían tallado y custodiado desde antes de '
                'los barcos, y aquella misma noche llegó una emisaria con una llave de conchas y '
                'la vieja ley al hombro: quien cruza un paso prestado lo devuelve o lo paga. '
                'De aquella sala de cartas nació, al terminar las travesías, '
                'la escuela de navegación.'),
        ),
        dict(
            title='Un camino para los naga',
            goal='escort',
            biome='islands',
            antagonist='Custodia Eshka',
            opening=(
                'Una emisaria naga aceptó guiar a los isleños hasta el núcleo. Eshka, defensora de la '
                'vieja ley, prefería hundir los pasos antes que permitir que manos extranjeras los '
                'cruzaran. En el fondo del canal hay escalones tallados por manos naga hace siglos, y '
                'cada escalón tiene un nombre raspado y otro escrito encima. Issa habla por las '
                'comunidades que ya aceptaron apagar la máquina; Eshka responde por las que aún '
                'confían en ella. La llave de conchas abre '
                'la puerta del núcleo con dos vueltas y catorce comunidades a la espalda. Cruzar '
                'cuesta la vuelta, porque Eshka ha jurado hundir los escalones antes que verlos '
                'pisados por manos extranjeras; no cruzar cuesta a Issa las pocas aldeas que aún '
                'la escuchan. Al otro lado de los escalones espera la puerta del núcleo, y Eshka '
                'corre para llegar a ella antes que la fila.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: escolta a Issa hasta la bandera del núcleo. Si cae, el paso queda cerrado.'),
                ('companion', (
                    'La emisaria ha perdido más nombres que nosotros. Y aun así recuerda cómo '
                    'confiar.')),
                ('hero', 'No caminaremos delante de ella como conquistadores. Le cubriremos la espalda.'),
                ('protected', 'Mi gente guarda los pasos desde antes de que existieran los barcos. Es un oficio, no un trono.'),
                ('Custodia Eshka', 'Issa, has vendido el arrecife por un puñado de nombres extranjeros.'),
                ('protected', 'He traído a quien puede apagar la máquina. Eso no es vender, es terminar un contrato.'),
                ('Custodia Eshka', 'La ley dice que un paso se cierra desde dentro. Y yo estoy dentro.'),
                ('hero', 'También están dentro vuestras crías, en las pozas del norte, con los nombres ya borrados.'),
                ('Custodia Eshka', 'Eso lo sé mejor que tú. Los primeros borrados fuimos nosotros.'),
                ('protected', 'Entonces caminemos juntos, y que nadie más elija entre su ley y su familia.'),
                ('companion', 'Hay dos pasos: los escalones y el canal profundo. El canal es más rápido y más oscuro.'),
                ('hero', 'Vamos por los escalones. Issa marca el ritmo y nosotros cerramos la fila.'),
                ('Custodia Eshka', 'No os atacaré en los escalones. Os atacaré donde la ley me obligue: en la puerta.'),
                ('protected', 'Esa puerta la conozco. Tiene un cerrojo de conchas y una sola llave.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Custodia Eshka', 'Quien nombra un paso lo posee, y este lo nombraron las mías cuando aún no había barcos. Vosotros lo cruzáis prestado, y lo prestado se devuelve o se paga.'),
                    ('narrator', 'El canal tiene dos vías: los escalones tallados, abiertos y estrechos, y la zanja honda, oscura pero sin vigías. Eshka guarda la puerta final y no el camino: decide quién marca el ritmo, Issa por los escalones o Luar por la zanja.'),
                ]),
                ('turn 4', [
                    ('protected', 'En el escalón sexto hay un nombre raspado y otro escrito encima con una concha.'),
                    ('companion', 'Lo copio con un nudo. Si el agua sube, al menos queda la cuenta.'),
                ]),
                ('half strength', [
                    ('protected', 'Me han dado en la aleta. Seguid, yo cierro la fila.'),
                    ('hero', 'Nadie cierra nada. Luar, cógela del brazo y sube con ella.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Con cada marea los escalones se cubren y aprietan la fila. Decide si subes a Issa a hombros, que gana un turno, o la dejas marcar el paso con su aleta.'),
                    ('Custodia Eshka', 'Las aldeas que me siguen viven de la calma que la máquina todavía les paga. Si la apagáis, seré yo quien tenga que explicarles el hambre, y empezaré explicándoselo a la que la trajo.'),
                    ('hero', 'Se lo explicarás a todos. A ella la cubro yo.'),
                ]),
                ('turn 8', [
                    ('Custodia Eshka', 'La puerta tiene dos lados. Al que la cruce primero lo llamarán traidor.'),
                    ('protected', 'Entonces cruzo yo primero. La traición es un nombre que ya llevo puesto.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la poza del norte las crías naga nadan en círculo alrededor de una piedra sin inscripción.'),
                    ('hero', 'Esa piedra tenía un nombre. Lo escribiremos antes de irnos.'),
                ]),
                ('time limit', [
                    ('narrator', 'La corriente cambia en el canal. Queda una ronda para cruzar la puerta.'),
                    ('companion', 'Issa está cerca. Nadie la suelta ahora.'),
                ]),
            ],
            victory=[
                ('protected', 'La llave tiene catorce conchas. Cada una es una comunidad que dijo sí.'),
                ('hero', '¿Y la que falta?'),
                ('protected', 'Falta la de mi propia aldea. La añadiré cuando volvamos con la máquina apagada.'),
                ('companion', 'Eshka se ha quedado en la puerta. No ha cruzado.'),
                ('narrator', 'La emisaria entregó la llave y pidió que la primera vuelta la diera un humano, para que la ley quedara cumplida por las dos partes.'),
            ],
            protected=('Issa, emisaria del arrecife', 'Naga Fighter'),
            resolution=(
                'Al llegar, la emisaria entregó una llave hecha de conchas. Cada concha representaba '
                'una comunidad que había aceptado apagar la máquina. Nerea la pesó en la mano y la '
                'encontró ligera; Issa le explicó que las llaves naga no pesan por lo que abren, sino '
                'por lo que prometen. Añadieron su concha al final, con el nombre de la aldea escrito '
                'por dentro. La cerradura dio dos vueltas y la puerta '
                'del núcleo cedió hacia una sala de bronce. Dentro, algo repetía una orden grabada '
                'y esperaba a que alguien la firmara de nuevo.'),
        ),
        dict(
            title='El último mar en calma',
            goal='survive',
            biome='ruins',
            antagonist='Centinela del Núcleo',
            opening=(
                'Apagar el núcleo exigía mantener sus válvulas abiertas durante un ciclo completo. '
                'Los centinelas interpretaron la maniobra como una avería y atacaron a quienes la '
                'ejecutaban. El que guarda la sala no tiene nombre ni ley: repite una orden grabada '
                'en bronce. En la placa de los constructores el último renglón está raspado y vuelto '
                'a raspar con una uña, y debajo se adivina una fecha: el año en que empezaron las '
                'mareas quietas. Mantener las válvulas '
                'abiertas cuesta las tormentas que estas islas llevan veinte años sin saber '
                'enterrar, y cerrarlas devuelve una calma que se cobra en nombres ajenos. Y en '
                'medio queda la orden de bronce, que hará lo único que sabe hasta el último '
                'turno.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('narrator', 'Objetivo: mantén a Nerea con vida hasta el comienzo del turno doce. Las válvulas deben seguir abiertas.'),
                ('companion', 'Después habrá tormentas. No podremos prometer que todos regresen de cada viaje.'),
                ('hero', 'Podremos prometer que los recordaremos.'),
                ('Centinela del Núcleo', 'Orden: mantener el mar en calma. No consta ninguna excepción.'),
                ('hero', 'La excepción está escrita en tu propia placa. Mírala.'),
                ('Centinela del Núcleo', 'La placa está incompleta. La orden no lo está.'),
                ('companion', 'El renglón raspado llevaba un nombre. Debajo hay una fecha, y la fecha es el año en que el mar se quedó quieto.'),
                ('hero', 'Ese nombre es el de mi madre. Firmó la máquina y luego intentó pararla. Las dos cosas caben en la placa.'),
                ('narrator', 'Las válvulas están en tres salas. Una unidad por válvula y el grupo de Nerea aguantando el centro.'),
                ('companion', 'Los centinelas no se cansan. Nosotros sí. Relevad a la gente cada cuatro turnos.'),
                ('hero', 'Los heridos al pasillo del agua dulce. Hasta allí no llegan.'),
                ('Centinela del Núcleo', 'Habéis venido a apagar lo que dio de comer a estas islas. Contadlo también.'),
                ('hero', 'Lo contaremos todo. Empezando por lo que costó.'),
                ('narrator', 'Si las válvulas se cierran, el núcleo vuelve a arrancar. No cedáis el centro.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Centinela del Núcleo', 'Orden grabada: mantener el mar en calma. Quien empezó la excepción no la terminó de escribir, y lo que no está escrito no me obliga.'),
                    ('narrator', 'Las válvulas están en tres salas y el núcleo ocupa el centro sin un solo parapeto, que es justo lo que los centinelas quieren. Decide si cubres las tres válvulas a la vez o defiendes el centro con todo el grupo.'),
                ]),
                ('turn 4', [
                    ('companion', 'En la placa de bronce hay cuatro nombres de constructores y un quinto raspado.'),
                    ('hero', 'Adivino cuál es. Sigue leyendo, que yo cubro la puerta.'),
                ]),
                ('turn 6', [
                    ('narrator', 'Los centinelas entran por los dos pasillos y empujan hacia las válvulas sin descanso. Decide cada cuánto relevas a los heridos en el pasillo de agua dulce: en dos turnos sin relevo no quedará nadie para girarlas.'),
                    ('Centinela del Núcleo', 'Este núcleo dio de comer a estas islas durante veinte años, y mi orden lo recuerda aunque vosotros hayáis decidido olvidarlo. Mañana cerraré las válvulas y devolveré la calma.'),
                    ('hero', 'Mañana habrá olas. Guárdame esa orden para cuando aprendas a romperla.'),
                ]),
                ('turn 8', [
                    ('Centinela del Núcleo', 'Vuestra madre raspó su nombre para que la máquina no la reclamara. Sigue reclamándola.'),
                    ('hero', 'Entonces volveré a escribirlo, y que reclame lo que quiera.'),
                ]),
                ('turn 10', [
                    ('narrator', 'Los centinelas han tomado el pasillo oeste. El centro de la sala queda expuesto.'),
                    ('companion', 'Dos heridos fuera y una válvula sin relevo. Aguanta tres turnos más.'),
                ]),
                ('time limit', [
                    ('narrator', 'Última ronda. Las válvulas siguen abiertas y el núcleo aún no ha vuelto a arrancar.'),
                    ('hero', 'Nadie se mueve del centro. Ni un paso.'),
                ]),
            ],
            victory=[
                ('companion', 'El núcleo se ha enfriado. No ha hecho ruido al morir.'),
                ('hero', 'Mi madre raspó su nombre aquí. Deberíamos volver a escribirlo.'),
                ('Centinela del Núcleo', 'Sin orden no tengo función. ¿Qué se hace cuando el mar deja de obedecer?'),
                ('hero', 'Se aprende a nadar.'),
                ('narrator', 'Por primera vez en décadas, una ola rompió sin obedecer a una máquina.'),
            ],
            protected=None,
            resolution=(
                'El núcleo se enfrió. Por primera vez en décadas, una ola rompió sin obedecer a una '
                'máquina. Nerea raspó la sal de la placa hasta encontrar el renglón borrado y '
                'escribió encima el nombre de su madre, Aldara Vado, con la punta de un cuchillo. '
                'Luar añadió la fecha. El centinela miró hacerlo y no dijo nada, porque ya no tenía '
                'orden que recitar. Luego bajó la '
                'marea natural, la primera en veinte años, y se metió por las galerías sin pedir '
                'permiso. Al final de la última galería esperaban las barcas, y entre Nerea y '
                'ellas quedaba un custodio que ya no tenía nada que guardar.'),
        ),
        dict(
            title='Nombres sobre el agua',
            goal='escape',
            biome='harbor',
            antagonist='Último Custodio',
            opening=(
                'Las galerías se inundaron cuando regresó la marea natural. El último custodio quiso '
                'retener a Nerea para reiniciar el mecanismo. Las barcas aguardaban más allá de los '
                'muelles partidos. No viene a matar: viene a buscar la mano de quien conoce la firma, '
                'porque cree que Nerea es la única que puede volver a darla. El agua sube a la altura '
                'de la rodilla y el tablero de nombres del puerto aún cuelga de dos clavos. El custodio no '
                'empuña una lanza siquiera: busca la mano que sabe la firma y cree que sin ella '
                'el mar se quedará huérfano de calma. Salir cuesta dejar el puerto sin nadie que '
                'sepa volver a arrancar la máquina; quedarse cuesta firmar por su madre una '
                'segunda vez. Las barcas sueltan amarras con la marea, y los dos clavos del '
                'tablero no durarán otra.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Tu madre dejó una salida en los planos. La dibujó incluso cuando pensaba '
                    'quedarse.')),
                ('hero', 'Entonces la usaremos. Su historia no tiene que terminar dos veces igual.'),
                ('narrator', 'Objetivo: lleva a Nerea hasta la bandera del muelle alto. Después de esa bandera solo queda mar abierto.'),
                ('Último Custodio', 'Tu madre firmó el arranque y nadie volvió a firmar. Solo falta tu mano.'),
                ('hero', 'Mi mano escribe nombres, no contratos.'),
                ('Último Custodio', 'Sin contrato no hay calma. Vuestras islas vivirán con miedo al agua.'),
                ('companion', 'Con miedo y con nombres. Prefiero eso.'),
                ('hero', 'Que cada isla decida. Nosotros solo abrimos la puerta.'),
                ('narrator', 'Las galerías se inundan en dos rondas. La salida está en el muelle alto y el agua ya cubre los primeros escalones.'),
                ('companion', 'Hay dos pasos: el de los planos y el del desagüe. El de los planos está vigilado.'),
                ('hero', 'Vamos por el de los planos. Quiero que vea lo que dibujó mi madre.'),
                ('Último Custodio', 'El cuaderno no os salvará. Ya no queda nadie que sepa leer esa tinta.'),
                ('hero', 'Quedan dos. Y una de ellas va a salir de aquí.'),
                ('narrator', 'En el muelle hay barcas cargadas. No te detengas a discutir con nadie.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('Último Custodio', 'Esa mano vale más escribiendo la firma que nadando hacia las barcas. La calma que vuestras islas van a echar de menos solo sale de ella.'),
                    ('narrator', 'Las galerías se inundan por los dos extremos y el paso de los planos está vigilado arriba. Decide si aguantas la subida por los planos, donde te verán venir, o bajas por el desagüe, que se llena en dos rondas.'),
                ]),
                ('turn 4', [
                    ('narrator', 'El agua sube un escalón más. El tablero de nombres del puerto queda a la altura de los ojos.'),
                    ('companion', 'Las letras están rascadas. Alguien quitó su nombre con una piedra.'),
                ]),
                ('turn 6', [
                    ('narrator', 'El custodio empuja el tablero para cortar el pasillo, y el tablero se desprende de un clavo a cada ronda. Decide si lo aguantas con una unidad o corres por debajo mientras aún cuelga.'),
                    ('Último Custodio', 'He guardado veinte años este puerto vacío porque alguien tenía que quedarse cuando todos se marchaban. Ahora me quedo sin orden y sin nombre: dejadme al menos la copia del cuaderno.'),
                    ('hero', 'La copia se queda donde cualquiera pueda leerla. Ni un paso más.'),
                ]),
                ('turn 8', [
                    ('Último Custodio', 'Vuestra madre me pidió que la detuviera si volvía. Estoy cumpliendo su palabra.'),
                    ('hero', 'Cumpliste. Yo también cumplo la mía, y la mía dice que salgamos todos.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la caseta del práctico hay un cuaderno de bitácora con las últimas páginas arrancadas.'),
                    ('hero', 'Las arrancó alguien que quería olvidar. Nosotros escribiremos encima.'),
                ]),
                ('time limit', [
                    ('narrator', 'Las barcas sueltan amarras. Última llamada desde el muelle alto.'),
                    ('companion', 'Falta la tuya. Suelta el cabo y salta.'),
                ]),
                ('enemy leader defeated', [
                    ('Último Custodio', 'Dejadme una copia del cuaderno. Alguien tendrá que detener lo que venga después.'),
                    ('hero', 'Te dejo la copia con los nombres escritos. Ese es el cambio.'),
                ]),
            ],
            victory=[
                ('companion', 'Las barcas están fuera de la dársena. Falta la tuya.'),
                ('hero', 'Sube tú. Yo suelto el amarre.'),
                ('Último Custodio', 'Guardad el cuaderno donde se pueda leer. Aunque nadie sepa la tinta.'),
                ('hero', 'Aprenderán. Eso también se enseña.'),
                ('companion', 'Nadie se queda atrás con una vela sin izar.'),
                ('narrator', 'Nerea subió a la última barca y el muelle alto se hundió detrás de ella sin hacer ruido.'),
            ],
            protected=None,
            resolution=(
                'Nerea salió a un mar difícil y libre. En el cuaderno escribió el nombre de cada '
                'persona que había vuelto con ella, y después añadió los de quienes no volvieron y el '
                'de su madre al final, con letra clara para que nadie tuviera que adivinar. El '
                'cuaderno se mojó en la primera página, y esa fue la única tinta que se perdió. Delante '
                'de las barcas, las islas iban diciendo sus nombres en voz alta, unos por otros, '
                'hasta que el mar los devolvió escritos. Nerea los apuntó todos en el margen: un '
                'nombre nombrado a tiempo ya no lo borra ninguna marea.'),
        ),
    ],
)
