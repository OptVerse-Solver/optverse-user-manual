from pathlib import Path
import shutil


project = "OptVerse Reference Manual"
author = "Huawei OptVerse Team"
release = "3.5.1"

extensions = []
exclude_patterns = []
html_theme = "basic"
html_show_sphinx = False
html_show_sourcelink = False


def publish_prebuilt_docs(app, exception):
    """Publish the complete, versioned HTML manual stored in the repository."""
    if exception is not None or app.builder.name != "html":
        return

    repository_root = Path(__file__).resolve().parents[1]
    prebuilt_html = repository_root / "build" / "html"
    output_dir = Path(app.outdir).resolve()

    if not (prebuilt_html / "index.html").is_file():
        raise RuntimeError(f"Prebuilt documentation is missing: {prebuilt_html}")

    shutil.copytree(prebuilt_html, output_dir, dirs_exist_ok=True)


def setup(app):
    app.connect("build-finished", publish_prebuilt_docs)

