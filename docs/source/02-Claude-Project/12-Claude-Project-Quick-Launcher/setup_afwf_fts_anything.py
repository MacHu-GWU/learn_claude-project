# -*- coding: utf-8 -*-

from pathlib import Path
from learn_claude.setup_afwf_fts_anything import setup_afwf_fts_anything

path = Path(__file__).absolute().parent.joinpath("claude_project.html")
setup_afwf_fts_anything(html=path.read_text())
