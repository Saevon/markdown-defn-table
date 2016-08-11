#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from markdown import Extension
from markdown.preprocessors import Preprocessor
import re


class DefnTableExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        '''
        Adds the DefnTableExtension to Markdown
        '''
        md.registerExtension(self)
        md.preprocessors.add(
            'paired-list',
            DefnTablePreprocessor(md),
            "_end"
        )

class DefnTablePreprocessor(Preprocessor):
    OPEN_RE = re.compile(
        r'^~ Paired List',
        re.DOTALL,
    )

    DATA_RE = re.compile(
        r'^(?P<term>.*?):(?P<defn>.*)$',
        re.DOTALL,
    )

    CLOSE_RE = re.compile(
        r'^\s*$',
        re.DOTALL,
    )

    def __init__(self, md):
        super(DefnTablePreprocessor, self).__init__(md)

    def run(self, lines):
        is_open = False

        new_lines = []
        for line in lines:
            if is_open:
                match = DefnTablePreprocessor.CLOSE_RE.search(line)
                if match:
                    is_open = False
                    data = self.on_close(match, line)
                else:
                    match = DefnTablePreprocessor.DATA_RE.search(line)
                    if match:
                        data = self.on_data(match, line)
            else:
                # See if this opens a list
                match = DefnTablePreprocessor.OPEN_RE.search(line)
                if match:
                    is_open = True
                    data = self.on_open(match, line)
                else:
                    # If we didn't start a list, then use the original data
                    data = [line]

            # Add the resulting data to the document
            new_lines += data

        return new_lines

    def on_open(self, match, line):
        return ['<div markdown=1 class="paired-list">', ' | ', '-|-']

    def on_close(self, match, line):
        return ['</div>']

    def on_data(self, match, line):
        return [match.group('term') + ' | ' + match.group('defn')]


def makeExtension(configs=None):
    return DefnTableExtension(configs=configs)
