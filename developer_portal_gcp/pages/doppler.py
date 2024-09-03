"""The doppler page."""
import reflex as rx
from developer_portal_gcp.templates import template
from developer_portal_gcp.components.doppler_components import ProjectState, project_button

@template(route="/doppler", title="Doppler")
def doppler() -> rx.Component:
    """The doppler page.

    Returns:
        The UI for the doppler page.
    """
    return rx.vstack(
        rx.heading("Doppler", size="8"),
        tabs(),
        rx.container(
            rx.text(
                "You can edit this page in ",
                rx.code("{your_app}/pages/doppler.py"),
            ),
        )
    )

def tabs():
    """The tabs for the page."""
    projects = ProjectState.projects
    return rx.hstack(
        rx.tabs.root(
            rx.tabs.list(
                rx.foreach(projects, tabs_trigger),
            ),
            rx.foreach(projects, tab_content),
        ),
    )

def tab_content(_project: dict) -> rx.Component:
    """The content for the tabs."""
    return rx.box(
        rx.tabs.content(
            rx.container(
                rx.box(
                    rx.text("Project Description: ",
                            weight="bold",
                            ),
                    rx.text(f'{_project["description"]}'),
                    spacing="2",
                    padding="8px",
                ),
                rx.box(
                    rx.text("Project ID: ",
                            weight="bold",
                            ),
                    rx.text(f'{_project["name"]}'),
                    spacing="2",
                    padding="8px",
                ),
                rx.box(
                    rx.text("Created At: ",
                            weight="bold",
                            ),
                    rx.text(f'{_project["created_at"]}'),
                    spacing="5",
                    padding="8px",
                ),
                rx.box(
                    rx.text("Updated At: ",
                            weight="bold",
                            ),
                    rx.text(f'{_project["updated_at"]}'),
                    spacing="2",
                    padding="8px",
                ),
            ),
            value=f'{_project["name"]}',
        ),
        margin="12px",
    )

def tabs_trigger(_project: dict) -> rx.Component:
    """The trigger for the tabs."""
    return rx.tabs.trigger(f'{_project["name"]}', value=f'{_project["name"]}')
