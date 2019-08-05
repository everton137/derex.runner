#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `derex.runner` package."""

from itertools import repeat
from types import SimpleNamespace
from click.testing import CliRunner
import contextlib
import sys
import pytest
import io
import os
from contextlib import redirect_stdout
import shutil


runner = CliRunner()


def test_ddc(sys_argv):
    """Test the derex docker compose shortcut."""
    from derex.runner.cli import ddc

    os.environ["DEREX_ADMIN_SERVICES"] = "False"
    result = runner.invoke(ddc, ["config"])
    assert "mongodb" in result.output
    assert "adminer" not in result.output

    os.environ["DEREX_ADMIN_SERVICES"] = "True"
    result = runner.invoke(ddc, ["config"])
    assert "adminer" in result.output


def test_ddc_ironwood(sys_argv, mocker):
    """Test the open edx ironwood docker compose shortcut."""
    from derex.runner.cli import ddc_ironwood

    # It should check for services to be up before trying to do anything
    check_services = mocker.patch("derex.runner.cli.check_services")

    check_services.return_value = False
    result = runner.invoke(ddc_ironwood, ["config"])
    assert "ddc up -d" in result.output

    check_services.return_value = True
    result = runner.invoke(ddc_ironwood, ["config"])
    assert "cms_worker" in result.output


def test_ddc_ironwood_reset_mysql(sys_argv, mocker):
    """Test the open edx ironwood docker compose shortcut."""
    from derex.runner.cli import ddc_ironwood

    mocker.patch("derex.runner.cli.check_services", return_value=True)
    client = mocker.patch("derex.runner.docker.client")
    client.containers.get.return_value.exec_run.side_effect = [
        SimpleNamespace(exit_code=-1)
    ] + list(repeat(SimpleNamespace(exit_code=0), 10))

    result = runner.invoke(ddc_ironwood, ["--reset-mysql"])
    assert result.exit_code == 0


@pytest.fixture
def sys_argv(mocker):
    @contextlib.contextmanager
    def my_cm(eargs):
        with mocker.mock_module.patch.object(sys, "argv", eargs):
            try:
                yield
            except SystemExit as exc:
                if exc.code != 0:
                    raise

    return my_cm
