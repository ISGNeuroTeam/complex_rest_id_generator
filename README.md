# complex_rest_id_generator

Plugin for [complex rest](https://github.com/ISGNeuroTeam/complex_rest/tree/develop)
that generates various types of ids (autoincrement, uuid, Snowflake).

### Limitations

Can create **no more** than 100 IDs per request.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Deploy [complex rest](https://github.com/ISGNeuroTeam/complex_rest/tree/develop).

### Installing

* Make symlink for `id_generator/id_generator` in plugins directory
* Run `create_db.sh` if you want to use database-dependent IDs such as sequence.
* You can configure your own database but don't forget to add it into `id_generator.conf`.
* Run complex rest server.

## Running the tests
Run all tests:
```bash
python complex_rest/manage.py test \
    plugin_dev/id_generator/tests \
    --settings=core.settings.test
```

## Deployment

* Make plugin archive:
    ```bash
    make pack
    ```
* Unpack archive into `complex_rest/plugins` directory.

## Built With

* [Django](https://docs.djangoproject.com/en/3.2/) - The web framework used.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ISGNeuroTeam/complex_rest_id_generator/tags). 

## Authors

- Ilia Sagaidak (isagaidak@isgneuro.com)

## License

[OT.PLATFORM. License agreement.](LICENSE.md)