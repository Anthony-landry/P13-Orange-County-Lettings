Déployer et gérer
=================

Il est toujours recommandé d'utiliser les commandes docker-compose car elles
sont plus concis et ils ont tous les environnements et variables nécessaires
configurés.

Exécuter l'application
----------------------

docker-compose
``````````````

#. exécutez le serveur et exposez-le sur le port 3050 sur l'hôte

   .. code:: shell

      docker-compose up --remove-orphans web

#. pour vérifier si l'application fonctionne

   .. code:: shell

      curl https://127.0.0.1:3050

#. pour arrêter l'application, vous pouvez ouvrir un autre shell dans le même
   shell et exécuter

   .. code:: shell

      docker-compose down web

   ou utilisez ``CTRL+^C`` suivi de l'ancienne commande. Si vous ne supprimez
   pas le service, le port restera occupé.

.. important:: La commande pour docker-compose V2 est ``docker compose``, sans
               un trait d'union, et non ``docker-compose``! Vérifiez la
               version.

Manuellement
````````````

#. construire l'image Docker

   .. code:: shell

      docker build --env-file=.env --tag lettings .

#. exécutez le serveur et exposez-le sur le port 3050 sur l'hôte

   .. code:: shell

      docker run -p 3050:8000 --env-file=.env \
        --volume=$(pwd)/profiles/migrations:/oc_p13_lettings/profiles/migrations \
        --volume=$(pwd)/db:/oc_p13_lettings/db \
        lettings 

#. pour vérifier si l'application fonctionne

   .. code:: shell

      curl https://127.0.0.1:3050

   ou utilisez un navigateur Web

#. utilisez ``CTRL+^C`` pour arrêter

Accéder au shell
----------------

Pour effectuer certaines tâches administratives, vous devez accéder au shell
du Docker container.

docker-compose
``````````````

#. exécutez cette commande

   .. code:: shell

      docker-compose run web sh

#. utilisez ``CTRL+^D`` pour quitter
#. arrêter

   .. code:: shell

      docker-compose down

Manuellement
````````````

#. exécutez cette commande

   .. code:: shell

      docker run -ti -p 3050:8000 --env-file=.env \
        --volume=$(pwd)/profiles/migrations:/oc_p13_lettings/profiles/migrations \
        --volume=$(pwd)/db:/oc_p13_lettings/db \
        lettings \
        /bin/sh

#. utilisez ``CTRL+^D`` pour quitter

Mise à jour de la base de données
---------------------------------

Après avoir modifié les modèles d'application, la base de données doit être
mise à jour. Cette étape est appelé migration. Soyez conscient que des
problèmes peuvent survenir en cas de conflits avec d'autres migrations ou de
problèmes avec vos définitions de modèle.

docker-compose
``````````````

#. cette commande génère les fichiers de migration et les applique

   .. code:: shell

      docker-compose up migrate

#. arrêter

   .. code:: shell

      docker-compose down

Manuellement
````````````

#. ouvrez un shell dans le container Docker. Voir les sections précédentes
#. générer les fichiers de migration

   .. code:: shell

      python manage.py makemigrations

#. faire la migration

   .. code:: shell

      python manage.py migrate

#. quittez le shell avec ``CTRL+^C``

Changer les mots de passe des utilisateurs
------------------------------------------

Pour changer le mot de passe d'un utilisateur, procédez comme suit:

#. accéder à un shell dans le container Docker. Voir les sections précédentes
#. exécutez cette commande

   .. code:: shell

      python manage.py changer le mot de passe ${user}

   remplacez ``${user}`` par le nom d'utilisateur que vous souhaitez modifier
#. quittez le shell. Voir les sections précédentes

Construire cette documentation
------------------------------

docker-compose
``````````````

#. cette commande construit cette documentation HTML dans l'annuaire
   ``./docs/_build/html``

   .. code:: shell

      docker-compose up docs

.. important:: Pour régénérer la documentation de l'API, vous devez reconstruire le
               Image Docker! Cela se produit parce que le code est copié dans le
               phase de construction de l'image et il n'est pas monté côme une
               volume.

Manuellement
````````````

#. ouvrez un shell dans le container Docker. Vous devez monter le volume
   ``docs`` aussi.

   .. code:: shell

      docker run --env-file=.env \
        --volume=$(pwd)/docs:/oc_p13_lettings/docs \
        -ti lettings /bin/sh

#. construire la documentation

   .. code:: shell

      sphinx-build -b html docs /oc_p13_lettings/docs/_build/html

#. quittez le shell avec ``CTRL+^C``
