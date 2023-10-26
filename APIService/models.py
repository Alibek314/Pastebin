from django.db import models
from sequences import Sequence
import base64
# Create your models here.

# Following sequence used for generating unique URLs for each post in DB
url_seq = Sequence("unique_url_seq", initial_value=1000000)


class Text(models.Model):
    """
    Base model for all posts.
    """
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @classmethod
    def create(cls):
        """
        This method have to be called when instance is just created(when initiated).
         Method creates unique url using base64 encoding
        """
        uniq_url_num = str(url_seq.get_next_value())
        uniq_url_num = uniq_url_num.encode('ascii')
        uniq_url = base64.b64encode(uniq_url_num)
        uniq_url = uniq_url.decode()
        text = cls(url=uniq_url)
        return text
