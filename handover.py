import streamlit as st
from streamlit_tags import st_tags 

# Set page layout and title
st.set_page_config(page_title="Įrankio Dokumentacija", layout="centered")

# Section: Handover / Ataskaitos Dokumentacija
st.subheader("Įrankio dokumentacija")
st.text_input("Ataskaitos pavadinimas", placeholder="Įrašykite ataskaitos pavadinimą")
col1, col2 = st.columns(2)  # Create two columns for input fields
with col1:
    st.text_input("Projekto vykdytojas", placeholder="Įrašykite projekto vykdytoją")
with col2:
    st.text_input("Projekto užsakovai", placeholder="Nurodykite projekto užsakovus")
st.text_input("Savininkas", placeholder="Nurodykite atsakingą asmenį")
st.multiselect("Įrankio tipas", options=["Power BI", "Python", "Power Apps", "Excel", "Kita"])
st.text_area("Paskirtis", placeholder="Apibrėžkite ataskaitos paskirtį ir jos naudą")
st.multiselect("Ataskaitos tematika", options=["Finansai", "IT", "GV", "SMART", "Kita"])
tags = st_tags(
    label="Jei nėra, pridėkite savo temų kategorijas:",
    text="Pridėkite temas",
    value=[],
    suggestions=["Finansai", "IT", "Analitika"],
)
st.write("**Pateiktos temos:**", ", ".join(tags))

st.markdown("---")
st.subheader("Duomenų Šaltiniai")

# Initialize 'data_sources_count' in session_state to count the data sources displayed
if 'data_sources_count' not in st.session_state:
    st.session_state['data_sources_count'] = 1  # Start with the first data source

# Ensure 'data_sources' is initialized in session_state to store data source details
if 'data_sources' not in st.session_state:
    st.session_state['data_sources'] = [{"type": "", "details": ""}]  # Initialize with the first data source

# Function to add a new data source entry
def add_data_source():
    st.session_state['data_sources'].append({"type": "", "details": ""})

# Logic to loop through and display data sources
for i in range(st.session_state['data_sources_count']):
    st.markdown(f"<span style='color:green'>**Duomenų šaltinis {i + 1}</span>**", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])

    with col1:
        st.session_state['data_sources'][i]["type"] = st.selectbox(
            f"Tipas {i + 1}", 
            options=["DWH", "Sharepoint", "Excel", "API", "Kita"], 
            key=f"type_{i}"
        )

    with col2:
        st.session_state['data_sources'][i]["details"] = st.text_area(
            f"Detalės {i + 1}", 
            placeholder="Įrašykite detales apie šaltinį", 
            key=f"details_{i}"
        )

    # Only show the "Add New Data Source" button if the current data source is fully filled
    if i == st.session_state['data_sources_count'] - 1:
        if st.session_state['data_sources'][i]["type"] and st.session_state['data_sources'][i]["details"]:
            if st.button("Pridėti naują duomenų šaltinį"):
                add_data_source()
                st.session_state['data_sources_count'] += 1

# Section: Transformacijos Sekcija
st.markdown("---")
st.subheader("Transformacijos Sekcija")
st.text_area("Pagrindiniai punktai", placeholder="Pateikite pagrindinius duomenų transformacijos veiksmus")
st.text_input("Kodo Orchestratorius", placeholder="pvz., Jenkins, Azure Pipelines, Azure Data Factory")
st.radio("GitLab integracija", options=["Taip", "Ne"], horizontal=True)
st.markdown("---")

# Section: Saugumo Aspektai
st.subheader("Saugumo Aspektai")
st.radio("Prieiga prie duomenų (RLS)", options=["Taip", "Ne"], horizontal=True)

# Section: Ataskaitos naujinimasis
st.markdown("---")
st.subheader("Ataskaitos Atnaujinimo Grafikas")
st.selectbox("Atnaujinimų dažnumas", options=["Kasdien", "Kas savaitę", "Kas mėnesį"])
st.time_input("Naujinimų laikas")
st.radio("Ar naudojamas Data Gateway?", options=["Taip", "Ne"], horizontal=True)

# Section: Priskirtas Procesas
st.markdown("---")
st.subheader("Priskirtas procesas")
st.text_input("Kokiam procesui", placeholder="Nurodykite, prie kokio proceso ar verslo srities priskirta ataskaita")

# Section: Komentarai / Pastabos
st.markdown("---")
st.subheader("Komentarai / Pastabos")
st.text_area("Komentarai / Pastabos", placeholder="Pateikite papildomus komentarus arba pastabas")

# Submit Button
st.button("Baigti pildyti ir pateikti duomenis")
