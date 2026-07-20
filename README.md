# OptVerse User Manual

This repository publishes the English and Simplified Chinese OptVerse 3.5.1
user manuals on Read the Docs.

## Documentation

- [English](https://optverse-user-manual.readthedocs.io/en/3.5.1/en/)
- [Simplified Chinese](https://optverse-user-manual.readthedocs.io/en/3.5.1/zh_cn/)

## Repository structure

- `build/html/`: prebuilt English and Simplified Chinese HTML documentation.
- `rtd/`: minimal Sphinx entry point used by Read the Docs.
- `.readthedocs.yaml`: Read the Docs build configuration.

## Local verification

The project uses [uv](https://docs.astral.sh/uv/) to manage its Python
environment:

```bash
uv run --with-requirements requirements.txt \
  sphinx-build -b html rtd build/ci-html -W --keep-going
```

Read the Docs automatically builds and publishes the documentation after a
push to the `main` branch.
