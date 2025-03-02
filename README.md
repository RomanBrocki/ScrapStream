​ScrapStream is a Streamlit-based web application designed to scrape web novels using Selenium and compile them into structured eBook formats.​

Features:

Web Novel Scraping: Automates the extraction of content from web novels.​
Interactive Interface: Provides a user-friendly interface for inputting novel details and initiating the scraping process.​
eBook Compilation: Compiles the scraped content into structured eBook formats.​
github.com
Installation:

1 - Clone the repository:
  git clone https://github.com/RomanBrocki/ScrapStream.git
  cd ScrapStream

2 - Set up a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3 - Install the required packages:
  pip install -r requirements.txt

Usage:
1 - Run the Streamlit app:
  streamlit run app.py

2 - Access the application:

  Open your web browser and navigate to http://localhost:8501.

3 - Provide the necessary inputs:

  Nome do Ebook: Enter the desired name for your eBook.​
  URL do primeiro capítulo: Provide the URL of the novel's first chapter.​
  URL do último capítulo: Provide the URL of the novel's last chapter.​
  Caminho para salvar o ebook: Specify the directory path where the eBook should be saved.​

4 - Initiate the scraping process:

  Click on the "Iniciar Scrap" button to start scraping and compiling the eBook.

File Structure:

  app.py: Main Streamlit application file.​
  novel_scraper.py: Contains the NovelScraper class responsible for the scraping logic.​
  assets/: Directory containing static assets like background images and GIFs.​
  requirements.txt: List of Python dependencies required for the project.​
Dependencies:

  Streamlit: For building the web interface.​
  Selenium: For automating web browser interaction to scrape content.​
  Python-docx: For creating .docx files from the scraped content.​
  All dependencies are listed in the requirements.txt file.
