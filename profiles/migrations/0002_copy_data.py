from django.db import migrations


def move_profiles(apps, *args, **kwargs):
    """
    Fonction qui permet de copier les données de l'ancienne table,
    dans les tables des appplications
    :param apps: Registre des applications installées pour retrouver des modèles.
    :type apps: Apps
    :param args: -
    :type args: -
    :param kwargs: -
    :type kwargs: -
    :return: -
    :rtype: None
    """
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    NewProfile = apps.get_model('profiles', 'Profile')

    objs = list()

    for old_object in OldProfile.objects.all():
        old_favorite_city = old_object.favorite_city
        old_user_id = old_object.user_id

        new_profile = NewProfile(
            favorite_city=old_favorite_city,
            user_id=old_user_id
        )
        objs.append(new_profile)

    NewProfile.objects.bulk_create(objs)


class Migration(migrations.Migration):
    """
    Class qui représente une migration et qui importe djangi db.

    Attributs:
        dependencies : Liste des opérations à effectuer depuis django.db.migrations.operations
        operations : Liste de tuples de (app_path, migration_name)

    """
    dependencies = [
        ('profiles', '0001_initial'),
        ('lettings', '0002_copy_data')
    ]

    operations = [
        migrations.RunPython(move_profiles, migrations.RunPython.noop),
    ]
