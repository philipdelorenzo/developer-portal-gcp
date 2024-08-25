"""The doppler page."""

from developer_portal_gcp.templates import template

import reflex as rx


@template(route="/github", title="Github")
def github() -> rx.Component:
    """The github page.

    Returns:
        The UI for the github page.
    """
    return rx.vstack(
        rx.heading("Github", size="8"),
        rx.text("Github API Data - Coming Soon!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/github.py"),
        ),
    )
