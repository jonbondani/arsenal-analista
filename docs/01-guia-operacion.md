# Guía de operación

[Volver al índice](../README.md)

## Preparar el entorno

Para seguir las capturas no hace falta ejecutar FreeFloat. Si se va a trabajar con el servidor, se necesita un laboratorio autorizado, una VM aislada y un snapshot al que volver. Comprueba la configuración de red y evita que el servicio quede accesible desde Internet.

En el laboratorio original se utiliza Windows 11 sobre VirtualBox. La documentación cita IDA Free 9.4 para Windows x64 y carga el ejecutable como PE 80386. Las capturas muestran EIP y ESP, correspondientes al proceso x86.

La arquitectura de Windows no determina la del programa. Un sistema x64 puede ejecutar un proceso de 32 bits. El depurador y la lectura de registros deben corresponder al proceso analizado.

También hay dos entornos Python distintos: el de los scripts externos y el que carga mona dentro del depurador. Sus versiones y dependencias se anotan por separado.

## Identificar los archivos

Guarda el origen y el SHA-256 del ejecutable, la build del sistema, el snapshot y las versiones de las herramientas. En la [ficha de sesión](../plantillas/sesion.md) hay campos para estos datos.

El nombre `FTPServer.exe` y la versión comercial no bastan para identificar una copia concreta. Para repetir el laboratorio original faltan, entre otros datos, el hash de esa muestra y las versiones completas de Immunity y mona.

Separa los archivos de cada sesión: entrada utilizada, patrón, tabla de referencia, capturas y resultados. Si cambia el binario, el comando, el prefijo o la configuración, registra el cambio antes de continuar.

## Empezar en IDA

Localiza las cadenas del protocolo y abre sus referencias. Sigue la función que las utiliza y revisa las condiciones que llevan a cada operación de copia.

Anota funciones, direcciones, origen de los datos y destino. Si el pseudocódigo sugiere un tipo o tamaño que afecta a la explicación, compruébalo en ensamblador y en los llamadores.

En el caso de FreeFloat se observa una copia en la rama de `USER`. Para relacionarla con una prueba de `NOOP` hay que seguir esa otra ruta. El [caso práctico](03-caso-practico.md) explica la diferencia.

## Continuar en el depurador

Identifica proceso, hilo y causa de la detención. Guarda los registros y la memoria antes de reanudar, porque el estado puede cambiar al continuar.

Un timeout no basta para confirmar un crash. El proceso puede estar pausado, el servicio puede haberse detenido o puede haber un problema de red. Revisa el contexto del depurador para distinguirlo.

Si EIP contiene un marcador, relaciónalo con la entrada de esa sesión. Para una comparación de memoria, localiza el primer byte de la referencia y registra la dirección y la longitud. ESP puede apuntar dentro de la secuencia.

## Pasar ubicaciones entre herramientas

IDA y el depurador pueden mostrar bases distintas. Guarda el módulo, su base y el RVA de la ubicación que se está siguiendo. El RVA es la posición respecto a la base del módulo; no es lo mismo que un offset dentro del archivo.

Al cambiar de sesión, comprueba de nuevo las direcciones. Una dirección válida en una ejecución puede variar por la carga de módulos, la versión o las mitigaciones.

## Guardar los resultados

Cada captura debe quedar relacionada con la acción anterior y con los archivos utilizados. En una comparación interesa conservar el hash de la referencia, sus exclusiones, la dirección inicial y la salida de mona.

Mantén los originales. Si hay que ocultar información en una copia, guarda la versión sin editar aparte y anota el cambio.

Al cerrar, recoge los resultados en el [informe](../plantillas/informe.md) y señala las comprobaciones que falten. Por ejemplo, estudiar la estabilidad de una dirección requiere comparar módulo, base y RVA en sesiones independientes, también después de reiniciar.
