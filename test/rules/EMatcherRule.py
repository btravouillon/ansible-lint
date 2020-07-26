from typing import TYPE_CHECKING, Union

from ansiblelint.rules import AnsibleLintRule

if TYPE_CHECKING:
    from ansiblelint.file_utils import TargetFile


class EMatcherRule(AnsibleLintRule):
    id = 'TEST0001'
    description = 'This is a test rule that looks for lines ' + \
                  'containing the letter e'
    shortdesc = 'The letter "e" is present'
    tags = {'fake', 'dummy', 'test1'}

    def match(self, file: "TargetFile", line: str = "") -> Union[bool, str]:
        return "e" in line
