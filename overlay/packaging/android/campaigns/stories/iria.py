"""La deuda del cielo — Iria Salcedo. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='iria',
    title='La deuda del cielo',
    hero='Iria Salcedo',
    companion='Belis',
    companion_type='Elvish Shaman',
    race='human',
    recruit='Elvish Fighter,Elvish Archer,Elvish Shaman,Scout,Mage',
    enemy='velarios',
    length='Media · 7 escenarios · 4–6 horas',
    premise=(
        'Una sombra borra los campos de los mapas de Iria. Los velarios, seres alados de quitina '
        'nacarada, cosechan la luz para sostener sus ciudades suspendidas. Cada victoria de la '
        'cartógrafa acerca esas ciudades a una caída sobre los pueblos que quiere proteger.'),
    ending=(
        'Los velarios desmontaron sus ciudades antes de que cayeran. Iria dibujó caminos entre '
        'pueblos que hasta entonces solo se habían conocido como sombras. En el margen dejó espacio '
        'para los nombres que aún faltaban.'),
    chapters=[
        dict(
            title='Un mediodía negro',
            goal='survive',
            biome='forest',
            antagonist='Recolectora Thess',
            opening=(
                'Iria descubrió que la tinta de su mapa se secaba antes que el trigo. Una estructura '
                'alada tapaba el sol y guerreros de cuatro brazos descendían a buscar los cristales '
                'de los molinos. La sombra no viajaba como una nube: avanzaba en línea recta y se '
                'detenía donde terminaban las eras. Iria ató una piedra a su cuerda de medir y '
                'comprobó que la mancha crecía cada vez que un velario tocaba el prisma del molino.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Las raíces sienten frío. No es una nube: alguien está llevándose el día.'),
                ('hero', (
                    'Resistiremos hasta evacuar a los segadores. Luego dibujaré de dónde viene esa '
                    'sombra.')),
                ('narrator', (
                    'Los segadores cruzan el río en tres tandas. Aguantad los cuatro turnos que '
                    'tardan en pasar y nadie quedará bajo la sombra.')),
                ('antagonist', (
                    'Traemos la cuota del distrito alto. Cada vela de esta nave da de beber a un '
                    'barrio entero; no venimos a matar, venimos a cobrar.')),
                ('hero', (
                    'Enséñame esa cuenta. Los molinos también riegan los campos de aquí abajo, y '
                    'esos campos no vuelan.')),
                ('antagonist', (
                    'La cuenta es simple: doscientos cristales por nave, treinta naves al mes. Si no '
                    'la lleno, me la quitan a mí y la llena otro que no pregunta.')),
                ('companion', 'Hay algo vivo dentro del cristal. Late, como una semilla al sol.'),
                ('narrator', (
                    'La sombra tarda seis turnos en girar. Mientras gire, la aldea no recibe luz ni '
                    'agua de la acequia.')),
                ('hero', 'Belis, marca los prismas de cada molino. Quiero saber cuál se apaga primero.'),
                ('companion', 'El del norte. Ya pierde color por la junta.'),
                ('narrator', (
                    'Cuando una ciudad del cielo desciende, no baja vacía: apiña tres mil vecinos en '
                    'caminos que ya tienen dueño y seca el acueducto que comparte con los pueblos.')),
                ('hero', (
                    'Por eso dibujo los caminos antes que las batallas. Un mapa cuenta cuánta agua '
                    'hay para todos.')),
                ('antagonist', (
                    'No me hables de mapas. El mío dice que si no subo la cuota, el consejo suelta '
                    'lastre, y el lastre son personas.')),
                ('hero', 'Entonces sube la cuota de otra parte. Aquí abajo solo hay trigo y gente.'),
                ('companion', (
                    'Thess tiene razón en una cosa: si su nave se apaga, alguien pagará por ello. '
                    'Solo que no elegiremos nosotros a quién.')),
                ('hero', 'Que sea ella la primera que mire a los ojos de los que paga.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 3', [
                    ('narrator', (
                        'La sombra gira sobre el molino del norte. El cristal pierde color por la '
                        'junta.')),
                    ('antagonist', (
                        'Si me lo entregáis entero, prometo dejar la aldea fuera de la próxima '
                        'cuenta.')),
                ]),
                ('village captured', [
                    ('hero', (
                        'Quitad los prismas del molino y ponedlos a la sombra. Que la luz vuelva al '
                        'canal.')),
                    ('narrator', (
                        'El agua vuelve a la acequia; los segadores pueden beber mientras cruzan.')),
                ]),
                ('turn 6', [
                    ('companion', (
                        'La nave está inclinándose. Si sigue así, soltará lastre sobre los campos.')),
                    ('hero', (
                        'Que suelten. Nosotros ya tenemos los molinos mapeados y ellos no tienen el '
                        'río.')),
                ]),
                ('time limit', [
                    ('narrator', (
                        'Última tanda de segadores en el vado. Queda un turno para que la sombra '
                        'llegue al río.')),
                    ('hero', (
                        'Todos al agua. Dejamos las lanzas si hace falta, pero no a nadie atrás.')),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'No era la guerra. Era la cuota del distrito alto, y ahora no la cobra '
                        'nadie.')),
                    ('hero', (
                        'Que la cobre quien sepa cuánta agua hay. Yo te dejo la cuenta abierta.')),
                ]),
            ],
            victory=[
                ('companion', 'Los segadores han cruzado. Nadie ha quedado bajo la sombra.'),
                ('hero', (
                    'He dibujado el giro de la nave. Tres veces al día, siempre sobre el mismo '
                    'punto.')),
                ('narrator', (
                    'En el cielo, la ciudad de Thess ya recorta su cuota en otro valle. En el suelo, '
                    'la acequia vuelve a llenarse.')),
                ('companion', 'La lanza rota aún guarda luz. Puedo oírla latir.'),
                ('hero', 'Guárdala. La primera estrella de un mapa se planta donde menos se espera.'),
            ],
            protected=None,
            resolution=(
                'Una lanza rota conservaba luz en su interior. Belis oyó un corazón al acercarla a '
                'una semilla. Iria añadió al mapa la primera línea honesta: la ruta de la sombra, '
                'con horas y con nombres. Alguien del cielo la leería algún día, y no le gustaría.'),
        ),
        dict(
            title='Los molinos sin sombra',
            goal='beacons',
            biome='plains',
            antagonist='Custodio Oth',
            opening=(
                'Tres molinos concentraban la cosecha de luz. Iria decidió desconectar sus prismas '
                'antes de atacar la estructura suspendida. Los velarios defendían cada eje como si '
                'fuera una cuna. Cada molino alimentaba una ciudad distinta, y las tres ciudades, '
                'juntas, sumaban dos millones de alas. Iria escribió en el margen los nombres de las '
                'aldeas que bebían del mismo acueducto y comprobó que ninguna figuraba en los mapas '
                'velarios.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Hay voces dentro de los cristales. Están manteniendo algo vivo.'),
                ('hero', (
                    'Desconectaremos los molinos sin romper los depósitos. Necesitamos respuestas, no '
                    'ruinas.')),
                ('narrator', (
                    'Encended los tres depósitos en orden, de sur a norte, antes de que Oth reciba '
                    'refuerzos. Cada depósito apagado es una ciudad que pierde altura.')),
                ('antagonist', (
                    'Los tres haces sostienen cuarenta mil personas. No es una amenaza: es una resta. '
                    'Si me quitáis un molino, caen catorce mil.')),
                ('hero', (
                    'Y si te dejo los tres, se mueren de sed dos valles. Enséñame el número que falta '
                    'en esa resta.')),
                ('antagonist', (
                    'El número que falta sois vosotros. Vuestra cosecha, vuestro río, vuestra agua. '
                    'Lo demás son decimales.')),
                ('companion', (
                    'Los cristales no guardan luz: guardan años. Cada uno es un verano que no volverá '
                    'a estos campos.')),
                ('narrator', (
                    'La estructura suspendida pierde un codo de altura por cada molino que deja de '
                    'girar. Oth lo repite a sus hombres como una plegaria.')),
                ('hero', (
                    'Belis, no me interesa su miedo. Me interesa su aritmética: quiero los tres '
                    'depósitos encendidos y las dos aldeas enteras.')),
                ('companion', (
                    'El del sur está minado. Si lo forzamos, el depósito revienta y con él el '
                    'canal.')),
                ('narrator', (
                    'Cuando una ciudad del cielo baja por falta de luz, sus barrios se apiñan en los '
                    'rellanos, las fuentes se racionan por horas y el acueducto que compartía con el '
                    'pueblo sirve a dos ciudades a la vez.')),
                ('hero', (
                    'Eso quiero ver escrito abajo: cuánta agua se reparte, no cuánta se roba.')),
                ('antagonist', (
                    'Escribiréis mi derrota y la llamaréis justicia. Arriba se llamará hambre, y el '
                    'hambre tiene la memoria larga.')),
                ('hero', (
                    'Entonces que la memoria sea de los dos lados. Yo firmo mis mapas; firma tú los '
                    'tuyos.')),
                ('companion', (
                    'Oth no firma nada. Los custodios no escriben: solo impiden que otros '
                    'escriban.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('narrator', (
                        'Primer depósito encendido. La estructura suspendida baja un codo y se oye '
                        'un rumor de correas tensándose.')),
                    ('antagonist', (
                        'Ese rumor son cuarenta mil personas agarrándose a una barandilla. '
                        'Contádselo a vuestro mapa.')),
                ]),
                ('beacon lit 2', [
                    ('companion', (
                        'Segundo depósito. Los barrios del cielo se mueven: los veo apiñarse en los '
                        'rellanos.')),
                    ('hero', (
                        'Dos de tres. Queda el del norte, y es el que alimenta el acueducto de las '
                        'Dos Villas.')),
                ]),
                ('village captured', [
                    ('hero', (
                        'Asegurad el pozo. Si la ciudad baja aquí, este pozo es lo primero que '
                        'habrá que compartir.')),
                ]),
                ('turn 6', [
                    ('antagonist', (
                        'He cortado el canal para que no bebáis mientras me quitáis la luz. Ahora '
                        'pagamos los dos.')),
                    ('hero', 'Abre ese canal y te prometo que tus depósitos no se rompen.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'No he defendido una fortaleza. He defendido una resta que no me dejaba '
                        'ganar.')),
                    ('hero', 'Nadie te pidió que ganaras. Te pedí que contaras bien.'),
                ]),
            ],
            victory=[
                ('companion', 'Los tres depósitos giran otra vez. El agua vuelve a las Dos Villas.'),
                ('narrator', (
                    'Desde abajo, la estructura suspendida recupera altura, pero más despacio que '
                    'antes.')),
                ('hero', (
                    'He medido la subida con la cuerda: once codos en una noche. Con esa cifra se '
                    'puede negociar.')),
                ('Esh', (
                    'Me llamo Esh. Traigo una cría que no sabe plegar las alas; no he venido a '
                    'pelear, he venido a que alguien cuente lo que acabáis de apagar.')),
                ('hero', 'Entonces siéntate donde pueda verte. Tengo preguntas y tú tienes cifras.'),
            ],
            protected=None,
            resolution=(
                'Al cesar el flujo, un velario aterrizó sin armas. Se llamaba Esh y llevaba una cría '
                'demasiado débil para plegar las alas. Iria le dio el sitio seco junto al fuego y le '
                'pidió que repitiera, despacio, cuánta luz consumía una ciudad en un año.'),
        ),
        dict(
            title='El prisionero del viento',
            goal='rescue',
            biome='ruins',
            antagonist='Jueza Veyth',
            opening=(
                'Esh fue capturado por quienes prohibían hablar con los habitantes del suelo. En su '
                'juicio no lo acusaron de traición, sino de haber revelado que las ciudades del '
                'cielo estaban muriendo. La sala del tribunal era una nave vacía con las vigas a la '
                'vista, y cada viga llevaba grabado el nombre de un barrio. Iria contó once nombres '
                'y ninguno se repetía.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Si lo liberamos, también tendremos que escuchar lo que no queremos oír.'),
                ('hero', 'Un mapa que oculta la mitad del terreno solo sirve para perderse.'),
                ('narrator', (
                    'El tribunal dicta sentencia al amanecer. Sacad a Esh de la sala y llevadlo al '
                    'portón agrietado antes del fallo.')),
                ('antagonist', (
                    'No juzgo a un traidor. Juzgo a un velario que dijo en voz alta que el cielo '
                    'pesa menos cada año.')),
                ('hero', 'Y por decirlo, ¿qué pena? ¿Que el resto se entere?'),
                ('antagonist', (
                    'Que el resto se tire por un balcón. Lo he visto pasar una vez y no pienso verlo '
                    'dos.')),
                ('companion', 'La jueza no miente. Su miedo tiene fecha y nombre.'),
                ('hero', (
                    'Entonces no discutiremos su miedo. Le enseñaremos la salida y que se atreva a '
                    'mirarla.')),
                ('antagonist', (
                    'La ciudad no baja porque no sepamos hacerlo. Baja porque nadie quiere ser el '
                    'que lo anuncie.')),
                ('hero', 'Anúncialo tú. Yo lo dibujo y tú lo anuncias. Repartimos el oficio.'),
                ('narrator', (
                    'Esh está en la celda de las vigas, con las alas plegadas. Tiene fiebre y no '
                    'podrá volar en dos días.')),
                ('protected', (
                    'Puedo andar. Solo no puedo volar. No me llevéis por el aire, que me caigo del '
                    'mapa.')),
                ('narrator', (
                    'Cuando una ciudad del cielo se asienta junto a un pueblo, sus familias se '
                    'apilan en las eras, las fuentes se cuentan por cubos y el acueducto viejo '
                    'revienta en la primera sequía.')),
                ('hero', (
                    'Por eso se mide el agua antes de bajar a nadie. Belis, cuenta los aljibes del '
                    'pueblo y guárdame el número.')),
                ('companion', 'Cuarenta y dos. Con la ciudad encima, caben veinte.'),
                ('hero', 'Ese número es mi mapa. Ahora hay que hacer que la jueza lo vea.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('half strength', [
                    ('protected', 'No puedo correr. Dejadme y llevad los planos del anclaje.'),
                    ('hero', 'Los planos se copian. Tú no. Sigue andando.'),
                ]),
                ('turn 4', [
                    ('antagonist', (
                        'He cerrado el portón agrietado. Si lo rompéis, la sala se derrumba con el '
                        'acusado dentro.')),
                    ('narrator', (
                        'La sentencia se lee en dos turnos. El portón tarda uno en abrirse con la '
                        'palanca.')),
                ]),
                ('village captured', [
                    ('hero', 'Un aljibe asegurado. Con veinte más, el pueblo aguanta la ciudad encima.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'Leed mi sentencia y llamadla miedo. Llevará vuestro nombre y será el nombre '
                        'correcto.')),
                    ('hero', (
                        'Que se lea entera. También la parte donde dice que la ciudad baja sola.')),
                ]),
                ('time limit', [
                    ('narrator', (
                        'Suena la campana de la sentencia. Queda un turno para sacar a Esh por el '
                        'portón.')),
                    ('hero', 'Todos al portón. Si no cabe, salgo yo el último y ya está.'),
                ]),
            ],
            victory=[
                ('protected', 'El portón era el único sitio bajo. Lo sabíais. Gracias.'),
                ('companion', 'La jueza no ha huido. Está mirando cómo salimos.'),
                ('hero', (
                    'Que mire. En dos días podrá volar y le contaremos lo que vimos desde el '
                    'muro.')),
                ('narrator', (
                    'Esh pronunció por primera vez una palabra del suelo: aljibe. La repitió hasta '
                    'aprendérsela.')),
                ('hero', 'Y yo aprendí la vuestra: lastre. Ninguna de las dos es bonita.'),
            ],
            protected=('Esh', 'CBM Velario Vigia'),
            resolution=(
                'Esh contó que los velarios habían gastado sus reservas durante una guerra lejana. El '
                'consejo prefería robar estaciones enteras antes que admitir que debían aterrizar. '
                'Iria anotó la fecha de la guerra en el borde del mapa: era la misma que la del '
                'primer verano sin cosecha en su pueblo.'),
        ),
        dict(
            title='La garganta de las alas',
            goal='escape',
            biome='mountain',
            antagonist='Acechante Uru',
            opening=(
                'Las patrullas aladas cerraron la garganta. Iria llevaba los planos de los anclajes '
                'solares y la promesa de Esh: si lograban llegar al observatorio, podrían bajar las '
                'ciudades lentamente. El desfiladero tenía dos salidas y Uru vigilaba una; la otra '
                'era una cornisa que solo aparecía en los mapas viejos. Iria había copiado esa '
                'cornisa de un mapa que nadie más conservaba.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Por el aire nos ven. Por el fondo del paso no podremos correr.'),
                ('hero', (
                    'No hace falta correr más que sus alas. Hace falta llegar donde sus alas no '
                    'quepan.')),
                ('narrator', (
                    'El observatorio está al otro lado de la garganta. Cruzad el desfiladero antes '
                    'de que Uru cierre los dos extremos.')),
                ('antagonist', (
                    'No persigo por gusto. Cada fugitivo que baja es una boca más que reclama agua '
                    'en los barrios altos.')),
                ('hero', (
                    'Y cada boca que baja es un par de manos para el acueducto. Tu resta tiene dos '
                    'columnas y solo miras una.')),
                ('antagonist', (
                    'Miro la que se desborda. Arriba ya hay dos familias por habitación y el pozo se '
                    'raciona desde el equinoccio.')),
                ('companion', 'Uru caza por el paso. Conoce cada repisa y cada eco.'),
                ('hero', 'Conozco cada curva del paso porque la dibujé. Ese es mi mapa y su ruina.'),
                ('narrator', (
                    'Uru vuela en círculos cerrados. Se cansa antes que un caminante, pero ve tres '
                    'veces más lejos.')),
                ('hero', (
                    'Belis, guíame por la cornisa baja. Si nos ven, que nos vean donde el aire es '
                    'estrecho.')),
                ('companion', (
                    'En el estrecho sus alas no caben. Tendrán que posarse, y en el suelo somos '
                    'más.')),
                ('narrator', (
                    'Si la ciudad que vigila Uru desciende aquí, sus tres mil vecinos vivirán '
                    'hacinados entre las rocas, beberán de un manantial racionado y el acueducto de '
                    'la garganta no dará para todos.')),
                ('hero', (
                    'Ese es el cálculo que quiero enseñarle: no cuántos bajan, sino cuánta agua hay '
                    'cuando lleguen.')),
                ('antagonist', 'El consejo ya hizo ese cálculo. Decidió que era más barato no hacerlo.'),
                ('hero', 'Entonces el consejo está mal de aritmética, y tú de jefe.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('hero', 'Una repisa asegurada. Desde aquí veo el observatorio y su puerta cerrada.'),
                ]),
                ('turn 5', [
                    ('antagonist', (
                        'He mandado tapiar el observatorio. Sus ventanas dan al paso y ahí no entra '
                        'nadie sin mi permiso.')),
                    ('hero', 'Sus ventanas dan al este. Nadie ha mirado nunca el mapa al revés.'),
                ]),
                ('turn 8', [
                    ('companion', (
                        'La niebla baja del nevero y el paso se estrecha. La cornisa se ve a ratos.')),
                    ('hero', 'A ratos me basta. Yo dibujo lo que veo y lo que recuerdo.'),
                ]),
                ('time limit', [
                    ('narrator', (
                        'Uru cierra el paso por el sur en dos turnos. La salida es la cornisa baja '
                        'del este.')),
                    ('companion', 'La marea de alas sube detrás de nosotros. Se oye el viento en las juntas.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Contaba bocas. Nunca conté manos.'),
                    ('hero', 'Pues empieza ahora. Baja y cuenta las que te van a ayudar.'),
                ]),
            ],
            victory=[
                ('companion', 'El observatorio está abierto y su telescopio apunta al suelo, no al cielo.'),
                ('hero', (
                    'Es el primer mapa honesto que veo en un año. Aquí abajo está dibujado cada pozo '
                    'de la región.')),
                ('narrator', (
                    'Iria copió los pozos, los aljibes y los canales en su cuaderno, y por primera '
                    'vez su mapa y el de los velarios coincidieron.')),
                ('hero', 'Con esto puedo bajar una ciudad sin secar un pueblo. Solo hay que elegir dónde.'),
                ('companion', 'Y ese dónde se llama ahora. Elige bien, que una ciudad no se desdice.'),
            ],
            protected=None,
            resolution=(
                'Desde el observatorio, Iria vio que una ciudad ya se inclinaba. Bajo ella estaba el '
                'pueblo donde había aprendido a escribir. Marcó la inclinación con dos trazos y '
                'calculó, por primera vez sin equivocarse, cuántos días quedaban antes de que la '
                'sombra tocara los tejados.'),
        ),
        dict(
            title='El pueblo que sostuvo el cielo',
            goal='escort',
            biome='plains',
            antagonist='Recolectora Neth',
            opening=(
                'Belis encontró un cristal capaz de estabilizar la ciudad inclinada. Un transportista '
                'lo llevaría hasta el anclaje, mientras los recolectores intentaban recuperarlo para '
                'sus propios barrios. El cristal pesaba lo que un niño y latía como un pájaro. Iria '
                'trazó el camino más corto entre la acequia y el anclaje, y en el mapa marcó con '
                'tinta roja los tres vados que lo cortaban.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Cada calle que salvemos arriba puede costarnos una cosecha abajo.'),
                ('hero', 'Hoy evitamos la caída. Mañana obligaremos a sus jefes a compartir esa cuenta.'),
                ('narrator', (
                    'Escoltad a Barun con el cristal hasta el anclaje del oeste. Si muere, la ciudad '
                    'inclinada no vuelve a enderezarse.')),
                ('antagonist', (
                    'Ese cristal es nuestro. Lo pagamos con un invierno de racionamiento; mis vecinos '
                    'se turnan el agua desde entonces.')),
                ('hero', (
                    'Y si la ciudad cae sobre el pueblo, tus vecinos tendrán menos agua todavía. '
                    'Piénsalo dos veces.')),
                ('antagonist', 'Lo he pensado doscientas. Barrio Alto lleva treinta días con un cubo por familia.'),
                ('companion', 'No es codicia lo que la mueve. Es sed.'),
                ('hero', 'Con la sed se negocia con cifras. Con la codicia no se negocia.'),
                ('protected', 'Yo llevo el cristal. Solo necesito que alguien me diga qué esquina está minada.'),
                ('hero', 'Te lo diré yo. Voy delante con la cuerda y marco cada paso con una piedra.'),
                ('narrator', (
                    'El camino cruza la acequia tres veces. Cada cruce es un sitio donde os pueden '
                    'cortar el paso.')),
                ('narrator', (
                    'Si la ciudad inclinada cae sobre el pueblo, dos mil vecinos del cielo dormirán '
                    'en las eras, el acueducto compartido perderá presión y las fuentes bajarán a un '
                    'cubo por familia.')),
                ('companion', 'La misma sed, arriba y abajo. Solo cambia quién la cuenta.'),
                ('hero', 'Entonces la contamos juntos y que salga una sola cifra.'),
                ('antagonist', (
                    'Si salvas mi barrio, retiraré a mis recolectores. Te lo prometo por el pozo de '
                    'mi madre.')),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('half strength', [
                    ('protected', 'Me han dado. Puedo seguir, pero el cristal pesa el doble.'),
                    ('hero', 'Dámelo a mí un tramo. El cristal no distingue de quién es la espalda.'),
                ]),
                ('village captured', [
                    ('hero', 'Asegurad la acequia. Si el anclaje falla, esta zanja es lo único que nos queda.'),
                ]),
                ('turn 6', [
                    ('antagonist', 'Mis recolectores han cortado el vado. Habrá que cruzar por el molino viejo.'),
                    ('narrator', 'El molino viejo aguanta un solo carro. Barun tendrá que dejar el cristal y volver por él.'),
                ]),
                ('turn 9', [
                    ('companion', 'El anclaje ya se ve. Le queda una sola luz encendida de las tres.'),
                    ('hero', 'Pues caminamos hacia esa luz y no miramos atrás.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Prometí retirarme si salvabas mi barrio. No he visto tu barrio, solo mi sed.'),
                    ('hero', 'Tu sed va a beber de este pozo mucho tiempo. Yo me encargo de que no se seque.'),
                ]),
            ],
            victory=[
                ('protected', 'El anclaje está encendido. La ciudad ya no cruje.'),
                ('companion', 'Desde arriba bajan cuerdas. Traen agua y preguntan por el nombre del portador.'),
                ('narrator', (
                    'Los velarios del Barrio Alto bajaron cuerdas con agua y alimentos. Algunos '
                    'habían visto quién los salvó, y lo dijeron en voz alta.')),
                ('hero', 'Apunta los nombres, Belis. Un mapa también sirve para saber a quién se le debe.'),
                ('hero', 'Y mañana subo a cobrar la cuenta con cifras, no con lanzas.'),
            ],
            protected=('Barun, portador del cristal', 'Peasant'),
            resolution=(
                'El anclaje resistió. Desde las plataformas bajaron cuerdas con agua y alimentos: '
                'algunos velarios habían visto quién los había salvado. Iria anotó junto al anclaje '
                'los cubos que bajaron y los que faltaban, y dejó la resta escrita donde cualquiera '
                'pudiera leerla.'),
        ),
        dict(
            title='La torre de los acreedores',
            goal='conquer',
            biome='ruins',
            antagonist='Arconte Sesher',
            opening=(
                'Sesher exigió otro invierno de oscuridad a cambio de negociar. Iria reunió a quienes '
                'habían trabajado en los anclajes para tomar su torre y abrir los registros de '
                'consumo. La torre tenía tres patios y una sola puerta, y en la puerta un escriba '
                'anotaba cada nombre que entraba. Iria se detuvo a leer la lista y reconoció tres '
                'apellidos de su propio pueblo.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Dirá que el cielo le pertenece porque sus antepasados lo levantaron.'),
                ('hero', 'Entonces leerá cuántos inviernos llevan pagándolo los nuestros.'),
                ('narrator', (
                    'Tomad la torre y abrid la cámara de registros. El libro de consumo está en la '
                    'sala alta; sin él no hay prueba.')),
                ('antagonist', (
                    'Los antepasados que levantaron esta ciudad pagaron con sus pulmones cada codo de '
                    'altura. ¿Y ahora queréis que baje porque a vosotros os da sombra?')),
                ('hero', 'Quiero que baje donde haya agua. Tu legado no riega ningún campo.'),
                ('antagonist', (
                    'El legado no se riega. Se hereda. Vosotros no heredasteis nada porque nunca '
                    'construisteis nada alto.')),
                ('companion', 'Su voz tiembla al decir alto. No es orgullo: es vértigo.'),
                ('hero', (
                    'Vértigo cuesta arriba o cuesta abajo, da igual. Los libros dirán cuál de los dos '
                    'le pagó sus torres.')),
                ('narrator', 'La guardia de Sesher defiende los tres patios. Ninguno ha visto los registros que guarda.'),
                ('hero', 'Belis, abre la puerta de la cámara y no la cierres. Quiero testigos, no secretos.'),
                ('antagonist', (
                    'Hay cuentas que sostienen una ciudad. Si las sacáis a la luz, se rompe la '
                    'confianza y con ella el techo.')),
                ('narrator', (
                    'Cuando una ciudad del cielo se asienta sin planificar, sus vecinos se apilan en '
                    'los graneros, el agua se compra por turnos y el acueducto del pueblo revienta '
                    'antes del verano.')),
                ('hero', 'Por eso quiero los registros: para saber cuánta agua cabe antes de bajar a nadie.'),
                ('companion', 'Y para saber quién bebió de la que no le tocaba.'),
                ('hero', 'Eso lo dirá el libro. Yo solo paso las páginas.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('hero', 'Un patio tomado. La cámara de registros está en el siguiente.'),
                ]),
                ('turn 5', [
                    ('antagonist', (
                        'Alto a mis hombres: nadie sube a la sala alta. Prefiero quemar el libro '
                        'antes que verlo en vuestras manos.')),
                    ('hero', 'Entonces el libro vale más de lo que dice. Subid, y subid rápido.'),
                ]),
                ('turn 8', [
                    ('narrator', (
                        'Los guardias oyen las cifras desde el patio: seis barrios gastan menos luz '
                        'que el palacio de Sesher.')),
                ]),
                ('time limit', [
                    ('narrator', (
                        'La sala alta se atranca. Queda un turno para abrir el libro antes de que lo '
                        'quemen.')),
                    ('hero', 'Que quemen las tapas. Las cifras ya las he copiado en el brazo.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'No he robado. He administrado. La ciudad vive porque alguien decide quién '
                        'sobra.')),
                    ('hero', 'Tu libro decide muy bien quién sobra. Empieza siempre por los que no firman.'),
                ]),
            ],
            victory=[
                ('companion', 'El libro está abierto en la mesa y la guardia lo está leyendo.'),
                ('narrator', (
                    'Un guardia señaló una línea con el dedo: el palacio consumía más luz que seis '
                    'barrios juntos.')),
                ('hero', 'Copiad esa página. Es el único mapa que nos faltaba: el de quién paga.'),
                ('companion', 'Los guardias han dejado las lanzas en el suelo. No han dicho nada, y eso dice mucho.'),
                ('hero', 'Dejadlas donde están. Ya no hacen falta para leer.'),
            ],
            protected=None,
            resolution=(
                'Los registros mostraron que el palacio gastaba más luz que seis barrios. La guardia '
                'de Sesher abandonó sus puestos al conocer los números. Iria copió las cuatro '
                'columnas del libro en una sola tabla y la clavó en la puerta de la torre, para que '
                'el siguiente que entrara supiera de antemano cuánto le iban a cobrar.'),
        ),
        dict(
            title='Donde termina la sombra',
            goal='beacons',
            biome='harbor',
            antagonist='Vigía de la Última Altura',
            opening=(
                'La facción que rechazaba el descenso bloqueó los tres anclajes del puerto. Iria y '
                'Belis debían sincronizarlos mientras las familias velarias esperaban sobre '
                'plataformas que crujían. Los tres anclajes eran antiguos cabrestantes de barco, y '
                'ninguno estaba calculado para el peso de una ciudad. Iria midió la sombra que '
                'proyectaban sobre el agua y supo que la ciudad bajaría justo sobre los muelles.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Cuando aterricen, habrá menos cielo y mucha más gente en nuestros caminos.'),
                ('hero', 'Habrá vecinos. Los mapas sirven para encontrarles sitio.'),
                ('narrator', (
                    'Sincronizad los tres anclajes del puerto. Los tres a la vez, o la ciudad se '
                    'parte al tocar tierra.')),
                ('antagonist', (
                    'He visto bajar una ciudad mal. Se abrió como una nuez y cuatro mil personas '
                    'cayeron con ella.')),
                ('hero', 'Y yo he visto secarse un pueblo por falta de agua. También se abre, solo que despacio.'),
                ('antagonist', 'Por eso no bajo ninguna. Prefiero que caiga sola a que la parta yo.'),
                ('companion', 'Su miedo es un mapa cerrado. No ha medido nada desde hace años.'),
                ('hero', 'Entonces le llevo mis medidas. Que compare.'),
                ('narrator', (
                    'Los anclajes del puerto están pensados para barcos, no para ciudades. Cada uno '
                    'aguanta la mitad del peso calculado.')),
                ('hero', (
                    'Belis, sincroniza el del faro y yo el del dique. El tercero lo dejamos para el '
                    'último, que es el que está minado.')),
                ('antagonist', 'El del dique lo miné yo. Si alguien lo enciende, el agua entra en los barrios bajos.'),
                ('narrator', (
                    'Cuando la ciudad aterrice, sus familias acamparán en los muelles, el pozo del '
                    'puerto se racionará y el acueducto tendrá que servir a dos ciudades de golpe.')),
                ('hero', (
                    'Dibuja eso, Belis: el acueducto soporta dos ciudades once días. Después, obra '
                    'nueva.')),
                ('companion', 'Y en esos once días, ¿quién bebe?'),
                ('hero', 'Los dos. Mitad y mitad, y quien firme el reparto lo firma en público.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('narrator', (
                        'Primer anclaje encendido. La ciudad se endereza un grado y el muelle cruje '
                        'entero.')),
                    ('antagonist', 'Un grado. Cuatro mil personas han notado ese grado.'),
                ]),
                ('beacon lit 2', [
                    ('companion', (
                        'Segundo anclaje. Las familias de las plataformas se sientan, ya no pueden '
                        'quedarse de pie.')),
                    ('hero', 'Queda el del dique. Decidme cuántos turnos aguanta el faro.'),
                ]),
                ('village captured', [
                    ('hero', 'Muelles asegurados. El agua del puerto es lo primero que vamos a compartir.'),
                ]),
                ('time limit', [
                    ('narrator', (
                        'Última marea de la noche. Si el tercer anclaje no enciende ahora, la ciudad '
                        'toca el agua.')),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', (
                        'No quería que cayeran. Quería que cayeran por su propio peso, no por mi '
                        'mano.')),
                    ('hero', 'Da igual la mano. Lo que cuenta es cuánta agua hay después.'),
                ]),
            ],
            victory=[
                ('narrator', 'Los tres anclajes ardieron juntos. La ciudad bajó despacio, como una vela que se recoge.'),
                ('companion', 'Nadie ha caído. Ni del cielo ni del muelle.'),
                ('hero', 'Once días de agua hay en el acueducto. Después habrá que cavar más pozos.'),
                ('antagonist', 'El tercer anclaje lo encendisteis mal. Se habría partido si soplara viento.'),
                ('hero', 'Tienes razón. Ven a corregir el siguiente y firmamos los dos.'),
            ],
            protected=None,
            resolution=(
                'Las ciudades tocaron tierra al atardecer. Nadie aplaudió al principio: todos estaban '
                'escuchando un silencio sin motores. Iria abrió el mapa en el suelo del muelle y '
                'señaló el primer pozo que habría que cavar, con la fecha escrita al lado y el '
                'nombre del pueblo que lo bebería.'),
        ),
    ],
)
