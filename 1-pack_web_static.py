#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """define a do_pack function"""

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = "versions/web_static_{}.tgz".format(now)

    print("Packing web_static to {}".format(file_path))
    local("mkdir -p versions")
    local("tar -cvzf {} web_static".format(file_path))
