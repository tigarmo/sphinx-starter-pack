def setup(app):
    app.add_config_value(
        "disable_feedback_button", default=False, rebuild=True, types=bool
    )
    app.add_config_value("slug", default="", rebuild=True, types=str)

    extra_extensions = [
        "sphinx_design",
        "sphinx_tabs.tabs",
        "sphinx_reredirects",
        "youtube-links",
        "related-links",
        "custom-rst-roles",
        "terminal-output",
        "sphinx_copybutton",
        "sphinxext.opengraph",
        "myst_parser",
        "sphinxcontrib.jquery",
        "notfound.extension",
    ]
    for ext in extra_extensions:
        app.setup_extension(ext)
    app.connect("config-inited", config_inited)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def config_inited(app, config):
    app.config.myst_enable_extensions.update(["substitution", "deflist", "linkify"])

    app.config.exclude_patterns.extend(
        [
            "_build",
            "Thumbs.db",
            ".DS_Store",
            ".sphinx",
        ]
    )

    slug = app.config.slug
    if slug:
        app.config.notfound_urls_prefix = "/" + slug + "/en/latest/"

    app.config.html_theme = "canonical_sphinx_theme"
    app.config.html_last_updated_fmt = ""
    app.config.html_permalinks_icon = "¶"

    if app.config.html_title == "":
        app.config.html_theme_options = {"sidebar_hide_name": True}

    # data_path = Path(__file__).parent / "assets"
    # app.config.html_static_path = [str(data_path / "_static")]
    #
    # app.config.templates_path = [str(data_path / "_templates")]
    #
    # # Update with the local path to the favicon for your product
    # # (default is the circle of friends)
    # html_favicon = str(data_path / "_static/favicon.png")
    # if not app.config.html_favicon:
    #     app.config.html_favicon = html_favicon

    extra_css = [
        "custom.css",
        "header.css",
        "github_issue_links.css",
        "furo_colors.css",
    ]
    app.config.html_css_files.extend(extra_css)

    html_js_files = ["header-nav.js"]

    html_context = app.config.html_context
    disable_feedback_button = app.config.disable_feedback_button
    # disable_feedback_button = False

    if html_context.get("github_issues") and not disable_feedback_button:
        html_js_files.append("github_issue_links.js")

    app.config.html_js_files.extend(html_js_files)
