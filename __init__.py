"""
Search the Laravel Documentation
"""

from pathlib import Path

from albert import Action, Item, QueryHandler, openUrl, info, debug
import json
import os
import urllib.parse
import html
import re
from algoliasearch.search_client import SearchClient

md_iid = "0.5"
md_version = "0.4"
md_id = __name__
md_name = "Laravel Docs"
md_description = "Albert extension for quickly and easily searching the Laravel documentation"
# md_license = "BSD-2"
md_url = "https://github.com/use-the-fork/albert-laravel-docs/issues"
md_maintainers = "@use-the-fork"


client = SearchClient.create("E3MIRNPJH5", "1fa3a8fec06eb1858d6ca137211225c0")
index = client.init_index("laravel")

GOOGLE_ICON_PATH = "{}/google.svg".format(os.path.dirname(__file__))
ICON_PATH = "{}/icon.svg".format(os.path.dirname(__file__))

docs = "https://laravel.com/docs/"


class Plugin(QueryHandler):
    def id(self):
        return md_id

    def name(self):
        return md_name

    def description(self):
        return md_description

    def defaultTrigger(self):
        return "lv "

    def handleQuery(self, query):
            query.add(
                Item(
                    id=f'{md_name}/open_laravel_docs',
                    icon=[ICON_PATH],
                    text="Open Laravel Docs",
                    subtext="No match found. Open laravel.com/docs...",
                    actions=[
                        Action(
                            "Open",
                            'Open the Laravel Documentation',
                            lambda u=docs: openUrl(u)
                        )

                    ],
                )
            )

