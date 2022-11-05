from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.get_routes),
    path('import/', views.import_data),
    # POST request na stiahnutie dat zo subora json
    path('detail/<str:model_name>/', views.all_data),
    # GET request na zobrazenie všetkých dat na zaklade nazvu modelu
    path('detail/<str:model_name>/<str:pk>/', views.data_by_id),
    # GET request zobrazenie dat na zakade nazvu modelu a id
]