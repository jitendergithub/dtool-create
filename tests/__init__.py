"""Test fixtures."""

import os
import shutil
import tempfile

import pytest

_HERE = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(_HERE, "data")
SAMPLE_FILES_DIR = os.path.join(TEST_DATA_DIR, "sample_files")


@pytest.fixture
def chdir_fixture(request):
    d = tempfile.mkdtemp()
    curdir = os.getcwd()
    os.chdir(d)

    @request.addfinalizer
    def teardown():
        os.chdir(curdir)
        shutil.rmtree(d)


@pytest.fixture
def tmp_dir_fixture(request):
    d = tempfile.mkdtemp()

    @request.addfinalizer
    def teardown():
        shutil.rmtree(d)
    return d


@pytest.fixture
def local_tmp_dir_fixture(request):
    d = tempfile.mkdtemp(dir=_HERE)

    @request.addfinalizer
    def teardown():
        shutil.rmtree(d)
    return d
