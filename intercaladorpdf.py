import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

st.title("Intercalar páginas de dos PDFs")

pdf1_file = st.file_uploader("📄 Sube el PDF 1", type="pdf")
pdf2_file = st.file_uploader("📄 Sube el PDF 2 (se invertirá)", type="pdf")

if pdf1_file and pdf2_file:
    if st.button("🔁 Intercalar PDFs"):
        pdf1 = PdfReader(pdf1_file)
        pdf2_pages = list(PdfReader(pdf2_file).pages)
        pdf2_pages.reverse()

        output = PdfWriter()
        max_pages = max(len(pdf1.pages), len(pdf2_pages))

        for i in range(max_pages):
            if i < len(pdf1.pages):
                output.add_page(pdf1.pages[i])
            if i < len(pdf2_pages):
                output.add_page(pdf2_pages[i])

        result = BytesIO()
        output.write(result)
        result.seek(0)

        st.success("✅ ¡PDF intercalado con éxito!")
        st.download_button(
            label="📥 Descargar PDF intercalado",
            data=result,
            file_name="intercalado.pdf",
            mime="application/pdf"
        )
