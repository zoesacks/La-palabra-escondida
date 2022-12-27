# La-palabra-escondida
Introducción

El trabajo consiste en hacer un juego cuyo objetivo es adivinar una palabra. No se arriesgan letras sino palabras completas. Se sabe de antemano la longitud de la palabra y el juego debe avisar cuales letras de las palabras son incorrectas (no están en la palabra), cuales son parcialmente correctas (están en la palabra pero en otra ubicación) y cuales correctas (están en la palabra exactamente en esa ubicación). Por ejemplo: La palabra oculta es "TRAPO" y el usuario escribe "CUERO" el juego debe avisar que son incorrectas las letras "C U E", es parcialmente correcta "R" y es correcta la "O". Así hasta acertar o acabar 5 intentos o haber transcurrido un tiempo predefinido.


Reglas del Juego:

Se juega de a un jugador, que cuenta con 60 segundos o 5 intentos para adivinar la palabra. 


Lo que ya está implementado:

 El juego constaba de un archivo con el programa principal, otro de configuración y uno de extras. Estos se encargan de capturar la entrada del teclado, llevar la cuenta del tiempo, así como también de dibujar en la pantalla. Se brinda como ejemplo un archivo de texto con un lemario, palabras del diccionario sin las definiciones que puede cambiar.


Lo que falta implementar:

La función nuevaPalabra(lista): Que recibe una lista de palabras y devuelve una de ellas elegida al azar

La función lectura(archivo, salida, largo): lee el archivo que ya fue abierto en principal y carga en salida solo las palabras cuya longitud es el indicado en el tercer parámetro (largo).

La función revision(palabraCorrecta, palabra, correctas, incorrectas, casi) chequéala palabra ingresada por el usuario, carga las letras en la lista que corresponda y devuelve True en caso de que la palabra sea la correcta y False en caso contrario.

No permitir que el usuario ingrese palabras de longitud diferente a la palabra que se desea adivinar.

No permitir que el usuario ingrese palabras que no estén en el lemario.

Mostrar las letras incorrectas, correctas parcialmente y correctas de diferentes colores.

Si el usuario acierta la palabra aparece una nueva. El reto es acertar muchas palabras en un lapso de tiempo.

Evita que el usuario ingrese más de una vez una palabra ya utilizada.

Que el usuario tenga opciones de niveles donde se modifique el juego, por ejemplo: el usuario indica la longitud que deben tener las palabras

