## Requisitos 
Para poder ejecutar correctamente el proyecto es necesario tener instalado `Python`,
ademas de un servidor de bases de datos como **[MySQL](https://dev.mysql.com/downloads/workbench/)** o `MariaDB`.

## Instalando el proyecto
Realice la instalación de las librerias necesarias para la ejecución del proyecto usando el comando

```
$ pip install -r requirements.txt
```

Edite la configuración de usuario y contraseña de `MySQL` para la conexion de la base de datos en el archivo `dashboard_men/settings.py`

**NOTA:** debe crear previamente una base de datos para el proyecto y agregar el nombre a la configuración en el campo "[database_name]".

Una vez cambiada la información para la conexión a la base de datos y las librerias necesarias esten instaladas, debe realizar lo siguiente para la migración
de las tablas a la base de datos creada previamente en **MySQL**.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Para realizar la inserción de los datos, edite la configuración de usuario y contraseña de la base de datos para la conexion con **MySQL**
en el script `data_management.py`:

```
'mysql+pymysql://[user]:[password]@127.0.0.1/[database_name]'
```

Ejecutando el script en una consola con el siguiente comando se realizará la inserción de los datos en **MySQL**:

```
$ python data_management.py
```

Finalmente, para ejecutar el servidor de **Django** se debe usar el siguiente comando en una consola:

```
$ python manage.py runserver
```

## Funcionamiento del proyecto
- Cree un usuario administrador con el comando:

```
$ python manage.py createsuperuser
```

