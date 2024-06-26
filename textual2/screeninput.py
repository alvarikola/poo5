from textual.app import App, ComposeResult
from textual.widgets import Input, Button
from textual.containers import Horizontal


class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")

        yield Horizontal(
                    Button("Aceptar"),
                    Button("Cancelar"),
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))


if __name__ == "__main__":
    app = InputApp()
    print(app.run())

