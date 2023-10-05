#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['34.229.137.183', '18.204.15.18']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
