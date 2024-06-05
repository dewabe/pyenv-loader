import os
from dotenv import load_dotenv

def load_env_var(variable, value=None):
    """
    Load a specific environment variable.

    This function retrieves the value of the specified environment variable. If the environment variable is not set,
    it will return the provided default value if given, otherwise, it raises an EnvironmentError.

    Args:
        variable (str): The name of the environment variable.
        value (str, optional): The default value to return if the environment variable is not set. Defaults to None.

    Returns:
        str: The value of the environment variable, or the default value if the environment variable is not set.

    Raises:
        EnvironmentError: If the environment variable is not set and no default value is provided.
    """
    env_var = os.getenv(variable)

    # If the environment variable is not set, raise an exception
    if env_var is None and value is None:
        raise EnvironmentError(f'{variable} is not set')
    if env_var is None:
        return value
    
    return env_var

def load_env_vars(env='PYTHON_CONFIG_PATH'):
    """
    Load environment variables from a .env file specified by an environment variable.

    This function retrieves the path to the .env file from a given environment variable
    and loads the environment variables from the specified .env file. If the .env file
    cannot be loaded or any other error occurs, the function returns False and prints 
    the error message.

    Args:
        env (str): The name of the environment variable that contains the path to the .env file.
                   Defaults to 'PYTHON_CONFIG_PATH'.

    Returns:
        bool: True if the environment variables are loaded successfully, otherwise False.
    """
    try:
        # Get the path to the .env file from an environment variable
        env_path = load_env_var(env)

        # Load environment variables from .env file
        load_dotenv(dotenv_path=env_path)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

load_env_vars()
