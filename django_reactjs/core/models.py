from django.db import models

# Create your models here.


class Files(models.Model):
    pdf = models.FileField(upload_to='store/pdfs/')

    def __str__(self):
        return self.pdf
