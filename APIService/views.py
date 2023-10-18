from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Text
# Create your views here.


class TextAPIView(APIView):

    def get(self, request):
        content = Text.objects.all().values()
        return Response({"content": list(content)})

    def post(self, request):
        new_text = Text.create()
        new_text.content = request.data["content"]
        new_text.save()
        return Response({"url": new_text.url})


@api_view()
def post(request, post_url):
    """
    Simply returns text for requested url
    """
    text = get_object_or_404(Text, url=post_url)
    return Response(model_to_dict(text))
