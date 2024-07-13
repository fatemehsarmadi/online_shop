from django.db import models

class AbstractProductModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        abstract = True

class Mobile(AbstractProductModel):
    brand = models.CharField(max_length=100)
    dimensions_height = models.FloatField(verbose_name='height')
    dimensions_width = models.FloatField(verbose_name='width')
    dimensions_thickness = models.FloatField(verbose_name='thickness')
    weight = models.CharField(max_length=50)

    body_structure = models.CharField(max_length=255)

    SIZE_CHOICES = (
        ('S', 'Standard'),
        ('M', 'Micro'),
        ('N', 'Nano'),
        ('E', 'eSIM'),
    )
    sim_card_size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    sim_card_number = models.IntegerField(max_length=1)

    chip = models.CharField(max_length=200)
    cpu_type = models.CharField(max_length=200)
    cpu_frequency = models.CharField(max_length=50)
    MEMORY_CARD_CHOICES = (
        ('N', 'Not supported'),
        ('MM2', 'Memory Stick Micro-M2'),
        ('MSD', 'microSD'),
        ('MSDHC', 'MicroSDHC'),
        ('MSD', 'miniSD'),
        ('NM', 'Nano Memory'),
        ('SD', 'SD')
    )
    memory_card_support = models.CharField(max_length=5, choices=MEMORY_CARD_CHOICES)

    screen_technology = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=80)
    screen_resolution = models.CharField(max_length=80)

    supporting_the_1G = models.BooleanField()
    supporting_the_2G = models.BooleanField()
    supporting_the_3G = models.BooleanField()
    supporting_the_4G = models.BooleanField()
    supporting_the_5G = models.BooleanField()

    wifi_is_supported = models.BooleanField()
    bluetooth_is_supported = models.BooleanField()
    gps_is_supported = models.BooleanField()

    camera_resolution = models.CharField(max_length=50)
    os = models.CharField(max_length=30)