import requests
from bs4 import BeautifulSoup
import streamlit as st


def extract_company_name(url):
    company_names = []

    url = url.replace("https://", "")
    url = url.replace("www.", "")
    url = url.split(".")[0]
    company_names.append(url)
    return company_names[0]

def add_prefixes(domains):
    corrected_domains = []
    for domain in domains:
        if not domain.startswith("http"):
            domain = "https://" + domain
        if not domain.startswith("https://www."):
            domain = domain.replace("https://", "https://www.")
        corrected_domains.append(domain)
    return corrected_domains



def classify_website(url):
    # Scrape the website's HTML
    """page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Extract relevant information from the HTML
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        description = description.get('content', '')
    else:
        description = ''

    h1_text = soup.find('h1')
    if h1_text is not None:
        h1_text = h1_text.get_text()
    else:
        h1_text = """

    
    # Use the OpenAI API to classify the website's category
    prompt = (f'Ciao a tutti\n, Sono Federico Utzeri, amministratore di Hybrida, l’agenzia vincitrice dell’evento più grande in Europa sul paid advertising.\n'
              f"Ho visto il vostro eCommerce {url}, e penso che alcuni dei vostri prodotti nel 2023 abbiano un’ottima prospettiva di crescita\n"
              f'Stiamo offrendo a 5 eCommerce un workshop (gratuito) in cui realizziamo un’analisi delle vostre metriche e creiamo un piano d’azione personalizzato che l’eCommerce può seguire per crescere.\n'
              f'Mi piacerebbe davvero fare questo workshop con {extract_company_name(url)} perché credo ne possiate trarne informazioni interessanti.\n'
              f'Possiamo fare una chiamata senza impegno per darvi più contesto su come funziona il workshop?\n'
              f'Qui sotto trovate qualche info per avere contesto su cosa fa Hybrida:\n'
              f'Hybrida dal 2019 offre agli eCommerce dei team di crescita per aumentare il fatturato.\n'
              f'Abbiamo vinto nel 2022 l’evento più grande in Europa sulla pubblicità a pagamento: https://www.adworldexperience.it/en/speakers/\n'
              f'Abbiamo aiutato brand come Bialetti Perù, Fortune Italia, Skinlabo e crescere nel mercato italiano, europeo e internazionale.\n'
              f'Trovate tante altre informazioni su di noi e suoi nostri casi studio sul nostro sito: https://www.hybrida.io e sul nostro canale Youtube: https://www.youtube.com/@hybridamarketing6776.\n'
              f'A presto!\n'
              f'Federico')
    subject = (f'Possiamo offrire un Workshop gratuito per {extract_company_name(url)}')
    return prompt, subject

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')