from django.db import migrations


def copy_lettings(apps, schema_editor):
    """
    Fonction qui permet de copier les données de l'ancienne table,
    dans les tables des appplications
    nouvellement crées.
    :param apps: Registre des applications installées pour retrouver des modèles.
    :type apps: Apps
    :param schema_editor: -
    :type schema_editor: -
    :return: -
    :rtype: None
    """
    SiteLetting = apps.get_model('oc_lettings_site', 'Letting')
    AppLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')

    objs = list()

    fields = (
        'number',
        'street',
        'city',
        'state',
        'zip_code',
        'country_iso_code'
    )

    for old_object in SiteLetting.objects.all():
        title = old_object.title
        old_address = old_object.address

        dict_fields = {k: getattr(old_address, k, None) for k in fields}
        address, created = NewAddress.objects.get_or_create(**dict_fields)

        new_letting = AppLetting(title=title, address=address)
        objs.append(new_letting)

    AppLetting.objects.bulk_create(objs)


class Migration(migrations.Migration):
    """
    Class qui représente une migration et qui importe djangi db.

    Attributs:
        dependencies : Liste des opérations à effectuer depuis django.db.migrations.operations
        operations : Liste de tuples de (app_path, migration_name)
    """
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_lettings, migrations.RunPython.noop),
    ]
