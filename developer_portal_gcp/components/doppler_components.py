"""The doppler page."""
import os
import pprint
from developer_portal_gcp.templates import template

import reflex as rx
from dopplersdk import DopplerSDK

DOPPLER_TOKEN = os.environ.get("DOPPLER_TOKEN")
doppler = DopplerSDK()  
doppler.set_access_token(DOPPLER_TOKEN)

class ProjectState(rx.State):
    project: list[dict] = vars(doppler.projects.list())["projects"]

def project(_project: dict) -> rx.Component:
    """The project component."""
    return rx.container(
        rx.dialog.root(
            rx.dialog.trigger(rx.button(f'{_project["name"]}')),
            rx.dialog.content(
                rx.dialog.title(f'Project Name: {_project["name"]}', size="4"),
                rx.dialog.description(f'{_project["description"]}'),
                rx.container(
                    rx.box(
                        rx.text("Project ID: ",
                                weight="bold",
                                ),
                        rx.text(f'{_project["name"]}'),
                        spacing="2",
                        padding="8px",
                    ),
                    #rx.spacer(direction="column", spacing="1"),
                    rx.box(
                        rx.text("Created At: ",
                                weight="bold",
                                ),
                        rx.text(f'{_project["created_at"]}'),
                        spacing="5",
                        padding="8px",
                    ),
                    #rx.spacer(direction="column", spacing="1"),
                    rx.box(
                        rx.text("Updated At: ",
                                weight="bold",
                                ),
                        rx.text(f'{_project["updated_at"]}'),
                        spacing="2",
                        padding="8px",
                    ),
                    #rx.spacer(direction="column", spacing="1"),
                ),
                rx.dialog.close(
                    rx.button("Close Project", size="3"),
                ),
            ),
        )
    )
