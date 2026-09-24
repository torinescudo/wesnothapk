"""The world these six campaigns share: one era, one map, one cast.

Everything here is the frame the stories must not contradict. The campaigns are
six views of the same years: the fall of the sky cities, the waking of the
litario chambers, the machine that buys calm with memory, and the empire that
turns funeral debt into an army. A character who appears in two campaigns is the
same person, and a place that appears in two campaigns is the same place.

Branching is explicit (`branch` on a chapter), and shared places are explicit
(`shared` on a chapter): the same map can carry two campaigns' fights, with
different objectives and a different year on it.

SPDX-License-Identifier: GPL-2.0-or-later
"""

# The era: the years of the seven embers. The campaigns run in this order and
# overlap; Darian's crosses all of them.
ERA = 'los años de las siete brasas'

# Places two campaigns can share. A shared key names one map and one story
# place; the generator draws it once and each campaign brings its own fight.
SHARED_PLACES = {
    'valdara-harbor': 'el puerto de Valdara, sin murallas',
    'velario-city': 'la ciudad velaria a punto de descender',
    'litario-door': 'la puerta que escucha, entrada de las cámaras litarias',
    'capital-maura': 'la capital bajo la ley de los contratos funerarios',
    'reef-machine': 'el núcleo de la máquina que compra calma con memoria',
    'ember-fields': 'los campos de grano donde nació la quinta brasa',
}

# People who are the same person wherever they appear.
RECURRING = {
    'Alba': 'capitana del puerto de Valdara, guardó su oficio de faro',
    'Sira de las Siete Vetas': 'portadora litaria de siete memorias, abrió las cámaras',
    'Iria Salcedo': 'cartógrafa, dibujó caminos entre quienes solo eran sombras',
    'Maura Vey': 'archivera y reina de los contratos, la tirana de esta época',
    'Nerea Vado': 'capitana del archipiélago, apagó la máquina del olvido',
    'Darian de Linde': 'correo de las siete cartas, el que junta la alianza',
    'Sevrin': 'firmó un contrato con Maura y es la única voz que le discute',
    'Esh': 'velario que desertó y enseñó a aterrizar sin robar luz',
}

# The order of the years, so two campaigns can agree on what just happened.
TIMELINE = [
    'Maura firma el primer contrato funerario y aprende a llamar por nombre.',
    'Las ciudades velarias empiezan a robar estaciones enteras de luz.',
    'Los litarios despiertan cuando las perforadoras abren la primera grieta.',
    'La máquina del olvido compra calma en el archipiélago al precio de nombres.',
    'Valdara se hunde y su gente funda un puerto sin murallas.',
    'Las siete cartas salen de Linde y la alianza empieza a existir.',
]

# Branch points. A chapter that sets `branch` asks the player something at its
# end and follows the answer to the scenario named in this table. Every branch
# ends in the campaign's own ending, so a choice changes the path and the tone,
# never the fact that the campaign finishes.
BRANCHES = {
    'alba': {
        3: [('¿Salvar las piedras o la gente?', ['salvar-gente', 'salvar-piedras']),
            ('¿Quemar el aceite en la plaza o en el faro?', ['aceite-plaza', 'aceite-faro'])],
    },
    'sira': {
        5: [('¿Hablar con una voz o con siete?', ['una-voz', 'siete-voces'])],
    },
    'iria': {
        7: [('¿Bajar las ciudades o romper los anclajes?', ['bajar-ciudades', 'romper-anclajes'])],
    },
    'maura': {
        4: [('¿Guardar las notas del notario o quemarlas?', ['guardar-notas', 'quemar-notas'])],
        9: [('¿Abrir el archivo al pueblo o guardarlo?', ['archivo-abierto', 'archivo-guardado'])],
    },
    'nerea': {
        6: [('¿Devolver los nombres al mar o a las islas?', ['nombres-al-mar', 'nombres-a-las-islas'])],
        12: [('¿Dejar la máquina apagada o desmontarla?', ['maquina-apagada', 'maquina-desmontada'])],
    },
    'darian': {
        5: [('¿Firmar las reparaciones o solo el alto el fuego?', ['firmar-reparaciones', 'firmar-tregua'])],
        15: [('¿Juzgar a Maura o desterrarla?', ['juzgar-maura', 'desterrar-maura'])],
    },
}

