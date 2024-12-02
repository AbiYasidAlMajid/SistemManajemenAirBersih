from django.db import models

class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    
    nama_admin = models.CharField(max_length=100)
    email_admin = models.EmailField(unique=True)
    password_admin = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_admin

class Lokasi(models.Model):
    id_lokasi = models.AutoField(primary_key=True)
    
    nama_lokasi = models.CharField(max_length=50)
    alamat_lokasi = models.TextField()
    jumlah_penduduk = models.IntegerField()
    id_sumber_air = models.ForeignKey('SumberAir', on_delete=models.CASCADE, related_name='lokasi')
    faktor_tarif = models.FloatField()

    def __str__(self):
        return self.nama_lokasi

class GolonganPelanggan(models.Model):
    id_golongan_pelanggan = models.AutoField(primary_key=True)
    
    kelompok_pelanggan = models.CharField(max_length=100)
    tarif_0_3 = models.FloatField(help_text='Dalam rupiah (Rp), untuk penggunaan 0-3 m3')
    tarif_3_10 = models.FloatField(help_text='Dalam rupiah (Rp), untuk penggunaan 3-10 m3') 
    tarif_10_20 = models.FloatField(help_text='Dalam rupiah (Rp), untuk penggunaan 10-20 m3')
    tarif_diatas_20 = models.FloatField(help_text='Dalam rupiah (Rp), untuk penggunaan di atas 20 m3')

    def __str__(self):
        return self.kelompok_pelanggan

class User(models.Model):
    JK=(
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    
    id_user = models.AutoField(primary_key=True)
    
    nama_user = models.CharField(max_length=50)
    nik_user = models.CharField(max_length=16, unique=True)
    jenis_kelamin_user = models.CharField(max_length=10, choices=JK)
    alamat_user = models.TextField()
    kecamatan = models.CharField(max_length=50)
    id_lokasi = models.ForeignKey(Lokasi, on_delete=models.CASCADE, related_name='user')
    id_golongan_pelanggan = models.ForeignKey(GolonganPelanggan, on_delete=models.CASCADE, related_name='user')
    
    email_user = models.EmailField(max_length=50, unique=True)
    no_telepon_user = models.CharField(max_length=15)
    password_user = models.CharField(max_length=30)
    
    def _str_(self):
        return f"Nama: {self.nama_user} - NIK: {self.nik_user}"
    
class Petugas(models.Model):
    JK=(
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    )
    
    id_petugas = models.AutoField(primary_key=True)
    
    nama_petugas = models.CharField(max_length=100)
    nik_petugas = models.CharField(max_length=20, unique=True) 
    jenis_kelamin_petugas = models.CharField(max_length=10, choices=JK)
    alamat_petugas = models.TextField()
    wilayah_penugasan = models.TextField()
    
    email_petugas = models.EmailField(max_length=50, unique=True)
    no_telepon_petugas = models.CharField(max_length=15)
    password_petugas = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nama: {self.nama_petugas} - NIK: {self.nik_petugas}"

class SumberAir(models.Model):
    SSumberAir = (
        ('Atf', 'Aktif'),
        ('TdkAtf', 'Tidak Aktif'),
    )
    
    id_sumber_air = models.AutoField(primary_key=True)
    
    nama_sumber_air = models.CharField(max_length=100)
    alamat_sumber_air = models.TextField()
    jenis = models.CharField(max_length=50)
    kualitas = models.CharField(max_length=50)
    kapasitas = models.IntegerField(help_text='Dalam liter per detik (lps)')
    status_sumber_air = models.CharField(max_length=20, choices=SSumberAir)

    def __str__(self):
        return self.nama_sumber_air
    
class Pengaduan(models.Model):
    SPengaduan = (
        ('Tkr', 'Terkirim'),
        ('Prs', 'Diproses'),
        ('Sls', 'Selesai'),
        ('Btl', 'Dibatalkan'),
    )
    
    id_pengaduan = models.AutoField(primary_key=True)
    
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pengaduan')
    
    tanggal_pengaduan = models.DateField()
    jenis_pengaduan = models.CharField(max_length=50)
    isi_pengaduan = models.TextField()
    status_pengaduan = models.CharField(max_length=20, choices=SPengaduan)
    
    id_petugas = models.ForeignKey(Petugas, on_delete=models.CASCADE, related_name='pengaduan')
    tanggapan_petugas = models.TextField()

    def __str__(self):
        return f"User: {self.id_user} - Jenis Pengaduan: {self.jenis_pengaduan}"

class Tagihan(models.Model):
    STagihan = (
        ('BlmByr', 'Belum Dibayar'),
        ('SdhByr', 'Sudah Dibayar'),
    )
    
    id_tagihan = models.AutoField(primary_key=True)
    
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tagihan')
    
    periode = models.CharField(max_length=50)
    penggunaan_air = models.FloatField(help_text='Penggunaan air dalam m3')
    nominal_tagihan = models.IntegerField(help_text='Dalam rupiah (Rp)')
    tenggat = models.DateField()
    status_tagihan = models.CharField(max_length=20, choices=STagihan)
    
    def __str__(self):
        return f"Tagihan #{self.id_tagihan} - User: {self.id_user} - Periode: {self.periode}"
    
class Pembayaran(models.Model):
    SPembayaran = (
        ('Prs', 'Diproses'),
        ('Sls', 'Selesai'),
        ('Btl', 'Dibatalkan'),
    )
    
    id_pembayaran = models.AutoField(primary_key=True)
    
    id_tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE, related_name='pembayaran')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pembayaran')
    
    nominal_pembayaran = models.IntegerField(help_text='Dalam rupiah (Rp)')
    metode_pembayaran = models.CharField(max_length=50)
    tanggal_pembayaran = models.DateField()
    status_pembayaran = models.CharField(max_length=20, choices=SPembayaran)

    def __str__(self):
        return f"Pembayaran #{self.id_pembayaran} - User: {self.id_user} - Tagihan: {self.id_tagihan}"
