import sys, os, django
import superlist
import unittest

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "../superlist.settings")
    django.setup()
    unittest.main(warnings='ignore')
