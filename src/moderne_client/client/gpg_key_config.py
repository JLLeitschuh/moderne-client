import os
from dataclasses import dataclass

import gnupg

from moderne_client.util.env import load_env_variables


@dataclass(frozen=True)
class GpgKeyConfig:
    key_passphrase: str
    key_private_key: str
    key_public_key: str

    @classmethod
    def load(cls):
        if "GPG_KEY_ID" in os.environ:
            return cls.load_from_gnugpg_env()
        return cls.load_from_env()

    @classmethod
    def load_from_env(cls) -> 'GpgKeyConfig':
        env_vars = load_env_variables(
            "GPG_KEY_PASSPHRASE",
            "GPG_KEY_PRIVATE_KEY",
            "GPG_KEY_PUBLIC_KEY"
        )
        return cls(
            key_passphrase=env_vars[0],
            key_private_key=env_vars[1],
            key_public_key=env_vars[2]
        )

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
        env_vars = load_env_variables(
            "GPG_KEY_ID",
            "GPG_KEY_PASSPHRASE"
        )
        return cls.load_from_gnugpg(
            keyid=env_vars[0],
            passphrase=env_vars[1]
        )
