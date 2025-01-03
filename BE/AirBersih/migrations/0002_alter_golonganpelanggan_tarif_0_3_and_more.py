# Generated by Django 5.1.2 on 2024-12-02 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirBersih', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golonganpelanggan',
            name='tarif_0_3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='golonganpelanggan',
            name='tarif_10_20',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='golonganpelanggan',
            name='tarif_3_10',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='golonganpelanggan',
            name='tarif_diatas_20',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='lokasi',
            name='faktor_tarif',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='petugas',
            name='jenis_kelamin_petugas',
            field=models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=10),
        ),
        migrations.AlterField(
            model_name='tagihan',
            name='penggunaan_air',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='jenis_kelamin_user',
            field=models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=10),
        ),
    ]
