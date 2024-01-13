from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page(orientation="portrait", format="a4")
        self._pdf.set_font("helvetica", "U", 45)
        self._pdf.cell(0, 50, "CS50 Shirtificate", align="C")
        self._pdf.image("shirtificate.png",10,70,190)
        self._pdf.set_font("helvetica", "B", 35)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=52.5, y=140, txt=f"{name} took CS50")
        self._pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ")
    PDF(name)



if __name__ == "__main__":
    main()
