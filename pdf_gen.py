from fpdf import FPDF

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)

    pdf.set_font("Arial", size=12)

    clean_text = text.encode("latin-1", "replace").decode("latin-1")

    for line in clean_text.split("\n"):

        if "Name:" in line or "Skills:" in line or "Projects:" in line or "Education:" in line or "Key Strengths:" in line:
            pdf.set_font("Arial", style='B', size=13)
        else:
            pdf.set_font("Arial", size=11)

        pdf.multi_cell(0, 8, line)

    file_path = "result.pdf"
    pdf.output(file_path)

    return file_path