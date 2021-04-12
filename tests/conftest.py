# import pytest
#
#
# @pytest.fixture
# def app():
#     yield app
#
#
# @pytest.fixture
# def client(app):
#     return app.test_client()

import inspect
import os
import sys

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pytest
import app as flask_app


@pytest.fixture
def app():
    app = flask_app.app
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
