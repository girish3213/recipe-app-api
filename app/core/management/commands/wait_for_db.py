
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available""" # noqa
    def handle(self, *args, **options):
        """Entrypoint for command"""  # noqa
        self.stdout.write('Waiting for database...')
        db_up = False # noqa
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True # noqa
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
        # noqa