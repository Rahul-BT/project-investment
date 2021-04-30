from django.urls import path, re_path
from invst import views

urlpatterns = [
    path("", views.HomePageView, name='home'), # Notice the URL has been named
    path("invst", views.HomePageView, name='invst'),
    path("mf", views.mfView, name='mf'),
#    path("dental", views.dentalView, name='dental'),
    path("add-invst", views.addInvestment, name='add_investment'),
    path("add-mf", views.addMF, name='add_mf'),
#    path("add-dental", views.addDental, name='add_dental'),
    path("delete-<str:modelName>-<int:list_id>", views.delInvestment, name='del_investment'),
    path("testing", views.testing, name='testing'),
    # re_path(r'^delete-(\d*)$', views.delInvestment, name='del_investment')

    path("account/login/", views.loginView, name='login_view'),
    path("account/register/", views.registerView, name='register_view'),
    path("account/logout/", views.logoutView, name='logout_view'),
]