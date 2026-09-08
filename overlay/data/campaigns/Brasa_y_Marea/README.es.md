# Crónicas de la Brasa y la Marea

Seis campañas originales de fantasía para Wesnoth Phone, escritas en español.
El idioma no determina una ambientación española. Las seis historias transcurren
en un mundo ficticio y se pueden empezar por separado.

| Campaña | Protagonista | Escenarios | Experiencia |
| --- | --- | ---: | --- |
| La última luz de Valdara | Alba | 3 | Rescatar a una ciudad costera y evacuarla |
| Los que escuchan la piedra | Sira de las Siete Vetas | 5 | Un pueblo de piedra viva defiende su memoria |
| La deuda del cielo | Iria Salcedo | 7 | Combatir a los velarios que cosechan la luz |
| El trono de ceniza | Maura Vey | 9 | Encarnar a una villana y construir su tiranía |
| Las mareas sin nombre | Nerea Vado | 12 | Explorar un archipiélago que pierde sus recuerdos |
| El pacto de las siete brasas | Darian de Linde | 16 | Reunir una alianza contra el imperio de Maura |

## Jugar

En el inicio de Wesnoth Phone pulsa **Campañas originales** y elige una historia.
También aparecen en el selector de campañas del juego. Las partidas se guardan
con el sistema normal de Wesnoth; las unidades supervivientes se pueden
reincorporar y conservan su experiencia. Se transfiere el 40 % del oro.

Toca una unidad y un destino; después pulsa **Mover / atacar**. Usa **Más →
Objetivos** para consultar la misión y **Más → Guardar partida** para guardar.
El protagonista y su acompañante deben sobrevivir. En las escoltas y rescates
también debe sobrevivir la persona protegida. Las banderas marcan los destinos;
los braseros marcan los puntos de activación, que cuentan una sola vez.

## Las nuevas razas

**Litarios:** seres de basalto con memoria colectiva. Cuatro líneas de unidades
con una evolución cada una: guardián/bastión, resonador/voz profunda,
tejedor/restaurador y buscavetas/caminante. Resisten cortes y perforaciones;
el frío es su debilidad. La campaña de Sira recluta unidades litarias.

**Velarios:** seres alados de quitina y cuatro brazos que almacenan luz. Cuatro
líneas con una evolución cada una: lancero/arconte, cosechador/prisma,
vigía/acechante y cantor/aurora. Vuelan sobre terreno difícil, pero son vulnerables
a lanzas y fuego. Son los adversarios principales de Iria. Ambas razas pueden
incorporarse a la alianza durante la campaña de Darian.

## Recursos y mantenimiento

- 52 mapas y escenarios, con seis clases de objetivo y finales propios.
- 22 tipos de unidad: 16 de las nuevas razas y seis protagonistas.
- Retratos y sprites originales generados con la herramienta integrada de imágenes.
  Las instrucciones de generación se conservan en `ART_PROMPTS.json`.
- Doce composiciones instrumentales originales, aproximadamente dieciséis minutos,
  creadas con síntesis aditiva. `music/cbm/score.json` conserva motivos y métricas.
- Los terrenos, objetos de señalización y unidades clásicas proceden de Wesnoth
  y conservan sus licencias y créditos. No se han presentado como arte nuevo.

La fuente narrativa está en `packaging/android/campaigns/stories.py`.
`build_campaigns.py` genera el WML y los mapas deterministas. Edita las fuentes
y regenera, porque los cambios directos en los escenarios se sobrescribirán.
`compose_music.py` reproduce la banda sonora con `numpy` y `soundfile`.

`validate_campaigns.py` verifica sintaxis WML, identificadores, recursos,
transiciones y accesibilidad de los destinos. Las pruebas del emulador comprueban
las aperturas reales y añaden eventos de prueba únicamente a los archivos
extraídos del emulador para activar las condiciones de victoria. Esas pruebas
no equivalen a completar las campañas manualmente ni a medir su equilibrio.

Consulta `VALIDATION.md` en la raíz del proyecto de construcción para el resultado
de la última ejecución. Las duraciones del selector son estimaciones; dependen
del ritmo de juego, las derrotas y el uso del guardado.
