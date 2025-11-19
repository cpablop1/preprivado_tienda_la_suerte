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
`preprivado_tienda_la_suerte/<b>
├── manage.py<b>
├── requirements.txt<b>
├── sorteo/ (Configuración del proyecto)<b>
├── app/ (Aplicación principal)<b>
└── templates/ (Templates HTML)`

## INSTRUCCIONES DE INSTALACIÓN PASO A PASO
### PREREQUISITOS
- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)
- PASO 1: PREPARAR EL ENTORNO
- Descargar o clonar el proyecto
- Abrir terminal/consola en la carpeta del proyecto
- PASO 2: CREAR ENTORNO VIRTUAL