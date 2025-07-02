from django.urls import path
from .views import CreateManagerView, ListManagersView

urlpatterns = [
    path('create-manager/', CreateManagerView.as_view(), name='create_manager'),
        path('managers/', ListManagersView.as_view(), name='list-managers'),

]
