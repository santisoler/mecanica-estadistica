# Mecánica Estadística 2019

[![Website][website-shield]][website]
[![Travis CI][travis-shield]][travis-ci]
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]


En este repositorio podrás encontrar prácticas, apuntes y materiales de la
cátedra.


## Prácticas

Aquí iremos subiendo las prácticas de la materia a medida que estén listas:

- [Práctica 1: Repaso de Termodinámica y Análisis Combinatorio][practica1]
- [Práctica 2: Colectivo Microcanónico][practica2]
- [Práctica 3: Colectivo Canónico][practica3]
- [Práctica 4: Colectivo Macrocanónico][practica4]
- [Práctica 5: Gases Cuánticos][practica5]


## Bibliografía

### Mecánica Estadística:

- J. Ortín y J. M. Sancho. **Curso de Física Estadística**.  Ed. Universidad de Barcelona.
- B. Cowan. **Topics in Statistical Mechanics**.  Imperial College Press, 2005.
- R.K. Pathria. **Statistical Mechanics**. Second edition.  Butterworth Heinemann. 1997.
- D. Landau and K. Binder.  **A Guide to Monte Carlo Simulations in Statistical Physics**.  Cambridge, 2015.
- W. Krauth. **Statistical Mechanics: Algorithms and Computations**.  Oxford University Press. 2006.
- F. Reif. **Fundamentos de Física Estadística y Térmica**. McGraw-Hill.
- G. Zgrablich. **Elementos de Mecánica Estadística**.  Ed. UAM, México. 2009.
- L. Landau y E. Lifshitz. **Física Estadística**. Reverté.
- D. McQuarrie. **Statistical Thermodynamics**. University Science Books.
- T. Hill. **An Introduction to Statistical Thermodynamics**. Dover.
- G. Wannier. **Statistical Physics**. Dover.
- K. Binder. **Monte Carlo Methods in Statistical Physics**. Springer, 1979.
- V.P. Zhdanov. **Elementary Physicochemical Processes on Solid Surface**.  Plenum Press, 1991.

### Otras áreas complementarias:

- **Termodinámica:** Zemansky y Dittman, *Heat and Thermodynamics*
- **Mecánica Cuántica:** Cohen-Tannoudji, Diu and Laloe, *Quantum Mechanics*

### Apuntes y otros materiales
- N.P. Vásquez, [**Mecánica Estadística: una introducción**][vasquez], Universidad de Los Andes, Mérida, Venezuela, 2002


## Recursos

A lo largo de las prácticas será necesario realizar gráficas, resolver
límites, integrales y derivadas de manera analítica, etc.
Para ello recomendamos utilizar el sistema de álgebra computacional
[Maxima](http://maxima.sourceforge.net/), o bien una de las versiones del
mismo con interfaz gráfica: [wxMaxima](https://andrejv.github.io/wxmaxima/).
Ambos programas son
[Software Libre](https://es.wikipedia.org/wiki/Software_libre) y pueden ser
sencillamente instalados.

### Ubuntu y Debian

Para instalar wxMaxima bajo Ubuntu, Debian y distribuciones derivadas de ellas
primero actualizaremos la lista de repositorios con:

    sudo apt-get update

Y luego procedemos a instalar wxMaxima:

    sudo apt-get install wxmaxima

### ArchLinux, Manjaro o derivadas

Para instalar wxMaxima bajo Manjaro, ArchLinux u otras distribuciones derivadas de la
última primero actualizamos la lista de repositorios con:

    sudo pacman -Sy

Y luego instalamos wxMaxima (junto con `gnuplot`):

    sudo pacman -S wxmaxima gnuplot

### Windows y otras distribuciones de GNU/Linux

[Aquí](https://andrejv.github.io/wxmaxima/download.html) encontrarán links
de descarga para la versión de Windows.

Para otras distribuciones de GNU/Linux recomendamos buscar el paquete
`wxmaxima` con su gestor de paquetes.


## Licencia
Copyright (c) 2018 Santiago R. Soler. Todos los derechos reservados.

Todo el material presente en este repositorio se encuentra disponible bajo la
licencia [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CreativeCommons][cc-by-sa-image]][cc-by-sa]

<!--Urls-->
[website]: https://santisoler.github.io/mecanica-estadistica
[website-shield]: https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=my-website
[travis-ci]: https://travis-ci.org/santisoler/mecanica-estadistica/builds
[travis-shield]: https://img.shields.io/travis/santisoler/mecanica-estadistica/master.svg
[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
[cowan-google-books]: https://books.google.com.ar/books?id=Cs42DwAAQBAJ&pg=PA1&source=gbs_toc_r&cad=4#v=onepage&q&f=false
[vasquez]: http://webdelprofesor.ula.ve/ciencias/pantoja/documents/estadistica.pdf

<!--Urls a practicas-->
[practica1]: https://github.com/santisoler/mecanica-estadistica/raw/pdf/practica1.pdf
[practica2]: https://github.com/santisoler/mecanica-estadistica/raw/pdf/practica2.pdf
[practica3]: https://github.com/santisoler/mecanica-estadistica/raw/pdf/practica3.pdf
[practica4]: https://github.com/santisoler/mecanica-estadistica/raw/pdf/practica4.pdf
[practica5]: https://github.com/santisoler/mecanica-estadistica/raw/pdf/practica5.pdf
