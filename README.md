# webService_ferramas
Pagina e-comerce de ferreteria "Ferremas"

PASO 2 (Construcción e integración):
"FERREMAS" ya dispone de un sitio web básico para ventas, que ha sido desarrollado en JAVA
con una arquitectura de capas. Este sitio es intuitivo, simple y visualmente atractivo, diseñado
para facilitar la experiencia de compra del cliente. En la página principal se destacan los
productos en promoción y los lanzamientos recientes, mientras que el resto de los productos
están organizados en categorías específicas de ferretería y construcción, tales como:
Herramientas:
Herramientas Manuales
● Martillos
● Destornilladores
● Llaves

Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 1- 2023 4

● Herramientas Eléctricas
● Taladros
● Sierras
● Lijadoras
● Materiales de Construcción
Materiales Básicos
● Cemento
● Arena
● Ladrillos
● Acabados
● Pinturas
● Barnices
● Cerámicos
Equipos de Seguridad
● Casos
● Guantes
● Lentes de Seguridad
● Accesorios Varios
Tornillos y Anclajes
Fijaciones y Adhesivos
Equipos de Medición
Con la base ya desarrollada y aprobada por FERREMAS, se desea construir una
API/Webservice que permita consultar información detallada de los productos, incluyendo
precios, modelos, marcas, códigos y stock. El objetivo de esta API/Webservice es, primero, que
las distintas sucursales de "FERREMAS" puedan hacer pedidos y mantener un inventario
apropiado para sus ventas locales (consumo API/Webservice de forma interna); y segundo, que
otras tiendas puedan consultar precios y detalles desde sus propias aplicaciones conectándose
a la API/Webservice (consumo API/Webservice de forma externa vía Internet).
Además, se añadirá una sección de contacto en el sitio web para que los clientes puedan
comunicarse con un vendedor en caso de tener consultas específicas. Por ejemplo, la estructura
de datos de la API podría ser:
{
"Código del producto": "FER-12345",
"Marca": "Bosch",
"Código": "BOS-67890",
"Nombre": "Taladro Percutor Bosch",
"Precio": [
{
"Fecha": "2023-05-10T03:00:00.000Z",

Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 1- 2023 5

"Valor": 89090.99
}
]
}
Para la API/Webservice se debe considerar las pruebas y documentación base para que los
desarrolladores internos y externos, puedan realizar las implementaciones y posterior consumo
de las mismas. Puede utilizar la herramienta Postman para ambas actividades.
Para las compras realizadas con tarjetas de débito y/o crédito en el sitio web, se utilizará el
sistema de pagos "WEBPAY", que permite a los clientes pagar de manera segura y práctica. La
integración de este sistema se puede realizar mediante la API proporcionada por "WEBPAY" o
utilizando su WebService, disponible en su sitio oficial de desarrolladores.
Finalmente, los administradores de "FERREMAS" han identificado una oportunidad de negocio
con el aumento de pedidos desde el extranjero. Para expandirse a mercados internacionales y
gestionar envíos al exterior, será necesario implementar una funcionalidad de conversión de
divisas en tiempo real. La conversión automática de la moneda extranjera a la moneda nacional
se realizará a través de la integración con la API del Banco Central de Chile, cuyas instrucciones
e integración están disponibles en su sitio web oficial.
PASO 3 (Pruebas, validación y documentación):
Tras concluir la construcción y la mejora del sitio de "FERREMAS" mediante el desarrollo de
WebService, se inicia la etapa de pruebas para verificar la funcionalidad del sistema y la correcta
integración de sistemas a través de las API/Webservices implementadas.
La primera tarea consiste en elaborar un diseño de casos de prueba para cada componente de
la aplicación y los elementos de integración. Esto significa preparar al menos un caso de prueba
por cada funcionalidad desarrollada, además de las pruebas de integración pertinentes.
La plantilla para los casos de prueba estará disponible en la sección ANEXOS del documento
de especificaciones.
Una vez diseñados los casos de prueba, se procede a su ejecución. Esta ejecución puede ser
manual inicialmente y luego se puede auxiliar con herramientas como Testlink, una herramienta
gratuita que facilita la creación, gestión y registro de resultados de los casos de pruebas en
planes de prueba estructurados.
Para finalizar la etapa de pruebas, se elaborará un documento de Plan de pruebas que
evidenciará todo el proceso. Este plan incluirá:
Propósito
● Explicación del propósito del documento del Plan de pruebas.
Alcance
● Especificación de los requisitos de software y módulos a probar.

Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 1- 2023 6

Descripción:
● Descripción general del sistema y sus características clave.
Resumen de las pruebas
● Identificación de los módulos a probar.
● Objetivos específicos de las pruebas.
● Tipos de pruebas a realizar.
● Técnicas de pruebas aplicadas.
● Definición de roles y responsabilidades en el proceso de pruebas.
Entorno y configuración de las pruebas
● Detalles de los requisitos de software y hardware necesarios para ejecutar las pruebas.
Calendarización de las pruebas
● Cronograma de actividades, tareas, duración, fechas y responsables.
Resumen de riesgos
● Listado y análisis de riesgos identificados, utilizando una matriz de riesgos.
Condiciones para el cierre del proyecto
● Criterios de aceptación para finalizar las pruebas y márgenes de tolerancia para
defectos.
Glosario:
● Definiciones de términos técnicos utilizados en el documento.
Es importante destacar que el sistema debe ser sometido a, como mínimo, a dos tipos de
pruebas automatizadas con herramientas como Selenium, JMeter, Postman, entre otras para
asegurar los atributos de calidad e integraciones del sitio que será entregado en producción.
