import streamlit as st
import pandas as pd
from text_processing import get_sentences
from plagiarism_decetor import get_similarity, compute_similarities
from file_handling import extract_text_from_file
from web_scraper import get_url, get_text_from_url

st.set_page_config(page_title='Plagiarism Detector')
st.title('Plagiarism Detector')

st.sidebar.image("data:image/png;base64,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", width=150)



st.write("""
### Upload files or enter text to check for plagiarism.
""")

option = st.radio("Choose input method:", ('Enter text', 'Upload file', 'Compare multiple files'))

if option == 'Enter text':
    text = st.text_area("Enter text here:", height=200)
    uploaded_files = []
elif option == 'Upload file':
    uploaded_file = st.file_uploader("Upload a file (.docx, .pdf, .txt)", type=["docx", "pdf", "txt"])
    text = extract_text_from_file(uploaded_file) if uploaded_file else ""
    uploaded_files = [uploaded_file] if uploaded_file else []
else:
    uploaded_files = st.file_uploader("Upload multiple files", type=["docx", "pdf", "txt"], accept_multiple_files=True)
    texts, filenames = [], []
    for uploaded_file in uploaded_files:
        extracted_text = extract_text_from_file(uploaded_file)
        if extracted_text:
            texts.append(extracted_text)
            filenames.append(uploaded_file.name)
    text = " ".join(texts)

if st.button('Check for Plagiarism'):
    if not text:
        st.error("No text found! Please enter text or upload a file.")
        st.stop()

    if option == 'Compare multiple files':
        similarities = compute_similarities(texts, filenames)
        df = pd.DataFrame(similarities, columns=['File 1', 'File 2', 'Similarity']).sort_values(by=['Similarity'], ascending=False)
        st.write("### File Similarity Results")
        st.dataframe(df)
    else:
        st.write("### Checking for plagiarism...")
        sentences = get_sentences(text)
        url_results = {sentence: get_url(sentence) for sentence in sentences}
        plagiarism_data = []

        for sentence, url in url_results.items():
            if url:
                web_text = get_text_from_url(url)
                similarity = get_similarity(text, web_text)
                if similarity > 0.5:
                    plagiarism_data.append((sentence, url, similarity))

        if plagiarism_data:
            df = pd.DataFrame(plagiarism_data, columns=['Sentence', 'Source URL', 'Similarity'])
            df['Source URL'] = df['Source URL'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
            st.write("### Plagiarism Detected!")
            st.write(df.to_html(escape=False), unsafe_allow_html=True)
        else:
            st.success("No plagiarism detected!")