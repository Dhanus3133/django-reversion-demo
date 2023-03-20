from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import reversion


@reversion.register()
class Question(models.Model):

    """Question Paper Model"""

    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    priority = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(3)]
    )

    def save(self, *args, **kwargs):
        self.question = self.question.strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question}"


# Create your models here.
