# Generated by Django 4.2.4 on 2023-08-22 20:21

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_nit', models.CharField(blank=True, max_length=15, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('company_short_name', models.CharField(blank=True, max_length=12, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Carpeta',
                'verbose_name_plural': 'Carpetas',
            },
        ),
        migrations.CreateModel(
            name='tEtapas_trans',
            fields=[
                ('id_etapa_trans', models.AutoField(primary_key=True, serialize=False)),
                ('etapa_name', models.CharField(blank=True, max_length=50, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
            },
        ),
        migrations.CreateModel(
            name='tJson_trans',
            fields=[
                ('idjson_trans', models.AutoField(primary_key=True, serialize=False)),
                ('json_trans', models.JSONField(blank=True, null=True)),
                ('json_url_trans', models.CharField(blank=True, max_length=100, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Json',
                'verbose_name_plural': "Json's",
            },
        ),
        migrations.CreateModel(
            name='tLanguage',
            fields=[
                ('Id_language', models.AutoField(primary_key=True, serialize=False)),
                ('description_language', models.CharField(blank=True, max_length=30, null=True)),
                ('short_description_language', models.CharField(blank=True, max_length=3, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.CreateModel(
            name='tPerson',
            fields=[
                ('id_person', models.AutoField(primary_key=True, serialize=False)),
                ('identity_person', models.CharField(blank=True, max_length=15, null=True)),
                ('first_name_person', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name_person', models.CharField(blank=True, max_length=30, null=True)),
                ('alias_person', models.CharField(blank=True, max_length=60, null=True)),
                ('description_person', models.CharField(blank=True, max_length=1024, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('Id_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.tlanguage')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='tRoles_trans',
            fields=[
                ('id_roles_trans', models.AutoField(primary_key=True, serialize=False)),
                ('rol_transcrip_name', models.CharField(blank=True, max_length=50, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='tType_identity',
            fields=[
                ('id_type_identity', models.AutoField(primary_key=True, serialize=False)),
                ('name_type_identity', models.CharField(blank=True, max_length=50, null=True)),
                ('short_name_type_identity', models.CharField(blank=True, max_length=50, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tipo de Identidad',
                'verbose_name_plural': 'Tipos de Identidades',
            },
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Usr_company',
            fields=[
                ('usr_company_id', models.AutoField(primary_key=True, serialize=False)),
                ('usr_mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario Autorizado',
                'verbose_name_plural': 'Usuario Autorizado',
            },
        ),
        migrations.CreateModel(
            name='tTranscript',
            fields=[
                ('id_transcript', models.AutoField(primary_key=True, serialize=False)),
                ('number_proces_transcript', models.CharField(blank=True, max_length=15, null=True)),
                ('name_transcript', models.CharField(blank=True, max_length=60, null=True)),
                ('date_transcript', models.DateTimeField(auto_now=True)),
                ('description_transcript', models.CharField(blank=True, max_length=1024, null=True)),
                ('s3_video_url', models.CharField(blank=True, max_length=100, null=True)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('id_etapa_trans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.tetapas_trans')),
                ('id_folder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.folder')),
                ('idjson_trans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.tjson_trans')),
            ],
            options={
                'verbose_name': 'Transcripción',
                'verbose_name_plural': 'Transcripciones',
            },
        ),
        migrations.CreateModel(
            name='tSpeakers_trans',
            fields=[
                ('id_spk_trans', models.AutoField(primary_key=True, serialize=False)),
                ('name_spk_trans', models.CharField(blank=True, max_length=50, null=True)),
                ('spks_timestamp_trans', django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(), null=True, size=None)),
                ('enable', models.BooleanField(default=False)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('id_person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.tperson')),
                ('id_roles_trans', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.troles_trans')),
                ('id_transcript', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.ttranscript')),
                ('uploaded_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transcripts', to='Aplicaciones.uploadedfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
            },
        ),
        migrations.AddField(
            model_name='tperson',
            name='id_type_identity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Aplicaciones.ttype_identity'),
        ),
    ]
