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
                'Todos los nombres desaparecieron de las cartas del puerto. Vaska arrestó al único '
                'piloto que aún recordaba la salida y vendió permisos de navegación imposibles de '
                'usar. En el registro de la aduana cada isla figura como «sin designar» y cada barco '
                'como carga de valor variable. Ciro está en la celda del muelle con las manos atadas '
                'y una tablilla de precios colgada del cuello, sin una sola letra de su calle. Desde '
                'la torre, la marea sube con una calma que no le corresponde.'),
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
                ('turn 4', [
                    ('narrator', 'El agua cubre el primer escalón de la celda. Alguien ha abierto las compuertas del arrecife.'),
                    ('Recaudadora Vaska', 'No he sido yo. La máquina mantiene el mar quieto y cobra lo que nadie usa.'),
                ]),
                ('half strength', [
                    ('protected', 'No puedo correr. Dejadme con la tablilla y salid vosotros.'),
                    ('hero', 'La tablilla pesa menos que tú. Camina y no discutas con quien te saca de una celda.'),
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
                'libro y se marchó del puerto sin que nadie le pidiera el permiso.'),
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
                'marcada con una bandera.'),
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
                ('turn 4', [
                    ('companion', 'Sus lanzas se mueven con la resaca, no contra ella. Están dejando pasar el agua.'),
                    ('hero', 'Aprovecha el hueco. Cuenta hasta tres y corre.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la cala hay una pizarra de pescadores con seis nombres y un séptimo borrado a mano.'),
                    ('companion', 'El séptimo nudo. Aquí también les falta alguien.'),
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
                'que alguien ataba un nombre en lugar de cortarlo.'),
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
                'tinta, y alguno tiene la marca de un pulgar reciente.'),
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
                'volviera a cubrirla; Issar lo miró hacerlo y no lo impidió.'),
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
                'levantar la cal.'),
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
                ('turn 4', [
                    ('narrator', 'Refuerzos por el embarcadero. Serkos ha mandado abrir el almacén de armas.'),
                    ('companion', 'Dos barcas con gente armada. Cuento veinte remos.'),
                ]),
                ('village captured', [
                    ('narrator', 'En la caseta del muelle hay una etiqueta de equipaje con un precio y ninguna letra de nombre.'),
                    ('hero', 'La guardamos. Servirá de prueba cuando alguien pregunte por los baúles.'),
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
                'cuaderno seguía existiendo; Nerea tardó en contestar.'),
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
                'sabe deshacer.'),
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
                'temiera perderlo antes de terminar de escribir.'),
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
                'hasta el alba para embarcar a todos.'),
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
                ('turn 4', [
                    ('narrator', 'Tres familias a bordo y la cala ya huele a humo. Uss ha cortado las redes del muelle.'),
                    ('companion', 'Sin redes no hay excusa para quedarse. Empujad las barcas.'),
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
                'ninguno tenía nombre, porque ya nadie recordaba cómo se llamaba la cala.'),
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
                'que él llama fianzas.'),
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
                'palabra: libre. La palabra duró hasta la siguiente pleamar.'),
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
                'alimenta con lo que las compuertas sueltan.'),
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
                'dejado cordeles en las paredes para que alguien, algún día, pudiera deshacerlos.'),
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
                'es la suya.'),
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
                ('turn 4', [
                    ('companion', 'En la campana del barco viejos han limado el nombre. La campana sigue sonando igual.'),
                    ('hero', 'Que la toquen ellos cuando quieran rendirse. Así la oímos todos.'),
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
                'preguntar de quién era. De aquella sala de cartas nació, al terminar las travesías, '
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
                'confían en ella.'),
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
                ('turn 4', [
                    ('protected', 'En el escalón sexto hay un nombre raspado y otro escrito encima con una concha.'),
                    ('companion', 'Lo copio con un nudo. Si el agua sube, al menos queda la cuenta.'),
                ]),
                ('half strength', [
                    ('protected', 'Me han dado en la aleta. Seguid, yo cierro la fila.'),
                    ('hero', 'Nadie cierra nada. Luar, cógela del brazo y sube con ella.'),
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
                'por dentro.'),
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
                'mareas quietas.'),
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
                ('turn 4', [
                    ('companion', 'En la placa de bronce hay cuatro nombres de constructores y un quinto raspado.'),
                    ('hero', 'Adivino cuál es. Sigue leyendo, que yo cubro la puerta.'),
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
                'orden que recitar.'),
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
                'de la rodilla y el tablero de nombres del puerto aún cuelga de dos clavos.'),
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
                ('turn 4', [
                    ('narrator', 'El agua sube un escalón más. El tablero de nombres del puerto queda a la altura de los ojos.'),
                    ('companion', 'Las letras están rascadas. Alguien quitó su nombre con una piedra.'),
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
                'cuaderno se mojó en la primera página, y esa fue la única tinta que se perdió.'),
        ),
    ],
)
