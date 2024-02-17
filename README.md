# hackudc-ci

## Introduccion

Este repositorio trata de la creación de un CI y de un ecosistema para Codee para la optimización de códico para los desarrolladoras y mejoras en su código.

## Problema

1. Ausencia de pipeline de CI
2. Falta de información para usuario

## Solucion

* Creación de pipeline de CI con Buildbot.
* Información y métricas del código al desarrollador.

## Problemas de implementacion

* Problemas con implementación con repositorios eexternos.
* Escasez de tiempo para la implementación de representación de la información para el usuario final.

## Instalación automatizada:

1. Clonamos el repositorio y accedemos al directorio raíz:

```bash
git clone https://github.com/APardoO/hackudc-ci.git
cd hackudc-ci
```

2. Asignamos los permisos necesarios para las herramientas automatizadas:

```bash
chmod +x scripts/*.sh buildbot-ci/script.sh
```

3. Lanzamos el entorno ejecutando el siguiente script:

```bash
./scripts/buildbot_script.sh
```
> En teoria esto deberia provocar una cascada de llamadas a los scripts en scripts/ y en proc-json/
> Para comprobar el entorno virtualizado, desde el navegador, se puede acceder clicando en el **[enlace](http://localhost:8010)**.
> El entorno virtualizado con Docker no ha sido posible llevarlo a cabo.

## Instalación manual:

### Setup de repositorios externos

#### Codee 
	Extraer Codee en el directorio base del repositorio

#### Libreria de c/c++ para analizar
	Como ejemplo tenemos mbedtls. hacemos un git clone

### Lanzamiento de Codee
	Codee se ejecuta con scripts/codee-launch.sh

### Procesado de json
	proc-json/order.py se encarga de ordenar los errores segun su orden de gravedad

### Autofix de codigo
	proc-json/autofix.py se encarga de ejecutar los comandos dados por codee

## Eliminación del entorno virtualizado (automatizado):

* Para detener la ejecución del entorno virtualizado, ejecuta el siguiente comando:
```bash
./scripts/buildbot_script.sh -d
```