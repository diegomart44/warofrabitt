# warofrabitt

Documentación e Instrucciones para "Batalla de Conejos"
Índice
Introducción
Requisitos del Sistema
Instalación
Cómo Jugar
Estructura del Código
Explicación del Código
Mejoras Futuras
Créditos
1. Introducción
"Batalla de Conejos" es un juego sencillo de disparos por turnos donde dos jugadores controlan conejos y lanzan zanahorias para intentar reducir la vida del oponente a cero. El objetivo del juego es derrotar al otro conejo antes de que te derroten a ti.

2. Requisitos del Sistema
Python 3.x
Pygame 2.x
3. Instalación
Instala Python 3.x: Si no tienes Python instalado, puedes descargarlo desde python.org.

Instala Pygame: Abre una terminal o símbolo del sistema y ejecuta:

sh
Copiar código
pip install pygame
Descarga el código fuente: Guarda el archivo del juego (batalla_conejos.py) en una carpeta de tu elección.

Obtén las imágenes: Asegúrate de tener las imágenes background.jpg, rabbit.png, y carrot.png en la misma carpeta que el archivo del juego.

4. Cómo Jugar
Inicia el Juego: Ejecuta el script batalla_conejos.py:

sh
Copiar código
python batalla_conejos.py
Pantalla de Inicio: Presiona cualquier tecla para comenzar el juego.

Turnos: El juego es por turnos. Cada jugador controla un conejo y puede disparar una zanahoria en su turno.

Disparar:

Haz clic en el conejo durante tu turno para comenzar a apuntar.
Arrastra el ratón para ajustar el ángulo y la potencia del disparo.
Suelta el botón del ratón para disparar la zanahoria.
Vida de los Conejos: Cada conejo comienza con 3 vidas. Los impactos de las zanahorias reducen la vida del conejo impactado. El juego termina cuando la vida de un conejo llega a cero.
