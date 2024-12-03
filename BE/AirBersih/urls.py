from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, LokasiViewSet, GolonganPelangganViewSet, UserViewSet, PetugasViewSet, SumberAirViewSet, PengaduanViewSet, TagihanViewSet, PembayaranViewSet

router = DefaultRouter()
router.register(r'admin', AdminViewSet)
router.register(r'lokasi', LokasiViewSet)
router.register(r'golonganpelanggan', GolonganPelangganViewSet)
router.register(r'user', UserViewSet)
router.register(r'petugas', PetugasViewSet)
router.register(r'sumberair', SumberAirViewSet)
router.register(r'pengaduan', PengaduanViewSet)
router.register(r'tagihan', TagihanViewSet)
router.register(r'pembayaran', PembayaranViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
