from django.urls import path
from . import views


urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("emp-list", views.employee, name="list"),
    path("emp-detail/<str:pk>/", views.employee_detail, name="detail"),

    path("emp-update/<str:pk>/", views.update, name="update"),
    path("emp-delete/<str:pk>/", views.employee, name="update"),
]







#selasi234