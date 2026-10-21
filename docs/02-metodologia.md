# Metodología de análisis

[Volver al índice](../README.md)

El análisis empieza en IDA y continúa con los registros y la memoria del depurador. Después se contrastan los patrones y los bytes con mona. Los archivos de cada prueba se guardan con su sesión.

## Flujo de trabajo

```mermaid
flowchart TD
    A[Definir objetivo y entorno autorizado] --> B[Registrar muestra, hash y versiones]
    B --> C[Localizar cadenas y referencias en IDA]
    C --> D[Anotar la ruta de código que se va a estudiar]
    D --> E[Revisar la captura o sesión disponible]
    E --> F{El contexto está completo}
    F -->|Sí| G[Examinar excepción, registros y memoria]
    F -->|No| H[Anotar los datos que faltan]
    G --> I[Contrastar patrones y referencias con mona]
    I --> J[Comprobar representaciones y archivos con Python]
    J --> K[Redactar resultados y limitaciones]
    H --> K
    K --> L[Revisar el material antes de compartirlo]
```

## Preparación

Registra la muestra, su origen, hash y arquitectura. Añade las versiones del sistema y las herramientas, el snapshot y el objetivo de la sesión. Si se trabaja solo con capturas, deja constancia de esa condición: una imagen permite revisar un resultado, pero no recuperar todo el estado del proceso.

La [ficha de sesión](../plantillas/sesion.md) recoge los archivos y el entorno. Si falta algún dato, se deja indicado.

## Revisión estática

En IDA se parte de las cadenas y sus referencias para localizar el código relevante. A partir de ahí se sigue la procedencia de los datos, las condiciones de cada rama y las operaciones de copia.

El pseudocódigo facilita la lectura, aunque los tipos y nombres pueden ser inferidos. Cuando una conclusión depende de la capacidad de un destino o de un cálculo de punteros, hay que comprobarla también en ensamblador y en los llamadores.

En el caso de FreeFloat, la rama de `USER` aporta una pista sobre una copia. La ruta asociada a `NOOP` necesita su propio seguimiento. La relación entre ambas debe apoyarse en el flujo real del programa.

## Revisión dinámica

El depurador permite observar una detención concreta. Primero se identifica la causa y después se examinan registros, pila y memoria. Un valor reconocible en EIP puede ser compatible con una entrada controlada, pero la relación necesita conservarse con la prueba y sus archivos.

La información mínima incluye proceso, hilo, excepción, registros, instrucción y acción previa. Si se analiza una dirección, también interesan el módulo, su base y los permisos de la página.

## Contraste con mona y Python

mona ayuda a localizar una secuencia en un patrón y a comparar bytes con una referencia. Antes de interpretar el resultado, comprueba el archivo de referencia, la longitud y la dirección del primer byte. ESP puede apuntar al interior del dato.

Con Python se comprueba el orden de bytes, se comparan archivos y se calculan sus hashes. Antes hay que confirmar que los archivos corresponden a la misma prueba.

## Relación entre estático y dinámico

```mermaid
sequenceDiagram
    participant A as Analista
    participant I as IDA
    participant D as Depurador
    participant M as mona
    participant R as Registro de sesión
    A->>I: Seguir una cadena hasta su código
    I-->>A: Ramas y operaciones relevantes
    A->>R: Guardar la ruta y los datos por comprobar
    A->>D: Revisar una detención identificada
    D-->>A: Excepción, registros y memoria
    A->>M: Comparar una referencia desde su inicio
    M-->>A: Coincidencias y diferencias
    A->>R: Relacionar resultados y explicar sus límites
```

## Alcance de las conclusiones

Los resultados se interpretan según lo que se haya podido comprobar:

1. El servicio deja de responder. Todavía hay que separar un problema de red, una pausa y una excepción.
2. El depurador registra una detención. Ya existe un estado que estudiar, aunque su causa puede necesitar más contexto.
3. Aparece un valor compatible con la entrada. La sesión y los archivos permiten comprobar esa relación.
4. Un patrón sitúa el dato en una posición concreta. El offset queda referido al inicio de ese patrón y a esa prueba.
5. Se observa una redirección o una interrupción esperada. La estabilidad entre sesiones y las mitigaciones requieren comprobaciones adicionales.

En el informe se indica qué se ha comprobado. Las capturas del laboratorio y los ejemplos locales se registran por separado.

## Cierre

El informe reúne cada observación con su archivo, la interpretación y los datos que falten. Para facilitar otra revisión, cambia una variable cada vez, conserva la referencia original y registra cualquier cambio de configuración. El [caso práctico](03-caso-practico.md) aplica este método a las capturas de FreeFloat.
