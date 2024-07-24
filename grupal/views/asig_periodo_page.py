import reflex as rx



class AsigPeriodoState(rx.State):
    pass

@rx.page(route="/asignatura_periodo", title="Asignatura Periodo")
def asig_periodo_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Asignatura Periodo", size="5", center=True, style={"align": "center"}),
        rx.button("Asignar Periodo", variant="outline"),
    )