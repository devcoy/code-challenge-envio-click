# Envío Click code challenge

## Support

Jorge Cervantes <jcdev1825@gmail.com>

## Prerequisites

1. Python installed

### Assumptions

1. No se debe hacer uso de funciones nativas del lenguaje como por ejemplo:

- contains
- in
- find
- substr
- index
- sort
- etc

## Exercise 01

### Description

Escribe un script que haga lo siguiente: dado un texto, deberá decir las veces que
ese texto aparece en un párrafo cualquiera.

### Expect
Párrafo de ejemplo:

*La logística Digital es un concepto que surge de la integración entre la logística tradicional
y la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando
productos físicos, podríamos estar hablando de un golpe devastador para la industria de
la logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha
introducido las innovaciones digitales.*

texto a buscar: `logística`

> El resultado de salida debería ser: 4 ocurrencias encontradas.

### How to execute

1. Within `input_01.txt` file you should add the paragraph (text) that will use to search the word.

2. Execute the `script_01.py` Python file.

## Exercise 02

### Description

Dado el arreglo de entrada, ordenar por prioridad (priority) únicamente los
elementos que cumplan los criterios establecidos por las siguientes variables:

- width
- height
- length
- weight

El ordenamiento debe ser mediante los criterios indicados y la propiedad priority en modo
descendente. Colocar en la parte inicial del arreglo los elementos que cumplan las
condiciones y agregar los elementos restantes sin alterarlos.

### Expect

Ejemplo:

Tu algoritmo recibe el input entry.

`entry = [
{"id": 12340, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":125, "priority": 2},
{"id": 12341, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":127, "priority": 4},
{"id": 12342, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":129, "priority": 6},
{"id": 12343, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":131, "priority": 0},
{"id": 12344, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":133, "priority": 0},
{"id": 12345, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":135, "priority": 0},
{"id": 12346, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":137, "priority": -1},
{"id": 12347, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":139, "priority": 0},
{"id": 12348, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":141, "priority": 2},
{"id": 12349, "weight": 1, "width": 1, "height": 1, "length": 1, "cost":143, "priority": 0},
{"id": 12350, "weight": 2, "width": 1, "height": 1, "length": 1, "cost":145, "priority": 0},
{"id": 12351, "weight": 2, "width": 1, "height": 1, "length": 1, "cost":147, "priority": 10},
{"id": 12352, "weight": 2, "width": 1, "height": 1, "length": 1, "cost":149, "priority": 0},
{"id": 12353, "weight": 2, "width": 1, "height": 1, "length": 1, "cost":151, "priority": 0},
{"id": 12354, "weight": 2, "width": 1, "height": 1, "length": 1, "cost":153, "priority": 0},
{"id": 12355, "weight": 2, "width": 1, "height": 1, "length": 10, "cost":155, "priority": 0},
{"id": 12356, "weight": 2, "width": 1, "height": 1, "length": 10, "cost":157, "priority": 0},
{"id": 12357, "weight": 2, "width": 1, "height": 1, "length": 10, "cost":159, "priority": 0},
{"id": 12358, "weight": 2, "width": 1, "height": 1, "length": 10, "cost":161, "priority": 0},
{"id": 12359, "weight": 2, "width": 1, "height": 1, "length": 10, "cost":135, "priority": 0},
{"id": 12360, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":137, "priority": 0},
{"id": 12361, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":139, "priority": 0},
{"id": 12362, "weight": 3, "width": 3, "height": 1, "length": 10, "cost":141, "priority": -2},
{"id": 12363, "weight": 3, "width": 3, "height": 1, "length": 10, "cost":153, "priority": -2},
{"id": 12364, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":145, "priority": -6},
{"id": 12366, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":147, "priority": 0},
{"id": 12367, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":149, "priority": 0},
{"id": 12365, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":151, "priority": 2},
{"id": 12368, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":181, "priority": 2},
{"id": 12369, "weight": 3, "width": 1, "height": 1, "length": 10, "cost":183, "priority": 0}
]`

*El criterio de ordenamiento ordenamiento que recibe tu algoritmo es el siguiente:*

`criteria1 = [
('weight', '=', 3)
]`

> Tras ejecutar el ordenamiento con el criterio indicado, el array original debe quedar ordenado de la siguiente manera.

`output = [
{'id': 12368, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
181, 'priority': 2},
{'id': 12365, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
151, 'priority': 2},
{'id': 12360, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
137, 'priority': 0},
{'id': 12361, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
139, 'priority': 0},
{'id': 12366, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
147, 'priority': 0},
{'id': 12367, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
149, 'priority': 0},
{'id': 12369, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
183, 'priority': 0},
{'id': 12363, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
153, 'priority': -2},
{'id': 12362, 'weight': 3, 'width': 3, 'height': 1, 'length': 10, 'cost':
141, 'priority': -2},
{'id': 12364, 'weight': 3, 'width': 1, 'height': 1, 'length': 10, 'cost':
145, 'priority': -6},
{'id': 12340, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
125, 'priority': 2},
{'id': 12341, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
127, 'priority': 4},
{'id': 12342, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
129, 'priority': 6}, {'id': 12343, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
131, 'priority': 0},
{'id': 12344, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
133, 'priority': 0},
{'id': 12345, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
135, 'priority': 0},
{'id': 12346, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
137, 'priority': -1},
{'id': 12347, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
139, 'priority': 0},
{'id': 12348, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
141, 'priority': 2},
{'id': 12349, 'weight': 1, 'width': 1, 'height': 1, 'length': 1, 'cost':
143, 'priority': 0},
{'id': 12350, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
145, 'priority': 0},
{'id': 12351, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
147, 'priority': 10},
{'id': 12352, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
149, 'priority': 0},
{'id': 12353, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
151, 'priority': 0},
{'id': 12354, 'weight': 2, 'width': 1, 'height': 1, 'length': 1, 'cost':
153, 'priority': 0},
{'id': 12355, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
155, 'priority': 0},
{'id': 12356, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
157, 'priority': 0},
{'id': 12357, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
159, 'priority': 0},
{'id': 12358, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
161, 'priority': 0},
{'id': 12359, 'weight': 2, 'width': 1, 'height': 1, 'length': 10, 'cost':
135, 'priority': 0},
]`

### How to execute

1. Within `input_02.json` file you should add the data (tejsonxt) that will use to parse.

2. Within `script_02.py` (line 92) file you shoud define your criteria.

3. Execute the `script_02.py` Python file.
