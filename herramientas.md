---
title: Herramientas
layout: page
pager: false
---

# wxMaxima

A lo largo de las prácticas será necesario realizar gráficas, resolver
límites, integrales y derivadas de manera analítica, etc.
Para ello recomendamos utilizar el sistema de álgebra computacional
[Maxima](http://maxima.sourceforge.net/), o bien una de las versiones del
mismo con interfaz gráfica: [wxMaxima](https://andrejv.github.io/wxmaxima/).
Ambos programas son
[Software Libre](https://es.wikipedia.org/wiki/Software_libre) y pueden ser
sencillamente instalados.


## Ubuntu y Debian

Para instalar wxMaxima bajo Ubuntu, Debian y distribuciones derivadas de ellas
primero actualizaremos la lista de repositorios con:

    sudo apt-get update

Y luego procedemos a instalar wxMaxima:

    sudo apt-get install wxmaxima

## ArchLinux, Manjaro o derivadas

Para instalar wxMaxima bajo Manjaro, ArchLinux u otras distribuciones derivadas de la
última primero actualizamos la lista de repositorios con:

    sudo pacman -Sy

Y luego instalamos wxMaxima (junto con `gnuplot`):

    sudo pacman -S wxmaxima gnuplot

## Windows y otras distribuciones de GNU/Linux

[Aquí](https://wxmaxima-developers.github.io/wxmaxima/download.html) encontrarán links
de descarga para la versión de Windows.

Para otras distribuciones de GNU/Linux recomendamos buscar el paquete
`wxmaxima` con su gestor de paquetes.

