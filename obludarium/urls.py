from django.urls import path,include
from . import views
from . import url_handlers
from search.views import search

urlpatterns = [
    path("atleti_index/",views.AtletIndex.as_view(), name="atleti_index"),
    path("<int:pk>/atlet_detail/",views.CurrentAtletView.as_view(),name="atlet_detail"),
    path("create_atlet/",views.CreateAtlet.as_view(),name="novy_atlet"),
    path("create_vykon/",views.CreateVykon.as_view(),name="novy_vykon"),
    path("<int:pk>/edit/",views.EditAtlet.as_view(), name = "edit_atlet"),
    path("register/",views.UzivatelViewRegister.as_view(),name="registrace"),
    path("login/",views.UzivatelViewLogin.as_view(),name="login"),
    path("logout/",views.logout_user,name="logout"),
    path("", url_handlers.index_handler),
    path("search/",search,name="search"),

]