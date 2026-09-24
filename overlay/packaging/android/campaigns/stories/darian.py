"""El pacto de las siete brasas — Darian de Linde. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='darian',
    title='El pacto de las siete brasas',
    hero='Darian de Linde',
    companion='Ena',
    companion_type='White Mage',
    race='human',
    recruit='Spearman,Bowman,Mage,Elvish Fighter,Elvish Shaman',
    enemy='undead',
    length='Épica · 16 escenarios · 12–18 horas',
    premise=(
        'Un correo transporta siete cartas para pueblos que no confían entre sí. Mientras el imperio '
        'de Maura reclama vivos y muertos, Darian debe construir una alianza entre puertos libres, '
        'litarios, velarios y antiguos enemigos. Se puede jugar sin completar las otras cinco '
        'campañas.'),
    ending=(
        'Las siete brasas no se fundieron en una corona. Cada pueblo conservó una, y el pacto exigía '
        'que cualquier decisión pudiera ser rechazada. Darian volvió al camino con una bolsa más '
        'ligera: por primera vez llevaba respuestas en vez de ultimátums.'),
    chapters=[
        dict(
            title='Siete cartas, ningún rey',
            goal='escape',
            biome='forest',
            antagonist='Recaudador de Ceniza',
            opening=(
                'Darian salió de Linde con siete cartas y un caballo que perdió en el primer control '
                'imperial. Las cartas proponían reunir a quienes Maura todavía no había sometido. '
                'Ninguna llevaba un sello real. El control estaba en el bosque de Alda, donde los '
                'alguaciles del Recaudador de Ceniza registraban hasta las sillas de montar. Bastaba '
                'una carta sin sello para declarar espía a quien la llevara. Ena contó los puestos de '
                'guardia y Darian eligió un paso que nadie vigilaba. Ninguno de los dos sabía todavía '
                'que aquellas siete cartas iban a ser contestadas por siete pueblos distintos.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Sin un rey detrás, dirán que no representamos a nadie.'),
                ('hero', 'Representamos a quienes todavía pueden responder que no.'),
                ('narrator', 'Objetivo: cruzad el bosque de Alda y llevad a Darian y a Ena hasta la '
                             'bandera del arroyo, al este.'),
                ('antagonist', 'Toda carta sin sello imperial es contrabando. Entregadla y os dejaré '
                               'seguir con el caballo que os queda.'),
                ('hero', 'No llevamos caballos ni sellos. Solo preguntas que nadie ha querido leer.'),
                ('Sela', 'Puedo guiaros por el paso del arroyo, con una condición: nada de fuegos en '
                         'el bosque. La última columna imperial quemó dos aldeas para no dejar '
                         'testigos.'),
                ('hero', 'Aceptada. Si alguien enciende una antorcha, será para devolverla apagada.'),
                ('Sela', '¿Y si respondo que no a vuestro pacto? No he jurado nada a nadie.'),
                ('hero', 'Entonces os dejamos las cartas y seguimos camino. Un pacto que no se puede '
                         'rechazar es una leva con otro nombre.'),
                ('companion', 'Siete cartas, siete puertas. La primera persona que las lea decidirá si '
                              'somos correos o culpables.'),
                ('narrator', 'El Recaudador ha apostado ballesteros en los tres vados. El paso del '
                             'arroyo sigue libre porque nadie lo cree transitable.'),
                ('Sela', 'Los imperiales cobran por cada carta requisada. Mi hermano trabaja en su '
                         'registro y volvió a casa con las manos manchadas de tinta.'),
                ('hero', 'Cuando salgamos del bosque, escribirás tú la respuesta. La firmamos los dos '
                         'o no la firma nadie.'),
                ('companion', 'Puedo curar heridas, no silencios. Si disparan primero, no prometas '
                              'clemencia a los ballesteros.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 3', [
                    ('antagonist', 'Cerrad el paso. Prefiero un correo muerto a una provincia que '
                                   'aprenda a escribir.'),
                    ('narrator', 'Los ballesteros avanzan hacia el arroyo. La salida queda al este de '
                                 'la bandera.'),
                ]),
                ('village captured', [
                    ('Sela', 'Ese molino es lo único que queda en pie. Si lo usáis de fortaleza, sus '
                             'dueños perderán la cosecha.'),
                    ('hero', 'Lo usaremos como puesto de agua y nada más. Anotadlo en la carta de '
                             'Sela.'),
                ]),
                ('turn 6', [
                    ('companion', 'Las cartas pesan menos que un herido. Dadme dos turnos para '
                                  'vendarlos.'),
                    ('hero', 'Tómalos. Si el Recaudador llega antes, negociaré con él hasta que '
                             'termines.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El registro de cartas requisadas cayó al arroyo. La corriente se '
                                 'llevó los nombres antes de que nadie pudiera leerlos.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que el cerco se cierre del todo. La '
                                 'bandera del arroyo sigue al este.'),
                ]),
            ],
            victory=[
                ('Sela', 'Conozco el paso desde niña. Ningún imperial lo ha cruzado nunca.'),
                ('hero', 'Entonces serás la primera persona que reciba su carta en mano.'),
                ('Sela', 'No prometo firmar. Prometo leerla delante de mi aldea.'),
                ('companion', 'No pedimos más. La respuesta también puede ser no.'),
                ('narrator', 'En el margen del mapa, Darian escribió una sola línea: primera entrega, '
                             'sin firma.'),
            ],
            protected=None,
            resolution=(
                'Ena salvó las cartas de una acequia. La primera estaba dirigida a una ciudad que el '
                'mar ya se había llevado, y su destinatario había muerto antes de abrirla. Darian no '
                'la reescribió: anotó al dorso que el pacto debía alcanzar también a quienes ya no '
                'podían contestar. Sela guardó el pliego en un zurrón de cuero y prometió leerlo en '
                'voz alta ante su aldea.'),
        ),
        dict(
            title='La luz que emigró',
            goal='survive',
            biome='harbor',
            antagonist='Teniente del Tributo',
            opening=(
                'Los supervivientes de Valdara habían construido un puerto nuevo. Alba aceptó leer la '
                'carta si Darian ayudaba a defender a los recién llegados de los cobradores de '
                'cuerpos del imperio. El puerto se levantaba sobre pilotes, sin murallas, con una '
                'lámpara encendida por cada familia que el mar había devuelto. El Teniente del '
                'Tributo llamaba a eso una ciudad sin dueño y traía listas para demostrarlo. Cada '
                'barca que atracaba añadía un nombre a sus registros y una razón más para cobrar.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Alba no necesita promesas. Necesita tiempo para desembarcar familias.'),
                ('hero', 'Entonces nuestra primera firma se ganará aquí, junto a las barcas.'),
                ('Alba', 'La carta dice que el pacto defenderá a los puertos libres. Yo pregunto cómo '
                         'vais a defender un puerto sin murallas.'),
                ('hero', 'Con barcos y con camas. Si el precio de la alianza es una muralla, hoy no '
                         'firmamos nada.'),
                ('Alba', 'Firmaré cuando cumpláis dos condiciones: que ningún cobrador toque a quien '
                         'ya ha desembarcado y que no levantéis un muro alrededor de mi puerto.'),
                ('hero', 'Aceptadas las dos. Las escribiréis con vuestra letra en la carta.'),
                ('narrator', 'Objetivo: mantened a Darian y a Ena con vida hasta el comienzo del turno '
                             '12, mientras las familias terminan de desembarcar.'),
                ('antagonist', 'El imperio reclama a los muertos de Valdara y a los vivos que los '
                               'enterraron. Pagad la tasa o entregadme diez barcas.'),
                ('Alba', 'El mar se llevó la ciudad entera. ¿Vais a cobrarme también por el agua?'),
                ('companion', 'Cada barca que atracamos se convierte en una familia que el imperio '
                              'querrá registrar.'),
                ('Alba', 'Y si digo que no a vuestra alianza, ¿qué haréis? ¿Incendiar mi puerto?'),
                ('hero', 'Nos iremos con las barcas vacías. El pacto solo sirve si cada pueblo puede '
                         'seguir diciendo no.'),
                ('Alba', 'Hay tres muelles. El del faro está libre porque los cobradores le tienen '
                         'miedo a la luz.'),
                ('hero', 'Entonces defenderemos el muelle del faro. Que traigan sus listas y las lean '
                         'a la vista de todos.'),
                ('companion', 'Puedo encender lámparas, no romper contratos. Las heridas se curan; '
                              'las deudas, no.'),
                ('narrator', 'El Teniente avanza por el muelle largo. Sus hombres llevan cadenas '
                             'vacías, medidas para cuerpos que aún respiran.'),
                ('Alba', 'Oren y yo aprendimos a contar barcas antes que deudas. Si sobrevivimos al '
                         'turno doce, la carta tendrá respuesta.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He comprado el muelle corto. Cada familia que baje por él queda '
                                   'registrada como propiedad del imperio.'),
                    ('narrator', 'Los desembarcos siguen por el muelle del faro. El corto está '
                                 'cortado por cadenas.'),
                ]),
                ('turn 6', [
                    ('Alba', 'Los recién llegados no saben remar. Dadme dos turnos y pondré a los '
                             'suyos en los remos.'),
                    ('hero', 'Tómalos. Defenderemos tu muelle mientras enseñas a tu gente.'),
                ]),
                ('village captured', [
                    ('narrator', 'La primera casa del puerto izó una lámpara encendida. Esa lámpara '
                                 'marca a los vuestros como refugiados, no como carga.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'No era una tasa. Era un registro para saber a quién llamar '
                                   'cuando llegue la reina.'),
                    ('narrator', 'El libro de registros quedó abierto sobre la pasarela, con las '
                                 'hojas mojadas y los nombres ilegibles.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos para completar el desembarco. Mantened la '
                                 'posición junto a los muelles.'),
                ]),
            ],
            victory=[
                ('Alba', 'Las familias están en tierra. No he firmado nada todavía.'),
                ('hero', 'Lo sé. La carta espera en tu mesa y la respuesta es tuya.'),
                ('Alba', 'Mi condición se mantiene: barcos y camas, ninguna muralla.'),
                ('companion', 'La anotamos con tu letra y no con la nuestra, para que se lea igual '
                              'dentro de cien años.'),
                ('narrator', 'Alba encendió una lámpara sobre la carta antes de guardarla. La segunda '
                             'entrega quedó marcada con luz, no con sello.'),
            ],
            protected=None,
            resolution=(
                'Alba encendió una lámpara sobre la carta: el puerto aportaría barcos y refugio, pero '
                'no aceptaría volver a ser un muro que encerrara a su gente. Esa misma noche los '
                'recién llegados preguntaron si podían devolver el favor remando. El Teniente había '
                'anotado sus nombres en un registro; el puerto respondió escribiéndolos en una lista '
                'de vecinos, que cualquiera podía leer y tachar.'),
        ),
        dict(
            title='La puerta que escucha',
            goal='beacons',
            biome='mountain',
            antagonist='Tasador de las Vetas',
            opening=(
                'La entrada de los litarios solo se abría cuando tres resonadores repetían una '
                'petición sin órdenes. Los tasadores imperiales rodeaban el valle para apropiarse de '
                'sus cámaras de nacimiento. Sira de las Siete Vetas vigilaba la puerta desde dentro y '
                'Tarek del Eco contaba las columnas enemigas desde la ladera. El imperio había '
                'tasado la montaña veta por veta y había clavado postes con precios hasta la nieve. '
                'Los litarios no pedían ejército: pedían que alguien escuchara tres veces la misma '
                'pregunta.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Podrías exigir entrada en nombre de la alianza.'),
                ('hero', 'Todavía no existe una alianza. Empecemos por pedir permiso.'),
                ('Sira', 'La puerta repite lo que oye. Si le habláis de ejércitos, os responderá con '
                         'piedra.'),
                ('Tarek', 'Los tres resonadores deben repetir una petición sin órdenes. Si uno solo '
                          'manda, la puerta se cierra durante un siglo.'),
                ('narrator', 'Objetivo: llevad una unidad a cada resonador del valle y activad los '
                             'tres puntos.'),
                ('antagonist', 'El imperio tasa las vetas de esta montaña. Las cámaras de nacimiento '
                               'son un yacimiento, y sus habitantes, mineral.'),
                ('Sira', 'Os dejo pasar con una condición: ninguna de vuestras cartas se leerá dentro '
                         'de las cámaras. Lo que allí se dice no viaja.'),
                ('hero', 'Aceptado. Y si alguno de los míos lo olvida, lo atará Sira, no yo.'),
                ('Tarek', 'Y si mi consejo responde que no a vuestro pacto, ¿volveréis con espadas?'),
                ('hero', 'Volveré con la misma pregunta. El pacto incluye el derecho a rechazarlo.'),
                ('companion', 'Los tasadores traen cadenas de medir, no de portar. Aun así vienen '
                              'armados.'),
                ('Sira', 'Los resonadores están en las laderas. El del este tiene guardia; los otros '
                         'dos llevan años apagados.'),
                ('Tarek', 'Cuando la puerta oiga tres veces la misma petición se abrirá un paso '
                          'pequeño. No esperéis un ejército: solo cabe una fila.'),
                ('narrator', 'El Tasador de las Vetas ya ha clavado sus postes en el valle. Cada poste '
                             'lleva un número y un precio.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('Sira', 'El primer resonador repite vuestra voz. Ahora la montaña ya sabe que '
                             'habéis venido.'),
                    ('narrator', 'Dos puntos siguen apagados en las laderas del norte y del este.'),
                ]),
                ('beacon lit 2', [
                    ('antagonist', 'Seguid encendiendo piedras. Cada una que activéis me dice cuánto '
                                   'vale.'),
                ]),
                ('turn 5', [
                    ('Tarek', 'La guardia del este baja hacia el segundo punto. Si llega antes, lo '
                              'apagará con agua.'),
                    ('hero', 'Que llegue tarde. Nosotros vamos por la ladera alta.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'Los postes cayeron y las cadenas de medir quedaron tendidas en la '
                                 'nieve, señalando un valle sin precio.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que el tasador cierre el desfiladero. '
                                 'El último resonador sigue en la ladera.'),
                ]),
            ],
            victory=[
                ('Sira', 'La puerta pequeña está abierta. Nadie ha tenido que dar una orden.'),
                ('hero', 'Guardad la carta y contestadla cuando queráis.'),
                ('Sira', 'Los litarios enviarán guardianes si el pacto reconoce que una montaña puede '
                         'pertenecer a sus habitantes.'),
                ('Tarek', 'No hemos jurado nada. Solo hemos escuchado tres veces lo mismo.'),
                ('narrator', 'La primera respuesta del valle fue una piedra que repitió, sin cambiar '
                             'una palabra, la petición de Darian.'),
            ],
            protected=None,
            resolution=(
                'Sira abrió la puerta pequeña. Los litarios enviarían guardianes si el pacto '
                'reconocía que una montaña podía pertenecer a sus habitantes. Antes de cerrarla, la '
                'puerta repitió la petición en la lengua de las vetas, y ninguna de las siete cartas '
                'volvió a sonar igual cuando se leyó en voz alta.'),
        ),
        dict(
            title='Los hijos de la sombra',
            goal='rescue',
            biome='plains',
            antagonist='Carcelero de las Alas',
            opening=(
                'En una ciudad velaria recién asentada, el imperio capturaba a quienes no podían '
                'volar. Darian debía liberar a una intérprete antes de presentar la tercera carta. '
                'La ciudad se sostenía sobre las mismas acequias que regaban los campos de abajo, y '
                'sus consejos llevaban veinte años discutiendo por el agua. El carcelero encerraba a '
                'los que habían perdido las alas en la guerra, y llamaba carga a un pueblo entero. '
                'Iria Salcedo y Belis esperaban en el canal, contando lámparas encendidas.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Los campesinos recuerdan los inviernos sin luz. No todos querrán '
                              'ayudarlos.'),
                ('hero', 'No les pediremos que olviden. Les pediremos que nadie vuelva a pagar una '
                         'deuda con su vida.'),
                ('Iria', 'La ciudad velaria se asienta sobre las acequias que riegan vuestros campos. '
                         'Si os vengáis de ella, el agua se va con vosotros.'),
                ('Belis', 'Las raíces del sur ya sienten frío. Eso no es un presagio: es un '
                          'calendario.'),
                ('antagonist', 'Quien no puede volar no es un pueblo, es carga. La intérprete seguirá '
                               'en la jaula hasta que aprenda a hablar sin mentir.'),
                ('narrator', 'Objetivo: llegad con cualquier unidad a la prisión, liberad a la '
                             'intérprete y escoltadla hasta la bandera.'),
                ('Iria', 'Firmaré la carta cuando aceptéis dos condiciones: que nadie corte las alas '
                         'de un prisionero y que la intérprete hable ante mi consejo sin cadenas.'),
                ('hero', 'Aceptadas las dos. Escribidlas vos y yo firmo debajo.'),
                ('Belis', 'Y si el consejo la rechaza, ¿declararéis la guerra a los velarios?'),
                ('companion', 'No. Rechazar una carta no es un crimen; encadenar a quien la trae, '
                              'sí.'),
                ('Iria', 'Hay una puerta de servicio bajo la acequia. Se abre con el peso de dos '
                         'personas, no con llaves.'),
                ('hero', 'Entraremos por el agua. Ena, prepara tus vendas: la intérprete llevará '
                         'grilletes.'),
                ('protected', 'No me llaméis por mi nombre delante de ellos. Si lo oyen, mis hermanos '
                              'pagarán por cada letra.'),
                ('narrator', 'El Carcelero ha apostado guardias en las pasarelas. La jaula está junto '
                             'al canal, sobre suelo blando.'),
                ('companion', 'Un cantor herido se cura con luz, no con prisa. Sacadla entera o no la '
                              'saquéis.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('half strength', [
                    ('protected', 'Las alas… no, no son mis alas. Se llevaron las de mi hermano.'),
                    ('hero', 'Nadie volará en esta ciudad hoy. Camina y deja que Ena trabaje.'),
                ]),
                ('turn 5', [
                    ('antagonist', 'Cerrad las compuertas. Si el canal sube, la jaula se llena y '
                                   'nadie tendrá que decidir quién se ahoga primero.'),
                    ('narrator', 'El agua sube un palmo por turno. La jaula está a dos palmos del '
                                 'suelo.'),
                ]),
                ('village captured', [
                    ('Iria', 'Los vecinos dejan lámparas en las ventanas. Son las mismas que '
                             'encendían cuando vuestros abuelos llegaban al mercado.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'Las llaves del carcelero quedaron dentro del canal, y el agua las '
                                 'llevó hacia las acequias de los campos.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que el canal cubra la jaula. La bandera '
                                 'está al otro lado de la pasarela.'),
                ]),
            ],
            victory=[
                ('protected', 'Firmo esta carta como intérprete, no como prisionera. Que se lea en '
                              'las dos lenguas.'),
                ('Iria', 'Mi consejo añadirá un mapa: campos y ciudades comparten las mismas '
                         'acequias.'),
                ('Belis', 'Nadie ha prometido perdonar. Solo hemos acordado quién habla y en qué '
                          'orden.'),
                ('hero', 'Con eso me basta por hoy. La respuesta completa la escribís vosotros.'),
                ('narrator', 'La cuarta carta viajó al norte con una lista de nombres alados y otra '
                             'de nombres campesinos, unidas por la misma acequia.'),
            ],
            protected=('Seyth, intérprete', 'CBM Velario Cantor'),
            resolution=(
                'La intérprete llevó la carta al consejo. Iria añadió un mapa donde los campos y las '
                'ciudades aladas compartían las mismas acequias. Belis hizo copiar el mapa en las dos '
                'lenguas, y Seyth exigió que su nombre apareciera escrito al pie, sin grilletes y sin '
                'traducción que lo suavizara.'),
        ),
        dict(
            title='El puente de los agravios',
            goal='escort',
            biome='forest',
            antagonist='Capitán Rusk',
            opening=(
                'Una delegada campesina aceptó cruzar el antiguo frente para negociar con los '
                'velarios. Rusk, enriquecido con la guerra, anunció que cualquier acuerdo sería una '
                'traición a los muertos. El puente de los agravios unía dos orillas que llevaban veinte '
                'años llamándose enemigas, y Rusk cobraba peaje por cada carro que lo cruzaba. Rella '
                'llevaba en la mano una lista de daños escrita por su propia aldea. Darian no podía '
                'negociar por ella: solo podía conseguir que llegara viva al otro lado.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'La delegada perdió a dos hermanos durante la oscuridad.'),
                ('hero', 'Por eso es ella quien decide cruzar. Nosotros haremos que llegue.'),
                ('protected', 'Cruzo con dos condiciones: nadie de mi comitiva llevará armas velarias '
                              'y la primera palabra del otro lado será para las familias, no para '
                              'los generales.'),
                ('hero', 'Pactado. Tus condiciones van delante de nuestra escolta.'),
                ('antagonist', 'Un acuerdo con quienes os arrancaron los ojos es una traición a los '
                               'muertos. El puente está cerrado.'),
                ('narrator', 'Objetivo: escoltad a la delegada hasta la bandera al otro lado del '
                             'puente sin que muera.'),
                ('companion', 'Rusk no defiende el puente: lo alquila. Cada carro que pasa paga '
                              'peaje.'),
                ('hero', 'Entonces tomaremos los dos extremos y dejaremos el centro libre para '
                         'Rella.'),
                ('protected', 'Si mi pueblo decide no firmar, lo diréis sin castigarlo. Esa es la '
                              'parte que más me cuesta creer.'),
                ('hero', 'Puedes comprobarlo hoy mismo. Si dices no, te devolvemos al otro lado sin '
                         'un reproche.'),
                ('antagonist', 'He visto tres treguas firmarse sobre este tablero. Todas acabaron '
                               'con los mismos nombres en las mismas tumbas.'),
                ('hero', 'Por eso esta vez no firmamos tregua. Escribimos un calendario.'),
                ('companion', 'Los veteranos de Rusk cobran por semana. Si dejáis de darles trabajo, '
                              'se dispersan solos.'),
                ('narrator', 'El puente tiene dos torres y un solo camino. Rusk ha apostado '
                             'ballesteros en la torre del sur.'),
                ('protected', 'Los míos esperan al otro lado. No me hagáis cruzar delante de sus '
                              'ojos como un trofeo.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He mandado cargar el puente de brea. Si cruzáis, arderá con '
                                   'vosotros dentro.'),
                    ('narrator', 'El centro del puente está seco. Las torres todavía no.'),
                ]),
                ('half strength', [
                    ('protected', 'No es grave. Seguid andando; las listas no esperan a nadie.'),
                    ('hero', 'Las listas pueden esperar. Ena, dos pasos y sigues.'),
                ]),
                ('village captured', [
                    ('narrator', 'La aldea del vado izó la bandera de los campos. Los carros de Rusk '
                                 'ya no pueden cobrar peaje aquí.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'Rusk cayó junto al tablero donde firmaba sus treguas. Nadie '
                                 'recogió su libro de peajes.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos para cruzar. La bandera está al final del '
                                 'puente.'),
                ]),
            ],
            victory=[
                ('protected', 'He cruzado sin que nadie me llamara embajadora. Gracias por dejar que '
                              'lo hiciera a pie.'),
                ('hero', 'Las condiciones eran tuyas. Nosotros solo hemos pagado el peaje con '
                         'tiempo.'),
                ('protected', 'La negociación empezará con una lista de daños. No prometo perdón.'),
                ('companion', 'Nosotros no lo hemos pedido. Solo pedimos que la lista se lea en voz '
                              'alta.'),
                ('narrator', 'En la torre sur quedó una bandera de los campos. Alguien escribió '
                             'debajo: aquí no se cobra peaje.'),
            ],
            protected=('Rella, delegada de los campos', 'Peasant'),
            resolution=(
                'La negociación comenzó con una lista de daños y terminó con un calendario de '
                'reparaciones. Nadie lo llamó perdón. Rella hizo copiar el calendario en las dos '
                'orillas, y sobre el puente quedó una tercera copia clavada para que cualquiera '
                'pudiera añadir lo que faltaba.'),
        ),
        dict(
            title='La cuarta brasa',
            goal='conquer',
            biome='coast',
            antagonist='Almirante del Sello',
            opening=(
                'Nerea había reunido una flota de puertos libres, pero un almirante imperial cerraba '
                'la salida al estrecho. Darian necesitaba despejarlo antes de que llegaran los '
                'refugiados del interior. El Almirante del Sello tendía una cadena entre dos fragatas '
                'y cobraba un registro de almas por cada bodega. Nerea Vado no prestaba un solo barco '
                'sin una cláusula escrita: ninguna nave de la alianza transportaría cautivos, ni '
                'vivos ni muertos. La cuarta brasa iba a encenderse en un faro pequeño, con aceite de '
                'puerto libre.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'La capitana exige que ninguna nave de la alianza transporte cautivos.'),
                ('hero', 'Escribámoslo antes de pedirle un solo barco.'),
                ('Nerea', 'Cada barco de puerto libre navega con el nombre de su capitán y sin '
                          'registro de carga. Si la alianza transporta cautivos, pierdo la flota '
                          'entera.'),
                ('hero', 'Escribamos esa condición antes de pedir un solo barco.'),
                ('narrator', 'Objetivo: derrotad al líder enemigo y abrid la salida al estrecho.'),
                ('antagonist', 'El sello imperial cierra el estrecho. Ningún barco sale sin pagar el '
                               'registro de almas.'),
                ('Nerea', 'Firmaré la brasa cuando la cláusula figure en la carta: ninguna nave de '
                          'la alianza lleva cautivos, ni vivos ni muertos.'),
                ('companion', 'Los registros de almas se cuentan por familias. Si una nave los '
                              'transporta, en tierra quedarán los nombres de quienes los esperaban.'),
                ('hero', 'Y si un puerto decide no firmar, seguirá siendo puerto libre. Nuestras '
                         'cartas no bloquean puertos.'),
                ('Nerea', 'He navegado veinte años y nunca vi un convoy sin registro. Enseñadme uno '
                          'y os creeré.'),
                ('hero', 'Empezaremos por tus barcos. Revisa tú misma cada bodega antes de zarpar.'),
                ('companion', 'El Almirante tiene dos fragatas en la boca del estrecho y una cadena '
                              'tendida entre ambas.'),
                ('Nerea', 'La cadena se ancla al faro pequeño. Quien lo apague abre el paso.'),
                ('narrator', 'El estrecho es estrecho de verdad: dos barcos de frente y ninguna '
                             'maniobra. El líder enemigo manda desde la fragata norte.'),
                ('Nerea', 'Si tomamos su nave, el sello cae. Si solo matamos marineros, otro '
                          'almirante heredará el puesto.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'Cerrad la cadena. Los que no paguen esperarán a la marea, y la '
                                   'marea tarda.'),
                    ('narrator', 'La cadena sube entre las dos fragatas. El paso queda cortado al '
                                 'norte del faro.'),
                ]),
                ('village captured', [
                    ('Nerea', 'Ese muelle era de mi padre. Que nadie lo queme: si arde, la alianza '
                              'no tendrá dónde descargar.'),
                ]),
                ('turn 7', [
                    ('companion', 'Las fragatas están separadas. Si atacamos la del norte, la del '
                                  'sur no llegará a tiempo.'),
                    ('hero', 'Entonces atacamos hoy. Mañana estarán unidas otra vez.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'La cadena se iza sola al morir su custodio. Recordadlo cuando '
                                   'otro almirante la tienda.'),
                    ('narrator', 'La cadena cayó al agua y el estrecho quedó abierto de una orilla a '
                                 'otra.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que llegue el convoy de refugiados.'),
                ]),
            ],
            victory=[
                ('Nerea', 'El estrecho está abierto. Firmo con tinta común, para que cualquiera '
                          'pueda leer las condiciones.'),
                ('hero', 'Tinta común y copia en cada puerto. Nadie firmará la parte que no haya '
                         'leído.'),
                ('Nerea', 'La cláusula de los cautivos queda escrita con las palabras de mi padre. '
                          'Cambiarla exigirá tres puertos, no uno.'),
                ('companion', 'Los refugiados entran en la rada. Ninguna bodega lleva un nombre que '
                              'no esté en la lista.'),
                ('narrator', 'La cuarta brasa se encendió en el faro pequeño, con aceite de puerto '
                             'libre y una mecha que cualquiera podía apagar.'),
            ],
            protected=None,
            resolution=(
                'El estrecho quedó abierto. Nerea firmó con tinta común, para que cualquiera pudiera '
                'leer las condiciones. Antes de zarpar hizo revisar cada bodega delante de dos '
                'testigos de la alianza, y la cláusula de los cautivos quedó grabada en la piedra '
                'del faro pequeño, a la vista de quien llegara a apagarlo.'),
        ),
        dict(
            title='Quienes no firmaron',
            goal='survive',
            biome='quarry',
            antagonist='Prefecto Arven',
            opening=(
                'Las canteras albergaban a desertores de ambos bandos. No querían unirse a ningún '
                'ejército. El prefecto los declaró propiedad abandonada del Estado y marchó a '
                'recogerlos. En las galerías vivían mineros que habían dejado una lanza y no '
                'pensaban tomar otra, con herramientas propias y un censo que nadie había firmado. '
                'Arven traía cadenas contadas según su propio registro y piqueros para cobrarlas. '
                'Darian necesitaba aguantar la cantera sin convertirla en cuartel.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Si los defendemos, quizá se marchen sin darnos nada.'),
                ('hero', 'Ese es el derecho que decimos defender.'),
                ('Halen', 'No hemos venido a alistarnos. Hemos venido a que nos dejéis cavar en '
                          'paz.'),
                ('hero', 'Nadie os va a alistar. Ese es justamente el punto.'),
                ('narrator', 'Objetivo: mantened a Darian con vida hasta el comienzo del turno 12.'),
                ('antagonist', 'Los desertores son propiedad abandonada del Estado. Contarlos y '
                               'devolverlos es mi trabajo.'),
                ('Halen', 'Aceptamos vuestro refugio con dos condiciones: ninguna leva en la cantera '
                          'y ninguna lista escrita con nuestros nombres.'),
                ('hero', 'Concedidas. Las herramientas se apuntan a nombre de la cantera, no de las '
                         'personas.'),
                ('companion', 'Si después de defendidos deciden marcharse, se marcharán sin que '
                              'nadie los llame traidores.'),
                ('hero', 'Y sin escolta que los vigile. Eso también lo escribimos.'),
                ('Halen', 'El prefecto trae cadenas de dos clases: unas para las manos y otras para '
                          'los papeles.'),
                ('companion', 'La cantera tiene tres bocas. La del norte es la única que no vigilan.'),
                ('hero', 'Defended el norte y el centro. Nosotros aguantaremos la plaza hasta que se '
                         'cansen de subir.'),
                ('narrator', 'El Prefecto ha apostado piqueros en la rampa. Sus cadenas esperan en '
                             'carros, contadas y numeradas.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He traído tantas cadenas como cabezas conté en el censo. Ni una '
                                   'más, ni una menos.'),
                    ('narrator', 'Los carros de cadenas suben por la rampa. El censo viaja en el '
                                 'primero.'),
                ]),
                ('village captured', [
                    ('Halen', 'Esa casa de aperos tiene agua limpia. Dejadla para los heridos y no '
                              'como puesto de mando.'),
                ]),
                ('turn 8', [
                    ('companion', 'Han empezado a contar en voz alta. Los nuestros ya no distinguen '
                                  'cuántos son.'),
                    ('hero', 'Que cuenten. Nosotros solo tenemos que seguir contando los turnos.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El censo quedó abierto bajo la rampa. Nadie puso su nombre en la '
                                 'lista.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos de asedio. La plaza de la cantera sigue en '
                                 'pie.'),
                ]),
            ],
            victory=[
                ('Halen', 'No hemos jurado nada. Ofrecemos herramientas, guías y un lugar donde '
                          'dormir.'),
                ('hero', 'Lo tomo. Vuestra quinta brasa no llevará juramento.'),
                ('Halen', 'Guías sí tenemos: conocemos cada galería del imperio, porque las cavamos '
                          'nosotros.'),
                ('companion', 'Y si mañana queréis marcharos, la puerta estará abierta.'),
                ('narrator', 'Darian anotó la brasa con una raya y ninguna firma. En el margen '
                             'escribió: sin juramento, sin leva.'),
            ],
            protected=None,
            resolution=(
                'Los desertores no juraron lealtad. Ofrecieron herramientas, guías y un lugar donde '
                'descansar. Darian anotó la quinta brasa sin añadir un juramento. Halen mandó tallar '
                'en la pared de la cantera una sola frase: aquí nadie fue contado dos veces.'),
        ),
        dict(
            title='El mensajero de hueso',
            goal='rescue',
            biome='ruins',
            antagonist='Custodio del Archivo',
            opening=(
                'Sevrin había logrado enviar una petición de auxilio desde los archivos de Maura. La '
                'guardia lo encadenó a su propio contrato para impedir otra fuga. Liberarlo revelaría '
                'cómo romper el sello central. El archivo guardaba los contratos funerarios por '
                'orden de firma, y el suyo era el número doscientos. El Custodio lo llamaba '
                'prisionero voluntario y repetía que un contrato firmado no se rompe, se cumple. '
                'Darian necesitaba su testimonio, no su arrepentimiento.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Ha dirigido ejércitos contra todos nuestros aliados.'),
                ('hero', 'Tendrá que responder por ello. Primero debe poder elegir sus respuestas.'),
                ('narrator', 'Objetivo: alcanzad la prisión del archivo, liberad a Sevrin y '
                             'escoltadlo hasta la bandera.'),
                ('antagonist', 'El prisionero firmó un contrato voluntario. Un contrato voluntario '
                               'no se rompe: se cumple.'),
                ('hero', 'Enséñame su letra. Si firmó voluntariamente, no le costará reconocerla.'),
                ('protected', 'No os acerquéis a la reja sin mirar las cadenas. Están atadas a un '
                              'libro, no a la pared.'),
                ('hero', 'Entonces liberaremos libro y prisionero a la vez.'),
                ('protected', 'Acepto salir con vosotros con una condición: si el archivo os pide '
                              'algo a cambio, podéis negaros. Esa es la única regla del pacto, y '
                              'también me protege a mí.'),
                ('companion', 'Las cadenas funerarias tiran del contrato. Cortar el contrato no '
                              'corta la cadena.'),
                ('narrator', 'El archivo tiene tres salas. Sevrin está en la tercera, encadenado al '
                             'armario de los registros.'),
                ('hero', 'Entra por el sur con dos hombres. Yo distraeré a los custodios con '
                         'preguntas que no pueden contestar.'),
                ('protected', 'Si tardo en andar, no me dejéis atrás sin cortar antes el libro.'),
                ('narrator', 'Los custodios no llevan armas de filo: llevan sellos, tinta y llaves '
                             'de hierro viejo.'),
                ('hero', 'Que nadie queme un solo legajo. Los nombres que hay aquí también son '
                         'pruebas.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('half strength', [
                    ('protected', 'Corta el libro, no la cadena. La cadena me sostiene de pie.'),
                    ('hero', 'Ena, cúralo. Yo corto el libro con la mano libre.'),
                ]),
                ('turn 4', [
                    ('antagonist', 'He quemado el índice. Ahora nadie sabrá nunca cuántos nombres '
                                   'faltan.'),
                    ('narrator', 'El humo sale por la ventana del sur. Los contratos del fondo se '
                                 'salvaron.'),
                ]),
                ('village captured', [
                    ('narrator', 'La primera sala tomada conserva los anaqueles intactos. Los '
                                 'guardianes huyen de la tinta, no del fuego.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El contrato se partió en el suelo del archivo. La cadena cayó con '
                                 'él, sin arrastrar a nadie.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que sellen la tercera sala. La bandera '
                                 'está en el patio exterior.'),
                ]),
            ],
            victory=[
                ('protected', 'El nombre verdadero del sello lo escribiré yo, y lo firmo aquí '
                              'mismo.'),
                ('hero', 'Lo escribiremos. Y no pediremos absolución por ti.'),
                ('protected', 'No la quiero. Quiero que mi testimonio incluya todo lo que hice, no '
                              'solo lo que sirve.'),
                ('companion', 'La venganza era fácil. Escucharle está siendo peor.'),
                ('narrator', 'Sevrin escribió dos páginas: una con lo que sabía del sello y otra con '
                             'su propia lista de muertos.'),
            ],
            protected=('Sevrin', 'Deathblade'),
            resolution=(
                'Sevrin entregó el nombre verdadero del sello. No pidió absolución; pidió que su '
                'testimonio incluyera todo lo que había hecho. Darian guardó las dos páginas en la '
                'misma funda, para que nadie pudiera leer la primera sin la segunda.'),
        ),
        dict(
            title='La sal de los juramentos',
            goal='beacons',
            biome='islands',
            antagonist='Vigía de las Cadenas',
            opening=(
                'Tres altares costeros guardaban copias de los contratos funerarios. Disolverlas en '
                'agua salada debilitaría la red de Maura. Los guardianes intentaron trasladarlas '
                'antes de la llegada de la flota. Cada copia era una lista de nombres atados a un '
                'remo, y las tres se repartían entre la isla del faro, la de las aves y la que no '
                'tenía nombre. Luar conocía el arrecife mejor que las cartas del imperio, y no '
                'guiaba a nadie sin un testigo del agua.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Cada sello roto libera una voz. También avisa a la reina de dónde '
                              'estamos.'),
                ('hero', 'Que escuche cuántas voces ha intentado callar.'),
                ('Luar', 'Las copias están bajo el agua clara. Quien las toque con hierro avisa a la '
                         'reina.'),
                ('hero', 'Entonces las tocaremos con sal. Luar, marca los tres altares desde el '
                         'arrecife.'),
                ('narrator', 'Objetivo: llevad una unidad a cada uno de los tres altares y activad '
                             'los tres puntos.'),
                ('antagonist', 'Los contratos funerarios sostienen la flota. Si los disolvéis, los '
                               'muertos dejarán de remar.'),
                ('Luar', 'Os guío con una condición: ningún altar se toca sin que un buceador del '
                         'arrecife lo vea. No quiero otra deuda en mi nombre.'),
                ('hero', 'Aceptada. Iremos con testigos, aunque tardemos más.'),
                ('companion', 'Si Luar decide retirarse a mitad de camino, volvemos sin altar y sin '
                              'reproche.'),
                ('hero', 'Sí. La marea no obedece a los pactos, y nosotros tampoco obligamos.'),
                ('Luar', 'Los altares están en tres islas: la del faro, la de las aves y la que no '
                         'tiene nombre.'),
                ('companion', 'La barca del Vigía es ligera y rema en silencio. Ena puede apagar '
                              'antorchas, no remos.'),
                ('hero', 'Iremos de isla en isla sin encender nada. Que la sal trabaje de noche.'),
                ('narrator', 'El Vigía de las Cadenas patrulla en dos barcas ligeras. Los altares se '
                             'apagan con agua, no con fuego.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('Luar', 'La primera copia se ha disuelto. He oído a un barquero cantar su '
                             'propio nombre.'),
                    ('narrator', 'Dos altares siguen intactos. La niebla se cierra sobre el '
                                 'arrecife.'),
                ]),
                ('beacon lit 2', [
                    ('antagonist', 'Habéis liberado dos. Ahora la reina ya sabe cuántos os quedan.'),
                ]),
                ('turn 6', [
                    ('companion', 'Las barcas ligeras se acercan remando en silencio. Si nos ven, no '
                                  'habrá tercera isla.'),
                    ('hero', 'Que remen. Nosotros bajamos al agua y dejamos la barca vacía.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El Vigía cayó entre sus cadenas, y el agua salada terminó de '
                                 'disolver la última copia.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que suba la niebla. El tercer altar '
                                 'está al este.'),
                ]),
            ],
            victory=[
                ('Luar', 'Las tres copias están rotas. Los muertos han señalado caminos que no '
                         'conocíamos.'),
                ('hero', '¿Caminos hacia dónde?'),
                ('Luar', 'Hacia los puertos donde cargan a los nuevos cautivos. Los dibujo en tu '
                         'mapa con tinta de arrecife.'),
                ('companion', 'La reina ya sabe dónde estamos. Lo sabía desde el primer sello.'),
                ('narrator', 'Los liberados no pidieron venganza. Pidieron que sus nombres se '
                             'escribieran en la lista de los vivos.'),
            ],
            protected=None,
            resolution=(
                'Los muertos liberados señalaron los caminos por los que eran transportados los '
                'nuevos cautivos. Darian los copió en su mapa antes de que la sal borrara las rutas, '
                'y Luar exigió que cada trazo llevara el nombre del buceador que lo había visto.'),
        ),
        dict(
            title='La sexta respuesta',
            goal='escort',
            biome='cave',
            antagonist='Cazador de Deudas',
            opening=(
                'Una escribana de la capital traía un registro de ciudadanos condenados al servicio '
                'después de morir. Debía cruzar las galerías litarias para que cada familia pudiera '
                'impugnar su contrato. El registro tenía once mil nombres, y Myr lo había copiado '
                'hoja por hoja sin dormir. Los litarios cobraban peaje en piedra y dejaban pasar sin '
                'mirar; el Cazador de Deudas cobraba en personas. La sexta brasa pertenecía a los '
                'barrios de la capital, y su respuesta iba a llegar sin un solo nombre.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'El registro pesa más que nuestras siete cartas juntas.'),
                ('hero', 'Entonces lo llevaremos entre todos.'),
                ('protected', 'El registro tiene once mil nombres. Si se publica aquí dentro, las '
                              'familias de la capital pagarán por cada hoja.'),
                ('hero', 'Entonces saldrá sin nombres. La sexta brasa será de los barrios, no de un '
                         'archivo.'),
                ('narrator', 'Objetivo: escoltad a la escribana y su registro hasta la bandera al '
                             'final de las galerías.'),
                ('antagonist', 'Las deudas no se perdonan, se cobran. Esa escribana ha robado la '
                               'contabilidad del imperio.'),
                ('protected', 'Os acompaño con una condición: el registro no se abre hasta que '
                              'estemos fuera, y lo abre una familia, no un ejército.'),
                ('hero', 'Aceptada. Nadie de la alianza leerá una sola página en las galerías.'),
                ('companion', 'Y si los barrios deciden no responder, su silencio también será una '
                              'respuesta válida.'),
                ('hero', 'Sí. Aquí nadie va a ser obligado a firmar ni a hablar.'),
                ('protected', 'Las galerías litarias son las únicas que no vigilan. Cobran peaje en '
                              'piedra, no en personas.'),
                ('companion', 'El Cazador de Deudas conoce los túneles: los usaba para llevar '
                              'contratos al norte.'),
                ('hero', 'Iremos por el ramal inundado. Ena, guarda la lámpara: si el agua sube, la '
                         'tinta se pierde.'),
                ('protected', 'Si me alcanzan, cortad el registro y no a mí. Sabréis por qué cuando '
                              'lleguemos.'),
                ('narrator', 'La bandera está al final de la galería larga. El Cazador ha apostado '
                             'ballesteros en dos bocas.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'Cerrad las compuertas del ramal. Prefiero ahogar la contabilidad '
                                   'a perdonar una sola deuda.'),
                    ('narrator', 'El agua sube por el ramal inundado. Quedan dos turnos antes de que '
                                 'cubra el paso.'),
                ]),
                ('half strength', [
                    ('protected', 'No he perdido el registro. Perdedme a mí, pero no lo abráis '
                                  'aquí.'),
                    ('hero', 'Nadie se pierde. Ena, tapa esa herida y seguimos.'),
                ]),
                ('village captured', [
                    ('narrator', 'La primera cámara litarias les deja beber y nada más. El peaje '
                                 'fue de piedra, como habían dicho.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El Cazador murió con una lista de deudores en la mano. La lista no '
                                 'llevaba nombres, solo cantidades.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que inunden la galería larga.'),
                ]),
            ],
            victory=[
                ('protected', 'Estamos fuera. Abrid el registro por la última página.'),
                ('hero', 'No. Lo abrirá una familia del barrio, como acordamos.'),
                ('protected', 'La sexta brasa es vuestra, barrios. Responded sin nombres: '
                              'publicarlos condenaría a quienes siguen dentro.'),
                ('companion', 'Once mil contratos, y ninguno se puede romper sin saber a quién '
                              'pertenece.'),
                ('narrator', 'La respuesta llegó escrita en una hoja sin firmas: siete distritos, '
                             'siete brasas y ninguna lista de culpables.'),
            ],
            protected=('Myr, escribana de la capital', 'Peasant'),
            resolution=(
                'La sexta brasa perteneció a los barrios de la capital. Su respuesta no llevaba '
                'nombres: publicarlos habría condenado a quienes seguían dentro. Myr dejó el registro '
                'en manos de una familia y volvió a las galerías con una copia sin firmas, dispuesta '
                'a impugnar los contratos uno por uno.'),
        ),
        dict(
            title='Un ejército de vecinos',
            goal='conquer',
            biome='plains',
            antagonist='Mariscal de Ceniza',
            opening=(
                'El mariscal concentró sus tropas en el granero central. La alianza debía tomarlo '
                'para alimentar a los barrios rebeldes, manteniendo abiertas las rutas de quienes no '
                'participaban en la guerra. Cuatrocientas familias habían traído carros y ochenta '
                'lanzas; el mariscal tenía veteranos pagados y las llaves del grano. Los delegados '
                'discutían todavía quién repartiría la primera ración. Darian necesitaba una victoria '
                'que nadie pudiera cobrar en nombre de otro.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Tenemos soldados de pueblos que hace un año se atacaban entre sí.'),
                ('hero', 'Hoy comparten una tarea. La confianza vendrá de cumplirla.'),
                ('Osk', 'Tenemos cuatrocientos vecinos y ochenta lanzas. Los cuatrocientos saben '
                        'dónde está el grano.'),
                ('hero', 'Entonces manda el grano. Objetivo claro: tomad el granero central y '
                         'derribad al mariscal.'),
                ('narrator', 'Objetivo: derrotad al líder enemigo. El granero central es su puesto de '
                             'mando.'),
                ('antagonist', 'Este granero alimenta tres provincias. Si lo tomáis, las tres se '
                               'morirán de hambre por vuestra culpa.'),
                ('Vesh', 'Marchamos con una condición: ninguna aldea decide la ración de otra. Ni la '
                         'vuestra.'),
                ('hero', 'Escrito queda. El reparto lo fija una asamblea de aldeas, con o sin '
                         'nosotros.'),
                ('companion', 'Y la aldea que no quiera dar carros, no los dará. Iremos más '
                              'despacio, nada más.'),
                ('Osk', 'Los mariscales cuentan con la deserción. Cuando falta el grano, se van '
                        'solos.'),
                ('hero', 'Que se vayan. No vamos a perseguir a quien deje la lanza.'),
                ('companion', 'El mariscal tiene ballesteros en el tejado y un carro blindado junto '
                              'a la puerta norte.'),
                ('hero', 'Entramos por la puerta sur, que da al mercado. Allí no puede disparar sin '
                         'matar a su propia gente.'),
                ('narrator', 'Los carros de grano esperan bajo el cobertizo. La bandera del mariscal '
                             'ondea sobre el tejado.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He repartido el grano entre mis veteranos. Que los vecinos '
                                   'aprendan cuánto vale una ración.'),
                    ('narrator', 'Los veteranos cobran en sacos. Los vecinos siguen esperando en la '
                                 'puerta sur.'),
                ]),
                ('village captured', [
                    ('Vesh', 'Esa aldea nos ha dado agua sin pedir nada. Devolvedle el doble y '
                             'anotadlo.'),
                ]),
                ('turn 8', [
                    ('companion', 'Los vecinos empiezan a reconocerse entre las filas enemigas. '
                                  'Algunos bajan las lanzas.'),
                    ('hero', 'Que bajen. Que nadie les pida explicaciones.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El mariscal cayó en el tejado del granero. Los carros siguieron '
                                 'cargados hasta el mediodía.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que el mariscal queme el granero.'),
                ]),
            ],
            victory=[
                ('Osk', 'Los carros están llenos y las escoltas son mixtas. Nadie ha recibido '
                        'permiso para decidir la ración de otro.'),
                ('hero', 'Que salgan de noche y por caminos distintos. Si alguien ataca un carro, no '
                         'sabrá a quién pertenece.'),
                ('Vesh', 'La asamblea de aldeas se reúne mañana. Yo llevo la balanza, no la espada.'),
                ('companion', 'Hace un año estas mismas aldeas se atacaban entre sí.'),
                ('narrator', 'Los carros salieron al anochecer, cada uno con dos banderas y ninguna '
                             'autoridad sobre los demás.'),
            ],
            protected=None,
            resolution=(
                'Los carros de grano salieron con escoltas mezcladas. Ningún pueblo recibió permiso '
                'para decidir la ración de otro. La asamblea se reunió bajo el cobertizo y acordó '
                'que la balanza viajara cada mes a una aldea distinta, para que nadie pesara siempre '
                'en su propia casa.'),
        ),
        dict(
            title='La noche de las dos órdenes',
            goal='survive',
            biome='forest',
            antagonist='Inquisidora Vael',
            opening=(
                'La inquisidora difundió órdenes falsas para dividir a la alianza. Darian reunió a '
                'los delegados alrededor de las brasas mientras las patrullas enemigas intentaban '
                'capturarlos por separado. Cada contingente había recibido una carta distinta, y '
                'todas parecían escritas por un mando legítimo. Vael no buscaba matarlos: buscaba que '
                'se acusaran entre ellos antes del amanecer. La séptima brasa iba a decidirse '
                'alrededor de un fuego, no en un campo de batalla.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Si cada contingente obedece su propia carta, no resistiremos.'),
                ('hero', (
                    'Que vengan y pregunten. Una orden que no admite preguntas ya nos ha hecho '
                    'bastante daño.')),
                ('antagonist', 'He enviado dos órdenes a cada contingente. Una es verdadera. Que '
                               'discutan cuál.'),
                ('hero', 'Que traigan ambas y las lean delante de todos. Objetivo: aguantar hasta el '
                         'turno doce sin que la alianza se parta.'),
                ('narrator', 'Objetivo: mantened a Darian con vida hasta el comienzo del turno 12.'),
                ('Vesh', 'He recibido una orden con mi propio sello. Nunca escribí esa orden.'),
                ('hero', 'Guárdala. Mañana la leeremos en la asamblea y que responda quien la '
                         'escribió.'),
                ('Neth', 'Exijo que cualquier delegado pueda levantarse y decir no. Sin eso, firmo '
                         'la retirada mañana mismo.'),
                ('hero', 'Esa es exactamente la séptima brasa: ninguna voz hablará por todas sin '
                         'poder ser contradicha.'),
                ('Rella', 'Las patrullas de los campos saldrán con una condición: no se separarán de '
                          'los velarios, ni de día ni de noche.'),
                ('hero', 'Aceptada. Nadie vigila a nadie: caminan juntos o no caminan.'),
                ('antagonist', 'Las órdenes falsas funcionan porque todos tenéis razón en algo. Eso '
                               'es lo que os pierde.'),
                ('companion', 'Las patrullas enemigas vienen por tres caminos. Las brasas están en '
                              'el claro.'),
                ('hero', 'Rodead las brasas y no las apaguéis por nada. Mientras ardan, todos sabrán '
                         'dónde está el centro.'),
                ('narrator', 'La noche es cerrada en el bosque. Las antorchas enemigas se cuentan de '
                             'dos en dos.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'Segunda orden enviada: los litarios cruzarán el río y los '
                                   'velarios cubrirán la retirada. Ninguno osará preguntar.'),
                    ('narrator', 'Dos contingentes se miran desde orillas opuestas. Ninguno se mueve '
                                 'todavía.'),
                ]),
                ('village captured', [
                    ('Vesh', 'La aldea nos ha dado mantas sin pedir juramento. Devolvedlas lavadas '
                             'al amanecer.'),
                ]),
                ('turn 8', [
                    ('companion', 'Han cortado el camino del este. Los contingentes tendrán que pasar '
                                  'por el claro o no pasar.'),
                    ('hero', 'Entonces pasarán por el claro. Que vean las brasas encendidas.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'Las copias falsas quedaron en el barro. Alguien las pisó hasta que '
                                 'la tinta dejó de leerse.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos hasta el amanecer. El claro sigue iluminado.'),
                ]),
            ],
            victory=[
                ('Neth', 'Hemos discutido toda la noche y ninguno ha desenfundado. Es la primera vez '
                         'que lo veo.'),
                ('hero', 'Las falsificaciones fallaron porque os conocíais. La séptima brasa no es un '
                         'juramento: es una regla.'),
                ('Vesh', 'Ninguna voz hablará por todas sin poder ser contradicha. Que se escriba '
                         'así, con esas palabras.'),
                ('Rella', 'Mañana volveré a los campos y diré que aquí se puede decir no delante de '
                          'todos.'),
                ('narrator', 'La inquisidora huyó hacia el norte. Su orden falsa quedó clavada en un '
                             'árbol, con las firmas tachadas una por una.'),
            ],
            protected=None,
            resolution=(
                'Las falsificaciones fallaron porque los delegados se conocían. La séptima brasa fue '
                'una regla: ninguna voz hablaría por todas sin poder ser contradicha. Darian hizo '
                'grabar la regla en las siete copias del pacto, y la inquisidora no volvió a enviar '
                'dos órdenes al mismo campamento.'),
        ),
        dict(
            title='El nombre del sello',
            goal='beacons',
            biome='ruins',
            antagonist='Notario Inmortal',
            opening=(
                'El nombre del sello estaba repartido entre tres archivos para que ningún servidor '
                'pudiera destruirlo. Sevrin recordaba sus ubicaciones. Darian debía reunir las '
                'inscripciones antes de entrar en palacio. Una estaba en un muro vivo, otra bajo un '
                'sello de cera y la tercera en una sala que ya no figuraba en los planos. Nadie '
                'había leído el nombre entero desde que Maura lo partió, y los escribientes del '
                'Notario Inmortal copiaban los mismos fragmentos desde hacía doscientos años.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Al romperlo, algunos de nuestros combatientes caerán. Luchan unidos a esos '
                    'mismos contratos.')),
                ('hero', 'Se lo diremos antes. Esta vez nadie decidirá por ellos.'),
                ('Sevrin', 'El nombre está repartido entre tres archivos: uno vivo, uno sellado y uno '
                           'que ya no existe. Lo que queda son tres inscripciones.'),
                ('narrator', 'Objetivo: llevad una unidad a cada inscripción y activad los tres '
                             'puntos.'),
                ('antagonist', 'Un nombre repartido no puede destruirse. Solo reescribirse, y eso es '
                               'cosa de notarios, no de correos.'),
                ('hero', 'Entonces no vamos a reescribirlo. Vamos a leerlo entero por primera vez.'),
                ('Sevrin', 'Os doy las ubicaciones con una condición: diréis a los nuestros qué se '
                           'rompe cuando se rompa el sello. Ellos deciden si siguen.'),
                ('hero', 'Se lo diremos antes de tocar la primera piedra.'),
                ('Sevrin', 'Soy uno de esos combatientes. Si lo rompéis, yo también puedo caer. Lo '
                           'digo ahora, no después.'),
                ('hero', 'Anotadlo. Si Sevrin quiere retirarse, se retira con el nombre a medio '
                         'leer.'),
                ('companion', 'Las tres inscripciones están en muros distintos. La del oeste tiene '
                              'guardia; la del norte, hielo.'),
                ('narrator', 'El Notario Inmortal no duerme. Sus escribientes copian el mismo '
                             'párrafo desde hace doscientos años.'),
                ('Sevrin', 'Cuando el nombre esté completo, decidlo en voz alta. Quiero oírlo yo '
                           'también.'),
                ('hero', 'Y que lo oigan los que aún sostienen los contratos. Ellos decidirán qué '
                         'hacen con la noticia.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('Sevrin', 'La primera parte dice "Vey". Quedan dos, y ya sé lo que significa.'),
                    ('narrator', 'Dos inscripciones siguen cerradas. Los escribientes no han dejado '
                                 'de copiar.'),
                ]),
                ('beacon lit 2', [
                    ('antagonist', 'Habéis leído dos tercios. Con eso ya no podéis fingir que no '
                                   'sabíais nada.'),
                ]),
                ('turn 6', [
                    ('companion', 'Los escribientes han empezado a borrar la tercera inscripción. Si '
                                  'la tocan, no se recupera.'),
                    ('hero', 'Corred hacia el muro del norte. Yo cubro la escalera.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El notario firmó su última hoja y el nombre completo quedó legible '
                                 'sobre tres muros distintos.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que llegue la guardia del archivo.'),
                ]),
            ],
            victory=[
                ('Sevrin', 'Maura Vey. Ese era el nombre del sello: el de la reina. No un objeto, '
                           'una persona.'),
                ('hero', 'Un nombre se puede leer sin destruir a nadie.'),
                ('companion', 'O se puede preguntar antes. Los muertos de la alianza merecen saber '
                              'qué se juega.'),
                ('Sevrin', 'Yo elegí sostener la última marcha. No todos elegirán lo mismo, y '
                           'ninguno será un traidor.'),
                ('narrator', 'Los muertos de la alianza escucharon el nombre completo y pidieron '
                             'tiempo para decidir.'),
            ],
            protected=None,
            resolution=(
                'Los muertos de la alianza eligieron sostener la última marcha. Cada uno pidió algo '
                'distinto para después. Sevrin anotó cada petición en una hoja aparte, y Darian '
                'prohibió que ninguna se resumiera en una sola frase.'),
        ),
        dict(
            title='La ciudad que abrió sus puertas',
            goal='rescue',
            biome='harbor',
            antagonist='Gobernador de las Cenizas',
            opening=(
                'Los barrios se alzaron, pero el gobernador tomó rehenes en la aduana. Liberar a su '
                'portavoz permitiría abrir las puertas interiores sin arrasar la ciudad que la '
                'alianza decía venir a salvar. La ceniza cubría las calles y las lámparas apagadas '
                'señalaban casa abierta y sin armas. Los arietes imperiales ya estaban en la puerta '
                'norte, y un correo tardaba menos en llegar que una orden. Irena llevaba dos días '
                'hablando con los rehenes para que no perdieran la calma.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Los arietes llegarán antes que nosotros si tomamos el camino largo.'),
                ('hero', (
                    'Envía un correo para detenerlos. No hemos cruzado medio mundo para entrar sobre '
                    'sus casas.')),
                ('protected', 'Los barrios aguantan desde dentro, pero la aduana tiene rehenes y el '
                              'gobernador tiene los arietes.'),
                ('hero', 'Objetivo: llegad a la aduana, sacad a Irena y llevadla a la bandera. Los '
                         'arietes se quedan fuera.'),
                ('narrator', 'Objetivo: alcanzad la prisión, liberad a la portavoz y escoltadla '
                             'hasta la salida.'),
                ('antagonist', 'Si la ciudad se alza, la reduzco a ceniza. Ya lo hice en dos '
                               'provincias y nadie me lo reprochó.'),
                ('protected', 'Salgo con una condición: ninguna unidad de la alianza entra en un '
                              'barrio con la antorcha encendida.'),
                ('hero', 'Aceptada. Que el correo detenga los arietes y que nadie encienda nada.'),
                ('companion', 'Y los barrios que no quieran abrir, no abrirán. Nos quedaremos fuera '
                              'con ellos dentro.'),
                ('hero', 'Exacto. Entrarán por la puerta que ellos elijan.'),
                ('protected', 'La aduana tiene el patio lleno de rehenes. Si atacáis la puerta '
                              'principal, morirán los primeros.'),
                ('companion', 'Hay una escalera de servicio junto a las lámparas apagadas. Nadie la '
                              'vigila porque no lleva a ningún sitio, salvo al archivo.'),
                ('hero', 'Por ahí. Ena, prepara dos vendajes para los rehenes que encontremos.'),
                ('protected', 'Cuando abramos las puertas interiores, que nadie corra. La ciudad se '
                              'asusta con las prisas.'),
                ('narrator', 'Las calles están cubiertas de ceniza. Los arietes imperiales ya están '
                             'en la puerta norte.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He dado la orden: si la portavoz sale, la aduana arde con todo '
                                   'lo que quede dentro.'),
                    ('narrator', 'Los arietes avanzan un tramo por turno. La escalera de servicio '
                                 'sigue sin guardia.'),
                ]),
                ('half strength', [
                    ('protected', 'Puedo andar. No carguéis conmigo delante de los rehenes: lo '
                                  'tomarían por una rendición.'),
                    ('hero', 'Andas tú, pero yo voy a tu lado. Nadie va a malinterpretar eso.'),
                ]),
                ('village captured', [
                    ('narrator', 'El primer barrio izó una lámpara apagada. Es la señal de los '
                                 'vecinos: casa abierta, sin armas.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El gobernador huyó por el muelle. Las puertas interiores se '
                                 'abrieron desde dentro, una por una.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que los arietes lleguen a la aduana.'),
                ]),
            ],
            victory=[
                ('protected', 'Abro las puertas interiores. Que entren sin correr y sin antorchas.'),
                ('hero', 'Los arietes se detienen fuera de las murallas. El correo llegó a tiempo.'),
                ('protected', 'Los barrios no juramentarán hoy. Solo han accedido a dejar pasar el '
                              'agua y el grano.'),
                ('companion', 'Con eso ya es una ciudad más abierta que antes.'),
                ('narrator', 'En la ceniza quedó una huella de sandalias, desde las puertas '
                             'interiores hasta el mercado.'),
            ],
            protected=('Irena, portavoz de los barrios', 'Peasant'),
            resolution=(
                'La portavoz abrió las puertas desde dentro. Los vecinos guiaron a la alianza por '
                'calles donde todavía ardían las lámparas. Nadie apagó ninguna: eran las señales de '
                'los barrios, y esa noche indicaban camino libre.'),
        ),
        dict(
            title='La reina que no descansaba',
            goal='conquer',
            biome='ruins',
            antagonist='Maura Vey',
            opening=(
                'Maura ofreció entregar provincias a cada aliado si abandonaban a los demás. Había '
                'preparado siete documentos, convencida de que cualquier pacto era una colección de '
                'ambiciones comprables. Cada tratado estaba escrito para un pueblo concreto, con '
                'fronteras generosas y una cláusula que dejaba a los demás fuera de la mesa. La '
                'reina no había dormido desde el comienzo de la guerra y seguía firmando de memoria. '
                'Darian entró en el palacio en ruinas con las siete respuestas en la mano.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Sus ofertas son reales. Algunos podrían salvar a su pueblo marchándose '
                              'ahora.'),
                ('hero', (
                    'Y condenar al siguiente. Hemos leído juntos la letra pequeña de demasiados '
                    'contratos.')),
                ('antagonist', 'He preparado siete tratados, uno por pueblo. Cada uno recibe '
                               'provincias si abandona a los demás. Firmad y marchaos.'),
                ('hero', 'Siete tratados y ninguna pregunta: eso no es una oferta, es un despiece.'),
                ('narrator', 'Objetivo: derrotad al líder enemigo. Maura Vey manda desde el palacio '
                             'en ruinas.'),
                ('Alba', 'Valdara aceptará un tratado si el mar sigue siendo de todos. Que lo lea mi '
                         'puerto, no tu notario.'),
                ('Nerea', 'Mi condición es más simple: ningún tratado menciona cautivos. Si aparece '
                          'la palabra, lo rompo.'),
                ('Sevrin', 'Yo firmé con la reina y sigo pagando esa firma. Aviso a quien vaya a '
                           'leer: se puede decir no.'),
                ('hero', 'Esta vez se puede decir no dos veces: primero al tratado, y después a la '
                         'guerra.'),
                ('antagonist', 'Ninguna alianza sobrevive a una mesa con siete sillas. Siempre hay '
                               'una que se levanta.'),
                ('hero', 'Entonces pondremos una silla de más, para quien quiera escuchar sin '
                         'firmar.'),
                ('companion', 'No creas que quiere negociar. Quiere que os peleéis por los '
                              'documentos.'),
                ('Alba', 'Que los lea la asamblea entera. Cada pueblo su tratado, en voz alta.'),
                ('hero', 'Y ninguna firma vale si alguien la leyó con una espada detrás. Que se '
                         'retiren las armas de la sala.'),
                ('narrator', 'El palacio conserva el archivo intacto. La reina no ha dormido desde '
                             'que empezó la guerra.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 5', [
                    ('antagonist', 'He quemado un tratado. El pueblo que lo recibió ya ha visto lo '
                                   'que cuesta esperar.'),
                    ('narrator', 'Quedan seis documentos sobre la mesa, y ninguna firma al pie.'),
                ]),
                ('village captured', [
                    ('Nerea', 'Ese patio tiene pozo. Dejadlo abierto a los vecinos y no lo uséis '
                              'como puesto.'),
                ]),
                ('turn 8', [
                    ('Sevrin', 'La reina ofrece lo mismo que me ofreció a mí. Firmé por miedo y '
                               'tardé veinte años en leer la letra pequeña.'),
                    ('hero', 'Pues que se lea ahora, entera, delante de todos.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'La reina cayó sin firmar nada, y los siete tratados quedaron sobre '
                                 'la mesa, cada uno con su silla vacía.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que la guardia real cierre la sala.'),
                ]),
            ],
            victory=[
                ('Alba', 'He leído el tratado de Valdara. Lo rechazo y el puerto sigue en la '
                         'alianza.'),
                ('hero', 'Anotadlo: rechazo sin consecuencias. Esa es la cláusula que la reina nunca '
                         'entendió.'),
                ('Nerea', 'Los otros seis siguen sobre la mesa. Que cada pueblo decida el suyo en su '
                          'casa.'),
                ('Sevrin', 'Yo no firmo nada más. Pero tampoco voy a impedir que otros lean.'),
                ('narrator', 'Maura fue llevada ante representantes de sus víctimas. Darian prohibió '
                             'que su nombre se añadiera a ningún contrato funerario.'),
            ],
            protected=None,
            resolution=(
                'Maura perdió el trono y fue llevada ante representantes de sus víctimas. Darian '
                'prohibió que su nombre se añadiera a ningún contrato funerario. Los siete tratados '
                'se archivaron sin firmas, y cada pueblo guardó el suyo como recordatorio de lo que '
                'había podido rechazar.'),
        ),
        dict(
            title='La última entrega',
            goal='escape',
            biome='mountain',
            antagonist='Guardián del Sello Roto',
            opening=(
                'El sello central debía destruirse en la montaña donde se había tallado. Sus últimos '
                'guardianes, incapaces de comprender que la reina ya no mandaba, persiguieron a '
                'Darian hasta la cámara abierta. El camino subía en cuatro revueltas, y en cada una '
                'esperaba una guardia que había jurado antes de que Maura naciera. Sevrin subía '
                'detrás, contando las cadenas que iban a romperse con el sello. La cima estaba '
                'cubierta de nieve y no tenía techo: allí no había archivo donde guardar nada.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Cuando lo destruyas, Sevrin podrá descansar. No habrá otra oportunidad de '
                    'preguntarle nada.')),
                ('hero', 'Ya dio su testimonio. No nos debe una eternidad.'),
                ('narrator', 'Objetivo: llevad a Darian y el sello hasta la bandera de la cámara '
                             'abierta, en la cima.'),
                ('Sevrin', 'Antes de que subáis, decidme dónde vais a depositar los nombres.'),
                ('hero', 'En las brasas, uno por pueblo. Ninguno irá a un archivo real.'),
                ('antagonist', 'El sello no se destruye: se entrega. Yo soy su último guardián y no '
                               'reconozco otra reina.'),
                ('hero', 'No te pido que reconozcas a nadie. Te pido que dejes pasar.'),
                ('antagonist', 'Los guardianes juramos antes de que naciera Maura. Un juramento no '
                               'caduca porque cambie el nombre.'),
                ('companion', 'Podemos romperlo delante de ti, para que lo veas. No hace falta que '
                              'lo creas.'),
                ('Sevrin', 'Os acompaño con una condición: si caigo en la subida, no me dejéis '
                           'convertido en contrato. Devolvedme a la piedra.'),
                ('hero', 'Dicho queda. Nadie escribirá tu nombre en un registro.'),
                ('Sevrin', 'Y si un pueblo decide no recibir brasa, se queda sin ella y sin '
                           'castigo. Ya lo he visto cumplirse.'),
                ('narrator', 'La cámara abierta está en la cima. El Guardián ha apostado esqueletos '
                             'en cada revuelta del camino.'),
                ('hero', 'Subiremos en fila, con el sello delante. Ena, si alguien cae, no te quedes '
                         'atrás sola.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', 'He sellado el camino bajo. Ahora solo queda la subida, y arriba '
                                   'no hay sombra donde esconderse.'),
                    ('narrator', 'La primera revuelta está cortada. Las otras tres siguen abiertas.'),
                ]),
                ('turn 7', [
                    ('companion', 'Los esqueletos del sello no atacan a quien no lleva el nombre. '
                                  'Sevrin, camina detrás de mí.'),
                    ('Sevrin', 'Detrás de ti o delante, da igual. Tampoco a mí me queda sombra.'),
                ]),
                ('village captured', [
                    ('narrator', 'Un refugio de pastores les deja pasar. No hay peaje: la montaña no '
                                 'pertenece a nadie, dicen.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El Guardián se quedó de pie hasta que el sello tocó la cámara. '
                                 'Entonces se sentó, muy despacio.'),
                ]),
                ('time limit', [
                    ('narrator', 'Quedan dos turnos antes de que la nieve cierre la cámara.'),
                ]),
            ],
            victory=[
                ('Sevrin', 'He oído romperse las cadenas de todos los que firmaron como yo. No todas '
                           'eran de la reina.'),
                ('hero', 'Las de la alianza también. Lo escribimos así.'),
                ('companion', 'Ya dio su testimonio. No nos debe una eternidad.'),
                ('Sevrin', 'No os debo nada. Pero quiero dejar una última hoja: la lista de los que '
                           'quedan por liberar.'),
                ('narrator', 'Darian depositó el sello entre las brasas y la nieve lo cubrió antes '
                             'del amanecer.'),
            ],
            protected=None,
            resolution=(
                'Darian depositó el sello entre las brasas. El último correo de la guerra fue una '
                'lista de nombres liberados, enviada a todos los pueblos sin exigir respuesta. '
                'Sevrin eligió quedarse en la cámara hasta que la nieve borró el camino, y nadie '
                'escribió su nombre en ningún registro.'),
        ),
    ],
)
