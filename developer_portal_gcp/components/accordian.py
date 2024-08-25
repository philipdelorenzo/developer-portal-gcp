import reflex as rx

from developer_portal_gcp import styles

def accordian_header() -> rx.Component:
    """Accordian header.

    Returns:
        The accordian_header component.
    """
    return rx.hstack(
        # The logo.
        rx.color_mode_cond(
            rx.image(src="/reflex_black.svg", height="2em"),
            rx.image(src="/reflex_white.svg", height="2em"),
        ),
        rx.spacer(),
        rx.link(
            rx.button(
                rx.icon("github"),
                color_scheme="gray",
                variant="soft",
            ),
            href="https://github.com/philipdelorenzo/developer-portal-gcp",
            is_external=True,
        ),
        align="center",
        width="100%",
        border_bottom=styles.border,
        padding_x="1em",
        padding_y="2em",
    )

def accordian_footer() -> rx.Component:
    """Accordian footer.

    Returns:
        The accordian_footer component.
    """
    return rx.hstack(
        rx.spacer(),
        rx.link(
            rx.text("Docs"),
            href="https://reflex.dev/docs/getting-started/introduction/",
            color_scheme="gray",
        ),
        rx.link(
            rx.text("Blog"),
            href="https://reflex.dev/blog/",
            color_scheme="gray",
        ),
        width="100%",
        border_top=styles.border,
        padding="1em",
    )

rx.accordion.root(
    rx.accordion.item(
        header="First Item",
        content="The first accordion item's content",
    ),
    rx.accordion.item(
        header="Second Item",
        content="The second accordion item's content",
    ),
    rx.accordion.item(
        header="Third item",
        content="The third accordion item's content",
    ),
    width="300px",
)