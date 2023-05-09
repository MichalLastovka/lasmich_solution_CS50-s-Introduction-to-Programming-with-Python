"""
Task:

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.

"""


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(w=210, h=None, txt="CS50 Shirtificate", align="C")
        self.ln(80)
        self.image("shirtificate.png", 27, 80, 156)


def main():
    name = get_name()
    print(name)
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=25)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 75, f"{name}", align="C")
    pdf.output("shirtificate.pdf")

def get_name():
    name = input("Name: ")
    return f"{name} took CS50"


if __name__ == "__main__":
    main()
