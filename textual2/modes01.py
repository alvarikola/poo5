from textual.app import App, ComposeResult
from textual.events import Mount
from textual.screen import Screen
from textual.widgets import Button, DataTable, Input
from textual.containers import Horizontal


ROWS = [
    ("ID", "Nombre"),
    (1, "Yoel"),
    (4, "Samuel"),
    (7, "Amaro"),
]


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Button("Edicion")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.switch_to_edit()

    def _on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])


class EditScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre")
        yield Horizontal(
                    Button("Aceptar"),
                    Button("Cancelar"),
            )
        yield Button("Principal")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.switch_to_main()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))


class ModesApp(App):
    BINDINGS = [
        ("m", "switch_mode('main')", "Principal"),  
        ("e", "switch_mode('edit')", "Edicion"),
    ]
    MODES = {
        "main": MainScreen,  
        "edit": EditScreen,
    }

    def on_mount(self) -> None:
        self.switch_mode("main")  


    def switch_to_edit(self):
        self.switch_mode("edit")


    def switch_to_main(self):
        self.switch_mode("main")


if __name__ == "__main__":
    app = ModesApp()
    app.run()



    