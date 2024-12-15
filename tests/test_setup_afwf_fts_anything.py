# -*- coding: utf-8 -*-

from pathlib import Path

from learn_claude.setup_afwf_fts_anything import (
    parse_claude_project_html,
    parse_chatgpt_project_html,
)

dir_here = Path(__file__).absolute().parent


def test_parse_claude_project_html():
    html = dir_here.joinpath("claude_project.html").read_text()
    parse_claude_project_html(html)


def test_parse_chatgpt_project_html():
    html = dir_here.joinpath("chatgpt_project.html").read_text()
    parse_chatgpt_project_html(html)


if __name__ == "__main__":
    from learn_claude.tests import run_cov_test

    run_cov_test(
        __file__,
        "learn_claude.setup_afwf_fts_anything",
        preview=False,
    )
