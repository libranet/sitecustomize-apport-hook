# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module sitecustomize_apport_hook."""


def test_entrypoint(capsys) -> None:
    import sitecustomize_apport_hook

    # Call the entrypoint function
    sitecustomize_apport_hook.entrypoint()

    # Capture the standard output
    captured = capsys.readouterr()

    # Check if the captured output matches the expected message
    # assert captured.out.strip() == "Hello!"

