from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from yami.views import index, checkout, shopingcart, shops, detail, contact
from accounts.views import loginview, logoutview, register, testre

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("login/", loginview, name="login"),
    path("register/", register, name="register"),
    path("logout/", logoutview, name='logout'),
    path("checkout/", checkout, name="checkout"),
    path("shopingcart/", shopingcart, name="shopingcart"),
    path("shops/", shops, name="shops"),
    path("shops/<int:pk>/", detail, name="detail"),
    path("contact/", contact, name="contact"),
    path("test/", testre, name="testre")
    
]

if settings.IS_DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
