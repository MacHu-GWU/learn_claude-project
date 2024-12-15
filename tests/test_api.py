# -*- coding: utf-8 -*-

from learn_claude import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_claude.tests import run_cov_test

    run_cov_test(__file__, "learn_claude.api", preview=False)
