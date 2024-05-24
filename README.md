# ProyectoHerramientas Changelog

## 21/05/2024

### Creación del Repositorio
- **Autor:** Santiago Vasco Lasso (`Vazkoo`)
- **Correo:** santiagovasco@javerianacali.edu.co

### Agregación de Colaboradores
Se agregan los siguientes colaboradores (miembros del grupo):
- **vqz19:** Juan Sebastián Vásquez (`juan19pelaez@gmail.com`)
- **Al3j00:** Alejandro Martínez Carrillo (`discorddealejandrowb@gmail.com`)

### Creación de Nuevas Ramas/Branches
Mediante el comando de Git `git checkout -b`, cada integrante crea su nueva rama:
- `rama_vasquez` (vqz19)
- `rama_martínez` (Al3j00)
- `rama_vasco` (Vazkoo)

### Creación de Aportes del Menú de Opciones
Con el comando `touch` y `git add` se crean y añaden los archivos para su debida programación:

1. **caracterabyte.py** (vqz19)
   - Se define la función que permite obtener la representación en byte de un carácter.

2. **palabraacaracter.py** (Al3j00)
   - Se define la función que permite obtener la representación en bytes de una palabra o mejor llamada cadena de caracteres.

3. **byteacadena.py** (Vazkoo)
   - Se define la función que permite obtener la representación del código ASCII de un byte que se ingrese.

### Commit Changes: Integración de Archivos a la Rama
Mediante `git commit -m`, cada integrante incorpora su archivo completo a su respectiva rama.

### Pull Requests: Integración de los Contenidos de las Ramas al Main
Cada integrante realiza un pull request para hacer merge de los cambios de su rama al `main`.

### Chequeo de Pull Request
Cada integrante del grupo hace revisión par del Pull Request antes de hacer merge al `main`:
- Entre sí, cada colaborador revisa el correcto funcionamiento del código del otro y deja un comentario.

### Merge al Main
Finalmente se hace merge al `main` incorporando los nuevos cambios de las respectivas ramas:
1. **caracterabyte.py** (`rama_vasquez`)
2. **palabraacaracter.py** (`rama_martínez`)
3. **byteacadena.py** (`rama_vasco`)

### Creación del Menú de Opciones
En base a los aportes de cada uno, se programa el Menú de Opciones **BAC** (Byte, ASCII, Character):
- Cada colaborador importa su función y arma la parte del código que le corresponde.

### Pull Request Final
Se incorpora el menú en la `rama_vasco` haciendo commit change, y con el debido Pull Request todos los integrantes lo testean y hacen el merge a la rama `main`.

### Incluir Exclusiones: Creación del Archivo `.gitignore`
Se incluye al repositorio el archivo `.gitignore` que contiene la información de exclusiones que el equipo considera necesarias.
