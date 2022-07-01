import os
# import modules.ask as ask
import modules.proj_name as pn
import modules.value_replace as vr


# Presentación.
print('\n### Programa para crear un proyecto nuevo desde el esquema base ###\n')

# Título del proyecto.
project_name = pn.pro_name()

# Obtenemos el path de la aplicación, nos movemos a él y lo mostramos.
p = os.path.abspath(os.getcwd())
os.chdir(p)
print('\nEl path actual es ', p)

# Creamos la carpeta inicial del proyecto.
print(f'Creando la carpeta inicial del proyecto {project_name}')
cmd = 'py.exe -m django startproject' + ' ' + project_name
os.system(cmd)

# Nos movemos al directorio del proyecto recién creado.
os.chdir(project_name)
p = os.path.abspath(os.getcwd())
print('Cambiar a ', p)

# Iniciamos la clonación del esquema base.
print('Clonación del esquema base...\n')
os.system('git clone https://github.com/tecasires/base.git')

# Nos movemos a la carpeta del proyecto base.
os.chdir('base')
p = os.path.abspath(os.getcwd())
print('\nCambiar a ', p)

# Eliminamos el repositorio antigüo si lo hubiese.
print('Eliminar el repositorio antiguo...')
os.system('rmdir /S /Q .git')

# Movemos las plantillas del directorio base al directorio principal de nuestro proyecto.
print('Moviendo plantillas...')
os.system('move templates ..')

# Movemos el archivo .gitignore del directorio base al directorio principal de nuestro proyecto.
print('Mover .gitignore...')
os.system('move .gitignore ..')

# Movemos el archivo LICENSE del directorio base al directorio principal de nuestro proyecto.
print('Mover LICENSE...')
os.system('move LICENSE ..')

# Movemos el archivo README.md del directorio base al directorio principal de nuestro proyecto.
print('Mover README.md...')
os.system('move README.md ..')

# Movemos el archivo requirements.txt del directorio base al directorio principal de nuestro proyecto.
print('Mover requirements.txt...')
os.system('move requirements.txt ..')

# Nos movemos al directorio principal.
os.chdir('..')
p = os.path.abspath(os.getcwd())
print('Cambiar a ', p)

# Eliminamos el subdirectorio que se llama igual que nuestro proyecto.
print('Eliminar directorio' + ' "' + project_name + '"' +  '...')
cmd = 'rmdir /S /Q' + ' '  + project_name
os.system(cmd)

# Renombramos el directorio base como base.old.
print('Renombrar base a base.old...')
os.system('move base base.old')

# Nos movemos al directorio base.old.
os.chdir('base.old')
p = os.path.abspath(os.getcwd())
print('Cambiar a ', p)

# Movemos el subdirectorio base a nuestro directorio principal.
print('Mover base...')
os.system('move base ..')

# Nos movemos al directorio principal.
os.chdir('..')
p = os.path.abspath(os.getcwd())
print('Cambiar a ', p)

# Eliminamos el directorio base.old.
print('Eliminar el directorio base.old...')
os.system('rmdir /S /Q base.old')

# Obtenemos el path de la aplicación y lo mostramos.
p = os.path.abspath(os.getcwd())
print('\nEl path actual es ', p)

# Modificamos el nombre del proyecto dentro del archivo manage.py.
print('\nActualizando el contenido del archivo manage.py ', p)
pn_settings = project_name + '.settings'
vr.value_replace('manage.py', pn_settings, 'base.settings')

# Imprimimos el mensaje final.
print('\n### PROCESO FINALIZADO ###')
