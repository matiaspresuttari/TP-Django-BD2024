from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class NombreAbstract(models.Model):
    nombre = models.CharField(
        _('Nombre'),
        help_text=_('Nombre descriptivo'),
        max_length=200,
        # unique=True,
    )

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nombre)
    
class tipoUva(models.Model):
    nombre = models.CharField(
        _('Nombre'),
        help_text=_('Nombre del tipo de uva'),
        max_length=100,
    )

    def __str__(self):
        return self.nombre

class regionVitivinicola(models.Model):
    nombre = models.CharField(
        _('Nombre'),
        help_text=_('Nombre de la región vitivinícola'),
        max_length=100,
    )

    def __str__(self):
        return self.nombre

class varietal(NombreAbstract):
    descripcion = models.TextField((
        _('Descripción')),
        help_text=_('Descripción del varietal'),
        blank=True,
    )
    porcentajeComposicion = models.DecimalField(
    _('Porcentaje de composición'),
    help_text=_('Porcentaje de composición del varietal en el vino'),
    max_digits=5,
    decimal_places=2,
)
    tipoUva = models.ForeignKey(
    'tipoUva',
    verbose_name=_('Tipo de uva'),
    help_text=_('Tipo de uva del varietal'),
    on_delete=models.SET_NULL,
    null=True,
)
    regionVitivinicola = models.ForeignKey(
        regionVitivinicola,
        verbose_name=_('Región vitivinícola'),
        help_text=_('Región vitivinícola del varietal'),
        null=True,
        on_delete=models.SET_NULL,
    )
    def __str__(self):
        return '{} {}'.format(self.descripcion, self.porcentajeComposicion)



    # class Meta:
    #     indexes = [models.index(field=['tipoUva', 'regionVitivinícola'])]