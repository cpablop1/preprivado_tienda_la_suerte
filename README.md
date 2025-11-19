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
- Base de Datos: MySQL
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

3. REALIZAR UNA VENTA
- Hacer clic en "Venta" en el menú lateral
- Seleccionar el cliente (o registrar uno nuevo)
- Seleccionar el tipo de sorteo
- Ingresar número (00-99)
- Ingresar monto a apostar
- Seleccionar número de sorteo del día
- Hacer clic en "Registrar Venta"
- El sistema generará automáticamente un voucher

4. REGISTRAR RESULTADOS DE SORTEOS
- Hacer clic en "Resultados" en el menú lateral
- Seleccionar tipo de sorteo
- Ingresar fecha del sorteo
- Ingresar número ganador (00-99)
- Especificar número de sorteo del día
- Hacer clic en "Registrar Resultado"

5. GENERAR REPORTES
REPORTE DE GANADORES:
- Ir a "Reportes" → "Ganadores"
- Seleccionar fecha deseada
- Ver lista de ganadores
REPORTE DE RECAUDACIÓN:
- Ir a "Reportes" → "Recaudación"
- Seleccionar rango de fechas
- Opcional: filtrar por sorteo específico
- Ver reporte con gráficos

## REGLAS DE NEGOCIO IMPLEMENTADAS
- Los números van del 00 al 99
- Un mismo número puede venderse a múltiples personas
- Bono del 10% adicional si el cliente cumple años el día de la venta
- Período de reclamación: 5 días hábiles después del sorteo
- Si no hay ganador, se muestra "ganador desierto"

## SOLUCIÓN DE PROBLEMAS COMUNES
PROBLEMA 1: Error "Reverse for 'voucher_venta' not found"\
SOLUCIÓN: Verificar que en views.py se use 'sistema:voucher_venta'

PROBLEMA 2: Error "Invalid filter: 'div'"\
SOLUCIÓN: Asegurarse que existe el archivo templatetags/custom_filters.py

PROBLEMA 3: No se cargan los datos iniciales\
SOLUCIÓN: Ejecutar estos comandos en orden:

- python manage.py makemigrations
- python manage.py migrate
- python manage.py load_initial_data

PROBLEMA 4: No se ven los estilos CSS\
SOLUCIÓN: Verificar la conexión a internet (Bootstrap usa CDN)

## URLS IMPORTANTES
- Sistema principal: http://127.0.0.1:8000/
- Administración Django: http://127.0.0.1:8000/admin/
- Gestión de clientes: http://127.0.0.1:8000/clientes/
- Ventas: http://127.0.0.1:8000/venta/
- Resultados: http://127.0.0.1:8000/resultados/
- Reportes: http://127.0.0.1:8000/reportes/

## INFORMACIÓN ADICIONAL
Este sistema fue desarrollado como proyecto académico para la Universidad Mariano Gálvez de Guatemala, Facultad de Ingeniería en Sistemas de Información.

Fecha de entrega: Noviembre 2025