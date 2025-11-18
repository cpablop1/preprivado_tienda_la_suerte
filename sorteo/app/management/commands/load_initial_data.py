from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Carga datos iniciales para el sistema de sorteos'

    def handle(self, *args, **options):
        # Importar modelos dentro del método para evitar problemas de importación
        Sorteo = apps.get_model('app', 'Sorteo')  # Cambia 'app' por el nombre de tu aplicación
        
        # Datos iniciales de sorteos
        sorteos = [
            {
                'nombre': 'LA_SANTA', 
                'factor_pago': 25.00, 
                'sorteos_diarios': 3,
                'activo': True
            },
            {
                'nombre': 'LA_RIFA', 
                'factor_pago': 70.00, 
                'sorteos_diarios': 1,
                'activo': True
            },
            {
                'nombre': 'EL_SORTEO', 
                'factor_pago': 150.00, 
                'sorteos_diarios': 2,
                'activo': True
            },
        ]
        
        for sorteo_data in sorteos:
            sorteo, created = Sorteo.objects.get_or_create(
                nombre=sorteo_data['nombre'],
                defaults=sorteo_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Sorteo {sorteo.get_nombre_display()} creado exitosamente')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠️ Sorteo {sorteo.get_nombre_display()} ya existe')
                )
        
        self.stdout.write(
            self.style.SUCCESS('🎉 Datos iniciales cargados exitosamente!')
        )