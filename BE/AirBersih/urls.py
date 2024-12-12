from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirBersihAdminViewSet, LokasiViewSet, GolonganPelangganViewSet, PenggunaViewSet, PetugasViewSet, SumberAirViewSet, PengaduanViewSet, TagihanViewSet, PembayaranViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views

router = DefaultRouter()
router.register(r'airbersihadmin', AirBersihAdminViewSet)
router.register(r'lokasi', LokasiViewSet)
router.register(r'golonganpelanggan', GolonganPelangganViewSet)
router.register(r'pengguna', PenggunaViewSet)
router.register(r'petugas', PetugasViewSet)
router.register(r'sumberair', SumberAirViewSet)
router.register(r'pengaduan', PengaduanViewSet)
router.register(r'tagihan', TagihanViewSet)
router.register(r'pembayaran', PembayaranViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
