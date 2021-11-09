from django.db import models

class Pozicija(models.Model):
    godina = models.IntegerField()
    pozicija_sifra = models.CharField(max_length=255)
    konto3 =models.IntegerField()
    pozicija_naziv =models.CharField(max_length=255)
    planirano = models.CharField(max_length=255)
    razdjel =models.CharField(max_length=255)
    glava =models.CharField(max_length=255)
    program =models.CharField(max_length=255)
    aktivnost =models.CharField(max_length=255)
    kategorija = models.CharField(max_length=255)
    podkategorija = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pozicija'
        verbose_name = 'pozicija'
        verbose_name_plural = 'pozicije'

