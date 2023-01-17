#!/usr/bin/python3
# -*- coding:utf-8 -*-
# License: MIT License (see LICENSE or http://opensource.org/licenses/mit).

import pathlib
import logging


class CodeManager(object):
    """ """

    def __init__(self, logger="DefaultLogger"):
        """ """
        self.logger_name = logger
        self.logger = logging.getLogger(logger)
        self.clear()

    def clear(self):
        """ """
        self.code_rows = []
        self.fields = []
        self.values_by_field = {}
        self.row_by_key = {}

    def get_fields(self):
        """ """
        return self.fields

    def get_values_by_field(self, field):
        """ """
        return self.values_by_field.get(field, [])

    def get_rows_by_key(self, field, value):
        """ """
        key = field + "+" + value
        return self.row_by_key.get(key, {})

    def load_data(self, directory="", file_name="codes.txt"):
        """ """
        self.clear()
        codes_path = pathlib.Path(directory, file_name)
        with codes_path.open("r", encoding="cp1252", errors="ignore") as indata_file:
            header = None
            # Convert rows to dictionaries.
            for row in indata_file:
                row = [item.strip() for item in row.strip().split("\t")]
                if row:
                    if header is None:
                        header = row
                    else:
                        row_dict = dict(zip(header, row))
                        self.code_rows.append(row_dict)
        # Iterate over rows.
        for row_dict in self.code_rows:
            field = row_dict.get("field", "")
            value = row_dict.get("public_value", "")
            if field and value:
                # Fields.
                if field not in self.fields:
                    self.fields.append(field)
                # Values by field.
                if field not in self.values_by_field:
                    self.values_by_field[field] = []
                if value not in self.values_by_field[field]:
                    self.values_by_field[field].append(value)
                # Row by key.
                key = field + "+" + value
                if key not in self.row_by_key:
                    self.row_by_key[key] = row_dict

        print("DEBUG")
