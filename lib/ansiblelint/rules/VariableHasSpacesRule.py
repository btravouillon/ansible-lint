# Copyright (c) 2016, Will Thames and contributors
# Copyright (c) 2018, Ansible Project
import re
from typing import TYPE_CHECKING, Union

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.file_utils import TargetFile


class VariableHasSpacesRule(AnsibleLintRule):
    id = '206'
    shortdesc = 'Variables should have spaces before and after: {{ var_name }}'
    description = 'Variables should have spaces before and after: ``{{ var_name }}``'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v4.0.0'

    variable_syntax = re.compile(r"{{.*}}")
    bracket_regex = re.compile(r"{{[^{' -]|[^ '}-]}}")

    def match(self, file: "TargetFile", line: str = "") -> Union[bool, str]:
        if not self.variable_syntax.search(line):
            return False
        line_exclude_json = re.sub(r"[^{]{'\w+': ?[^{]{.*?}}", "", line)
        return bool(self.bracket_regex.search(line_exclude_json))
