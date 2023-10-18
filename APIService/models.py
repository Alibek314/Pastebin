from django.db import models
from sequences import Sequence
import base64
# Create your models here.

url_seq = Sequence("unique_url_seq", initial_value=1000000)


class Text(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @classmethod
    def create(cls):
        uniq_url_num = str(url_seq.get_next_value())
        uniq_url_num = uniq_url_num.encode('ascii')
        uniq_url = base64.b64encode(uniq_url_num)
        uniq_url = uniq_url.decode()
        text = cls(url=uniq_url)
        return text
