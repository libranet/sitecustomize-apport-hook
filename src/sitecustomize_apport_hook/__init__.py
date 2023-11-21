"""sitecustomize_apport_hook.__init__."""
__version__ = "1.0"
__copyright__ = "Copyright 2023 Libranet."
__license__ = "MIT License"


def entrypoint() -> None:
    """Install the apport exception handler if available."""

    try:
        import apport_python_hook  # pylint: disable=import-outside-toplevel
    except ImportError:
        pass
    else:
        apport_python_hook.install()
