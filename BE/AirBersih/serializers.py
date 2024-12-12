from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .models import AirBersihAdmin, Lokasi, GolonganPelanggan, Pengguna, Petugas, SumberAir, Pengaduan, Tagihan, Pembayaran

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        
        if not user:
            raise serializers.ValidationError("Tidak valid")
        
        refresh = RefreshToken.for_user(user)
        
        return{
            'user' : user.username,
            'tokens' : {
                'tokenBaru' : str(refresh),
                'aksesToken' : str(refresh.access_token)
            }
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Error')

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

class PenggunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengguna
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