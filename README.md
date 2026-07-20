# OptVerse User Manual

OptVerse 3.5.1 中英文用户手册的 Read the Docs 发布仓库。

## 在线文档

- [English](https://optverse-user-manual.readthedocs.io/en/3.5.1/en/)
- [简体中文](https://optverse-user-manual.readthedocs.io/en/3.5.1/zh_cn/)

## 仓库结构

- `build/html/`：用于发布的中英文预构建 HTML 文档。
- `rtd/`：Read the Docs 使用的最小 Sphinx 入口。
- `.readthedocs.yaml`：Read the Docs 构建配置。

## 本地验证

项目使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境：

```bash
uv run --with-requirements requirements.txt \
  sphinx-build -b html rtd build/ci-html -W --keep-going
```

向 `main` 分支推送后，Read the Docs 会自动构建并发布文档。
