from django.db import models
from sequences import Sequence
import base64
# Create your models here.

# Following sequence used for generating unique URLs for each post
url_seq = Sequence("unique_url_seq", initial_value=1000000)


class Text(models.Model):
    """
    Base model for all posts.
    """
    url = models.URLField(unique=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def create_url(self):
        """
        Method creates unique url using base64 encoding
        """
        if self.url == "":
            uniq_url_num = str(url_seq.get_next_value())
            uniq_url_num = uniq_url_num.encode("ascii")
            uniq_url = base64.b64encode(uniq_url_num)
            uniq_url = uniq_url.decode()
            self.url = uniq_url
            return f'New URL {self.url}'
        else:
            return f'This object already have URL - {self.url}'
