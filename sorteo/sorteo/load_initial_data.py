from django.core.management.base import BaseCommand
from app.models import Sorteo

class Command(BaseCommand):
    help = 'Carga datos iniciales de sorteos'

    def handle(self, *args, **options):
        sorteos = [
            {'nombre': 'LA_SANTA', 'factor_pago': 25.00, 'sorteos_diarios': 3},
            {'nombre': 'LA_RIFA', 'factor_pago': 70.00, 'sorteos_diarios': 1},
            {'nombre': 'EL_SORTEO', 'factor_pago': 150.00, 'sorteos_diarios': 2},
        ]
        
        for sorteo_data in sorteos:
            sorteo, created = Sorteo.objects.get_or_create(
                nombre=sorteo_data['nombre'],
                defaults=sorteo_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Sorteo {sorteo.nombre} creado')
                )