# MANUAL DE INSTALACIÓN Y USO - SISTEMA DE GESTIÓN DE SORTEOS "LA SUERTE"
## DESCRIPCIÓN DEL PROYECTO
Sistema web desarrollado en Django para la gestión completa de sorteos de la tienda "La Suerte". Permite controlar ventas de números, registro de clientes, gestión de sorteos y generación de reportes.

## CARACTERÍSTICAS PRINCIPALES
- Gestión completa de clientes
- Venta de números (00-99) para tres tipos de sorteos
- Cálculo automático de premios con bono de cumpleaños
- Generación de vouchers de venta
- Registro de resultados de sorteos
- Reportes de ganadores y recaudación
- Control de períodos de reclamación (5 días hábiles)

## TECNOLOGÍAS UTILIZADAS
- Backend: Django 5.2.8
- Frontend: HTML5, Bootstrap 5, JavaScript
- Base de Datos: SQLite
- Gráficos: Chart.js
- Iconos: Font Awesome

## ESTRUCTURA DEL PROYECTO
preprivado_tienda_la_suerte/\
├── manage.py\
├── requirements.txt\
├── sorteo/ (Configuración del proyecto)\
├── app/ (Aplicación principal)\
└── templates/ (Templates HTML)

## INSTRUCCIONES DE INSTALACIÓN PASO A PASO
### PREREQUISITOS
- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)
### PASO 1: PREPARAR EL ENTORNO
- Descargar o clonar el proyecto
- Abrir terminal/consola en la carpeta del proyecto

### PASO 2: CREAR ENTORNO VIRTUAL
Ejecutar en la consola:
```
> python -m venv venv
```
Activar el entorno virtual:
```
- Windows: venv\Scripts\activate
- Linux/Mac: source venv/bin/activate
```

### PASO 3: INSTALAR DEPENDENCIAS
```
> pip install django
```

### PASO 4: CONFIGURAR LA BASE DE DATOS
```
> python manage.py makemigrations
> python manage.py migrate
```

### PASO 5: CARGAR DATOS INICIALES
```
> python manage.py load_initial_data
```

Este comando crea:
- Los 3 tipos de sorteos: La Santa, La Rifa, El Sorteo
- Un usuario administrador

### PASO 6: CREAR USUARIO ADMINISTRADOR
```
> python manage.py createsuperuser
```
Seguir las instrucciones para crear un usuario y contraseña.

### PASO 7: EJECUTAR EL SISTEMA
```
> python manage.py runserver
```
Abrir en el navegador: http://127.0.0.1:8000/

## CONFIGURACIÓN DE SORTEOS
El sistema incluye tres tipos de sorteos preconfigurados:
- LA SANTA: Paga Q25.00 por Q1.00 (3 sorteos diarios)
- LA RIFA: Paga Q70.00 por Q1.00 (1 sorteo diario)
- EL SORTEO: Paga Q150.00 por Q1.00 (2 sorteos diarios)

## MANUAL DE USUARIO
1. ACCEDER AL SISTEMA
- URL: http://127.0.0.1:8000/
- Usar las credenciales del superusuario creado
2. REGISTRAR UN CLIENTE
- Hacer clic en "Clientes" en el menú lateral
- Completar el formulario con:
  - Nombre completo
  - Teléfono
  - Dirección
  - Fecha de nacimiento
- Hacer clic en "Guardar Cliente"