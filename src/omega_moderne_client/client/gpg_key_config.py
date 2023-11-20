import os
import gnupg
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GpgKeyConfig:
    key_passphrase: str
    key_private_key: str
    key_public_key: str

    @classmethod
    def load_from_env(cls) -> 'GpgKeyConfig':
        env_vars = cls._load_env_variables(
            "GPG_KEY_PASSPHRASE",
            "GPG_KEY_PRIVATE_KEY",
            "GPG_KEY_PUBLIC_KEY"
        )
        return cls(
            key_passphrase=env_vars[0],
            key_private_key=env_vars[1],
            key_public_key=env_vars[2]
        )

    @staticmethod
    def _load_env_variables(*env_names: str) -> List[str]:
        missing_env_var_names = []
        present_env_vars = []
        for env_name in env_names:
            value = os.getenv(env_name)
            if not value:
                missing_env_var_names.append(env_name)
            else:
                present_env_vars.append(value)

        if missing_env_var_names:
            raise ValueError(f"Environment variables {missing_env_var_names} are not set")
        return present_env_vars

    @classmethod
    def load_from_gnugpg(cls, keyid: str, passphrase: str) -> 'GpgKeyConfig':
        gpg = gnupg.GPG()
        ascii_armored_public_keys = gpg.export_keys(keyid)
        ascii_armored_private_keys = gpg.export_keys(keyid, secret=True, passphrase=passphrase)
        return cls(
            key_passphrase=passphrase,
            key_private_key=ascii_armored_private_keys,
            key_public_key=ascii_armored_public_keys
        )

    @classmethod
    def load_from_gnugpg_env(cls) -> 'GpgKeyConfig':
        env_vars = cls._load_env_variables(
            "GPG_KEY_ID",
            "GPG_KEY_PASSPHRASE"
        )
        return cls.load_from_gnugpg(
            keyid=env_vars[0],
            passphrase=env_vars[1]
        )
