from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Text
from .serializers import TextSerializer
# Create your views here.


class TextAPIView(APIView):
    """
    Base View class processes GET/POST methods
    """
    def get(self, request):
        """
        Returns all posts from DB
        """
        content = Text.objects.all()
        return Response({"posts": TextSerializer(content, many=True).data})

    def post(self, request):
        """
        Saves new text in DB & return its url
        """
        new_data = TextSerializer(data=request.data)
        new_data.is_valid(raise_exception=True)
        new_data.save()
        return Response({"url": new_data.data["url"]})


@api_view()
def single_post(request, post_url):
    """
    Simply returns text for requested url
    """
    text = get_object_or_404(Text, url=post_url)
    return Response({"Text": TextSerializer(text).data["content"]})
