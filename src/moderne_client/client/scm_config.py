from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml

from moderne_client.util.env import load_env_variables


@dataclass(frozen=True)
class ScmConfig:
    type: str
    value: str

    @classmethod
    def load(cls):
        git_hub_from_file = cls.load_from_github_hub()
        if git_hub_from_file:
            return git_hub_from_file
        return cls.load_from_env()

    @classmethod
    def load_from_env(cls) -> 'ScmConfig':
        scm_variables = load_env_variables(
            "SCM_TYPE",
            "SCM_VALUE"
        )
        return cls(
            type=scm_variables[0],
            value=scm_variables[1]
        )

    @classmethod
    def load_from_github_hub(cls) -> Optional['ScmConfig']:
        hub_path = Path.home().joinpath('.config/hub')
        if hub_path.exists():
            with open(hub_path) as hub_file:
                hub_config = yaml.safe_load(hub_file)
            return cls(
                type="GITHUB",
                value=hub_config['github.com'][0]['oauth_token']
            )
        else:
            return None

