# Extract the human ensembl gene catalog to simple tables

## Development

```shell
# Install the environment
poetry install --no-root

# Update the lock file
poetry update

# Build the build to output
poetry run python ...

# Set up the git pre-commit hooks.
# `git commit` will now trigger automatic checks including linting.
pre-commit install

# Run all pre-commit checks (CI will also run this).
pre-commit run --all
```
