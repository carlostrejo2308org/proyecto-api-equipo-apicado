# Proyecto Final APICADO
## Rodriguez Juan | Ferrer Francisco | Guerrero Cristian | Moncada Uriel
___
# Objetivo
Aplicar los conocimientos adquiridos en el curso realizando este proyecto en el cúal una característica primordial de este es el consumo de alguna API de nuestra preferencia.
___
# ¿Qué hace?
Diferentes péticiones utilizando uno de los métodos de pitición más famosos y probablemente más utilizado, el método
GET.

Hace las peticiones a una API de base de datos nombrada RAWG la cuál se especializa en video juegos.

Y el json que resulte de las peticiones a dicha API se almacenan en una base de datos NoSQL, en este caso MongoDB.
___
# Conceptos/Tecnologías:
## JSON
JSON (acrónimo de JavaScript Object Notation, 'notación de objeto de JavaScript') es un formato de texto sencillo para el intercambio de datos.

## Pruebas unitarias
Las pruebas unitarias consisten en aislar una parte del código y comprobar que funciona a la perfección. Son pequeños tests que validan el comportamiento de un objeto y la lógica. El unit testing suele realizarse durante la fase de desarrollo de aplicaciones de software o móviles.

## Integracion
Las pruebas de integración dentro del software testing chequean la integración o interfaces entre componentes, interacciones con diferentes partes del sistema, como un sistema operativo, sistema de archivos y hardware o interfaces entre sistemas. Las pruebas de integración son un aspecto clave del software testing.

Es esencial que un probador de software tenga una buena comprensión de los enfoques de prueba de integración, para lograr altos estándares de calidad y buenos resultados. 

## MongoDB
MongoDB es un programa de gestión de base de datos NoSQL de código abierto. NoSQL se utiliza como alternativa a las bases de datos relacionales tradicionales. Las bases de datos NoSQL son bastante útiles para trabajar con grandes conjuntos de datos distribuidos. MongoDB es una herramienta que puede administrar información orientada a documentos, almacenar o recuperar información.

MongoDB admite varias formas de datos; en lugar de utilizar tablas y filas como en las bases de datos relacionales, la arquitectura de MongoDB se compone de colecciones y documentos.

## API
API es el acrónimo de Interfaz de programación de aplicaciones, que es un intermediario de software que permite que dos aplicaciones se comuniquen entre sí. Cada vez que usa una aplicación como Facebook, envía un mensaje instantáneo o consulta el clima en su teléfono, está usando una API.
___
# Testeando appDB
Esto se logro con el objeto tipo app y tambien para verificar atributos del objeto.

Para este testeo se utilizo la metodología llamada Test-Driven Development (TDD), es decir, 
primero se hicieron las pruebas y después el código dentro de [appDB.py](appDB.py).

Claro con algunos test como de coleccion de insertar y eliminar
con pruebas de entrada de datos y testeos varios.
Pruebas unitarias para cada funcion.
test_setCollection, test_eliminar, test_Insertar entre otras.
Tambien con algunas consultas.

# Integración : Testeando la api 
Ya que este modulo ([api.py](api.py)) dentro de la mayoría de sus funciones manda a llamar a algunas funciones del módulo [appDB.py](appDB.py), decidimos utilizar la métodología Bottom-Up, en la cual primero se deben de testear los modulos que no tienen dependencia/mandan a llamar a otros, así que primero testeamos appDB.py, como se menciono en
la parte anterior a esta, una vez con eso se procede a testear api.py .

Para verificaciones de los atributos del objeto se utilizaron verificaciones de codigo status.

Para las funciones dentro de api.py que mandan a llamar a las de appDB.py, primero se testeo
con parametros incorrectos para que regresaran la salida esperada en caso de que ocurriera.
Una vez con los parametros correctos se procedio a leer los archivos .json dentro de [ConsultaJson](/ConsultaJson/) los cuales son creados mediante la interacción de las funciones de ambos modulos, después teniendo el contenido de esos archivos, ahora se leen los archivos previamente creados por nosotros mismos en donde guardamos la información directamente.

Posteriormente se compara el contenido de ambos archivos y se comprueba que sean el mismo.

Finalizado esto nos damos cuenta que la integración entre ambos modulos es correcta, tal como se tenia pensado[.](https://www.youtube.com/watch?v=2th30Z3lXF4)


Video en donde se muestra la ejecución de api.py : [https://www.youtube.com/watch?v=-ADDd6DszI4](https://www.youtube.com/watch?v=-ADDd6DszI4)