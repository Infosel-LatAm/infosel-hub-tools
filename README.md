# infosel-hub-tools
Tools, scripts and other source code useful to run Hub on specific situations.


##  open_infosel_hub.py
Este script abre el browser chrome, se conecta a https://hub.infosel.com y hace login con un usuario y password especificado

Esta solución se provee como una facilidad a nuestros clientes pero se basa en herramientas de terceras partes sobre las cuales no tenemos control ni soporte. Infosel no asume responsabilidad alguna con respecto a su funcionamiento.

### Pre-requisitos
El siguiente software debe estar instalado en la máquina donde se va a correr el script

* python3
* chrome
* [driver de selenium apropiado para la version de chrome instalada](https://chromedriver.chromium.org/downloads) este driver debe estar en el mismo directorio que el script.
* open_infosel_hub.py (el script en este directorio)
* Debe modificar el script para que contenga el usuario y password que utiliza normalmente para ingresar a hub.
* Instalar las dependencias para el script.
.* una opcion simple es es ejecutar el comando `pip install selenium`
.* la opcion estandar es ejecutar el comando `pip install -r requirements.txt` utilizando el `requirements.txt` que se encuentra aquí 

## Operación
1. Ejecute el script desde una ventana de terminal.
2. El script abre chrome, que contendrá una leyenda indicando que esta siendo controlado por la herramienta de pruebas selenium
3. DONE! chrome queda abierto en infosel hub.

Este script puede ser ejecutado de manera automática de acuerdo a las necesidades del sistema operativo o a través de otros comandos.

## Related articles
Esta solución se basa en un conjunto de herramientas muy comun para testing, los siguientes articulos presentan soluciones muy similares:

[browserstack](https://www.browserstack.com/guide/login-automation-using-selenium-webdriver)

[linuxhint](https://linuxhint.com/logging_into_websites_python/)

[blog post by Dennis Niggl](https://pub.towardsai.net/automate-login-with-python-and-selenium-207981484007#)
