from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_form, name="login_form"),
    path("signin/",views.create_user,name="signin"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("edit_student/<int:student_id>/", views.edit_student, name="edit_student"),
    path("delete_student/<int:student_id>/", views.delete_student, name="delete_student"),
    path("add_student/", views.add_student, name="add_student"),
    path("search_student/", views.search_student, name="search_student"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
