from django.db import migrations


def populate_character_class_levels(apps, schema_editor):
    """Port each Character's dnd_class and level into a new CharacterClassLevel row."""
    Character = apps.get_model("adventurerscodexapi", "Character")
    CharacterClassLevel = apps.get_model("adventurerscodexapi", "CharacterClassLevel")

    for character in Character.objects.all():
        CharacterClassLevel.objects.create(
            character=character,
            dnd_class=character.dnd_class,
            level=character.level,
            subclass="",
        )


def reverse_populate(apps, schema_editor):
    """Remove all CharacterClassLevel rows."""
    CharacterClassLevel = apps.get_model("adventurerscodexapi", "CharacterClassLevel")
    CharacterClassLevel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("adventurerscodexapi", "0005_characterclasslevel"),
    ]

    operations = [
        migrations.RunPython(populate_character_class_levels, reverse_populate),
    ]
