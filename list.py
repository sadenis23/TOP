import streamlit as st
from urllib.parse import urlencode, quote_plus, unquote_plus
import re

# Helper function to generate a custom URL from the report's title and date
def generate_custom_url(report):
    """Generates a URL using the report title and date."""
    title_sanitized = re.sub(r'\W+', '-', report['title'].lower()).strip('-')
    return f"https://example.com/reports/{title_sanitized}-{report['date']}"

# Sample report data (fictional) with custom URLs
report_data = [
    {
        "title": "2024 metų pardavimų ataskaita",
        "author": "Aistė Jonaitė",
        "date": "2024-10-01",
        "description": (
            "Ši ataskaita apima 2024 metų pardavimų rezultatus, akcentuojant pagrindines tendencijas, "
            "regioninius pardavimus ir produktų linijos analizę. Joje pateikiama išsami informacija apie pajamų augimą, "
            "rinkos dalį ir metų pardavimų tikslus."
        ),
        "details": {
            "Pajamų augimas": "15% metinis pajamų padidėjimas.",
            "Geriausi regionai": "Šiaurės Amerika (30% augimas), Europa (25% augimas), APAC (20% augimas).",
            "Produktų linijos": "Elektronika (50% pardavimų), Drabužiai (30%), Buitinė technika (20%).",
            "Pagrindiniai rodikliai": "Bendri pardavimai: 12.5M € | Nauji klientai: 8,000+ | Pakartotinių pirkimų rodiklis: 45%"
        },
        "link": generate_custom_url({"title": "2024 metų pardavimų ataskaita", "date": "2024-10-01"}),
        "image": "https://via.placeholder.com/150"  # Placeholder image
    },
    {
        "title": "2023 metų rinkodaros apžvalga",
        "author": "Benas Kazlauskas",
        "date": "2023-12-20",
        "description": (
            "Ši ataskaita pateikia išsamų 2023 metų rinkodaros kampanijų vertinimą. Joje įtraukti pagrindiniai kampanijų "
            "rodikliai, investicijų grąža (ROI) ir strategijos, padėjusios auginti prekės ženklo žinomumą ir klientų įsitraukimą."
        ),
        "details": {
            "Geriausios kampanijos": "Vasaros produktų išleidimas, Kalėdinės nuolaidos, Nuomonės formuotojų kampanija.",
            "ROI rodikliai": "Vidutinis kampanijų ROI: 350%. Nuomonės formuotojų rinkodara prisidėjo 40% prie bendrų pardavimų.",
            "Klientų įsitraukimas": "Socialinių tinklų įsitraukimas išaugo 25%, el. pašto atidarymo rodiklis padidėjo 12%.",
            "Reklamos išlaidos": "Bendra reklamos išlaida: 1.2M € | Kliento įsigijimo kaina: 45 €"
        },
        "link": generate_custom_url({"title": "2023 metų rinkodaros apžvalga", "date": "2023-12-20"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "2024 metų klientų pasitenkinimo apklausa",
        "author": "Klara Petraitytė",
        "date": "2024-09-15",
        "description": "Rezultatai iš Q3 2024 metų klientų pasitenkinimo apklausos.",
        "link": generate_custom_url({"title": "2024 metų klientų pasitenkinimo apklausa", "date": "2024-09-15"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Produktų vystymo ataskaita 2024",
        "author": "Dainius Liaukis",
        "date": "2024-08-30",
        "description": "Išsamus 2024 metų produktų vystymo veiklos vertinimas.",
        "link": generate_custom_url({"title": "Produktų vystymo ataskaita 2024", "date": "2024-08-30"}),
        "image": "https://via.placeholder.com/150"
    },
    {
        "title": "Naujo produkto pristatymas 2024",
        "author": "Eglė Vaitkūnaitė",
        "date": "2024-07-15",
        "description": "Oficiali ataskaita apie naujo produktų linijos išleidimą 2024 metais.",
        "link": generate_custom_url({"title": "Naujo produkto pristatymas 2024", "date": "2024-07-15"}),
        "image": "https://via.placeholder.com/150"
    }
]

# Function to load report data (since it's already embedded here, no file read)
def load_report_data():
    """
    Returns a list of report data.
    """
    return report_data

# Reusable function to render a single report item in the list
def report_list_item(report):
    """
    Renders a horizontally aligned report item.
    """
    # Use a horizontal container (columns) for a list-like appearance
    col1, col2 = st.columns([1, 4])  # Adjust the ratio between image and text

    # Column for the image
    with col1:
        st.image(report['image'], width=120)

    # Column for the report information
    with col2:
        # Title with larger font size and bold
        st.markdown(f"<h3 style='margin-bottom: 5px;'>{report['title']}</h3>", unsafe_allow_html=True)
        # Display metadata: author and date
        st.markdown(f"<p style='color: #555; font-size: 14px;'>Autorius: {report['author']} | Data: {report['date']}</p>", unsafe_allow_html=True)
        # Short description of the report
        st.markdown(f"<p style='font-size: 16px; line-height: 1.6;'>{report['description']}</p>", unsafe_allow_html=True)
        
        # Add link to view the full report (using query parameters for routing)
        params = urlencode({"report": quote_plus(report['title'])})
        view_link = f"?{params}"
        st.markdown(f"<a href='{view_link}' style='text-decoration: none;'>"
                    f"<button style='background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; text-align: center; border-radius: 5px; cursor: pointer;'>📄 Peržiūrėti pilną ataskaitą</button>"
                    f"</a>", unsafe_allow_html=True)

    # Add a horizontal divider between items
    st.markdown("<hr style='border: none; height: 1px; background-color: #ddd;'>", unsafe_allow_html=True)


# Function to show full details of a single report
def show_report_details(report):
    """
    Displays full details of a single report.
    """
    st.image(report['image'], width=300)
    st.markdown(f"## {report['title']}")
    st.markdown(f"**Autorius:** {report['author']}  |  **Data:** {report['date']}")
    st.write(report['description'])

    # Show additional detailed information if available
    if 'details' in report:
        st.markdown("### Pagrindiniai akcentai:")
        for key, value in report['details'].items():
            st.markdown(f"**{key}:** {value}")
    
    st.markdown(f"[📄 Išorinis pilnos ataskaitos peržiūrėjimas]({report['link']})")

    # Back button to go back to the list
    st.markdown("<a href='/' style='text-decoration: none;'>"
                f"<button style='background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; text-align: center; border-radius: 5px; cursor: pointer;'>🔙 Grįžti į ataskaitų sąrašą</button>"
                f"</a>", unsafe_allow_html=True)


# Main Streamlit app
st.set_page_config(layout="wide")

# Load report metadata
reports = load_report_data()

# Parse the query parameters to check if a report is selected
query_params = st.query_params
selected_report_title = query_params.get('report', [None])[0]

# Ensure the title is valid and not None
if selected_report_title:
    selected_report_title = unquote_plus(selected_report_title).lower().strip()  # Normalize the query parameter
    # Normalize report titles to lowercase and strip extra spaces for comparison
    selected_report = next((r for r in reports if r['title'].lower().strip() == selected_report_title), None)

    if selected_report:
        show_report_details(selected_report)
    else:
        st.write("Ataskaita nerasta.")
else:
    # If no report is selected, show the list of reports
    st.title("📊 Organizacijos viršutinės ataskaitos")

    # Sidebar for filtering and sorting
    search_term = st.sidebar.text_input("Ieškoti pagal pavadinimą ar autorių")
    if search_term:
        reports = [r for r in reports if search_term.lower() in r['title'].lower() or search_term.lower() in r['author'].lower()]

    st.sidebar.header("Filtravimo ir rūšiavimo parinktys")
    filter_author = st.sidebar.selectbox("Filtruoti pagal autorių", ["Visi"] + list(set(report['author'] for report in reports)))
    sort_by = st.sidebar.selectbox("Rūšiuoti pagal", ["Data", "Pavadinimas"])

    # Filter reports by selected author
    if filter_author != "Visi":
        reports = [r for r in reports if r['author'] == filter_author]

    # Sort reports based on user selection
    if sort_by == "Data":
        reports = sorted(reports, key=lambda x: x['date'], reverse=True)
    elif sort_by == "Pavadinimas":
        reports = sorted(reports, key=lambda x: x['title'])

    # Display report count
    st.markdown(f"### Rodoma {len(reports)} ataskaitų", unsafe_allow_html=True)

    # Display the list of reports
    for report in reports:
        report_list_item(report)
