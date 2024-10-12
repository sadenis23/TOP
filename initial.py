import streamlit as st
import pandas as pd
from streamlit_tags import st_tags 

# Set page layout and title
st.set_page_config(page_title="Power BI Dokumentacija", layout="centered")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Styling for buttons and sidebar
st.markdown("""
    <style>
    /* General button styling */
    .stButton > button {
        border-radius: 8px;
        padding: 10px 30px;
        font-size: 16px;
        min-width: 200px;
    }
    /* Hover effect for general buttons */
    .stButton > button:hover {
        background-color: #f0f0f0;
    }
    /* Centered light green button styling */
    .submit-button {
        display: flex;
        justify-content: center;
    }
    .submit-button > button {
        background-color: #90EE90 !important;
        color: black !important;
        border-radius: 8px;
        padding: 10px 30px;
        font-size: 16px;
        min-width: 200px;
    }
    .submit-button > button:hover {
        background-color: #77dd77 !important;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f7f9fc !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1) !important;
    }
    /* Sidebar title styling */
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #007BFF;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Sidebar content styling */
    .sidebar-content {
        font-size: 16px;
        color: #333;
        padding: 10px 20px;
        background-color: #f0f4f7;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Custom CSS to style the button background to green
st.markdown("""
    <style>
    .stButton > button {
        background-color: #343a40;  /* Green background */
        color: white;  /* White text */
        font-size: 16px;  /* Adjust font size */
        border-radius: 8px;  /* Optional: Add rounded corners */
        padding: 10px 20px;  /* Optional: Add padding */
    }
    .stButton > button:hover {
        background-color: #23272b;  /* Darker green on hover */
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
# Sidebar with a professional title and collapsible instructions
st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: #000000;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    <div class='sidebar-title'>Naudingos nuorodos</div>
    """,
    unsafe_allow_html=True
)

with st.sidebar.expander("Kaip pildyti TOP ataskaitų formą?", expanded=False):
    st.markdown("""
        <div class="sidebar-content">
            <ol style="font-size: 16px; color: #333;">
                <li><b>Asmeninės informacijos pildymas</b>: Užpildykite visus asmeninės informacijos laukus.</li>
                <li><b>Pridėti naują ataskaitą</b>: Pradėkite paspausdami mygtuką <b>„Pridėti naują ataskaitą“</b>.</li>
                <li><b>Ataskaitos pildymas</b>: Pasirinkite ataskaitos pavadinimą ir užpildykite visus laukus pažymėtus žvaigždute (*).</li>
                <li><b>Pridėti daugiau ataskaitų</b>: Norėdami pridėti daugiau, po pirmo užpildymo paspauskite <b>„Pridėti dar vieną ataskaitą“</b>.</li>
                <li><b>Pateikti ataskaitas</b>: Kai baigsite, paspauskite <b>„Baigti pildyti formą“</b>, kad pateiktumėte ataskaitų informaciją.</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

# Add the benefits section to the sidebar with expand functionality
with st.sidebar.expander("Kodėl yra reikalinga turėti svarbiausių (TOP) Power BI ataskaitų sąrašą?", expanded=False):
    st.markdown("""
        <div style="background-color: #f0f4f7; padding: 20px; border-radius: 8px; border-left: 4px solid #007BFF;">
            <ul style="font-size: 16px; color: #333;">
                <li><b>Suteikti aukštesnį prioritetą</b>, ypač kai jos neatsinaujina laiku.</li>
                <li><b>DWH galės sparčiau atnaujinti</b> lentas šioms ataskaitoms.</li>
                <li><b>Galimybė perkelti ataskaitas</b> į naują „capacity“ erdvę, kas pagerintų jų prieinamumą ir veikimo greitį.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


# Load report titles from Excel
@st.cache_data
def load_data_from_excel(file_path):
    return pd.read_excel(file_path, engine='openpyxl')

file_path = r"/Users/nedasvaitkus/Desktop/ISM/AI course/AtaskaituDuomenis.xlsx"  # Replace with your actual path
df = load_data_from_excel(file_path)

# Assuming the report titles are in a column named 'Pavadinimas'
report_titles = ["Pasirinkite..."] + df['Pavadinimas'].tolist()

# Predefined categories for "Ataskaitos kategorija"
predefined_categories = ["SMART'ai", "GV", "Finansai", "Dujos", "Neeilinė situacija", "Kita"]

# Initialize session state for storing multiple reports and user info
if 'reports' not in st.session_state:
    st.session_state.reports = []
if 'user_info' not in st.session_state:
    st.session_state.user_info = {
        "Vardas": "",
        "Pavarde": "",
        "El. Paštas": ""
    }
if 'is_form_submitted' not in st.session_state:
    st.session_state.is_form_submitted = False

# Function to check if personal information is completely filled
def is_personal_info_filled():
    return all(st.session_state.user_info.values())

# Function to display personal information input fields
def display_personal_info():
    st.subheader("Asmeninė informacija")
    col1, col2 = st.columns(2)

    with col1:
        st.session_state.user_info["Vardas"] = st.text_input("Vardas *", 
                                                               placeholder="Įveskite savo vardą", 
                                                               value=st.session_state.user_info["Vardas"])

    with col2:
        st.session_state.user_info["Pavarde"] = st.text_input("Pavardė *", 
                                                                placeholder="Įveskite savo pavardę", 
                                                                value=st.session_state.user_info["Pavarde"])

    email = st.text_input("El. Paštas *", 
                           placeholder="Įveskite savo el. pašto adresą", 
                           value=st.session_state.user_info["El. Paštas"])

    if email and "@" not in email:
        st.warning("Prašome įvesti galiojantį el. pašto adresą, kuriame yra '@' simbolis.")
        st.session_state.user_info["El. Paštas"] = ""  # Clear the value if invalid
    else:
        st.session_state.user_info["El. Paštas"] = email  # Store the valid email

# Function to display report input fields with collapsible sections
def display_report_form(report_index):
    disabled_state = not is_personal_info_filled()  # Disable fields if personal info is not filled
    with st.expander(f"Ataskaita {report_index + 1}", expanded=True):
        st.markdown(f"<h3 style='color: #2E8B57;'>Ataskaita {report_index + 1}</h3>", unsafe_allow_html=True)

        # Add a delete button if it's not the first report
        if report_index > 0:
            if st.button(f"Pašalinti ataskaitą {report_index + 1}", key=f"delete_{report_index}", disabled=disabled_state):
                del st.session_state.reports[report_index]
                return None  # Return None to avoid rendering this report after deletion

        # Report form input fields
        Pavadinimas = st.selectbox("Pasirinkite ataskaitos pavadinimą *", report_titles, key=f"pavadinimas_{report_index}",
                                   disabled=disabled_state)

        Savininkas = st.text_input("Ataskaitos savininkas *", placeholder="Įveskite savininką", key=f"savininkas_{report_index}", disabled=disabled_state)

        Tema = st.text_area("Ataskaitos tema *", placeholder="Įveskite ataskaitos temą", key=f"tema_{report_index}", height=100, disabled=disabled_state)

        # Predefined multiselect categories with an option to add custom ones
        Kategorija = st.multiselect(
            "Kuriai kategorijai priskirtumėte ataskaitą? *", 
            options=predefined_categories, 
            default=None, 
            help="Pasirinkite vieną ar daugiau kategorijų. Jei pasirinksite 'Kita', turėsite įvesti papildomą kategoriją.",
            key=f"kategorija_{report_index}",
            disabled=disabled_state
        )

        # If "Kita" is selected, show a st_tags input field for additional categories
        custom_categories = []
        if "Kita" in Kategorija:
            custom_categories = st_tags(
                label="Įveskite papildomą kategoriją (-as):",
                text="Įrašykite naują kategoriją ir paspauskite Enter",
                value=[],
                key=f"custom_category_{report_index}"
            )
            # Append custom categories to selected categories
            Kategorija.extend(custom_categories)

        st.markdown("---")
        st.subheader("Skyrių informacija")
        col3, col4 = st.columns(2)

        with col3:
            Skyrius = st.text_input("Kuriam skyriui buvo kuriama ataskaita? *", placeholder="Skyrius, kuriam buvo kurta ataskaita", key=f"skyrius_{report_index}", disabled=disabled_state)

        with col4:
            Skyriai = st.text_input("Įvardinkite skyrius, kurie taip pat naudojasi ataskaita? *", placeholder="Skyriai, kurie naudojasi ataskaita", key=f"skyriai_{report_index}", disabled=disabled_state)

        st.markdown("---")
        st.subheader("Naudojimas")

        NaudojimoDaznumas = st.selectbox("Kiek dažnai ataskaita yra naudojama? *", 
                                  ['Pasirinkite...', 
                                   'Naudojama tik išimtiniais atvejais', 
                                   'Mažiau nei 1 kartą per savaitę', 
                                   '2-5 kartai per savaitę', 
                                   '6-10 kartai per savaitę',
                                   '11-20 kartai per savaitę', 
                                   'Daugiau nei 20 kartų per savaitę',
                                   'Sunku pasakyti, priklauso nuo daugelio veiksnių'],
                                  key=f"naudojimo_daznumas_{report_index}", disabled=disabled_state)

        # Place the radio buttons in two columns
        col5, col6 = st.columns(2)

        with col5:
            EsoBLNaudojimas = st.radio("Ar naudojama ESO BL rodiklių lentoje? *", 
                                        ['Pasirinkite...', 'Taip', 'Ne', 'Nežinau'],
                                        key=f"eso_bl_{report_index}", disabled=disabled_state)

        with col6:
            Isore = st.radio("Ar išeina į išorę? *", 
                              ['Pasirinkite...', 'Taip', 'Ne', 'Nežinau'],
                              key=f"isore_{report_index}", disabled=disabled_state)

        st.markdown("---")
        st.subheader("Svarbūs komentarai & pastabos apie ataskaitos svarbumą ir unikalumą")

        KomentaraiPastabos = st.text_area("Komentarai / Pastabos *", 
                                           placeholder="Įveskite kitus komentarus arba pastabas apie ataskaitą", 
                                           height=150, key=f"komentarai_{report_index}", disabled=disabled_state)
    
        return {
            "Pavadinimas": Pavadinimas,
            "Savininkas": Savininkas,
            "Tema": Tema,
            "Kategorijos": Kategorija,  # Use selected and custom categories
            "Skyrius": Skyrius,
            "Kiti skyriai": Skyriai,
            "Naudojimo dažnumas": NaudojimoDaznumas,
            "Naudojama ESO BL lentoje": EsoBLNaudojimas,
            "Išeina į išorę": Isore,
            "Komentarai/Pastabos": KomentaraiPastabos
        }

# Function to check for missing fields in all reports
def check_for_missing_fields():
    missing_fields = []
    for i, report in enumerate(st.session_state.reports):
        fields = []
        for key, value in report.items():
            if key == "Papildyta kategorija" and "Kita" not in report["Kategorija"]:
                continue  # Skip the "Papildyta kategorija" check if "Kita" is not selected
            if not value or (isinstance(value, str) and value == 'Pasirinkite...'):
                fields.append(key)
        if fields:
            missing_fields.append((i + 1, fields))
    return missing_fields

# Show button to add new report if personal info is filled
if st.session_state.page == 'main':
    # Title and subtitle in the center for a professional look
    st.markdown("<h1 style='text-align: center; color: #333;'>Power BI: TOP ataskaitos forma ir dokumentacija </h1>", unsafe_allow_html=True)
    image_path = "/Users/nedasvaitkus/Desktop/laptop-power-bi-1024x467.jpg"  # Replace this with the path to your image
    st.image(image_path, use_column_width=True)
    
    # Adding some vertical space for better UX
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    # Center the buttons on the page using column layout
    col1, col2 = st.columns([1, 1], gap="large")
    st.markdown("---")
    with col1:
        # Styled button for "TOP Ataskaitos" with better visibility
        if st.button('TOP Ataskaitos forma'):
            st.session_state.page = 'form'

    with col2:
        # "Learn More" styled button
        st.button('Ataskaitos dokumentacija')

    # Adding some vertical space for better UX
    st.markdown("<br><br>", unsafe_allow_html=True)

if st.session_state.page == 'form':
    display_personal_info()

    # Display existing reports and allow editing only if personal info is filled
    for i in range(len(st.session_state.reports)):
        report_data = display_report_form(i)
        if report_data:
            st.session_state.reports[i] = report_data

    # Display "Pridėti naują ataskaitą" button that matches the "Baigti pildyti formą" button size
    if is_personal_info_filled():
        if st.button("Pridėti naują ataskaitą"):
            st.session_state.reports.append(display_report_form(len(st.session_state.reports)))
    else:
        st.button("Pridėti naują ataskaitą", disabled=True)

    # Show button to submit the form only if personal info is filled and there is at least one report
    if is_personal_info_filled() and st.session_state.reports:
        st.markdown("---")
        
        # Center the "Baigti pildyti formą" button and make it green
        st.markdown('<div class="submit-button">', unsafe_allow_html=True)
        if st.button("Baigti pildyti formą"):
            missing_fields = check_for_missing_fields()
            if missing_fields:
                st.warning("Nepavyko pateikti duomenų, nes kai kurių ataskaitų laukų trūksta:")
                for report_index, fields in missing_fields:
                    st.warning(f"Ataskaita {report_index}: trūksta laukų: {', '.join(fields)}")
            else:
                st.session_state.is_form_submitted = True
                st.success("Ataskaitos sėkmingai pateiktos!")

                # Display submitted information
                st.markdown("## Jūsų pateikta informacija:")
                st.subheader("Asmeninė informacija")
                st.write(f"**Vardas:** {st.session_state.user_info['Vardas']}")
                st.write(f"**Pavardė:** {st.session_state.user_info['Pavarde']}")
                st.write(f"**El. Paštas:** {st.session_state.user_info['El. Paštas']}")
                
                st.markdown("## Ataskaitos:")
                for i, report in enumerate(st.session_state.reports):
                    st.write(f"### Ataskaita {i + 1}")
                    for key, value in report.items():
                        st.write(f"**{key}:** {value}")
        st.markdown('</div>', unsafe_allow_html=True)
