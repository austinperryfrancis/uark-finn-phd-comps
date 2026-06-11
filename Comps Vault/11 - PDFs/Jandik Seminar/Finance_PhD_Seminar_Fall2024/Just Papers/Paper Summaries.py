import glob
from openai import OpenAI
import PyPDF2
import pandas as pd
import os

# === Configuration (hard-coded) ===
API_KEY = "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"
MODEL = "deepseek/deepseek-r1:free"
PDF_FOLDER = "C:/Users/apf006/Documents/Finance_PhD_Seminar_Fall2024/Just Papers"
TEXT_OUTPUT_FOLDER = "summaries_text"  # Folder to save individual .txt summaries
OUTPUT_CSV = "summaries.csv"
TESTING = False  # Set to False to process all PDFs
MAX_SUMMARY_TOKENS = 16384  # Adjust output length as needed
TEMPERATURE = 0.7
# Optional headers for OpenRouter ranking (uncomment to use)
EXTRA_HEADERS = {
    # "HTTP-Referer": "https://your-site.example",
    # "X-Title": "Your Site Name",
}

# === Initialize OpenRouter client ===
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts all text from a PDF file."""
    texts = []
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    texts.append(page_text)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return "\n".join(texts)


def summarize_text(text: str, filename: str = "<unknown>") -> str:
    """Sends the full text to OpenRouter and returns a summary, with error handling."""
    prompt = (
        "Please summarize the following finance research paper into one or two concise paragraphs, and after the paragraphs, include 3 bullet points of key takeaways including any key coefficients. Here is the text:\n\n"
        + text
    )
    try:
        response = client.chat.completions.create(
            extra_headers=EXTRA_HEADERS,
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=TEMPERATURE,
            max_tokens=MAX_SUMMARY_TOKENS,
        )
    except Exception as e:
        print(f"API call failed for {filename}: {e}")
        return ""

    # Validate response structure
    try:
        choice = response.choices[0]
        if choice and choice.message and choice.message.content:
            return choice.message.content.strip()
        else:
            print(f"No content returned for {filename}. Response: {response}")
            return ""
    except Exception as e:
        print(f"Unexpected response format for {filename}: {e} | Full response: {response}")
        return ""


def main():
    # Ensure text output directory exists
    os.makedirs(TEXT_OUTPUT_FOLDER, exist_ok=True)

    summaries = []
    pdf_paths = glob.glob(os.path.join(PDF_FOLDER, "*.pdf"))
    if TESTING and pdf_paths:
        print("Testing mode: processing only the first PDF.")
        pdf_paths = pdf_paths[:1]

    for pdf_file in pdf_paths:
        print(f"Processing {pdf_file}...")
        full_text = extract_text_from_pdf(pdf_file)
        if not full_text:
            print(f"  Warning: No text extracted from {pdf_file}")
            continue
        base_name = os.path.splitext(os.path.basename(pdf_file))[0]
        summary = summarize_text(full_text, filename=base_name)
        if not summary:
            print(f"  Skipping {pdf_file} due to empty summary.")
            continue
        # Save individual summary as .txt
        txt_path = os.path.join(TEXT_OUTPUT_FOLDER, f"{base_name}.txt")
        try:
            with open(txt_path, "w", encoding="utf-8") as txt_file:
                txt_file.write(summary)
        except Exception as e:
            print(f"Failed to write summary file for {base_name}: {e}")

        summaries.append({
            "filename": base_name,
            "summary": summary
        })

    # After all individual summaries, write combined CSV
    if summaries:
        df = pd.DataFrame(summaries)
        df.to_csv(OUTPUT_CSV, index=False)
        print(f"Summaries saved to {OUTPUT_CSV}")
    else:
        print("No summaries to save.")


if __name__ == "__main__":
    main()
