# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import, print_function
import os
import yaml
import click
import logging.config
from infrad_ext.app import create_app
from infrad.endpoints.screenlock_plugin import SLockPlugin
from infrad.endpoints.emacsepc_plugin import SimpleEPCClient


def setup_logging(default_path='logging.yml',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration."""

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


@click.command()
def main():
    print('I am console_app_name')
    app = create_app()
    app.run(host='192.168.10.101')


if __name__ == "__main__":
    setup_logging()
    main()
