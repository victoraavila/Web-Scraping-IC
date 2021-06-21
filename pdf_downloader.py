import requests

# 7. Downloading the .pdf file available in the current link
def download_pdf_from_url(url):
    response = requests.get(url)

    with open("Componente Organizacional.pdf", "wb") as file:
        file.write(response.content)