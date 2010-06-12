#!/usr/bin/env python
from migrate.versioning.shell import main

main(url='postgresql://devtest:test123@localhost/tinvent',repository='migrate_repo')
