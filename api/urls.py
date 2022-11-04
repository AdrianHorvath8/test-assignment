from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.get_routes),
    path('import/', views.import_data),
    path('detail/attributes/', views.attributes),
]