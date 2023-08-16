# Generated by Django 4.2.1 on 2023-08-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("program", "0010_alter_speaker_pretalx_code_alter_talk_pretalx_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talk",
            name="video_id",
            field=models.CharField(
                blank=True,
                default="",
                help_text="YouTube ID (from URL)",
                max_length=100,
            ),
        ),
    ]
