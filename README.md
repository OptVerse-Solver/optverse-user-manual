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

## Licensing / 许可

公开文档 / Public documentation: [Apache 2.0](LICENSE). 第三方资源保留各自许可。 / Third-party assets retain their own licenses.

求解器与 SDK / Solver & SDKs: [EULA 中文](https://github.com/OptVerse-Solver/optverse-release/blob/main/licenses/3.8.1/optv-eula_cn.pdf) · [English](https://github.com/OptVerse-Solver/optverse-release/blob/main/licenses/3.8.1/optv-eula_en.pdf). 文档许可不适用于求解器、SDK 或 EULA。 / The documentation license excludes the solver, SDKs, and EULA.
