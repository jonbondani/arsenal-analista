# Guía de operación

[Volver al índice](../README.md)

## Preparar el análisis

Antes de abrir las herramientas, conviene fijar el objetivo de la sesión. En este caso se trata de relacionar una entrada con el estado del proceso y comprobar hasta dónde permiten llegar las evidencias disponibles.

Si trabajas sobre las capturas incluidas, puedes seguir toda la revisión sin ejecutar el servicio. Para una sesión dinámica hace falta un entorno autorizado, una VM desechable y un snapshot al que volver. La red debe estar aislada, por ejemplo mediante una red interna o host-only, sin exponer el servidor a Internet. La configuración real de la red debe quedar anotada junto al resto del entorno.

## Organizar los archivos

La [ficha de sesión](../plantillas/sesion.md) ayuda a reunir los datos básicos: fecha, objetivo, muestra, hash, arquitectura, herramientas y snapshot. Es más sencillo completar esta información al empezar que reconstruirla después a partir de varias capturas.

En el laboratorio original se describe FreeFloat FTP Server 1.0 en Windows 11 sobre VirtualBox. La guía cita IDA Free 9.4 para Windows x64 y la metodología identifica el ejecutable como PE 80386. Faltan el hash de esa muestra, la build de Windows y las versiones completas de Immunity y mona. Son datos necesarios para repetir el análisis con precisión.

El sistema operativo y el proceso no tienen por qué compartir arquitectura. Windows x64 puede ejecutar una aplicación x86. En las capturas se trabaja con EIP y ESP, así que la interpretación de esos registros corresponde a un proceso de 32 bits.

También hay que separar el Python utilizado para los scripts externos del intérprete que carga el plugin dentro del depurador. Actualizar uno no garantiza la compatibilidad del otro.

## Repartir el trabajo entre herramientas

**IDA Free** sirve para localizar cadenas, seguir referencias y estudiar los bloques que procesan una entrada. La salida útil es una ruta de código con sus ubicaciones y una explicación de lo que se espera comprobar en ejecución.

**Immunity Debugger** muestra los registros, la pila y la memoria del proceso detenido. Para conservar ese resultado hacen falta el contexto de la sesión, el hilo y la causa de la detención.

**mona** automatiza la consulta de patrones y la comparación de memoria. Sus resultados dependen de que la referencia, la longitud y la dirección inicial sean las correctas.

**Python** facilita comprobaciones pequeñas, como convertir un entero a bytes, encontrar una diferencia o calcular el hash de un archivo. Es útil para evitar errores de transcripción y mantener identificadas las evidencias.

## Revisar el estado del proceso

Un timeout de red es un síntoma. El depurador permite comprobar si el proceso está pausado, si se ha producido una excepción o si el servicio sigue activo. Conviene guardar el contexto antes de continuar, porque al reanudar la ejecución puede perderse el estado que se estaba examinando.

Al documentar una detención, conserva el proceso, el hilo, el tipo de excepción, los registros relevantes y la instrucción señalada. Si se compara memoria, añade la dirección inicial y la longitud de la referencia.

## Mantener separadas las sesiones

Un cambio de binario, prefijo, comando FTP, sistema o snapshot puede cambiar el resultado. Abre una sesión nueva o deja el cambio claramente registrado. Un offset o una dirección de otra ejecución pueden orientar la revisión, pero necesitan comprobarse de nuevo.

Al cruzar ubicaciones de IDA con el depurador, distingue la dirección virtual, la base del módulo y el RVA. El offset de archivo es otra medida y no se puede intercambiar directamente con ellas.

## Guardar las evidencias

Conserva las capturas originales y sus hashes. Si una copia pública necesita ocultar información, guarda el original aparte y registra la edición realizada. Mantén visibles los datos necesarios para entender la prueba.

Cada captura debe acompañarse de una explicación breve: operación realizada, resultado visible y alcance. En una comparación de memoria interesa saber qué referencia se utilizó y qué bytes se excluyeron. En un registro con un marcador interesa poder relacionarlo con la entrada de esa misma sesión.

## Cerrar el trabajo

El [informe](../plantillas/informe.md) recoge los resultados y las limitaciones. Las comprobaciones que falten deben describirse con suficiente detalle para poder retomarlas. Por ejemplo, para estudiar la estabilidad de una dirección hay que registrar módulo, base y RVA en sesiones independientes y comparar los resultados tras reiniciar.

La sesión queda bien documentada cuando otra persona puede seguir las evidencias, entender la conclusión y localizar la información que falta. El [checklist](08-checklist.md) permite revisar esos puntos antes de compartir el material.
