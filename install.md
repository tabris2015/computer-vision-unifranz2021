# Instalación del entorno de desarrollo

Este curso usará un entorno de desarrollo basado en el lenguaje de programación Python.

## Instalación en Windows 10

### Python 3

En windows, la instalación de python se puede realizar a través de los paquetes oficiales en [python.org](https://python.org), puede descargar el instalador de python 3.9.7 (versión estable a octubre 2021) directamente de este [enlace](https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe)

Ejecute el instalador y marque la opción para **agregar python a la variable PATH**.

Una vez instalado el paquete, verifique la instalación ingresando a una terminal de `powershell` ejecutando el comando `python`, este debería abrir el intérprete de python.


### pip

Pip viene incorporado en el instalador oficial de python, no es necesario instalarlo aparte.

### virtualenv

En windows podremos administrar entornos virtuales con el paquete `virtualenv`, pero no podremos usar `virtualenvwrapper` ya que requiere de bash para funcionar. Por tanto, solamente instale el paquete `virtualenv` con pip:

```powershell
pip install virtualenv
```

Sin embargo, antes de poder crear entornos virtuales es necesario activar la ejecución de scripts desde powershell para poder usarlo. 

Para tal cometido, abra una terminal de powershell en modo de administrador y ejecute el siguiente comando:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Para crear un entorno virtual, en una carpeta, ejecute el comando:

```powershell
virtualenv venv
```

se creara una carpeta llamada `venv` con todos los archivos correspondientes al entorno virtual. Es recomendable crear un entorno virtual por proyecto para mantener las dependencias aisladas.

Para instalar los paquetes refiera a la instalación en GNU/Linux.

### Visual Studio Code

Visual Studio Code es un editor de texto open source con muchas funcionalidades para el desarrollo de software y progamación. Se puede descargar el instalador desde su [sitio oficial](https://code.visualstudio.com/download).

Ejecute el instalador y siga las instrucciones.

Una vez instalado VSCode, necesita instalar también la extensión oficial de Python.


## Instalación en GNU/Linux

### Python 3

Para los sistemas operativos basados en GNU/Linux, si cuenta con una distribución reciente, python 3 ya viene instalado. 

### pip

Pip es un administrador de paquetes de python, usaremos pip para instalar las dependencias, librerías y herramientas necesarias para el desarrollo de sistemas de visión. Para instalar pip, abra una terminal y copie los siguientes comandos:

```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

### Virtualenv wrapper

Es buena práctica gestionar los entornos de desarrollo a través de entornos virtuales de python, usaremos los paquetes `virtualenv` y `virtualenvwrapper`.

```bash
sudo pip install virtualenv virtualenvwrapper
```

Una vez instalados los paquetes, abra el archivo `~/.bashrc` y copie los siguientes comandos al final del archivo:

```bash
# virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Guarde los cambios, y reinicie la terminal.

#### Crear y activar un entorno virtual

Para crear un entorno virtual, desde una terminal ejecute el comando: `mkvirtualenv [nombre del entorno]`

```bash
mkvirtualenv opencv
```

### Paquetes de python

Los paquetes específicos de python que necesitaremos son los siguientes:

  - OpenCV
  - Numpy
  - Jupyter

Primero, instale las dependencias necesarias para opencv:

```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-dev libgl1-mesa-glx
```

Luego, con un entorno virtual activado, instale las librerías necesarias:

```bash
pip install numpy jupyter opencv-contrib-python
```

Verifique la instalación ingresando al intérprete de python con el comando `python` desde la terminal y luego ingrese lo siguiente:

```python
import cv2
cv2.__version__
# salida: '4.5.3'
```

### Visual Studio Code

Visual Studio Code es un editor de texto open source con muchas funcionalidades para el desarrollo de software y progamación. Se puede descargar el paquete .deb desde su [sitio oficial](https://code.visualstudio.com/download).

Instale el paquete con el siguiente comando:

```bash
sudo dpkg -i code_1.60.2-1632313585_amd64.deb
```