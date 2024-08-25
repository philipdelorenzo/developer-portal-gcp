"""The google GCP page."""

from developer_portal_gcp.templates import template

import reflex as rx


@template(route="/gcp", title="GCP")
def google_gcp() -> rx.Component:
    """The GCP page.

    Returns:
        The UI for the GCP page.
    """
    return rx.vstack(
        rx.heading("GCP", size="8"),
        rx.text("GCP API Data - Coming Soon!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/google_gcp.py"),
        ),
    )
