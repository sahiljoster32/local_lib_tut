# Generated by Django 3.2.4 on 2021-07-24 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_librarian', 'Set user as librarian'), ('noooobie', 'boobie'))},
        ),
    ]