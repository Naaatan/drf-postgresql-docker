import uuid
from django.db import models

# Create your models here.
class TestData(models.Model):
    """
    テスト用モデル
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    name = models.TextField(verbose_name='名称')
    value = models.IntegerField()
