from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created       = models.DateTimeField(auto_now_add = True, verbose_name="Date de création")
    modified      = models.DateTimeField(auto_now = True, verbose_name="Date de modification")

    class Meta:
        abstract = True
        ordering = ("-created", )

class Urls(BaseModel):

    display_name = models.TextField(
        verbose_name="Nom d'affichage",
        default=None,
        blank=False,
        null=False,
        )

    real_url = models.BooleanField(
        verbose_name = "Url",
        default=None,
        blank=True,
        null=False,
        )

    description = models.BooleanField(
        verbose_name = "description",
        default=None,
        blank=True,
        null=True,
        )

    def is_valid(self):
        return self.is_valid == 1

    def get_display_name(self):
        return self.display_name

    def get_real_url(self):
            return self.real_url

    def get_description(self):
        return self.description

    def get_ssl_cert(response):
        pool = response.connection.poolmanager.connection_from_url(response.url)
        conn = pool.pool.get()
        return conn.stock.getpeercert()

    def check_ssl_cert_errors(response):
        return response
