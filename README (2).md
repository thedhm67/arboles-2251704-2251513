# Árboles de Huffman

## Introducción

Los Árboles de Huffman son una estructura usada para la **compresión de datos sin pérdida**, creada por David A. Huffman en 1952. Su objetivo es reducir el tamaño de la información asignando códigos más cortos a los datos más frecuentes.

---

## ¿Qué es el algoritmo de Huffman?

Es un método que asigna códigos binarios según la frecuencia de los símbolos:

* Símbolos frecuentes → códigos más cortos
* Símbolos menos frecuentes → códigos más largos

Esto se logra mediante un **árbol binario óptimo**.

---

## ¿Qué es el Árbol de Huffman?

Es un árbol binario donde:

* Las hojas representan los símbolos
* Cada símbolo tiene una frecuencia
* El recorrido desde la raíz hasta una hoja define su código binario

---

## Construcción básica

1. Se colocan los símbolos con sus frecuencias.
2. Se toman los dos de menor frecuencia.
3. Se combinan en un nuevo nodo.
4. Se repite hasta formar el árbol completo.

---

## Características

* Es un árbol binario
* No genera ambigüedad en los códigos
* Es óptimo para compresión sin pérdida

---

## Aplicaciones

* Compresión de archivos (ZIP)
* Transmisión de datos
* Codificación de información

---

## Conclusión

Los Árboles de Huffman permiten representar datos de forma más eficiente, reduciendo el espacio necesario sin perder información.
