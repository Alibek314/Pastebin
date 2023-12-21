from django.urls import path
from . import views
from .views import TextAPIView


urlpatterns = [
    path('api/v1/all_texts', TextAPIView.as_view()),
    path('api/v1/<str:post_url>', views.single_post)
]
