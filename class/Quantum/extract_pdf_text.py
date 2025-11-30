import sys
from pathlib import Path

def main():
    try:
        from PyPDF2 import PdfReader
    except Exception as e:
        print("PyPDF2 not installed:", e)
        sys.exit(1)

    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "quantum_with_intro&conclusion.pdf"
    out_path = pdf_path.with_suffix('.txt')

    reader = PdfReader(str(pdf_path))
    texts = []
    for i, page in enumerate(reader.pages):
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            texts.append("")
    content = "\n\n".join(texts)
    out_path.write_text(content, encoding='utf-8', errors='ignore')
    print(str(out_path))

if __name__ == "__main__":
    main()

