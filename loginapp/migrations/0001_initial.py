# Generated by Django 4.0 on 2022-02-17 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(default='255, 255, 255, 0', max_length=20, verbose_name='Culoare fundal')),
                ('titlecolor', models.CharField(default='0, 0, 0, 1', max_length=20, verbose_name='Culoare titlu')),
                ('finalpricecolor', models.CharField(default='0, 0, 0, 1', max_length=20, verbose_name='Culoare pret final')),
                ('reducerecolor', models.CharField(default='255, 26, 26, 1', max_length=20, verbose_name='Culoare reducere')),
                ('initialpretcolor', models.CharField(default='0, 0, 0, 1', max_length=20, verbose_name='Culoare pret initial')),
                ('starcolor', models.CharField(default='255, 255, 0, 1', max_length=20, verbose_name='Culoare stele rating')),
                ('showtitle', models.BooleanField(default=True, verbose_name='Afiseaza numele')),
                ('titlealign', models.CharField(choices=[('center', 'Centru'), ('end', 'Dreapta'), ('start', 'Stanga')], default='center', max_length=10, verbose_name='Alinierea titlului')),
                ('showprice', models.BooleanField(default=True, verbose_name='Afiseaza pret')),
                ('showdescription', models.BooleanField(default=True, verbose_name='Afiseaza descrierea')),
                ('showimage', models.BooleanField(default=True, verbose_name='Afiseaza imaginea produsului')),
                ('specificatii', models.CharField(default='marime gen', max_length=30, verbose_name='Specificatiile afisate')),
            ],
        ),
        migrations.CreateModel(
            name='FooterSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Art \xa0\xa0Traditional', max_length=30, verbose_name='Titlu')),
                ('titlefont', models.CharField(default='Alex Brush', max_length=40, verbose_name='Font')),
                ('fontmultiplier', models.IntegerField(default=200, verbose_name='Multiplicator font(%)')),
                ('fcolor', models.CharField(default='255, 255, 255, 1', max_length=20, verbose_name='Colare text')),
                ('bgcolor', models.CharField(default='33, 37, 41, 1', max_length=20, verbose_name='Culoare fundal')),
                ('credits', models.TextField(default='Drepturi de autor © 2022. Toate drepturile rezervate', max_length=200, verbose_name='Text footer')),
                ('imgsource', models.CharField(default='/media/BannerR.png', max_length=50, verbose_name='Imagine')),
            ],
        ),
        migrations.CreateModel(
            name='GalerieSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretmin', models.IntegerField(default=50, verbose_name='Pret minim')),
                ('pretmax', models.IntegerField(default=2000, verbose_name='Pret maxim')),
                ('pas', models.IntegerField(default=50, verbose_name='Pas')),
            ],
        ),
        migrations.CreateModel(
            name='NavbarSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Ie \xa0Romanească', max_length=50, verbose_name='Titlu')),
                ('titlefont', models.CharField(default='Alex Brush', max_length=40, verbose_name='Font')),
                ('fontmultiplier', models.IntegerField(default=200, verbose_name='Procent marime font titlu')),
                ('titlecolor', models.CharField(default='0, 0, 0, 1', max_length=20, verbose_name='Culoare titlu')),
                ('itemcolor', models.CharField(default='77, 77, 77, 0.8', max_length=20, verbose_name='Culoare iteme')),
                ('itemhovercolor', models.CharField(default='179, 179, 179, 0.9', max_length=20, verbose_name='Culoare iteme onhover')),
                ('color', models.CharField(default='127, 255, 212, 0.95', max_length=20, verbose_name='Culoare de fundal')),
                ('hidelogin', models.BooleanField(default=False, verbose_name='Ascunde Login-ul')),
            ],
        ),
        migrations.CreateModel(
            name='SlideShowSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgpath', models.CharField(default='SlideShow/', max_length=50, verbose_name='Folder-ul imaginilor din slideshow')),
                ('duration', models.IntegerField(default=10000, verbose_name='Numarul de milisecunde per imagine')),
                ('maxheight', models.IntegerField(default=500, verbose_name='Intaltimea maxima a slideshow-ului')),
                ('breakpoint', models.IntegerField(default=1000, verbose_name='Slideshow-ul opreste animatia la ecrane mai mici de(px)')),
            ],
        ),
        migrations.CreateModel(
            name='OwnSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showprice', models.BooleanField(default=True, verbose_name='Arata pret-ul')),
                ('allowrating', models.BooleanField(default=True, verbose_name='Permite rating')),
                ('title', models.CharField(default='Art Traditional', max_length=20, verbose_name='Titlul paginii')),
                ('productimagepath', models.CharField(default='Products/', max_length=20, verbose_name='Folder-ul unde se incarca imaginile produselor')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to='loginapp.cardsettings')),
                ('footer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='loginapp.footersettings')),
                ('galerie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='galerie', to='loginapp.galeriesettings')),
                ('navbar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='navbar', to='loginapp.navbarsettings')),
                ('slideshow', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='slideshow', to='loginapp.slideshowsettings')),
            ],
        ),
    ]