# What each option really costs, said out loud once it is chosen. Keyed by
# (campaign, chapter, decision number) and then by the option itself.
CHOICE_TEXT = {
    ('alba', 3, 1): {
        'salvar-gente': 'Embarcaste a la gente y dejaste las piedras al agua. El puerto '
                        'se llenó de voces y el faro de huecos.',
        'salvar-piedras': 'Guardaste las piedras y contaste las barcas que se fueron '
                          'sin cargar. El faro aguanta; el resto, a ver.'},
    ('alba', 3, 2): {
        'aceite-plaza': 'Quemaste el aceite en la plaza y la noche se hizo de día '
                        'dentro del pueblo. A cambio, el faro quedó a ciegas.',
        'aceite-faro': 'Guardaste el aceite para el faro y la plaza se quedó oscura. '
                       'Desde el agua se vio todo lo que dejaste sin alumbrar.'},
    ('sira', 5, 1): {
        'una-voz': 'Hablaste con una voz y las otras seis te oyeron callarse. Fue la '
                   'primera vez que una memoria aceptaba quedar segunda.',
        'siete-voces': 'Hablaste con las siete a la vez y la puerta no supo a cuál '
                       'creer. Algo de ti quedó repartido en todas.'},
    ('iria', 7, 1): {
        'bajar-ciudades': 'Bajaste las ciudades enteras y el mapa quedó obsoleto en '
                          'una tarde: hay descensos que solo se dibujan una vez.',
        'romper-anclajes': 'Cortaste los anclajes y las ciudades se quedaron donde '
                           'estaban, ligeramente más libres y mucho más solas.'},
    ('maura', 4, 1): {
        'guardar-notas': 'Guardaste las notas del notario y cargaste con los nombres '
                         'que nadie viene a buscar.',
        'quemar-notas': 'Quemaste las notas y el notario se quedó sin oficio. Hay '
                        'deudas que solo existen mientras están escritas.'},
    ('maura', 9, 1): {
        'archivo-abierto': 'Abriste el archivo al pueblo y la gente aprendió a leer '
                           'lo que les había pasado.',
        'archivo-guardado': 'Cerraste el archivo con llave y firmaste tú la lista de '
                            'a quién se le permite acordarse.'},
    ('nerea', 6, 1): {
        'nombres-al-mar': 'Devolviste los nombres al mar y las islas se quedaron mudas. '
                          'El agua ahora sabe cosas que la tierra olvidó.',
        'nombres-a-las-islas': 'Repartiste los nombres por las islas y el mar se quedó '
                               'sin nadie a quien llamar.'},
    ('nerea', 12, 1): {
        'maquina-apagada': 'Dejaste la máquina apagada y la memoria de las cosas siguió '
                           'viva en las cosas mismas.',
        'maquina-desmontada': 'Desmontaste la máquina pieza a pieza y te quedaste con '
                              'un recuerdo que ya no se puede comprobar.'},
    ('darian', 5, 1): {
        'firmar-reparaciones': 'Firmaste las reparaciones y cargaste con el plazo de '
                               'todos. A cambio, el territorio empezó a arreglarse.',
        'firmar-tregua': 'Solo firmaste la tregua y las reparaciones se quedaron en '
                         'el aire. La paz llegó a medias y se nota.'},
    ('darian', 15, 1): {
        'juzgar-maura': 'Juzgaste a Maura y la memoria de las siete brasas pasó a '
                        'tener una fecha y un juez.',
        'desterrar-maura': 'Desterraste a Maura y la dejaste fuera, con lo que sabe '
                           'y sin nadie que se lo reclame.'},
}

