# Generated by Django 5.1.4 on 2025-04-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cachorro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
                (
                    "sexo",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Fêmea", "Fêmea")], max_length=20
                    ),
                ),
                ("raca", models.CharField(max_length=100)),
                ("descricao", models.TextField()),
                ("imagem", models.ImageField(upload_to="cachorros/")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Disponível", "Disponível"),
                            ("Adotado", "Adotado"),
                            ("Em processo", "Em processo"),
                        ],
                        default="Disponível",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
