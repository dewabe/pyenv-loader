
# pyenv-loader

A package to load environment variables from a .env file specified by an environment variable.

## Installation

To install the package, use pip:

```bash
pip install git+https://github.com/dewabe/pyenv-loader.git
```

## Usage

This package provides functions to load environment variables from a .env file. The path to the .env file is specified by an environment variable.

### Functions

#### `load_env_var(variable)`

Load a specific environment variable.

**Args:**
- `variable` (str): The name of the environment variable.

**Returns:**
- `str`: The value of the environment variable.

**Raises:**
- `EnvironmentError`: If the environment variable is not set.

**Example:**

```python
from pyenv_loader import load_env_var

# Retrieve the value of an environment variable
value = load_env_var('MY_VARIABLE')
print(value)
```

#### `load_env_vars(env='PYTHON_CONFIG_PATH')`

Load environment variables from a .env file specified by an environment variable.

**Args:**
- `env` (str): The name of the environment variable that contains the path to the .env file. Defaults to 'PYTHON_CONFIG_PATH'.

**Returns:**
- `bool`: True if the environment variables are loaded successfully, otherwise False.

**Example:**

```python
from pyenv_loader import load_env_vars

# Load environment variables from the .env file
success = load_env_vars()
if success:
    print("Environment variables loaded successfully.")
else:
    print("Failed to load environment variables.")
```

## Example .env File

Create a `.env` file with the following format:

```dotenv
# .env
MY_VARIABLE=value
ANOTHER_VARIABLE=another_value
```

Set the `PYTHON_CONFIG_PATH` environment variable to the path of your `.env` file:

```bash
export PYTHON_CONFIG_PATH=/path/to/your/.env
```

Then, run your Python script to load the environment variables:

```python
from pyenv_loader import load_env_vars

load_env_vars()
```

## License

This project is licensed under the MIT License.

## Updates

### 0.1.1

We have updated the `load_env_var` function to include an optional default value parameter. Now, if the specified environment variable is not set, you can provide a default value that will be returned instead of raising an error. This allows for more flexibility and control in situations where certain environment variables might not be available.

Here is an example of how to use the updated `load_env_var` function:

```python
database_url = load_env_var('DATABASE_URL', 'sqlite:///default.db')
```

In this example, if DATABASE_URL is not set in your environment variables, the function will return 'sqlite:///default.db' as the default value, allowing your application to continue running with a fallback option.