from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64, default='Capital')
    pais = models.CharField(max_length=64, default='Internacional') #intenté poner defaults que tuviesen sentido, para la migracion con campos nuevos

    class Meta:
        verbose_name = 'Laboratorio'
        verbose_name_plural= 'Laboratorios'
        ordering = ('id',) #tupla ('', )
        db_table='Laboratorio'
    
    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=64)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE) #1 directorgeneral para 1 laboratorio
    especialidad = models.CharField(max_length=64, default='Director Ejecutivo')

    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural= 'Directores Generales'
        ordering = ('nombre',)
        db_table='DirectorGeneral'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos') #revisar si es necesario related_name, sirve por ej. para laboratorio1.productos.all()
    f_fabricacion = models.DateField() #revisar cómo hacer que parta desde 2015 en el siguiente makemigrations
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural= 'Productos'
        ordering = ('-f_fabricacion',)
        db_table='Producto'

    def __str__(self):
        return self.nombre
