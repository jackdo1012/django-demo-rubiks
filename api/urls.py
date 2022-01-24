from django.urls import path
from .views import RubiksView, SpecificRubiksView

urlpatterns = [
    path('rubiks', RubiksView.as_view()),
    path('rubiks/<int:pk>', SpecificRubiksView.as_view())
]

