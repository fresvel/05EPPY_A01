# 05EPPY_A01

## Instalación en Entorno Pipenv

Para instalar la aplicación copiar los archivos whl y tar.gz a un nuevo directorio y ejecutar:
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

## Instalación con make
1.- Instalar las herramientas necesarias
2.- Clonar el repositorio desde https://github.com/fresvel/05EPPY_A01
3.- Entrar en el directorio 05EPPY_A01
4.- Compilar
5.- Instalar

```bash
pip install setuptools wheel build
git clone https://github.com/fresvel/05EPPY_A01
cd 05EPPY_A01
make build
make install
```