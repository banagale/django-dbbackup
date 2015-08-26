"""
S3 Storage object.
"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from .. import settings
from .base import StorageError
from .builtin_django import Storage as DjangoStorage

STORAGE_PATH = 'storages.backends.s3boto.S3BotoStorage'


class Storage(DjangoStorage):
    """Filesystem API Storage."""

    def __init__(self, server_name=None, **options):
        self.name = 'AmazonS3'
        self._check_filesystem_errors(options)
        super(Storage, self).__init__(storage_path=STORAGE_PATH,
                                      bucket=options['aws_storage_bucket_name'],
                                      **options)

    def _check_filesystem_errors(self, options):
        """Check we have all the required settings defined."""
        required_args = ('aws_storage_bucket_name', 'aws_s3_access_key_id',
                         'aws_s3_secret_access_key')
        err_msg = "%s storage requires settings.DBBACKUP_STORAGE_OPTIONS['%s'] to be define"
        for arg in required_args:
            if arg not in options:
                raise StorageError(err_msg % (self.name, arg))
