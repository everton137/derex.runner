Manage Open edX projects
========================


.. image:: https://img.shields.io/azure-devops/tests/abstract-technology/derex/12/master?compact_message&style=for-the-badge
   :target: https://dev.azure.com/abstract-technology/derex/_build?definitionId=12&_a=summary&repositoryFilter=12&branchFilter=198
   :alt: Test results

.. image:: https://img.shields.io/azure-devops/coverage/abstract-technology/derex/12/master?style=for-the-badge
   :target: https://dev.azure.com/abstract-technology/derex/_build?definitionId=12&_a=summary&repositoryFilter=12&branchFilter=198
   :alt: Coverage results

Introduction
------------

Derex simplifies running Open edX: it takes care of starting the needed services
(mysql, mongodb, rabbitmq etc) and introduces the concept of Open edX *projects*.

A project is a directory that defines what an Open edX instance should look like.
It can specify additional requirements, custom themes and plugins.

``derex.runner`` uses docker compose (it's bundled, you don't have to
install it separately) to orchestrate the many necessary pieces.

It provides two commands, ``ddc-services`` to manage services (mysql, mongodb, elasticsearch etc)
and ``ddc-project`` to manage project-specific services (lms, cms, workers and maybe others if plugins are installed).

They are wrappers to ``docker-compose``: ddc stands for derex docker compose.
As such familiarity with docker compose is required to use derex.

Requirements
------------

Make sure you have python 3.6 or later and docker 19.03.5 or later installed.

A virtualenv is also recommended. For derex we use `direnv
<https://direnv.net/>`_. Its main purpose is to define directory-specific
environment variables, but it can also automatically activate a virtualenv when
you ``cd`` into a directory. We include a ``.envrc`` file that will instruct
``direnv`` to create and activate a local python3 virtualenv.

We recommend to `install it <https://direnv.net/docs/installation.html>`_ to try
out the following instructions. Alternatively you can replace ``direnv allow``
with your virtualenv activation command.


Quickstart
----------

Run the following commands:

.. code-block:: console

    git clone https://github.com/Abstract-Tech/derex.runner.git
    cd derex.runner
    direnv allow
    pip install -r requirements.txt -e .
    cd tests/fixtures/minimal/
    ddc-services up -d  # Start mysql, mongodb, rabbitmq and admin tools
    derex reset-mailslurper  # Prime the mailslurper mysql database
    derex reset-rabbitmq  # Create rabbitmq user and queue
    derex mysql reset  # Prime the mysql database
    derex create-bucket  # Create the S3-like buckets on Minio
    ddc-project up -d  # Start LMS/CMS daemons and workers

Run derex to see running services:

.. code-block:: console

    derex
    ...
    http://studio.minimal.localhost
    http://mailslurper.localhost  # (debug emails sent by the platform)
    http://minio.localhost
    http://adminer.localhost  # (mysql administration tool)
    http://flower.minimal.localhost  # (monitor celery workers)
    http://portainer.localhost  # (mysql administration tool)
    http://minimal.localhost


You can login to the CMS and LMS using one of these users (the password is
always ``secret``):

* Username: ``user``, email ``user@example.com``
  Represents a student user.
* Username: ``staff``, email ``staff@example.com``
  Represents a member of the teaching staff.
* Username: ``superuser``, email ``superuser@example.com``
  Represents an administrator of Open edX. This user
  has full permissions inside the platform.


Credits
-------

This work uses extensively parts of the `tutor <https://github.com/regisb/tutor>`_ project. Many thanks to Régis Behmo!

This package was created with `Cookiecutter
<https://github.com/audreyr/cookiecutter>`_ and the `cookiecutter-namespace-template
<https://github.com/veit/cookiecutter-namespace-template>`_ project template.
