from django.shortcuts import render

from rest_framework import viewsets
from .models import Admin, Lokasi, GolonganPelanggan, User, Petugas, SumberAir, Pengaduan, Tagihan, Pembayaran
from .serializers import AdminSerializer, LokasiSerializer, GolonganPelangganSerializer, UserSerializer, PetugasSerializer, SumberAirSerializer, PengaduanSerializer, TagihanSerializer, PembayaranSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class LokasiViewSet(viewsets.ModelViewSet):
    queryset = Lokasi.objects.all()
    serializer_class = LokasiSerializer

class GolonganPelangganViewSet(viewsets.ModelViewSet):
    queryset = GolonganPelanggan.objects.all()
    serializer_class = GolonganPelangganSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetugasViewSet(viewsets.ModelViewSet):
    queryset = Petugas.objects.all()
    serializer_class = PetugasSerializer

class SumberAirViewSet(viewsets.ModelViewSet):
    queryset = SumberAir.objects.all()
    serializer_class = SumberAirSerializer

class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

class TagihanViewSet(viewsets.ModelViewSet):
    queryset = Tagihan.objects.all()
    serializer_class = TagihanSerializer

class PembayaranViewSet(viewsets.ModelViewSet):
    queryset = Pembayaran.objects.all()
    serializer_class = PembayaranSerializer
