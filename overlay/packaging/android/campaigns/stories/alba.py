"""La última luz de Valdara — Alba. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='alba',
    title='La última luz de Valdara',
    hero='Alba',
    companion='Oren',
    companion_type='Merman Fighter',
    race='human',
    recruit='Spearman,Bowman,Footpad,Merman Fighter,Mage',
    enemy='outlaws',
    length='Breve · 3 escenarios · 1–2 horas',
    premise='Alba mantiene el faro de una ciudad que ya no figura en los mapas. '
            'Cuando llegan barcos sin tripulación, deberá elegir qué significa '
            'salvar su hogar: conservar sus muros o proteger a quienes viven en él.',
    ending='Valdara desapareció bajo el agua. Sus habitantes fundaron un puerto sin '
           'murallas y encendieron una lámpara por cada persona rescatada. Alba '
           'conservó su oficio: guiar a otros hacia una costa que aún no conocían.',
    chapters=[
        dict(
            title='Las barcas vacías',
            goal='rescue',
            biome='coast',
            antagonist='Sarel, el cobrador',
            opening='La campana del faro sonó a mediodía, aunque Alba había retirado su '
                    'badajo. En la playa aparecieron barcas vacías y, en sus bancos, '
                    'nombres de vecinos todavía vivos. Alba era la farera de Valdara: '
                    'encendía la torre al anochecer y cobraba de un concejo que llevaba '
                    'dos meses sin pagarle. Los hombres de Sarel cerraron el embarcadero '
                    'para cobrar por la huida. Nadie las había visto llegar: la marea las '
                    'dejó de costado, como si alguien las hubiera empujado desde dentro. '
                    'Alba contó once nombres escritos con una tinta que no era de la '
                    'ciudad, y reconoció la letra de su madre en el primero. Antes de la '
                    'pleamar quería escuchar esos once nombres fuera del agua, contados '
                    'uno por uno. Pero cada vecino que sacara de la aduana Sarel lo '
                    'apuntaría en su libro de deudas, y la primera cuenta del libro era el '
                    'faro. La vela del primer banco aún olía a brea, como si la barca '
                    'acabara de salir del astillero. Al anochecer midió el aceite que '
                    'quedaba en la torre: apenas tres fuegos, y en el concejo no quedaba '
                    'nadie a quien pedir más.',
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Mi hermana está encerrada en la aduana. Dice Sarel que '
                              'una deuda pesa más que una vida.'),
                ('hero', 'Abriremos esa puerta. Después discutiremos cuánto pesa su '
                         'libro de cuentas.'),
                ('narrator', 'La marea sube dos palmos por hora. La aduana tiene una sola '
                             'puerta y Sarel ha puesto dos hombres en ella.'),
                ('Sarel, el cobrador', 'Nadie sale del embarcadero sin pagar su fianza. '
                                       'Firmé con el concejo, no con la marea.'),
                ('hero', 'Enséñame esa firma y te la firmo yo delante de todo el muelle.'),
                ('Sarel, el cobrador', 'Puedes derribar la puerta. Yo firmo el destrozo '
                                       'y se lo cobro a los encerrados en la aduana.'),
                ('companion', 'Hay tres familias dentro. Si entramos con violencia, las '
                              'usarán de escudo.'),
                ('hero', 'Entonces entraremos por el agua. El embarcadero tiene muelles '
                         'bajos que nadie vigila, y tú sabes nadar mejor que ellos.'),
                ('companion', 'Conozco el paso. Pero la escalera de servicio cruje, y si '
                              'nos oyen tendremos que salir corriendo hacia la bandera.'),
                ('narrator', 'Nima, la hermana de Oren, está en la celda del fondo. '
                             'Escoltadla hasta la bandera de salida antes de la pleamar.'),
                ('companion', 'Ha estado tres días sin ver el mar. No la dejéis sola en '
                              'la primera esquina.'),
                ('hero', 'Va delante de nosotros. Siempre. Aunque grite que la dejemos.'),
                ('Sarel, el cobrador', 'Sé lo que escribieron en esas barcas. Si me '
                                       'quitáis la puerta, la ciudad se ahogará contando '
                                       'deudas.'),
                ('companion', 'La ciudad lleva contando deudas desde antes de que yo '
                              'aprendiera a nadar.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 2', [
                    ('antagonist', 'Once nombres en la arena y once fianzas sin pagar. '
                                   'Una ciudad que no puede pagar ya está perdida, y yo '
                                   'llevo sus cuentas.'),
                    ('hero', 'La ciudad está viva y subiendo a las barcas. Apunta eso en '
                             'tu libro, junto a la fecha.'),
                ]),
                ('village captured', [
                    ('antagonist', 'Todo lo que salga por esta playa queda escrito a '
                                   'vuestra cuenta. Mañana el concejo leerá mi libro y '
                                   'sabrá quién huyó sin pagar.'),
                    ('narrator', 'La marea cubre la senda de las dunas y solo queda seco '
                                 'el muelle estrecho. Sarel lo cierra con sus últimos '
                                 'hombres: decidid si lo forzáis o rodeáis por el agua.'),
                ]),
                ('turn 4', [
                    ('Sarel, el cobrador', 'He mandado abrir las compuertas del arrecife. '
                                           'Si no me pagáis, el agua hará mi trabajo.'),
                    ('narrator', 'La pleamar llegará antes del amanecer. El tiempo corre.'),
                ]),
                ('half strength', [
                    ('protected', 'Se me doblan las piernas. Volved por mí cuando baje '
                                  'la marea.'),
                    ('hero', 'La bandera está a un tiro de piedra. Apóyate en mi hombro '
                             'y la alcanzamos.'),
                ]),
                ('turn 6', [
                    ('antagonist', 'Sin mi libro esta plaza sería una pelea por los bancos '
                                   'de las barcas. El orden que os molesta es lo único que '
                                   'frena al más fuerte.'),
                    ('companion', 'Ese orden encerró a mi hermana tres días sin ver el '
                                  'mar.'),
                ]),
                ('turn 8', [
                    ('Sarel, el cobrador', 'Mis hombres no cobran por gusto. Cobran porque '
                                           'alguien tiene que decidir quién queda.'),
                    ('hero', 'Decide tú, entonces. Yo solo voy a sacar a los que quepan.'),
                ]),
                ('turn 10', [
                    ('Sarel, el cobrador', 'Cobraré la salida de cada nombre, aunque '
                                           'tenga que seguirla mar adentro. La deuda '
                                           'viaja con el deudor.'),
                    ('narrator', 'La pleamar ha borrado los muelles bajos y el agua llega '
                                 'ya a la cintura junto a la aduana. Sarel gana esperando: '
                                 'decidid si forzáis la bandera ahora o arriesgáis la '
                                 'subida completa.'),
                ]),
                ('enemy leader defeated', [
                    ('narrator', 'El libro de cuentas quedó abierto en el suelo del muelle. '
                                 'Nadie se detuvo a recogerlo.'),
                ]),
            ],
            victory=[
                ('protected', 'La tablilla dice que la marea subirá antes del amanecer. No '
                              'es una profecía: alguien abrió las compuertas del arrecife.'),
                ('companion', 'Velkan vendió el aceite del faro y ahora persigue a quien lo '
                              'vio hacerlo.'),
                ('hero', 'Pues que persiga. Nosotros ya sabemos dónde está la puerta.'),
                ('narrator', 'En la playa, las barcas vacías seguían esperando con sus '
                             'nombres a bordo.'),
            ],
            protected=('Nima', 'Peasant'),
            resolution='La cautiva llevaba una tablilla robada: la marea subiría antes del '
                       'amanecer. No era una profecía; alguien había abierto las compuertas '
                       'del arrecife. Alba mandó encender el faro sin badajo y comprendió '
                       'que ya no defendía una muralla, sino una lista de nombres. El libro '
                       'de Sarel se quedó abierto en el muelle y la marea lo firmó hoja por '
                       'hoja. Bajo la lámpara de la torre, la tinta de la tablilla era la '
                       'misma que Alba había visto en los bancos de las barcas. Antes del '
                       'alba, la niebla subió desde el agua y dejó mar adentro familias '
                       'remando a ciegas: solo tres luces juntas les enseñarían el camino '
                       'de vuelta.',
        ),
        dict(
            title='Tres fuegos en la niebla',
            goal='beacons',
            biome='coast',
            antagonist='Velkan, guardacostas',
            opening='Para que los pescadores encontraran a las familias evacuadas, había '
                    'que encender tres señales sobre los acantilados. Velkan había vendido '
                    'el aceite del faro y ahora perseguía a los testigos de su trato. Las '
                    'tres hogueras debían arder a la vez: una sola luz se confunde con un '
                    'reflejo, y dos parecen un incendio. Los barcos esperaban mar adentro, '
                    'remando a ciegas, guiándose por el ruido de la resaca. Alba subió al '
                    'primer acantilado con la última jarra de aceite y Oren contó los pasos '
                    'en la niebla: al vigésimo dejaron de verse las manos. La mecha del '
                    'primer brasero estaba cortada en seco, con hoja de cuchillo, no '
                    'gastada por la humedad. Si Velkan vendía la luz que nadie le había '
                    'pagado, Alba iba a encender la que la ciudad todavía debía a los '
                    'suyos. Al pie del acantilado el agua lamía ya el primer escalón de la '
                    'plaza, y por la calzada del norte venían antorchas a caballo: alguien '
                    'iba a cobrar antes de que la ciudad se hundiera.',
            intro=[
                ('companion', 'El aceite alcanza para tres fuegos pequeños. No para una '
                              'hoguera que vean los señores desde sus torres.'),
                ('hero', 'Las señales son para las barcas, Oren. Nunca fueron para los '
                         'señores.'),
                ('narrator', 'Tres puntos marcados en los acantilados. Llevad una unidad a '
                             'cada brasero antes de que la niebla cierre el puerto.'),
                ('companion', 'La niebla sube del agua y no del cielo. Esta noche nos '
                              'verán desde el mar y desde ningún otro sitio.'),
                ('Velkan, guardacostas', 'El aceite era mío. Vendí lo que sobraba después '
                                         'de cumplir con el faro.'),
                ('hero', 'Y el faro estuvo cuatro noches apagado hasta que lo '
                         'encendimos. Explícame qué cumpliste.'),
                ('Velkan, guardacostas', 'Explícame tú quién paga a los guardacostas cuando '
                                         'no hay barcos que cobren.'),
                ('hero', 'Nadie. Esa es la respuesta, y por eso hiciste mal el trabajo.'),
                ('companion', 'Sus hombres vigilan el sendero alto. Podemos subir por la '
                              'cala, pero tendremos que separarnos.'),
                ('hero', 'Nos separamos. Si uno no llega, los otros dos siguen encendiendo '
                         'fuegos.'),
                ('Velkan, guardacostas', 'Si enciendo una hoguera más, mañana no habrá '
                                         'guardacostas y los contrabandistas harán lo que '
                                         'quieran con el puerto.'),
                ('hero', 'Mañana habrá vecinos. Empieza por ahí y el resto sale solo.'),
                ('narrator', 'La niebla borra la costa a media altura. Los braseros se '
                             'encienden de dentro hacia fuera.'),
                ('companion', 'Oigo remos. No son de pesca: van muy despacio, para no '
                              'perderse.'),
            ],
            events=[
                ('turn 2', [
                    ('antagonist', 'Nadie pagó nunca por esa luz que vendí al mar: ni el '
                                   'concejo, ni los pescadores, ni vosotros. El aceite era '
                                   'lo único mío que quedaba dentro del faro.'),
                    ('hero', 'Esta noche la luz se paga con vecinos. Apúntalo en tu '
                             'cuaderno.'),
                ]),
                ('beacon lit 1', [
                    ('narrator', 'Primer fuego encendido. La niebla se tiñe de naranja y '
                                 'alguien responde desde el agua con dos golpes de remo.'),
                    ('antagonist', 'Apagad ese primer fuego y todavía podemos hablar. '
                                   'Puedo jurar que fue un incendio y ahorraros la cuenta '
                                   'del aceite.'),
                ]),
                ('beacon lit 2', [
                    ('Velkan, guardacostas', 'Dos luces son un incendio. Los señores '
                                             'mandarán gente a apagarlas.'),
                    ('hero', 'Que vengan a apagarlas con las manos.'),
                ]),
                ('turn 6', [
                    ('companion', 'Los guardacostas han cortado el sendero alto. Habrá que '
                                  'volver a bajar por la cala.'),
                    ('narrator', 'La cala queda a la vista del acantilado y el sendero alto '
                                 'ya no existe. Velkan os quiere separados para apagar un '
                                 'fuego cada vez: decidid si bajáis juntos o repartís '
                                 'unidades.'),
                ]),
                ('turn 8', [
                    ('antagonist', 'Cuando se levante la niebla recorreré las tres calas '
                                   'con mi cuaderno. Quien haya tocado el aceite firmará '
                                   'un pago, porque esta luz por fin se cobra.'),
                    ('narrator', 'El tercer acantilado solo se sube por una escalera '
                                 'estrecha y la niebla la borra a media altura. Velkan la '
                                 'defiende con sus últimos guardacostas: decidid quién '
                                 'sube y quién cubre la retirada.'),
                ]),
                ('turn 10', [
                    ('narrator', 'La niebla empieza a cerrarse sobre el tercer acantilado. '
                                 'Queda poco para que el puerto quede ciego.'),
                    ('Velkan, guardacostas', 'El faro ardió catorce años con mi aceite y '
                                             'mi sueldo. ¿Cuántas barcas se habrían '
                                             'salvado si alguien me hubiera pagado por '
                                             'encenderlo?'),
                ]),
                ('enemy leader defeated', [
                    ('Velkan, guardacostas', 'No vendí el aceite para huir. Lo vendí para '
                                             'comer, como todos.'),
                    ('hero', 'Nadie te ha pedido que te mueras de hambre. Te hemos pedido '
                             'que no apagues la luz.'),
                ]),
            ],
            victory=[
                ('companion', 'Tres luces respondieron desde el mar. Reconozco los golpes '
                              'de remo de mi familia.'),
                ('hero', 'Cuéntalos otra vez. Quiero saber cuántas barcas quedan fuera.'),
                ('companion', 'Cuatro barcas y una que va vacía, remolcada.'),
                ('narrator', 'Oren reconoció el ritmo de los golpes de remo de su familia. '
                             'Quedaba una última noche que comprarles.'),
            ],
            protected=None,
            resolution='Tres luces respondieron desde el mar. Oren reconoció el ritmo de los '
                       'golpes de remo de su familia. Quedaba una última noche que '
                       'comprarles, y Alba ya había decidido con qué iba a pagarla: con la '
                       'única cosa que la ciudad no había vendido todavía, su faro apagado. '
                       'En la arena del tercer acantilado apareció el cuaderno de '
                       'guardacostas de Velkan, con cada servicio anotado y ni un pago '
                       'firmado. Los braseros se consumieron antes del alba y la niebla se '
                       'los tragó sin dejar rescoldo. Antes de bajar a la plaza, Alba vio '
                       'antorchas avanzando por la calzada del norte: alguien venía a '
                       'cobrar lo suyo antes de que el agua cubriera el último escalón.',
        ),
        dict(
            title='El amanecer prestado',
            goal='survive',
            biome='harbor',
            antagonist='Sarel, sin puerto',
            opening='El agua lamía los peldaños de la plaza. Sarel regresó con mercenarios: '
                    'pretendía recuperar sus pagarés antes de que la ciudad se hundiera. '
                    'Alba instaló su última defensa junto a las barcas cargadas. No había '
                    'muralla que sostener, solo una fila de embarcaciones, doscientos '
                    'vecinos cargando cofres y una lámpara grande que ya nadie tenía fuerzas '
                    'para subir al acantilado. Alba seguía siendo la farera de Valdara, '
                    'aunque ya no quedara torre que encender: esta vez la luz tendría que '
                    'flotar. El badajo que había quitado de la campana colgaba del asa de '
                    'la lámpara, y con él tocaba la llamada cada vez que una barca quedaba '
                    'cargada. Antes del amanecer había que decidir qué se quedaba en la '
                    'plaza: las piedras o la última luz.',
            intro=[
                ('companion', 'Ya no queda sitio para la lámpara grande. Si la llevamos, '
                              'alguien tendrá que quedarse.'),
                ('hero', 'Entonces la dejamos encendida. Que la ciudad haga una última cosa '
                         'buena.'),
                ('narrator', 'Sarel ataca al amanecer. Resistid hasta que la última barca '
                             'esté cargada.'),
                ('Sarel, sin puerto', 'Me quitasteis la puerta y con ella mi oficio. Ahora '
                                      'todos pagaréis la mitad de lo que me debéis.'),
                ('hero', 'Nadie te debe nada. Y el agua no cobra intereses.'),
                ('Sarel, sin puerto', 'El agua no, pero mis mercenarios sí. Y son de fuera, '
                                      'así que no tienen familia en esta plaza.'),
                ('companion', 'Los veo desde aquí. Vienen por la rampa del mercado y por el '
                              'callejón de las redes.'),
                ('hero', 'Dos entradas y una lámpara. Pon a los niños a cargar y a los '
                         'viejos a gritar. Yo me quedo donde se rompa la fila.'),
                ('companion', 'Hay una barca más de las que contamos. Es la de la aduana.'),
                ('hero', 'Pues la cargamos. Y si hay que elegir, elegimos siempre la barca '
                         'que flota.'),
                ('narrator', 'Cada ronda ganada carga una barca. La plaza se hunde un '
                             'peldaño cada dos turnos.'),
                ('Sarel, sin puerto', 'Podéis salvar las piedras. Nadie os lo impide. Solo '
                                      'tendréis que quedaros dentro.'),
                ('hero', 'Las piedras ya están salvadas. Se llaman vecinos y van en esas '
                         'barcas.'),
            ],
            events=[
                ('turn 2', [
                    ('antagonist', 'No vengo por vuestras cabezas, vengo por mis pagarés. '
                                   'Una ciudad que no puede pagar ya está perdida, y '
                                   'vosotros la estáis cargando sin cerrar la cuenta.'),
                    ('narrator', 'La rampa del mercado admite cuatro hombres de frente y '
                                 'el callejón de las redes solo uno. Sarel empuja por '
                                 'ambos para llegar a las barcas: decidid cuál tapáis y a '
                                 'cuál dais la espalda.'),
                ]),
                ('turn 4', [
                    ('narrator', 'La mitad de las barcas están cargadas. La plaza ha perdido '
                                 'dos peldaños.'),
                    ('companion', 'Los mercenarios han encontrado el almacén de sal. Si lo '
                                  'prenden, arderá la rampa.'),
                    ('antagonist', 'Mi libro era lo único que esta plaza hacía por orden. '
                                   'Ahora cada cofre se carga por quien grita más alto, y '
                                   'eso también se apunta.'),
                ]),
                ('turn 6', [
                    ('Sarel, sin puerto', 'Cuando el agua llegue al arca, el mar se come '
                                          'mis pagarés y esta ciudad se queda debiendo '
                                          'para siempre. Llegaré antes que el agua.'),
                    ('narrator', 'La plaza ha perdido tres peldaños y la última barca se '
                                 'carga en marea alta. Sarel ataca donde la fila se rompe, '
                                 'buscando el arca de la aduana: decidid si tapáis el '
                                 'muelle o cubrís los últimos cofres.'),
                ]),
                ('turn 8', [
                    ('Sarel, sin puerto', 'Mis pagarés están en el arca de la aduana. '
                                          'Devolvedme el arca y dejaré las barcas.'),
                    ('hero', 'El arca se fue en la primera barca. Pregúntale al agua.'),
                ]),
                ('turn 10', [
                    ('narrator', 'Última barca en el muelle. Los que se queden no volverán '
                                 'a pisar tierra firme.'),
                    ('companion', 'Nima cuenta las cabezas. Todavía falta una familia.'),
                    ('antagonist', 'Os dejo las barcas y me llevo la cuenta entera. Mañana '
                                   'esta ciudad flotará, pero deberá cada luz que hoy '
                                   'regala.'),
                ]),
                ('enemy leader defeated', [
                    ('Sarel, sin puerto', 'Sin puerto no hay deuda. Sin deuda no hay '
                                          'ciudad. Eso es lo que me habéis enseñado.'),
                    ('hero', 'Entonces aprende algo nuevo antes de que suba el agua.'),
                ]),
            ],
            victory=[
                ('companion', 'Todas las barcas están fuera. La lámpara grande sigue '
                              'encendida en la plaza.'),
                ('hero', 'Que arda hasta que el agua la apague. Es lo último que le pedimos '
                         'a esta ciudad.'),
                ('narrator', 'Nadie le pidió a Alba que salvara las piedras. Ella apagó la '
                             'lámpara con agua de mar y subió a la última barca.'),
                ('companion', 'Cuando lleguemos a la otra costa, ¿qué encendemos?'),
                ('hero', 'Otra lámpara. Y una por cada persona que venga detrás.'),
            ],
            protected=None,
            resolution='Cuando la última barca salió, Alba apagó la lámpara con agua de mar. '
                       'Nadie le pidió que salvara las piedras. En la costa nueva nadie '
                       'conocía su nombre, y eso, por primera vez en su vida, no le pareció '
                       'una derrota. El badajo de la campana volvió al bolsillo de Alba: '
                       'era lo único que la torre había dejado salir. En la arena '
                       'encendieron una lámpara por cada persona que bajaba de una barca, y '
                       'Alba las contó despacio, una por una, hasta que la costa parecía '
                       'una constelación a ras del agua. Su oficio seguía siendo el mismo: '
                       'encender una luz para que alguien encontrara tierra.',
        ),
    ],
)
