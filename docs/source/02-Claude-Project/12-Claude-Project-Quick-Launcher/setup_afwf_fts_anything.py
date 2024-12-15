# -*- coding: utf-8 -*-

from pathlib import Path
from learn_claude.setup_afwf_fts_anything import (
    setup_afwf_fts_anything_for_claude,
    setup_afwf_fts_anything_for_chatgpt,
)

path = Path(__file__).absolute().parent.joinpath("claude_project.html")
setup_afwf_fts_anything_for_claude(html=path.read_text())

path = Path(__file__).absolute().parent.joinpath("chatgpt_project.html")
setup_afwf_fts_anything_for_chatgpt(html=path.read_text())
