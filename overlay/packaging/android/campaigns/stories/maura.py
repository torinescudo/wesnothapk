"""El trono de ceniza — Maura Vey. Original Spanish narrative for Wesnoth Phone.

Each chapter is an authored playable episode: story prose, the dialogue the
engine plays at its start and at scripted moments, and the closing beats.
SPDX-License-Identifier: GPL-2.0-or-later
"""

CAMPAIGN = dict(
    key='maura',
    title='El trono de ceniza',
    hero='Maura Vey',
    companion='Sevrin',
    companion_type='Deathblade',
    race='human',
    recruit='Skeleton,Skeleton Archer,Dark Adept,Ghoul,Vampire Bat',
    enemy='loyalists',
    length='Larga · 9 escenarios · 5–8 horas',
    premise=(
        'Encarnas a Maura Vey, una archivera que convierte la deuda de los muertos en un ejército. '
        'Sus adversarios tienen motivos para resistirse. Sus victorias construyen una tiranía, y '
        'ninguna revelación final la convierte en una heroína incomprendida.'),
    ending=(
        'Maura ocupó el trono sin abolir un solo impuesto. Añadió uno: todo ciudadano debía legar su '
        'cuerpo al Estado. Sevrin pidió permiso para descansar. La reina guardó su petición en un '
        'archivo que nunca pensaba abrir.'),
    chapters=[
        dict(
            title='El archivo prohibido',
            goal='beacons',
            biome='ruins',
            antagonist='Magistrado Helmor',
            opening=(
                'Maura descubrió que los contratos funerarios conservaban los nombres necesarios para '
                'llamar a los muertos. El magistrado ordenó quemar el archivo. Ella decidió '
                'apropiarse de sus tres sellos antes de que llegaran los alguaciles. El archivo '
                'ocupaba tres salas húmedas bajo el tribunal y cada sello cerraba una lista: los que '
                'murieron debiendo y nunca pudieron pagar. Maura había escrito muchas de esas listas '
                'con su propia letra, y Helmor lo ignoraba. Esa ignorancia era la primera ventaja de '
                'la noche.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Soy Sevrin. Firmé por una sepultura, no por otra guerra.'),
                ('hero', 'Firmaste obediencia a quien custodiara el sello. Ahora lo custodio yo.'),
                ('narrator', 'Tres sellos, tres braseros en la sala del archivo. Encendedlos antes de que lleguen los alguaciles.'),
                ('antagonist', 'Maura Vey, dejaste el archivo con una copia y vuelves con una tropa. Eso lo llamo robo.'),
                ('hero', 'Yo lo llamo inventario. Los contratos funerarios son deuda vencida y la deuda vencida se ejecuta.'),
                ('Dolm, escribano', 'Magistrado, la sala está llena de papeles mojados. Si prendemos fuego, la ciudad pierde cien años de registros.'),
                ('antagonist', 'Que se pierdan. Prefiero una ciudad sin memoria que una ciudad sin dueño.'),
                ('hero', 'Guarda esa frase. La citaré cuando firmes tu rendición.'),
                ('companion', 'Los alguaciles vienen por el pasillo largo. Puedo cerrar la puerta, pero no los dos patios.'),
                ('hero', 'No cierres nada. Necesito que me vean trabajar.'),
                ('Dolm, escribano', 'Los nombres de los muertos no son piedras. Cada uno era alguien que pidió ser enterrado y no devuelto.'),
                ('hero', 'Lo sé. Yo redacté muchos de esos contratos y conozco la letra pequeña mejor que sus familias.'),
                ('companion', 'El precio de esta noche es que ya no podrás distinguir a un soldado de un vecino.'),
                ('hero', 'Ese precio lo pago yo, y lo pago en la columna de los gastos.'),
                ('Dolm, escribano', 'Si enciendes el tercer sello, los nombres saldrán solos. No hacen falta tambores ni plegarias.'),
                ('hero', 'Mejor. Odio el teatro.'),
                ('narrator', 'La puerta principal resiste dos turnos. Los tres braseros arden de dentro hacia fuera.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('narrator', 'Primer sello abierto. Los nombres salen en orden alfabético y se colocan solos en la fila.'),
                    ('Dolm, escribano', 'Ese de la primera fila era mi padre. Lo enterramos con su nombre y su deuda.'),
                    ('hero', 'Ahora trabaja ordenado y ya no debe nada. Anótalo en la columna de las mejoras.'),
                ]),
                ('beacon lit 2', [
                    ('antagonist', 'Estáis robando cuerpos que ya pagaron su entierro.'),
                    ('hero', 'Pagaron un entierro, no una propiedad. Lee tu propio contrato antes de discutir conmigo.'),
                ]),
                ('turn 5', [
                    ('companion', 'Han roto la puerta del patio. Los oigo contar en voz alta, como si les sobrara gente.'),
                    ('hero', 'Déjalos contar. Los números son lo único que respeto de un enemigo.'),
                ]),
                ('time limit', [
                    ('narrator', 'Los alguaciles han traído antorchas y la sala ya huele a aceite. Queda poco archivo que salvar.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Quemé lo que pude. El resto te lo dejo por escrito, para que alguien te lo reclame.'),
                    ('hero', 'Recojo la reclamación. Todo lo que se escribe vuelve a mí.'),
                ]),
            ],
            victory=[
                ('companion', 'Los tres sellos están abiertos y la sala sigue en pie. No hemos quemado nada.'),
                ('hero', 'Quemar habría sido más barato. Conservar es lo que me hace reina.'),
                ('Dolm, escribano', 'Me habéis dejado sin archivo y con trabajo. No sé si daros las gracias.'),
                ('hero', 'Fírmame un contrato nuevo y podrás decidirlo con calma.'),
                ('narrator', 'En el patio del tribunal quedaron tres alguaciles y un montón de ceniza que ya nadie necesitaba.'),
            ],
            protected=None,
            resolution=(
                'Los muertos salieron en orden alfabético. Maura anotó la primera ventaja de su '
                'ejército: nadie preguntaba por la paga. Dolm, el escribano, siguió en nómina para '
                'copiar lo que se salvó del fuego, y en la primera página nueva escribió el nombre '
                'de su padre, tachado con una raya fina. Maura no le pidió que lo borrara. Un archivo '
                'con tachones es un archivo que alguien todavía recuerda.'),
        ),
        dict(
            title='Pan para los obedientes',
            goal='conquer',
            biome='plains',
            antagonist='Capitana Arel',
            opening=(
                'Los graneros alimentaban a la ciudad que había expulsado a Maura. Tomarlos le '
                'permitiría comprar soldados vivos y condenar al hambre a quienes no aceptaran su '
                'protección. La capitana Arel los defendía con milicianos que comían de ellos. '
                'Maura calculó la ración mínima que compraría cada juramento y la anotó antes de '
                'dar la orden.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Hay familias dentro. Puedo romper las puertas sin prender los sacos.'),
                ('hero', 'Conserva el grano. Necesito que sepan exactamente quién decide cuándo comen.'),
                ('narrator', 'Cuatro graneros rodean el mercado. Tomadlos antes de que la milicia forme en la plaza.'),
                ('antagonist', 'Esos sacos son la ración de invierno de tres mil personas. No vais a tocar ni uno.'),
                ('hero', 'Voy a tocar todos. La diferencia es que después repartiré yo.'),
                ('Hanna, molinera', 'Capitana, si se llevan el grano del molino, los niños de la calle del río no comen hasta la siega.'),
                ('antagonist', 'Ya lo sé, Hanna. Por eso estoy aquí y no en el cuartel.'),
                ('hero', 'Nadie te ha pedido que te quedes. Puedes irte a casa con tus molinos y tus milicianos.'),
                ('antagonist', 'Y tú puedes irte de esta provincia. Ninguna de las dos lo va a hacer.'),
                ('companion', 'Sus hombres están flacos. Llevan semanas con media ración para dársela a los suyos.'),
                ('hero', 'Perfecto. Un hambre conocida negocia mejor que una promesa.'),
                ('Hanna, molinera', '¿Y qué pondrás en los sacos cuando los vacíes? ¿A tus muertos?'),
                ('hero', 'Pondré formularios. Cada familia que firme su lealtad recibirá su ración con nombre y apellido.'),
                ('companion', 'El precio es que este invierno nadie comerá sin firmar. Lo digo para que conste en tu libro.'),
                ('hero', 'Que conste. Un reino se administra con constancias.'),
                ('narrator', 'La milicia duerme junto a los sacos. Cada granero tomado es una columna menos en la plaza.'),
                ('antagonist', 'Si llego a saber que la archivera volvería con un ejército, habría quemado el grano en otoño.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('narrator', 'El primer granero cambia de dueño sin que se derrame un solo saco.'),
                    ('Hanna, molinera', 'Están escribiendo nuestros nombres en una lista. ¿Para qué es la lista?'),
                    ('hero', 'Para saber a quién no habrá que volver a pedirle nada.'),
                ]),
                ('turn 5', [
                    ('antagonist', 'Mis milicianos racionan lo que les queda. Si aguantáis dos días más, se rendirán solos.'),
                    ('companion', 'Está contando en voz alta la comida que le queda. Eso no lo hace un cobarde.'),
                ]),
                ('time limit', [
                    ('narrator', 'Desde el otro lado del río la ciudad ya raciona. Mañana no quedará nada que tomar.'),
                    ('hero', 'Entonces firmamos esta noche.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Hanna tiene razón. Los que se rindan comerán y los demás aprenderán lo que es un invierno sin archivo.'),
                    ('hero', 'Tu molino sigue en pie. Es más de lo que habrías dejado tú.'),
                ]),
            ],
            victory=[
                ('companion', 'Los sacos salieron contados. Hanna se quedó en la puerta del molino mirando la lista.'),
                ('hero', 'Que la lea. Quiero que memoricen la letra de quien reparte.'),
                ('Hanna, molinera', 'No has vaciado el granero. Has vaciado la palabra reparto.'),
                ('hero', 'Exactamente. A partir de ahora se llama ración, y la firmo yo.'),
                ('narrator', 'En la calle del río los niños contaron los carros que se iban, sin que nadie les explicara que aquel pan era el último que llegaba sin condiciones.'),
            ],
            protected=None,
            resolution=(
                'Maura repartió raciones junto a formularios de lealtad. Los escribas registraron '
                'cada negativa. El primer invierno sin deuda fue también el primero en que un pan '
                'tuvo nombre y apellido. Hanna guardó el formulario de su familia sin firmar, y Maura '
                'lo archivó igualmente, en la carpeta de los que aún debían una respuesta. El granero '
                'siguió en pie; lo que se cerró fue la puerta por la que antes se entraba sin '
                'preguntar.'),
        ),
        dict(
            title='El testigo incómodo',
            goal='rescue',
            biome='forest',
            antagonist='Juez Calven',
            opening=(
                'Un notario había descubierto cómo romper los sellos funerarios. Maura quería sacarlo '
                'de la custodia real y encerrarlo en un lugar donde solo ella pudiera hacer '
                'preguntas. Calven lo vigilaba en una casa de guardia, entre robles, y prefería '
                'juzgarlo antes de que hablara. El notario Kelm llevaba tres días sin dormir y una '
                'copia de su método escondida en el forro del abrigo.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Podrías dejar que publicara el método. Algunos de nosotros volveríamos a dormir.'),
                ('hero', 'Y yo perdería un ejército. No vuelvas a confundir tus deseos con mis intereses.'),
                ('narrator', 'Kelm está en la casa de guardia, junto al vado. Alcanzadlo y llevadlo a la torre del sur.'),
                ('antagonist', 'Maura Vey, el notario está detenido por el reino. Si entras en el bosque, entrarás en un juicio.'),
                ('hero', 'Traigo mi propia sentencia y doscientos testigos. Empieza cuando quieras.'),
                ('companion', 'El juez ha puesto arqueros en los robles. No dispararán a Kelm: dispararán a quien lo saque.'),
                ('hero', 'Entonces saldremos por el arroyo. La maleza tapa el agua y el agua no deja huella.'),
                ('antagonist', 'Lo que Kelm escribió libera a todos los muertos del reino. También a los tuyos.'),
                ('hero', 'Ninguno de los míos firmó para esto. Esa es la parte que no pienso discutir.'),
                ('companion', '¿Y qué harás con él cuando lo tengas? ¿Preguntarle o enterrarlo?'),
                ('hero', 'Escucharé su método y quemaré sus notas. Un testigo vivo es útil; un testigo publicado es un problema.'),
                ('protected', 'No me saques de aquí para encerrarme en otra sala. Ya conozco esa clase de libertad.'),
                ('hero', 'No te saco por ti. Te saco porque tu método todavía no tiene dueño.'),
                ('companion', 'Ha dicho la verdad delante de todos, y el precio es que la verdad se quedará sin copia.'),
                ('hero', 'La verdad sin archivo se olvida en una generación. Yo trabajo a más largo plazo.'),
                ('narrator', 'Kelm caminará mientras tenga delante una puerta. Si cae herido, la escolta tendrá que cargarlo.'),
                ('antagonist', 'Si sale del bosque, juzgaré el caso desde la tumba. No tengo prisa: tengo toda la eternidad.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('half strength', [
                    ('protected', 'No puedo seguir. Dejadme aquí y llevad la carpeta.'),
                    ('hero', 'La carpeta pesa menos que tú. Y no discuto con quien va a resolverse el método.'),
                ]),
                ('village captured', [
                    ('companion', 'La aldea del vado nos ha dejado pasar. No han cerrado ni las puertas.'),
                    ('hero', 'Anota el nombre del alcalde. Se le devolverá el favor con intereses.'),
                ]),
                ('turn 6', [
                    ('antagonist', 'Los arqueros tienen orden de disparar a las piernas. Quiero a Kelm de pie para el juicio.'),
                    ('narrator', 'El juicio se celebra mañana al mediodía, en la plaza del mercado.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Firmé tu condena hace diez años, archivera. No pienso firmar tu absolución.'),
                    ('hero', 'Nadie te la ha pedido. Con tu firma me basta.'),
                ]),
            ],
            victory=[
                ('protected', 'Puedo caminar solo. Guardad la carpeta y no me miréis como a un saco.'),
                ('companion', 'Llegó vivo. No sé si eso es una victoria tuya o una derrota mía.'),
                ('hero', 'Apúntalo en la columna de los gastos. Todo lo que hago entra en esa columna.'),
                ('protected', 'Quemarás mis notas y las recordarás de memoria. Eso también es una forma de cárcel.'),
                ('hero', 'Es exactamente una forma de cárcel. Bienvenido a mi archivo.'),
                ('narrator', 'La torre del sur tiene una ventana que no da al bosque. Kelm tardó dos días en darse cuenta.'),
            ],
            protected=('Notario Kelm', 'Peasant'),
            resolution=(
                'El notario llegó vivo a la torre. Maura quemó sus notas después de aprenderlas de '
                'memoria. La aldea del vado no volvió a cerrar sus puertas, y por eso nadie recordó '
                'preguntar qué había sido de su alcalde. Kelm pidió papel y tinta, y Maura se lo '
                'concedió sin discutir: el papel se archiva, y todo lo archivado vuelve a ella cuando '
                'lo necesita.'),
        ),
        dict(
            title='La calzada del tributo',
            goal='escort',
            biome='mountain',
            antagonist='Guardiana Derra',
            opening=(
                'Un carro transportaba las notas que el notario había escrito en la torre. Los pueblos de la calzada '
                'intentaron detenerlo antes de que Maura pudiera reclamar a sus antepasados. El carro '
                'avanzaba despacio, con las ruedas hundidas y la escolta contada. Derra había jurado '
                'a los pueblos que ningún nombre saldría de la montaña sin permiso de su familia.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Nos arrojan piedras con los nombres de los que llevamos encadenados.'),
                ('hero', 'Recógelas. Facilitarán el próximo inventario.'),
                ('narrator', 'El carro debe cruzar el paso antes del anochecer. Si el conductor cae, la carga se queda en la calzada.'),
                ('antagonist', 'Ese carro lleva a mis abuelos. Ningún sello sale de esta montaña sin mi permiso.'),
                ('hero', 'Puedes acompañarlo hasta el paso. Te dejaré ver la carga entera y contar los nombres.'),
                ('antagonist', 'Y después los devolverás a sus tumbas.'),
                ('hero', 'Después seguirán trabajando. La diferencia es que tú lo habrás visto con tus ojos.'),
                ('protected', 'Guardiana, yo solo llevo las riendas. Me pagaron por el viaje, no por la guerra.'),
                ('hero', 'Cobra el doble y no hables. Eso es todo lo que te pido.'),
                ('companion', 'La calzada está cortada en dos curvas. Los pueblos han levantado muros de piedra seca.'),
                ('hero', 'Los muros son para el carro, no para mí. Subiremos por la ladera y el carro irá por el centro.'),
                ('antagonist', 'Mi gente entierra a sus muertos con nombre desde antes de que existiera tu tribunal.'),
                ('hero', 'Lo sé. Yo redacté los contratos que se lo permitían y ahora los estoy ejecutando.'),
                ('companion', 'El precio de esta carga es que aquí nadie volverá a enterrar a los suyos por su nombre.'),
                ('hero', 'Escribe esa frase en el informe. Quiero leerla otra vez cuando la calzada sea mía.'),
                ('narrator', 'Cada piedra del camino lleva un nombre grabado. Recogerlas es la lista de la próxima leva.'),
                ('antagonist', 'Si el carro cruza el paso, esta calzada dejará de ser un camino y será una frontera.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('narrator', 'El pueblo de la curva baja ha cerrado sus puertas y ha sacado a los niños al monte.'),
                    ('companion', 'Han escondido a los suyos. Eso lo hace quien espera volver.'),
                ]),
                ('turn 4', [
                    ('antagonist', 'He mandado soltar el alud sobre la calzada. El carro pasará, pero nadie podrá volver por donde vino.'),
                    ('protected', 'Las ruedas se hundirán en la grava. Si queréis que llegue, tendréis que despejar el paso con las manos.'),
                ]),
                ('half strength', [
                    ('protected', 'Me han dado en el hombro. Puedo seguir, pero llevaré las riendas con una mano.'),
                    ('hero', 'Una mano basta. La otra guárdala para cobrar.'),
                ]),
                ('time limit', [
                    ('narrator', 'La luz se va del paso y los muros se cierran al fondo. Mañana la calzada estará cortada.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Habéis derribado un muro de piedra seca. Se tarda una estación en levantarlo y una tarde en olvidar por qué estaba.'),
                    ('hero', 'Lo reconstruiré más alto y con tu nombre en la primera hilada.'),
                ]),
            ],
            victory=[
                ('protected', 'El carro cruzó el paso sin perder un saco. He cobrado el doble, como acordamos.'),
                ('companion', 'Mira la calzada. Ya nadie pone nombre a las piedras.'),
                ('hero', 'Pondrán nombres a las piedras nuevas. Es lo que hace la gente cuando no le queda otra cosa.'),
                ('companion', '¿Y tú qué harás cuando no te quede otra cosa?'),
                ('hero', 'Seguir contando. Es el único oficio que no se me ha dado mal.'),
                ('narrator', 'En el pueblo de la curva baja, la primera piedra nueva llevaba el nombre de la guardiana, y nadie la retiró.'),
            ],
            protected=('Udren, conductor del carro', 'Peasant'),
            resolution=(
                'El carro cruzó el paso. Detrás quedó una calzada donde ya nadie enterraba a sus '
                'muertos con nombre. Derra quedó bajo su propio muro de piedra seca, con la lista de '
                'sus abuelos en el bolsillo, y Maura ordenó copiarla antes de que la lluvia borrara '
                'la tinta. Udren cobró el doble y no volvió a conducir para nadie más. La montaña '
                'siguió siendo un paso, pero las familias de la ladera aprendieron a bautizar a sus '
                'muertos en voz baja.'),
        ),
        dict(
            title='La noche de los juramentos',
            goal='survive',
            biome='ruins',
            antagonist='General Vaust',
            opening=(
                'El general atacó mientras Maura vinculaba a su sello central los contratos robados. '
                'Romper el círculo antes del amanecer devolvería la libertad a miles de muertos. El '
                'campamento se levantaba sobre un cementerio antiguo y los veteranos de Vaust yacían '
                'a dos pasos del círculo. Maura tenía hasta la primera luz: después, la ciudad entera '
                'sabría que el sello funcionaba.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Aún puedes detener el ritual. Nadie te obligó a llegar hasta aquí.'),
                ('hero', 'Lo sé. Por eso esta corona será mía.'),
                ('narrator', 'Resistid hasta el amanecer. El círculo se cierra al salir el sol y nadie debe tocarlo antes.'),
                ('antagonist', 'Archivera, tus muertos son deuda. Los míos son soldados. Hay una diferencia y voy a enseñártela.'),
                ('hero', 'Ninguna diferencia sobrevive a la contabilidad. Lo comprobarás en la primera fila.'),
                ('companion', 'El general ha traído a sus veteranos. Son viejos, pero conocen el cementerio mejor que nosotros.'),
                ('hero', 'Entonces no pisemos las tumbas. Vaust no atacará donde están enterrados los suyos.'),
                ('antagonist', 'Cobarde no: previsor. Sé exactamente lo que cuesta levantar a un hombre.'),
                ('hero', 'Yo también. Cuesta un contrato, un sello y la paciencia de su familia.'),
                ('companion', 'Los nombres del círculo están saliendo en desorden. Alguno grita.'),
                ('hero', 'Que grite. Los que gritan se cuentan como presentes.'),
                ('antagonist', 'Si rompo el círculo antes del amanecer, devuelvo la libertad a miles. Es lo único que me queda.'),
                ('hero', 'Inténtalo. Te estaré esperando en el centro y no me moveré de ahí.'),
                ('companion', 'El precio es que miles de hombres que pidieron una tumba van a pasar la noche de pie.'),
                ('hero', 'Y la pasarán trabajando. Es más de lo que les habría dado su rey.'),
                ('narrator', 'Vaust ataca desde tres lados. El círculo resiste solo hasta que alguien lo interrumpa.'),
                ('antagonist', 'Cuando esto acabe, quiero que alguien escriba que lo intenté.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('narrator', 'El suelo del cementerio se ha movido dos palmos y el círculo sigue abierto.'),
                    ('companion', 'Los muertos del general están saliendo por su cuenta. No los llama nadie.'),
                ]),
                ('turn 8', [
                    ('antagonist', 'Mis veteranos caen y vuelven a levantarse enfrente. Sois un ejército que no necesita carga.'),
                    ('hero', 'Lo llamo logística.'),
                ]),
                ('time limit', [
                    ('narrator', 'Falta una hora para el amanecer. El círculo se cierra con la primera luz.'),
                    ('hero', 'Que nadie se acerque. Ni tú, Sevrin.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Escribe que lo intenté. Es lo único que te pido y ni eso me vas a conceder.'),
                    ('hero', 'Lo escribiré en la columna de los nombres útiles.'),
                ]),
            ],
            victory=[
                ('companion', 'No pude quedarme quieto. Me llamó y me moví.'),
                ('hero', 'Todos se movieron. Es lo que firmamos.'),
                ('companion', 'Yo firmé por una sepultura.'),
                ('hero', 'Y tienes una. Con lápida, con nombre y con turno de guardia.'),
                ('companion', 'Eso no es una sepultura. Es un puesto de trabajo.'),
                ('narrator', 'Al amanecer, los veteranos de Vaust formaron detrás de los muertos de Maura sin que nadie les diera la orden.'),
            ],
            protected=None,
            resolution=(
                'Al amanecer, el ejército entero giró hacia Maura al mismo tiempo. Sevrin intentó '
                'quedarse quieto y no pudo. Vaust fue enterrado con sus veteranos en la misma fosa '
                'que había defendido toda la noche, y Maura copió la lápida para archivarla como '
                'prueba de propiedad. El círculo no volvió a abrirse hasta que la ciudad entera '
                'estuvo en silencio, y para entonces ya nadie recordaba quién había pedido descansar.'),
        ),
        dict(
            title='Las tres campanas',
            goal='beacons',
            biome='harbor',
            antagonist='Abadesa Ysol',
            opening=(
                'Las campanas del santuario liberaban a los muertos que oían su repique. Maura ordenó '
                'silenciarlas antes de entrar en la capital. Los defensores dejaron abiertas las '
                'puertas para quienes huyeran de ella. El santuario daba pan y sal a quien lo pidiera '
                'y por eso era el único edificio del puerto con la puerta abierta de noche.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Incluso ahora nos ofrecen refugio.'),
                ('hero', 'Ofrecen deserción. Desmonta las campanas y funde sus badajos.'),
                ('narrator', 'Tres campanas repican en el santuario. Silenciadlas todas antes de que amanezca.'),
                ('antagonist', 'Esta puerta está abierta para quien huya de ti. No la cierro ni aunque me lo pidas con un ejército.'),
                ('hero', 'No te la voy a cerrar. Voy a quitar el badajo para que nadie la oiga desde el agua.'),
                ('Ondra, sacristana', 'Abadesa, si callamos las campanas, los muertos del puerto se quedarán sin su hora.'),
                ('hero', 'Tendrán la mía. Todo trabajo tiene horario.'),
                ('antagonist', 'Las campanas no llaman a los muertos. Avisan a los vivos de que alguien ha muerto y hay que ir a su casa.'),
                ('hero', 'Pues entraré yo primero y con la puerta abierta, para que se ahorren el duelo.'),
                ('companion', 'Hay refugiados en el claustro. Familias que llegaron huyendo de nosotras.'),
                ('hero', 'Que no se toquen. Necesito testigos, no bajas.'),
                ('Ondra, sacristana', 'El bronce de la campana grande tiene doscientos años y el nombre de su fundidor grabado.'),
                ('hero', 'Fundidor y fecha. Todo lo que tiene nombre se puede inventariar.'),
                ('companion', 'El precio es que una ciudad entera perderá la hora exacta en que muere su gente.'),
                ('hero', 'Yo misma redactaré el horario nuevo y lo pegaré en la puerta.'),
                ('antagonist', 'Cuando entres en la capital no te abrirán las puertas: te las dejarán abiertas para que salgas.'),
                ('narrator', 'El santuario tiene tres torres. Cada campana silenciada deja una parte del puerto a oscuras.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('beacon lit 1', [
                    ('narrator', 'La campana del alba cae muda. Media bahía deja de oír el repique.'),
                ]),
                ('beacon lit 2', [
                    ('Ondra, sacristana', 'La segunda era la de los entierros. Yo la tocaba desde los once años.'),
                    ('hero', 'Aprenderás a tocar el cambio de turno. Se paga mejor y no despierta a nadie.'),
                ]),
                ('beacon lit 3', [
                    ('antagonist', 'Has apagado la voz del santuario. Ahora tendrás que oír los nombres uno por uno.'),
                    ('hero', 'Los oigo desde el archivo. Es mi trabajo.'),
                ]),
                ('turn 6', [
                    ('companion', 'Los refugiados del claustro han salido a la playa. Uno lleva la campana pequeña a cuestas.'),
                    ('hero', 'Dejadlo llegar al agua. La marea se encargará del sonido.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'No has silenciado una campana. Has silenciado la costumbre de enterrar con nombre.'),
                    ('hero', 'La costumbre la escribo de nuevo. Con sello y con fecha.'),
                ]),
            ],
            victory=[
                ('companion', 'Las tres torres están mudas. Los barcos navegan a ciegas.'),
                ('Ondra, sacristana', 'La campana de los entierros se ha convertido en clavos. Lo he visto con mis ojos.'),
                ('hero', 'Clavos para la puerta nueva. Así todos los que pasen sabrán lo que hizo la vieja.'),
                ('companion', 'Nadie oye los clavos, Maura.'),
                ('hero', 'Los oiré yo cada mañana, cuando abra esa puerta.'),
                ('narrator', 'A la mañana siguiente el puerto amaneció sin repique y la panadería del muelle fue la primera en echar el cerrojo.'),
            ],
            protected=None,
            resolution=(
                'El bronce del santuario se convirtió en clavos para la puerta del palacio. Ysol se '
                'quedó en el claustro, con las manos vacías de badajos y la puerta abierta a quien '
                'llamara. Nadie llamó: el puerto había aprendido a no hacer ruido. Ondra siguió '
                'tocando una campana de madera, tan pequeña que solo la oían los que ya estaban '
                'dentro, y anotó en un cuaderno la hora de cada entierro que nadie pudo anunciar.'),
        ),
        dict(
            title='El precio de una tregua',
            goal='conquer',
            biome='forest',
            antagonist='Embajadora Nalis',
            opening=(
                'Una liga de villas ofreció reconocer a Maura si liberaba a sus caídos. Ella acudió a '
                'la negociación con el ejército desplegado: aceptaría el reconocimiento, pero no '
                'devolvería nada. Nalis hablaba en nombre de catorce villas y traía dos escribas, un '
                'mapa y ninguna escolta digna de ese nombre. Maura aceptó la reunión en el claro, con '
                'la infantería visible entre los árboles.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Podrías ganar una paz duradera con una sola firma.'),
                ('hero', 'Una paz que dependa de mi generosidad termina cuando deje de ser generosa.'),
                ('narrator', 'La liga acampa en el claro. Rodead la reunión y tomad el terreno antes de que firmen nada.'),
                ('antagonist', 'Traigo catorce firmas y una condición: devuelve a nuestros caídos y te reconoceremos.'),
                ('hero', 'Acepto el reconocimiento. La devolución no está en el orden del día.'),
                ('Tera, delegada', '¿Vamos a negociar con la infantería en el bosque? Esto no es una reunión, es una rendición con sillas.'),
                ('hero', 'Es una reunión con garantías. Las garantías son mías porque las pago yo.'),
                ('antagonist', 'Nuestros muertos defienden tus filas. Firman tus formularios, cavan tus zanjas y no pueden negarse.'),
                ('hero', 'Exacto. Y por eso valen más que una promesa tuya.'),
                ('companion', 'Los delegados han traído a sus hijos y los han puesto delante, en la primera fila.'),
                ('hero', 'Entonces no disparéis primero. Quiero que la liga recuerde quién empezó.'),
                ('antagonist', 'Si te reconocen, será con las manos de sus muertos sobre la mesa.'),
                ('hero', 'Me parece bien. Pondré una mesa más grande.'),
                ('Tera, delegada', 'Nos han contado lo del molino y lo de las campanas. Nadie firmará sin garantías por escrito.'),
                ('hero', 'Aquí tienes el borrador. Solo hay una página y la letra pequeña la he escrito yo.'),
                ('companion', 'Una página. En una página cabe la tregua, pero no cabe la libertad.'),
                ('hero', 'Cabe la palabra que necesito esta noche. Las demás las añadiré yo después.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('village captured', [
                    ('narrator', 'La primera villa de la liga ha izado tu estandarte sin resistencia.'),
                    ('Tera, delegada', 'Han izado tu bandera porque tienen miedo, no porque te reconozcan.'),
                ]),
                ('turn 5', [
                    ('antagonist', 'He mandado a los escribas quemar las copias. Si firmamos, firmamos con una sola página y sin archivo.'),
                    ('hero', 'Ya la tengo memorizada. Puedes quemar lo que quieras.'),
                ]),
                ('turn 9', [
                    ('companion', 'Los delegados discuten entre ellos. Dos quieren firmar y tres quieren luchar.'),
                    ('hero', 'Deja que discutan. El ruido cansa más que el hierro.'),
                ]),
                ('time limit', [
                    ('narrator', 'La luz se va y los delegados no se han movido. Mañana la liga se reunirá en otra provincia.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Firmé el reconocimiento de una reina que ya había decidido no devolver nada. Que conste en el acta.'),
                    ('hero', 'Constará, y con tu letra. Prefiero las pruebas que se firman solas.'),
                ]),
            ],
            victory=[
                ('companion', 'Firmaron todos. Ninguno te miró a los ojos.'),
                ('hero', 'No hace falta que me miren. Hace falta que cumplan.'),
                ('Tera, delegada', 'Nos dejas la tregua y te quedas con los muertos. ¿Sabes cómo llamamos a eso en mi aldea?'),
                ('hero', 'Lo llamáis de muchas maneras. Yo lo llamo capítulo primero.'),
                ('Tera, delegada', 'Lo llamamos deuda. Y nosotros también sabemos llevarla en libros.'),
                ('narrator', 'La liga firmó bajo vigilancia y en el claro quedaron las sillas vacías de los delegados que no volvieron aquella noche a sus aldeas.'),
            ],
            protected=None,
            resolution=(
                'Las villas firmaron bajo vigilancia. Maura conservó el documento como prueba de su '
                'legitimidad. La página única se archivó junto a los contratos funerarios, y en la '
                'carpeta de la liga anotó a mano el nombre de cada delegado que había perdido la voz '
                'al firmar. Tera no volvió a su aldea; su hija sí, años después, a buscar el archivo '
                'y a preguntar por qué su madre no estaba en la lista de los muertos.'),
        ),
        dict(
            title='La puerta sin retorno',
            goal='escape',
            biome='cave',
            antagonist='Paladín Eron',
            opening=(
                'La última defensa de la capital derrumbó el túnel que Maura utilizaba para '
                'infiltrarse. La reina aspirante debía alcanzar la cisterna interior antes de que sus '
                'perseguidores sellaran la salida. Eron mandaba a los últimos defensores y conocía el '
                'túnel mejor que sus propios pasillos. El agua de la cisterna era la única salida que '
                'no estaba vigilada, y también la que alimentaba a media ciudad.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Arriba luchan por sus hijos. Aquí abajo, ¿por quién luchamos nosotros?'),
                ('hero', (
                    'Tú luchas porque te lo ordeno. Yo, porque todavía hay alguien capaz de decirme '
                    'que no.')),
                ('narrator', 'La salida está sellada por el derrumbe. Alcanzad la cisterna interior antes de que Eron cierre también esa puerta.'),
                ('antagonist', 'Maura Vey, has entrado por donde entierro a mis muertos. Aquí no hay trono, solo agua.'),
                ('hero', 'El agua es una puerta como cualquier otra. Solo hay que saber a qué hora abrirla.'),
                ('companion', 'Las galerías bajas están inundadas hasta la rodilla y arriba se oye el pico de los zapadores.'),
                ('hero', 'Nos quedan dos túneles. Uno lleva a la cisterna y el otro a la sala de guardia.'),
                ('antagonist', 'Conozco cada piedra de esta cueva. Los zapadores derribarán el segundo túnel cuando os vean entrar.'),
                ('hero', 'Entonces iremos despacio. El que corre elige por mí.'),
                ('companion', 'Los defensores han dejado antorchas encendidas en las hornacinas. No son trampas: son señales para los suyos.'),
                ('hero', 'Apágalas al pasar. Que el que venga detrás no sepa cuánto hemos avanzado.'),
                ('antagonist', 'La cisterna alimenta a media ciudad. Si abres la compuerta, las fuentes se secarán en verano.'),
                ('hero', 'Lo sé. Por eso la abriré ahora y no en verano.'),
                ('companion', 'El precio lo pagarán las cocinas, los lavaderos y los enfermos que no pueden bajar al río.'),
                ('hero', 'Anota sus nombres. Cuando sea reina les pondré una fuente en la plaza.'),
                ('narrator', 'La compuerta tiene una sola palanca y dos guardianes. La palanca pesa más que una persona.'),
                ('antagonist', 'Cuando salgas de aquí te estaré esperando con lo que me quede. Que sea poco, será mío.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 4', [
                    ('narrator', 'Los zapadores han derribado el túnel del medio. Solo queda la galería del agua.'),
                    ('companion', 'La galería es estrecha. Si nos atacan aquí no cabe ni la orden de retirada.'),
                ]),
                ('turn 8', [
                    ('antagonist', 'He mandado encender las bombas. Si no llegas a la cisterna, te ahogarás con tus propios soldados.'),
                    ('hero', 'Anota: bombas encendidas antes de mi llegada. Eso lo pagará la ciudad.'),
                ]),
                ('time limit', [
                    ('narrator', 'El agua sube un palmo por turno. La cisterna queda al fondo, detrás de la compuerta.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Mis hijos beben de esa agua. Lo sabías cuando has entrado.'),
                    ('hero', 'Lo sabía. Y he entrado igual, que es la única respuesta que tengo.'),
                ]),
            ],
            victory=[
                ('companion', 'Salimos. El agua entra por el túnel como una columna más.'),
                ('hero', 'Cuenta los soldados que salen y compáralos con los que entraron. Esa es la factura.'),
                ('companion', 'No has contado la de la ciudad.'),
                ('hero', 'La contaré cuando pidan cuentas. Traerán un papel y yo tendré otro mejor.'),
                ('narrator', 'Aquella noche, en el barrio alto, alguien abrió el grifo de la fuente pública y no salió nada.'),
            ],
            protected=None,
            resolution=(
                'Maura emergió en la cisterna y abrió las compuertas para su ejército. El agua de la '
                'ciudad dejó de correr. Eron murió defendiendo la palanca, con el nombre de sus hijos '
                'grabado en el escudo, y los zapadores se rindieron sin que nadie se lo pidiera. Maura '
                'anotó las fuentes que se secarían en verano y las incluyó en el presupuesto del año '
                'siguiente, con una partida para pozos nuevos que nunca llegó a ejecutarse.'),
        ),
        dict(
            title='Una corona sin herederos',
            goal='conquer',
            biome='ruins',
            antagonist='Regente Alther',
            opening=(
                'Alther ofreció abdicar si Maura garantizaba la libertad de los muertos. Ella rechazó '
                'el trato ante ambos ejércitos. Quería una victoria que nadie pudiera confundir con '
                'un acuerdo. Alther había gobernado la ciudad durante treinta años y todavía le '
                'quedaban soldados leales y una guardia de palacio que no cobraba desde el invierno.'),
            # Beats played when the chapter opens: (speaker, line).
            intro=[
                ('companion', 'Cuando ya no quede nadie por conquistar, ¿nos dejarás descansar?'),
                ('hero', 'Un reino siempre necesita guardianes.'),
                ('narrator', 'La guardia de palacio defiende la sala del trono. Tomadla y acabad con la regencia.'),
                ('antagonist', 'Abdico hoy mismo si garantizas la libertad de los muertos. Firmo donde quieras.'),
                ('hero', 'Rechazo el trato delante de los dos ejércitos. Quiero una victoria que nadie confunda con un acuerdo.'),
                ('companion', 'Los soldados de palacio llevan sin cobrar desde el invierno y siguen en la puerta.'),
                ('hero', 'Pues entremos por la puerta. Quien no cobra y se queda merece ver quién lo sustituye.'),
                ('antagonist', 'Treinta años he firmado treguas con gente peor que tú. Ninguna me ha durado una estación.'),
                ('hero', 'Las treguas duran lo que dura la firma. Yo no vengo a firmar.'),
                ('companion', 'En el patio golpean la puerta de clavos. Es todo lo que queda de la campana de los entierros.'),
                ('hero', 'Que siga sonando. Necesito que la ciudad entera oiga lo que pasa hoy.'),
                ('antagonist', 'La guardia del trono no es un ejército. Son los hijos de esta ciudad con las ropas del padre.'),
                ('hero', 'Entonces que salgan los padres. Con los hijos no negocio.'),
                ('companion', 'El precio de esta tarde es que esa puerta sonará por gente que aún está viva.'),
                ('hero', 'Sonará por todos. Es lo más justo que va a pasar hoy en esta ciudad.'),
                ('narrator', 'La sala del trono tiene una sola entrada y veinte escalones. Cada escalón cuesta una vida.'),
                ('antagonist', 'Cuando termine esto, pide que te llamen lo que quieras. Yo pienso llamarte como te llamaba tu padre.'),
            ],
            # Scripted beats: (trigger, [(speaker, line), ...]).
            events=[
                ('turn 5', [
                    ('narrator', 'Los defensores han cerrado la puerta del ala oeste. La sala del trono queda al fondo.'),
                    ('companion', 'Están cantando dentro. No sé qué himno es, pero no es de victoria.'),
                ]),
                ('turn 9', [
                    ('antagonist', 'He mandado fundir la corona vieja. Si ganas, te sentarás con una corona nueva y sin historia.'),
                    ('hero', 'Perfecto. La historia la escribo yo y no necesito heredarla.'),
                ]),
                ('time limit', [
                    ('narrator', 'La ciudad ha empezado a apagar las luces de las ventanas. La sala del trono queda sola.'),
                ]),
                ('enemy leader defeated', [
                    ('antagonist', 'Muero sin haber firmado tu legitimidad. Es lo único que he ganado esta tarde.'),
                    ('hero', 'Levantadlo y ponedlo en la primera fila. Irá a la guardia del trono, como todos.'),
                ]),
            ],
            victory=[
                ('companion', 'Ganamos. La ciudad no ha ardido y nadie ha saqueado las casas.'),
                ('hero', 'Nadie saquea lo que va a administrar.'),
                ('antagonist', 'Me has puesto en tu guardia. Ni el consuelo de caer entero me has dejado.'),
                ('hero', 'Un regente que conoce cada pasillo vale más que uno que muere limpio.'),
                ('companion', 'Cumplí el contrato. Ahora quiero pedirte una cosa como firmante, no como soldado.'),
                ('hero', 'Pide lo que quieras por escrito. Hoy no es día de cambios en el organigrama.'),
                ('narrator', 'La puerta de clavos sonó toda la noche en el patio, sin que nadie la tocara: se movía con el aire que entraba por la puerta rota.'),
            ],
            protected=None,
            resolution=(
                'El regente cayó. Maura ordenó que lo incorporaran a la guardia del trono antes de '
                'limpiar la sala. Mandó fundir los badajos que quedaban, abrió un registro nuevo para '
                'los que llegaran vivos y en la primera página escribió su nombre. Debajo, con letra '
                'más pequeña, quedó el primer puesto vacante del reino: el de quien había pedido '
                'permiso para descansar y aún esperaba respuesta.'),
        ),
    ],
)