# what that place is and what it costs to be there.
SHARED_ACCOUNTS = {
    'valdara-harbor': {
        'alba': 'El puerto de Valdara, sin murallas: las barcas de Alba están varadas '
                'y los nombres de sus vecinos siguen en los bancos.',
        'darian': 'El mismo puerto, otro año: Darian cruza el agua con la firma a medio '
                  'hacer y los velarios ya se llevan las piedras.',
    },
    'velario-city': {
        'iria': 'La ciudad velaria a punto de descender: Iria lleva el mapa que decide '
                'por dónde baja, y por dónde no.',
        'darian': 'La misma ciudad antes del descenso: Darian llega a tiempo de ver '
                  'cómo se aflojan los anclajes.',
    },
    'litario-door': {
        'sira': 'La puerta que escucha: Sira llegó con siete memorias y solo una voz, '
                'y las cámaras litarias saben la diferencia.',
        'darian': 'La misma puerta desde el otro lado: Darian trae un recado que nadie '
                  'quiere oír y un plazo que nadie cumplirá.',
    },
    'ember-fields': {
        'darian': 'Los campos de brasa, donde la tierra todavía guarda el calor de la '
                  'primera de las siete brasas.',
    },
    'capital-maura': {
        'darian': 'La capital de Maura: Darian entra con una sentencia en el bolsillo '
                  'que no se ha atrevido a leer.',
    },
    'reef-machine': {
        'nerea': 'La máquina del arrecife, apagada o no: Nerea viene a devolver los '
                 'nombres al mar y no sabe a cuál de los dos.',
    },
}

# The closing scene the campaign reaches when the player kept choosing the
# other way through. Written apart from the main ending so it can disagree
# with it: this is what a second playthrough is for.
ENDING_ALT = {
    'alba': 'El faro se quedó sin aceite y la playa sin piedras. Alba bajó la escalera '
            'contando a quién no llegó a salvar y juró que la próxima campana sonaría '
            'a tiempo, aunque fuera la última luz.',
    'sira': 'Sira habló con una sola voz y las otras seis se quedaron mudas. Las cámaras '
            'cerraron con ella dentro de una memoria: la suya, la única que ya no podía '
            'prestar.',
    'iria': 'Las ciudades bajaron enteras y los anclajes siguen tensos. Iria guardó el '
            'mapa sin dibujar el descenso: hay caminos que solo existen para quien va a '
            'dejar de usarlos.',
    'maura': 'Las notas se quemaron y el notario se quedó sin oficio. Maura firmó, por '
             'primera vez, un registro que nadie leería: el de las personas a las que '
             'llamó por nombre antes de perderlas.',
    'nerea': 'Los nombres volvieron al mar y las islas se quedaron mudas. Nerea zarpó sin '
             'el cuaderno, porque un nombre que se devuelve no se puede contar dos veces.',
    'darian': 'Darian firmó solo la tregua y las reparaciones nunca llegaron. Cruzó el '
              'territorio con la firma a medio hacer y aprendió que un correo también '
              'puede elegir qué no entrega.',
}

# SHARED_PLACES entry: one map, two campaigns, two years.
SHARED = {
    ('darian', 2): 'valdara-harbor',
    ('darian', 3): 'litario-door',
    ('darian', 4): 'velario-city',
    ('darian', 5): 'ember-fields',
    ('darian', 8): 'capital-maura',
    ('nerea', 11): 'reef-machine',
}

# Mechanics a chapter can ask for, matched to the strategic difficulty its map
# is meant to have. The generator also derives a default from the chapter index,
# so an authored value here is a deliberate choice, not the norm.
#   fog      - enemy units are hidden until seen (raises the reading load)
#   shroud   - the map starts black and is explored (raises the planning load)
#   size     - 'skirmish' | 'battle' | 'siege', and the map is drawn to match
#   turns    - the deadline, which is the pressure the objective puts on the map
MECHANICS = {
    'skirmish': dict(size='skirmish', turns=22, fog=False, shroud=False),
    'battle':   dict(size='battle', turns=32, fog=False, shroud=False),
    'siege':    dict(size='siege', turns=38, fog=True, shroud=False),
    'voyage':   dict(size='battle', turns=30, fog=True, shroud=True),
    'hunt':     dict(size='skirmish', turns=24, fog=False, shroud=True),
}
