"""The doppler page."""
import reflex as rx
from developer_portal_gcp.templates import template
from developer_portal_gcp.components.doppler_components import ProjectState, project

@template(route="/doppler", title="Doppler")
def doppler() -> rx.Component:
    """The doppler page.

    Returns:
        The UI for the doppler page.
    """
    return rx.vstack(
        rx.heading("Doppler", size="8"),
        rx.foreach(ProjectState.project, project),
        #rx.text(f"Doppler Token: {DOPPLER_TOKEN}"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/doppler.py"),
        ),
    )
