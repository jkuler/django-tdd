import sys, os, django
import importlib
import unittest
module_name = "superlist"
importlib.import_module(module_name, package='superlist')

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlist.settings")
    django.setup()
    unittest.main(warnings='ignore')
