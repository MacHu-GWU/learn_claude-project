# -*- coding: utf-8 -*-

"""
https://docs.oracle.com/en/database/oracle/oracle-database/19/dbseg/administering-the-audit-trail.html
https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows
"""

import re
import dataclasses
from pathlib import Path

from markdownify import markdownify as md


def extract_markdown_title(text: str) -> str:
    """
    Convert markdown link to title only.
    """
    pattern = r"\[(.*?)\]\(.*?\)"
    return re.sub(pattern, r"\1", text)


dir_here = Path(__file__).absolute().parent
dir_html = dir_here.joinpath("html")
dir_md = dir_here.joinpath("md")
dir_md.mkdir(exist_ok=True, parents=True)
for path_html in dir_html.iterdir():
    if path_html.suffix != ".html":
        continue
    html = path_html.read_text()
    # Ref: https://github.com/matthewwithanm/python-markdownify
    text = md(
        html,
        heading_style="ATX",
        escape_underscores=False,
    )
    text = text.strip()
    # text = extract_markdown_title(text)  # convert markdown link to title only
    for _ in range(10):
        text = text.replace("\n\n\n", "\n\n")
    path_md = dir_md.joinpath(path_html.stem + ".md")
    path_md.write_text(text)
