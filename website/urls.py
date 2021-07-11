from django.urls import path
from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),  # トップページ('')にアクセス時、IndexView.as_view()で指定されたところを見に行く
    path('about/', AboutView.as_view()),  # ('about/')にアクセス時、AboutView.as_view()で指定されたところを見に行く
]