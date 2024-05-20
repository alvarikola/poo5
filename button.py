from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Footer
from textual.binding import Binding

class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"
    
    BINDINGS = [
        Binding(key="q", action="quit", description="Salir"),
    ]

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Button("Saludar", id="butSaludar"),
            ),
            VerticalScroll(
                Button.error("Salir",id="butSalir"),
            ),
        )
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "butSaludar":
            self.notify(
                "Desde aquí "
                "[b]Alvaro[/b] saluda al profe",
                title="Saludo",
                severity="warning",
            )
        else:
            self.exit(str(event.button))


    


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())