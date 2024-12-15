# -*- coding: utf-8 -*-

import typing as T
import json
import shutil
from pathlib import Path

from bs4 import BeautifulSoup

from .paths import path_claude_icon


def parse_claude_project_html(html: str) -> T.List[T.Tuple[str, str, str]]:
    """
    解析 Claude Project 的 HTML 页面, 返回项目的名称, 描述和 URL.
    """
    projects = list()
    soup = BeautifulSoup(html, features="html.parser")
    for a in soup.find_all("a"):
        href = a.attrs["href"]
        if href.startswith("/project/"):
            url = f"https://claude.ai{href}"
            span = a.find("span")
            name = span.text
            div = a.find("div", class_="text-text-300")
            description = div.text
            print(f"---------- {name}")
            print(description[:120])
            projects.append((name, description, url))
    return projects


def setup_afwf_fts_anything(html: str):
    """
    将 Claude Project 的索引数据写入到 ``$HOME/.alfred-afwf/afwf_fts_anything``
    目录并刷新缓存, 使得可以直接用
    `afwf_fts_anything <https://github.com/MacHu-GWU/afwf_fts_anything-project>`_
    立刻进行搜索.
    """
    projects = parse_claude_project_html(html)
    fts_data = [
        {
            "name": name,
            "description": desc,
            "url": url,
        }
        for name, desc, url in projects
    ]
    fts_settings = {
        "fields": [
            {
                "name": "name",
                "type_is_store": True,
                "type_is_ngram_words": True,
                "ngram_maxsize": 10,
                "ngram_minsize": 2,
                "weight": 5.0,
            },
            {
                "name": "description",
                "type_is_store": True,
                "type_is_phrase": True,
                "weight": 1.0,
            },
            {
                "name": "url",
                "type_is_store": True,
            },
        ],
        "title_field": "{name}",
        "subtitle_field": "{description}",
        "arg_field": "{url}",
        "autocomplete_field": "{name}",
        "icon_field": path_claude_icon.name,
    }
    dir_afwf_fts = Path.home().joinpath(".alfred-afwf", "afwf_fts_anything")

    keyword = "clp"
    # write clp-data.json
    path_data = dir_afwf_fts.joinpath(f"{keyword}-data.json")
    path_data.write_text(json.dumps(fts_data))
    # write clp-setting.json
    path_settings = dir_afwf_fts.joinpath(f"{keyword}-setting.json")
    path_settings.write_text(json.dumps(fts_settings))
    # create claude-icon.json
    dir_icon = dir_afwf_fts.joinpath(f"{keyword}-icon")
    dir_icon.mkdir(parents=True, exist_ok=True)
    path_icon = dir_icon.joinpath(path_claude_icon.name)
    path_icon.write_bytes(path_claude_icon.read_bytes())
    # reset index and cache
    dir_index = dir_afwf_fts.joinpath(f"{keyword}-whoosh_index")
    shutil.rmtree(dir_index, ignore_errors=True)
    dir_cache = dir_afwf_fts.joinpath(".cache")
    shutil.rmtree(dir_cache, ignore_errors=True)
