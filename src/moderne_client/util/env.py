import os


def load_env_variables(*env_names: str) -> list[str]:
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
