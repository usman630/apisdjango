from django.urls import path,include
from .views import view,add,filter,home,login,view_all,edit,update


urlpatterns = [
    path("login/",login,name='login'),
    path("home",home,name='home'),
    path("get/",view,name='view'),
    path("add",add,name="add"),
    path("filter",filter,name="filter"),
    path("all",view_all,name="view_all"),
    path("edit/<int:id>",edit,name='edit'),
    path("update/<int:id>",update,name='update')  
]