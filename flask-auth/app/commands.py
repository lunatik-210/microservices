# -*- coding: utf-8 -*-
from app import db

from app.models import User

from flask.ext.script import Command

import os
import json

class CreateStaticData(Command):

    curent_folder = ""

    def __init__(self):
        self.curent_folder = os.path.dirname(os.path.abspath(__file__))

    def run(self):
        pass
