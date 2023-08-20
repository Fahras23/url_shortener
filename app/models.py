from django.db import models


class Urls(models.Model):
    input_url = models.TextField(max_length=200)
    output_url = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.input_url} | {self.output_url}"
