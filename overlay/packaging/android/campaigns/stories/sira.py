"""Los que escuchan la piedra — Sira de las Siete Vetas. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='sira',
    title='Los que escuchan la piedra',
    hero='Sira de las Siete Vetas',
    companion='Tarek del Eco',
    companion_type='CBM Litario Resonador',
    race='cbm_litario',
    recruit='CBM Litario Guardian,CBM Litario Resonador,CBM Litario Tejedor,CBM Litario Explorador',
    enemy='loyalists',
    length='Corta · 5 escenarios · 2–4 horas',
    premise=(
        'Los litarios nacen cuando una montaña aprende a recordar. Sira, joven portadora de siete '
        'memorias incompatibles, debe salvar las cámaras de nacimiento de su pueblo sin convertirse '
        'en la voz única que su consejo exige.'),
    ending=(
        'El consejo dejó de hablar desde un solo pedestal. Cada cámara eligió a su portavoz y ninguna '
        'veta fue cerrada por disentir. Sira no fundó una dinastía: enseñó a escuchar el silencio '
        'entre dos respuestas.'),
    chapters=[
        dict(
            title='La primera grieta',
            goal='escape',
            biome='cave',
            antagonist='Capataz Edran',
            opening=(
                'La perforadora abrió una grieta en la cámara donde Sira despertaba. Los mineros '
                'creyeron haber encontrado estatuas. Solo cambiaron de opinión cuando una de ellas '
                'apartó del derrumbe a un niño humano. La mina se llama Vena Hundida y lleva tres '
                'generaciones arrancando basalto de sus galerías. Bajo la Séptima duerme la cámara '
                'del eco: si la perforadora llega antes, los litarios que aún no han despertado '
                'saldrán en bloques y nadie volverá a oír sus nombres. Sira tiene hasta que se '
                'cierre la puerta de basalto para sacarlos por el paso viejo. Un solo error y la '
                'montaña queda en silencio para siempre.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Si golpeamos sus herramientas, oirán una amenaza. Si no lo hacemos, no '
                    'volveremos a oír a los nuestros.')),
                ('hero', 'Abriremos un camino hasta la cámara del eco. Quien baje el pico podrá marcharse.'),
                ('antagonist', (
                    'Me llamo Edran, capataz de Vena Hundida. Tengo un contrato con la Casa del '
                    'Diezmo y una cuadrilla que cobra por bloque, no por preguntas.')),
                ('hero', (
                    'Yo soy Sira, portadora de siete memorias. Ninguna dice que un contrato pueda '
                    'comprar a quien todavía duerme.')),
                ('companion', (
                    'Habla bajo. Cada palabra tuya despierta a tres guardianes y a diez mineros '
                    'asustados.')),
                ('narrator', (
                    'La puerta de basalto está al este. Sira debe alcanzarla en menos de treinta y '
                    'dos turnos; si cae o vence el plazo, la cámara del eco se pierde.')),
                ('Nilo, el niño', (
                    'Yo bajé con mi padre. Él dice que las estatuas no sangran, pero tú me apartaste '
                    'del derrumbe.')),
                ('hero', (
                    'Sangramos poco y recordamos mucho. Quédate detrás de mí y no toques la piedra '
                    'que canta.')),
                ('narrator', (
                    'El niño humano seguirá a Sira hasta la salida. Si lo dejan atrás, el capataz lo '
                    'usará de rehén en la puerta.')),
                ('antagonist', (
                    'Si esa puerta no se abre a mi manera, la Casa manda inspectores y cierra la '
                    'mina. Cientos de familias se quedan sin jornal.')),
                ('hero', 'Entonces ábrela tú. Nadie te ha pedido que la cierres.'),
                ('companion', (
                    'Los mineros no son el enemigo. Tienen picos, tienen miedo y tienen hambre, y '
                    'las tres cosas aconsejan mal.')),
                ('hero', 'Que nadie golpee primero. Si un pico baja, apartadlo y seguid andando.'),
                ('antagonist', (
                    'Podéis iros. Dejadme los bloques ya cortados y no os seguiré. La Casa solo '
                    'quiere su peso en piedra.')),
                ('companion', 'La piedra que pesa es la que duerme. La que despierta no se deja cargar.'),
                ('hero', (
                    'Faltan dos voces en la Séptima. Cuéntalas cuando lleguemos, Tarek, y no me '
                    'digas que soy yo.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('narrator', (
                        'Almacén de la cuadrilla tomado. Los mineros que lo custodiaban dejan los '
                        'picos y retroceden.')),
                    ('hero', 'Que se retiren. No hemos venido a contar bajas.'),
                ]),
                ('turn 6', [
                    ('antagonist', (
                        'Cierro las compuertas de ventilación. Si queréis aire, abrid la puerta a mi '
                        'manera.')),
                    ('companion', 'El humo sube por el pozo viejo. Nos quedan dos rutas y una se estrecha.'),
                ]),
                ('turn 12', [
                    ('narrator', (
                        'Mitad del plazo. La perforadora sigue mordiendo la Séptima y las voces de '
                        'dentro se oyen más débiles.')),
                    ('hero', 'Aunque no lleguemos a todas, llegaremos a la puerta.'),
                ]),
                ('time limit', [
                    ('narrator', 'Últimos turnos. La puerta de basalto empieza a cerrarse sola.'),
                    ('hero', 'Corred. Yo sostengo la piedra hasta que pase el último.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'No era mi montaña, era mi jornal. Que la Casa mande a otro y le explique '
                        'la diferencia.')),
                    ('hero', 'Se la explicaremos nosotros, con la puerta abierta.'),
                ]),
            ],
            victory=[
                ('Nilo, el niño', (
                    'La puerta deja pasar el aire. Nunca había oído respirar a una piedra.')),
                ('companion', 'Cientos de voces. Muy débiles, pero cuentan y se responden.'),
                ('hero', 'Que cada una salga por su propio paso. No las apretéis en fila, se ahogan.'),
                ('narrator', 'Los nacidos cruzan la galería vieja mientras la perforadora se apaga detrás.'),
                ('hero', (
                    'Edran tenía razón en una cosa: alguien tendrá que explicar esto a la Casa del '
                    'Diezmo.')),
            ],
            protected=None,
            resolution=(
                'Tras la puerta de basalto, Sira oyó cientos de voces muy débiles. Los nacimientos se '
                'estaban apagando. Contó las que respondían y le faltaron dos: la perforadora había '
                'sellado la Séptima antes de detenerse. En la lista de la cuadrilla figuraban '
                'litarios que nadie había visto despertar, y la Casa del Diezmo la había firmado con '
                'una rúbrica que Sira reconocería más adelante.'),
        ),
        dict(
            title='Nombres bajo el martillo',
            goal='rescue',
            biome='quarry',
            antagonist='Inspectora Nes',
            opening=(
                'Los extractores habían numerado a los litarios cautivos según la pureza de sus '
                'vetas. Entre ellos estaba el guardián que recordaba el nombre de la montaña antes de '
                'que existieran los reinos humanos. La cantera de Piedra Partida lleva dos meses '
                'abierta y ya tiene catastro: cada prisionero lleva un número pintado en el hombro. '
                'El guardián se llama Varon de la Raíz y guarda ese nombre antiguo. Si lo cortan en '
                'bloques, el nombre se pierde para siempre y el catastro queda como la única memoria '
                'del pueblo. La inspectora Nes firma cada partida y cree que sus cifras no mienten.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'En la lista no aparece mi maestro. Solo una pieza de cuarenta arrobas.'),
                ('hero', 'Lo llamaremos por su nombre hasta que estas paredes lo recuerden.'),
                ('narrator', (
                    'Varon de la Raíz está enjaulado al norte. Liberadlo y llevadlo a la marca de '
                    'salida en menos de treinta y dos turnos; si muere, su nombre se pierde con él.')),
                ('antagonist', (
                    'Soy Nes, inspectora de la Casa. Cuarenta y una piezas, peso exacto, ninguna '
                    'merma. Las cifras no tienen opinión, por eso las prefiero.')),
                ('hero', 'Una cifra no distingue a un durmiente de un bloque. Esa es tu merma, inspectora.'),
                ('companion', (
                    'El maestro cantaba cuando lo sacaron. Ahora solo lo oigo contar hasta cuarenta.')),
                ('antagonist', (
                    'Nadie ha matado a nadie. Hay un contrato, hay una nómina y hay una cuenta que '
                    'cuadra. Enseñadme la ley que rompí.')),
                ('hero', (
                    'La ley que no está escrita: no se vende a quien no ha dicho que sí. Ese es todo '
                    'el pliego.')),
                ('narrator', (
                    'Los guardianes de Nes vigilan las grúas. La jaula no tiene puerta, tiene '
                    'cerrojo: hay que abrirla desde dentro.')),
                ('companion', 'Puedo resonar el cerrojo, pero me oirán. Tú decides cuándo.'),
                ('hero', 'Cuando el maestro esté a diez pasos. Ni antes ni después.'),
                ('protected', (
                    'No me saquéis por la grúa. Bajadme por la rampa, aunque tardemos; quiero sentir '
                    'el suelo bajo los pies.')),
                ('hero', 'Vas por delante. Si te hieren, paramos la extracción y no seguimos hasta curarte.'),
                ('antagonist', (
                    'Si sacáis esa pieza, el catastro queda incompleto. Un catastro incompleto cierra '
                    'la cantera, y la cantera da de comer a dos pueblos.')),
                ('hero', (
                    'Pues que la cierren con los nombres completos. Prefiero un pueblo con memoria '
                    'que dos con nómina.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('companion', (
                        'El primer puesto de control es nuestro. Las listas siguen colgadas en la '
                        'caseta, con los números todavía frescos.')),
                    ('hero', 'Arrancadlas. Que cada guardián se lleve su número a casa.'),
                ]),
                ('half strength', [
                    ('protected', 'Me han alcanzado el hombro donde pintaron el cuatro. Que no me lo tachen.'),
                    ('hero', 'Nadie va a tachar nada. Tarek, no lo dejes solo ni un turno.'),
                ]),
                ('turn 8', [
                    ('antagonist', (
                        'He cuadrado las cuentas con las piezas que quedan. Si falta una, el '
                        'descuadre es vuestro.')),
                    ('narrator', 'Las grúas giran hacia la jaula. Nes no manda cerrar: manda pesar.'),
                ]),
                ('time limit', [
                    ('narrator', (
                        'El plazo se agota. La siguiente partida sale al amanecer y Varon está en '
                        'ella.')),
                    ('hero', 'Entonces salimos antes. Nadie cobra un amanecer ajeno.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Los números eran neutrales. Yo también. ¿Y ahora quién carga con la cuenta?'),
                    ('hero', 'La Casa que te la encargó. Empieza por devolver el anticipo.'),
                ]),
            ],
            victory=[
                ('protected', (
                    'El nombre de la montaña es un río que todavía no ha bajado. Lo llevo yo y lo '
                    'digo entero cada noche.')),
                ('companion', 'Mi maestro ha vuelto a cantar. Desafina, pero canta.'),
                ('hero', 'Que lo canten los dos. Dos voces aguantan más que una, aunque se contradigan.'),
                ('narrator', (
                    'Varon cruza la marca de salida por la rampa, con el número cuatro todavía '
                    'pintado en el hombro.')),
                ('hero', (
                    'El catastro venía firmado. Si Nes lo firmó, alguien lo autorizó más arriba. '
                    'Seguiremos esa rúbrica.')),
            ],
            protected=('Varon de la Raíz', 'CBM Litario Explorador'),
            resolution=(
                'El guardián explicó que el consejo había autorizado la extracción a cambio de '
                'herramientas. Los contratos no distinguían la piedra dormida de la que soñaba. '
                'Varon guardó el número pintado en el hombro como prueba. Sira comparó la rúbrica '
                'del catastro con la séptima de sus memorias y no pudo dormir: la letra era la del '
                'consejero que había portado esas memorias antes que ella.'),
        ),
        dict(
            title='El consejo inmóvil',
            goal='beacons',
            biome='cave',
            antagonist='Custodio de la Veta Única',
            opening=(
                'El consejo selló los resonadores para que nadie escuchara sus pactos. Sira '
                'necesitaba despertar los tres archivos públicos. Sus custodios juraban que la '
                'obediencia era la única forma de conservar la memoria. La sala del consejo ocupa '
                'tres terrazas sobre la Veta Única y huele a aceite de lámpara. Los archivos están '
                'sellados con cera y con juramento: si Sira no los abre, el pacto que autorizó la '
                'extracción seguirá siendo secreto. El custodio de guardia la conoce desde niña y le '
                'enseñó a resonar; cree de verdad que una sola voz evita la guerra. Si Sira fracasa, '
                'el consejo fundirá las siete cámaras en una y nadie volverá a discrepar en la '
                'montaña.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Uno de tus siete recuerdos pertenece al consejero que firmó. ¿Cómo lucharás '
                    'contra ti misma?')),
                ('hero', 'Recordar un error no me obliga a repetirlo.'),
                ('narrator', (
                    'Objetivo: encender los tres archivos de la Veta Única en treinta y dos turnos. '
                    'Cada archivo iluminado revela una parte del pacto; si el plazo vence, el '
                    'consejo vuelve a sellarlos.')),
                ('antagonist', (
                    'Sira, yo te enseñé a sostener una nota sin romperla. No te enseñé a romper el '
                    'consejo que te dio la nota.')),
                ('hero', 'No vengo a romperlo, maestro. Vengo a que se le oiga firmar.'),
                ('antagonist', (
                    'Una voz única negocia. Siete voces se pelean y los humanos escuchan la pelea. '
                    'La obediencia ha salvado más cámaras que la razón.')),
                ('hero', (
                    'Y ha vendido más nacimientos. La obediencia no distingue lo que salva de lo '
                    'que calla.')),
                ('companion', 'Los custodios son tres. Conozco a dos: uno te abre la puerta y el otro te denuncia.'),
                ('narrator', (
                    'El primer archivo está en la terraza baja, el segundo junto al pozo y el '
                    'tercero en la sala sellada. Hacen falta los tres.')),
                ('antagonist', (
                    'Ese contrato lo firmé yo, no la montaña. Si lo publicas, la culpa es mía y el '
                    'castigo de todos.')),
                ('hero', (
                    'Por eso hay que publicarlo. La culpa de uno no puede costar la memoria de '
                    'todos.')),
                ('companion', (
                    'Tu séptima memoria es ese contrato. Cuando arda el tercer archivo, la vas a '
                    'recordar entera.')),
                ('hero', 'Ya la recuerdo entera. Lo que no recuerdo es haber dicho que sí.'),
                ('antagonist', (
                    'Si enciendes esos fuegos, el consejo te nombrará enemiga y yo tendré que firmar '
                    'la orden.')),
                ('hero', (
                    'Fírmala. Yo firmé algo peor sin saberlo; al menos tú lo harás con los ojos '
                    'abiertos.')),
                ('narrator', (
                    'En las galerías bajas siguen atrapados mineros humanos. El eco de los archivos '
                    'puede guiarlos o sepultarlos; la decisión es de Sira.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('narrator', (
                        'Primer archivo encendido. La terraza baja repite el nombre de la Casa del '
                        'Diezmo y la cifra de su anticipo.')),
                    ('antagonist', 'No sabes lo que has encendido. Ese nombre sostiene el techo que nos cubre.'),
                ]),
                ('beacon lit 2', [
                    ('companion', (
                        'Segundo archivo. El pacto menciona herramientas, sal y un pasillo abierto '
                        'para los carros humanos.')),
                    ('hero', 'Un pasillo, no una caravana. Que lo oiga quien lo negoció.'),
                ]),
                ('beacon lit 3', [
                    ('antagonist', 'Está entero. Ahora todos saben que fui yo quien firmó. ¿Contento?'),
                    ('hero', 'No. Ahora todos saben qué firmaste, que no es lo mismo.'),
                ]),
                ('turn 10', [
                    ('narrator', (
                        'Los custodios apagan lámparas para que los archivos no se lean desde fuera. '
                        'La sala se queda a oscuras por tramos.')),
                    ('hero', 'Encended con lo que tengáis. El pacto no necesita luz para ser cierto.'),
                ]),
                ('time limit', [
                    ('narrator', (
                        'Últimos turnos. El consejo prepara la fusión de las siete cámaras en una '
                        'sola voz.')),
                    ('hero', 'Todavía no. Falta el eco del pozo.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Una voz sola no discute. Yo quería eso: que nadie tuviera que elegir.'),
                    ('hero', 'Elegir es lo único que nos hace libres. Empieza tú.'),
                ]),
            ],
            victory=[
                ('companion', 'Los tres archivos arden a la vez. La montaña entera está repitiendo tu contrato.'),
                ('hero', 'Que lo oigan las cámaras y decidan si quieren seguir llamándome enemiga.'),
                ('antagonist', (
                    'He firmado la orden. Que conste que la firmé sabiendo lo que hacía, por primera '
                    'vez en treinta años.')),
                ('narrator', 'El consejo no se disuelve: se queda quieto, con las siete cámaras escuchándose entre sí.'),
                ('hero', 'Quieto no es lo mismo que sordo. Esperaremos a que aprendan a oírse.'),
            ],
            protected=None,
            resolution=(
                'Las cámaras oyeron el contrato completo. Algunas voces pidieron venganza; otras, '
                'ayuda para sacar a los humanos atrapados en las galerías. Sira abrió la galería '
                'baja antes de responder a ninguna de las dos. Cuando volvió a la terraza, el '
                'consejo seguía inmóvil, pero ya nadie fingía que el pacto no existía. En su séptima '
                'memoria, la rúbrica del consejero tenía ahora fecha, testigos y una voz que la leía '
                'en alto.'),
        ),
        dict(
            title='El peso de los vivos',
            goal='escort',
            biome='quarry',
            antagonist='Ingeniero Voss',
            opening=(
                'Voss intentó inundar las minas para borrar sus cuentas. Una aprendiz humana conocía '
                'la válvula de emergencia. Transportarla por las galerías abiertas dividió a los '
                'litarios que acababan de liberarse. La Cantera Alta baja en espiral hasta el nivel '
                'del río y Voss ya ha abierto dos compuertas. La aprendiz Leth lleva la llave de la '
                'válvula grabada en la piel de tanto usarla. Si el agua llega a la Séptima, se ahogan '
                'por igual los liberados y los mineros que siguen abajo. Voss dice que solo cumple '
                'una orden de la Casa: borrar los libros antes de que un auditor los lea.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', (
                    'Nos han vendido por peso. Ahora arriesgamos las vetas por alguien que apenas '
                    'pesa nada.')),
                ('hero', 'El peso nunca fue la medida correcta.'),
                ('narrator', (
                    'Leth debe llegar a la válvula, al oeste, dentro de treinta y dos turnos. Si cae '
                    'o el plazo vence, el agua sube hasta la cámara del eco.')),
                ('protected', (
                    'Sé dónde está la válvula. La cerré dos veces cuando era aprendiz, una por cada '
                    'turno de castigo.')),
                ('hero', 'Irás en medio de la columna. Ni delante ni detrás: donde puedas caer y alguien te recoja.'),
                ('antagonist', (
                    'No inundo nada por gusto. Tengo dos compuertas abiertas y una orden firmada para '
                    'vaciar los libros.')),
                ('hero', 'Hay libros y hay gente abajo. Ordena tus papeles por peso, a ver cuál se hunde primero.'),
                ('antagonist', (
                    'Los libros son la prueba de lo que pagamos. Si se pierden, vuestras '
                    'liberaciones no valen nada ante un tribunal.')),
                ('hero', 'Un tribunal que necesita ahogar testigos no es un tribunal. Es una compuerta más.'),
                ('companion', 'Los liberados discuten si escoltarla. Dicen que una humana no puede valer una veta.'),
                ('protected', 'Puedo llegar sola hasta la válvula. Solo necesito que alguien cierre la puerta detrás de mí.'),
                ('hero', (
                    'Vas acompañada. El que no quiera caminar a tu lado puede volver a su cámara y '
                    'esperar el agua.')),
                ('companion', (
                    'El agua sube dos tramos de escalera por hora. Si llegamos tarde, habrá que subir '
                    'a los rezagados a pulso.')),
                ('hero', 'Subiremos a quien quepa y volveremos por quien no. Nadie decide hoy quién se queda.'),
                ('antagonist', (
                    'Si cierras la válvula, el agua se queda dentro y la Casa me pedirá cuentas por '
                    'cada bloque no extraído.')),
                ('hero', 'Que te las pida. Nosotros ya hemos pagado la nuestra.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('narrator', (
                        'Primer relevo de la cantera tomado. En la caseta hay planos mojados: Voss '
                        'lleva contando compuertas desde el invierno.')),
                    ('hero', 'Guardadlos. Todo lo que cuente se lo devolveremos firmado.'),
                ]),
                ('half strength', [
                    ('protected', (
                        'Me he torcido el tobillo en la escalera. Dadme la pared y sigo; no pienso '
                        'ser el peso que os retrase.')),
                    ('hero', 'Tú marcas el paso. El que se retrase, se retrasa con nosotros.'),
                ]),
                ('turn 8', [
                    ('antagonist', 'He abierto la tercera compuerta. Ya no manda el ingeniero sobre el agua: manda el río.'),
                    ('companion', 'Se oye subir por el pozo. Nos quedan dos escaleras secas.'),
                ]),
                ('time limit', [
                    ('narrator', 'El agua alcanza el segundo tramo. La válvula está al final de la galería oeste.'),
                    ('hero', 'Corred hacia la válvula. Yo cierro las puertas que vayan quedando atrás.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'Los libros se mojan igual conmigo vivo que muerto. ¿De qué me sirvió cumplir '
                        'la orden?')),
                    ('hero', 'De nada. Pero la aprendiz conoce la válvula, y eso sí sirve.'),
                ]),
            ],
            victory=[
                ('protected', 'La válvula gira. El agua deja de subir a media escalera y se queda quieta, como si escuchara.'),
                ('companion', 'Hay mineros humanos en el tercer tramo. Suben agarrados a la misma cuerda que nosotros.'),
                ('hero', 'Que suban. La cuerda aguanta si no soltamos todos a la vez.'),
                ('protected', (
                    'Voss tenía razón en una cosa: los planos pesaban. Yo peso menos y he cerrado la '
                    'puerta que iba a borrarlos.')),
                ('narrator', (
                    'Cada cámara recibe una copia de los planos, todavía húmeda. Abrir o cerrar una '
                    'puerta ya no tiene un solo dueño.')),
            ],
            protected=('Leth, aprendiz de ingeniería', 'Peasant'),
            resolution=(
                'La aprendiz cerró la válvula y entregó a cada cámara una copia de los planos. Por '
                'primera vez, los litarios pudieron decidir qué puertas abrir. Sira guardó el plano '
                'con la firma de Voss y lo puso junto a la rúbrica de su séptima memoria: la misma '
                'mano, la misma prisa por borrar. Leth se quedó en la Séptima, enseñando a leer los '
                'niveles del agua a quien nunca había visto un río.'),
        ),
        dict(
            title='Una montaña, muchas voces',
            goal='survive',
            biome='cave',
            antagonist='Mariscal del Diezmo',
            opening=(
                'El mariscal llegó para confiscar las minas. Sira distribuyó los resonadores entre '
                'las cámaras: debían mantenerlos cantando hasta que la montaña cerrara sus accesos '
                'militares, dejando libres los caminos de intercambio. La orden viene firmada en la '
                'capital y no admite dudas: toda veta con memoria es un recurso militar. Si los '
                'resonadores se apagan, los ingenieros fundirán las cámaras en una sola y la montaña '
                'cantará la marcha que le impongan. Sira reparte un resonador por cámara: siete '
                'voces distintas, ninguna obediente y ninguna sola. Hay que mantenerlas cantando '
                'doce turnos, hasta que la piedra cierre los pasos estrechos del ejército.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Podrías ordenar un solo canto. Sería más fuerte.'),
                ('hero', 'Sería más fácil de romper. Que cada cámara conserve su voz.'),
                ('narrator', (
                    'Objetivo: mantener las siete cámaras cantando doce turnos. Si Sira o Tarek '
                    'caen, el canto se corta y el mariscal toma la montaña.')),
                ('antagonist', (
                    'La capital me dio cuarenta días y un diezmo que cuadrar. No me pidió que os '
                    'entendiera: me pidió que os contara.')),
                ('hero', 'Cuéntanos como recurso y te responderemos como vecinos. Empieza por la palabra diezmo.'),
                ('antagonist', (
                    'Un diezmo es lo que se entrega sin discutir. Si discutís, deja de ser diezmo y '
                    'empieza a ser rebelión. Yo solo sirvo a la primera palabra.')),
                ('hero', 'Yo sirvo a siete que no dicen lo mismo. Ninguna manda sobre las otras.'),
                ('companion', (
                    'Las cámaras discuten entre ellas. Una quiere pactar y otra quiere cerrar los '
                    'caminos para siempre.')),
                ('hero', 'Que discutan y que se oigan. Ese ruido es la única prueba de que seguimos vivos.'),
                ('narrator', (
                    'Los ingenieros miden los pasos estrechos para volarlos. Si la piedra se cierra '
                    'antes, el ejército no puede subir.')),
                ('antagonist', (
                    'Puedo esperar. Tengo víveres y tengo órdenes. Vosotros tenéis canciones y una '
                    'montaña que se cansa de cantarlas.')),
                ('hero', 'Entonces no cantaremos igual toda la noche. Cambiaremos de voz cuando una se rinda.'),
                ('companion', '¿Y si alguna cámara decide pactar a solas?'),
                ('hero', (
                    'Pactará con su voz y responderá con ella. No la obligaremos a callar ni la '
                    'dejaremos sola.')),
                ('narrator', (
                    'En la puerta pequeña del valle esperan visitantes sin cadenas. Nadie debe '
                    'cerrarla, aunque la batalla empuje hacia allí.')),
                ('hero', 'La puerta del valle queda abierta. Si hay que elegir entre una muralla y una puerta, elegimos la puerta.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('antagonist', (
                        'Los ingenieros han marcado el primer paso. Si lo vuelan, subiré con carros y '
                        'no quedará canción que oír.')),
                    ('companion', 'La cámara del pozo desafina. Le queda cuerda para dos turnos más.'),
                ]),
                ('village captured', [
                    ('narrator', 'Primer puesto del diezmo desmantelado. En su registro no hay nombres, solo tonelajes.'),
                    ('hero', 'Escribid los nombres en el reverso. Que el próximo auditor lea a quién contaba.'),
                ]),
                ('turn 8', [
                    ('narrator', (
                        'Las siete cámaras se han turnado para no callar. La más joven ya no canta: '
                        'tararea.')),
                    ('hero', 'Que tararee. Mientras alguien tararee, la montaña sigue despierta.'),
                ]),
                ('time limit', [
                    ('narrator', 'Últimos turnos. El ejército empuja hacia la puerta pequeña del valle.'),
                    ('hero', 'Cerrad todo menos esa puerta. La dejamos abierta a propósito.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'La capital me pedirá cuentas por cuarenta días perdidos. Diré la verdad: la '
                        'montaña no era un recurso.')),
                    ('hero', 'Di que era muchas voces. Con eso tu informe ya sirve para algo.'),
                ]),
            ],
            victory=[
                ('companion', (
                    'La piedra ha cerrado los pasos militares. Siguen abiertos los caminos de '
                    'intercambio, estrechos pero libres.')),
                ('hero', 'Contad las cámaras. Que cada una diga en qué voz terminó el día.'),
                ('narrator', 'Siete respuestas distintas, ninguna idéntica. El mariscal escucha desde el valle sin entender el idioma.'),
                ('companion', 'Podrías haber cantado tú sola. Te habría salido más fuerte.'),
                ('hero', (
                    'Habría salido más fuerte y más corta. Prefiero siete voces que se contradigan y '
                    'duren.')),
            ],
            protected=None,
            resolution=(
                'El ejército se retiró cuando sus máquinas quedaron encajadas en pasos demasiado '
                'estrechos. En el valle, una puerta pequeña siguió abierta para los visitantes sin '
                'cadenas. Sira no volvió a firmar en nombre de nadie. Guardó la rúbrica de su '
                'séptima memoria junto al contrato del consejo, y cada cámara eligió a su portavoz '
                'sin que ninguna veta fuera cerrada por disentir.'),
        ),
    ],
)
