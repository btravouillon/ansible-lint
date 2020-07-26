# Copyright (c) 2016, Tsukinowa Inc. <info@tsukinowa.jp>
# Copyright (c) 2018, Ansible Project

import os
from typing import TYPE_CHECKING, List, Union

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.file_utils import TargetFile


class PlaybookExtension(AnsibleLintRule):
    id = '205'
    shortdesc = 'Use ".yml" or ".yaml" playbook extension'
    description = 'Playbooks should have the ".yml" or ".yaml" extension'
    severity = 'MEDIUM'
    tags = ['formatting']
    done: List[str] = []
    version_added = 'v4.0.0'

    def match(self, file: "TargetFile", line: str = "") -> Union[bool, str]:
        if file['type'] != 'playbook':
            return False

        path = file['path']
        ext = os.path.splitext(path)
        if ext[1] not in ['.yml', '.yaml'] and path not in self.done:
            self.done.append(path)
            return True
        return False
