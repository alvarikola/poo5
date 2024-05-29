from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder, Button
from textual.containers import Horizontal, VerticalScroll



class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Pantalla Principal")
        yield Button("Edicion")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.switch_to_edit()


class EditScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Pantalla Edicion")
        yield Button("Principal")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.switch_to_main()


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
    print(app.run())



    