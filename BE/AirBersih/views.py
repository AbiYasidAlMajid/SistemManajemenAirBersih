from django.shortcuts import render
from rest_framework import viewsets, status, generics, views, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from .models import AirBersihAdmin, Lokasi, GolonganPelanggan, Pengguna, Petugas, SumberAir, Pengaduan, Tagihan, Pembayaran
from .serializers import LoginSerializer, LogoutSerializer, RegisterSerializer, AirBersihAdminSerializer, LokasiSerializer, GolonganPelangganSerializer, PenggunaSerializer, PetugasSerializer, SumberAirSerializer, PengaduanSerializer, TagihanSerializer, PembayaranSerializer

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response({
            'user': serializer.validated_data['user'],
            'tokens': serializer.validated_data['tokens']
        }, status=status.HTTP_200_OK)
        
class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except Exception as e:
            return Response({"detail": "Failed to logout"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
    
    
class AirBersihAdminViewSet(viewsets.ModelViewSet):
    queryset = AirBersihAdmin.objects.all()
    serializer_class = AirBersihAdminSerializer

class LokasiViewSet(viewsets.ModelViewSet):
    queryset = Lokasi.objects.all()
    serializer_class = LokasiSerializer

class GolonganPelangganViewSet(viewsets.ModelViewSet):
    queryset = GolonganPelanggan.objects.all()
    serializer_class = GolonganPelangganSerializer

class PenggunaViewSet(viewsets.ModelViewSet):
    queryset = Pengguna.objects.all()
    serializer_class = PenggunaSerializer

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
