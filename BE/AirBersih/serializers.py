from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import AirBersihAdmin, Lokasi, GolonganPelanggan, User, Petugas, SumberAir, Pengaduan, Tagihan, Pembayaran

class AirBersihAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirBersihAdmin
        fields = '__all__'
        
class LokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokasi
        fields = '__all__'

class GolonganPelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolonganPelanggan
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PetugasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petugas
        fields = '__all__'

class SumberAirSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumberAir
        fields = '__all__'

class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = '__all__'

class TagihanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tagihan
        fields = '__all__'

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'