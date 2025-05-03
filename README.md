# 05EPPY_A01

## Instalación con make
- 1.- Crear un directorio base
- 2.- Crear un entorno virtual
- 3.- Instalar las herramientas necesarias
- 4.- Clonar el repositorio desde https://github.com/fresvel/05EPPY_A01
- 5.- Entrar en el directorio 05EPPY_A01
- 6.- Compilar
- 7.- Instalar

```bash
pip install setuptools wheel build
git clone https://github.com/fresvel/05EPPY_A01
cd 05EPPY_A01
make build
make install
coockie-clicker
```

En esta isntalación es necesario ingresar por cmd la ruta del driver que se puede descargar desde: https://googlechromelabs.github.io/chrome-for-testing/


## Instalación en Entorno Pipenv
Al compilar con los comandos de arriba se crea un directorio dist con los archivos .whl y tar.gz, para instalar la aplicación copiar los archivos whl y tar.gz a un nuevo directorio y ejecutar:
```bash
pipenv shell
pip install cookie_clicker-0.1.0-py3-none-any.whl
```
## Ejecución
Para iniciar la aplicación, ejecutar:

```bash
coockie-clicker
```

De forma posterior le solicitará la ruta de acceso al driver (Chrome for testing). Se debe ingresar la ruta absoluta
