import flet as ft
import flet.canvas as cv

class TextEditor(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.textfield = ft.TextField(multiline=True, autofocus=True,
                                   border=ft.InputBorder.NONE, min_lines=40,
                                   on_change=self.save_text, content_padding = 30,
                                   cursor_color="red")
    def save_text(self, e:ft.ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)

    def load(self):
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except:
            self.textfield.hint_text = "Start typing"

    def build(self):
        self.textfield.value = self.load()
        return self.textfield

def main(page):
    page.window.width = 1000
    page.window.height = 1000

    logo = cv.Canvas(
        [
            cv.Path(
                [
                    cv.Path.MoveTo(460, 460),
                    cv.Path.LineTo(460, 540),
                    cv.Path.LineTo(530, 600),
                ],
                paint=ft.Paint(
                    style=ft.PaintingStyle.FILL,
                ),
            ),
            cv.Path(
                [
                    cv.Path.MoveTo(480, 460),
                    cv.Path.LineTo(565, 540),
                    cv.Path.LineTo(550, 590),
                    cv.Path.Close(),
                ],
                paint=ft.Paint(
                    stroke_width=2,
                    style=ft.PaintingStyle.STROKE,
                ),
            ),
        ],
        width=float("inf"),
        expand=True,
    )


    page.title = "Edit text"
    page.scroll = True
    page.add(logo)
    page.overlay.append(TextEditor())
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="Assets")