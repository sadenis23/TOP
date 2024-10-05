import streamlit as st
import pandas as pd
from streamlit_tags import st_tags  # Import for the chip-style custom categories input

# Set page layout and title
st.set_page_config(page_title="TOP Ataskaitų Forma", layout="centered")

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

    /* Primary buttons with no background color */
    .stButton > button {
        background-color: transparent !important;  /* No background */
        color: #333 !important;                    /* Dark text color */
        border: 2px solid #ccc !important;         /* Light gray border */
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 30px;
        min-width: 200px;
        cursor: pointer;
    }

    .stButton > button:hover {
        background-color: #f0f0f0 !important;  /* Light gray on hover */
    }

    /* Secondary button with a nice blue color */
    .submit-button {
        display: flex;
        justify-content: center;
    }

    .submit-button > button {
        background-color: #88ddaf !important;  /* Nice green */
        color: white !important;               /* White text color */
        font-size: 16px;
        border-radius: 8px;
        padding: 10px 30px;
        min-width: 200px;
    }

    .submit-button > button:hover {
        background-color: #70c996 !important;  /* Darker green on hover */
        border: 2px solid #808080 !important;  /* Grey border on hover */
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

    /* Input field error styling */
    .input-error {
        border: 2px solid red !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with a professional title and collapsible instructions
st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] .sidebar-title {
        color: #333333 !important;
        font-weight: bold;
        font-size: 20px;
    }
    </style>
    <div class='sidebar-title'>Pildymo Instrukcijos</div>
    """,
    unsafe_allow_html=True
)

with st.sidebar.expander("Rodyti Instrukcijas", expanded=False):
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

# Display Title and Description
st.markdown("<h1 style='text-align: center; color: #333333;'>Power BI TOP Ataskaitų Forma</h1>", unsafe_allow_html=True)

# Benefits Section with Professional Styling
st.markdown("""
    <div style="background-color: #f0f4f7; padding: 20px; border-radius: 8px; border-left: 4px solid #007BFF;">
        <h2 style="color: #696969;">Kodėl yra reikalinga turėti svarbiausių (TOP) Power BI ataskaitų sąrašą?</h2>
        <ul style="font-size: 16px; color: #333;">
            <li><b>Suteikti aukštesnį prioritetą</b>, ypač kai jos neatsinaujina laiku.</li>
            <li><b>DWH galės sparčiau atnaujinti</b> lentas šioms ataskaitoms.</li>
            <li><b>Galimybė perkelti ataskaitas</b> į naują „capacity“ erdvę, kas pagerintų jų prieinamumą ir veikimo greitį.</li>
        </ul>
    </div>
    <br>
""", unsafe_allow_html=True)

# Load report titles from Excel
@st.cache_data
def load_data_from_excel(file_path):
    return pd.read_excel(file_path, engine='openpyxl')

file_path = r"C:\DAS server data\TOP_forma\AtaskaituDuomenis.xlsx"
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

# Check if personal information is completely filled
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
        
        custom_categories = []
        if "Kita" in Kategorija:
            custom_category_input = st.text_input(
                "Įveskite papildomą kategoriją (-as):",
                key=f"custom_category_{report_index}")
    
            if custom_category_input:
                custom_categories = [cat.strip() for cat in custom_category_input.split(",") if cat.strip()]
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

        NaudojimoDaznumas = st.selectbox(
            "Kiek dažnai ataskaita yra naudojama? *",
            ['Pasirinkite...', 'Naudojama tik išimtiniais atvejais', 'Labai retai', 'Kartais', 'Dažnai', 'Labai dažnai', 'Nuolat'],
            key=f"naudojimo_daznumas_{report_index}",
            disabled=disabled_state)
        if NaudojimoDaznumas == "Pasirinkite...":
            st.markdown(f"<style>#naudojimo_daznumas_{report_index} {{border: 2px solid red !important;}}</style>", unsafe_allow_html=True)

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

# Function to check if all fields are filled
def are_all_fields_filled(report):
    # Ensure the "Papildyta kategorija" is checked only if "Kita" is selected
    for key, value in report.items():
        if key == "Papildyta kategorija" and "Kita" not in report["Kategorija"]:
            continue  # Skip validation for "Papildyta kategorija" if "Kita" is not selected
        if not value or (isinstance(value, str) and value == 'Pasirinkite...'):
            return False
    return True

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

# Display personal information input
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
    # Use st.columns to center the button
# Example function to check if any reports are filled out
# Example function to check if any reports are filled
def is_report_filled():
    # This function should check if there's at least one report in the session state that is filled
    # Assuming that if at least one report has a non-empty "Pavadinimas", it's considered filled
    for report in st.session_state.reports:
        if report.get("Pavadinimas") and report["Pavadinimas"] != "Pasirinkite...":
            return True
    return False

# Check if any reports are filled before showing the submission button
if is_report_filled():
    # Center the button using st.columns
    col1, col2, col3 = st.columns([1, 2, 1])  # Create three columns, center column is wider
    with col2:
        # Button in the center column
        if st.button("Baigti pildyti formą ir siųsti duomenis"):
            missing_fields = check_for_missing_fields()
            if missing_fields:
                st.session_state.form_errors = missing_fields
            else:
                # Handle submission of reports and user info
                st.session_state.is_form_submitted = True
                st.session_state.form_errors = None  # Clear any previous errors

# Now handle warnings and success messages outside the columns
if "form_errors" in st.session_state and st.session_state.form_errors:
    # Warning messages, not inside the columns, ensuring they are left-aligned
    for report_index, fields in st.session_state.form_errors:
        st.warning(f"Ataskaita {report_index}: trūksta laukų: {', '.join(fields)}")

# If the form is successfully submitted
if st.session_state.get("is_form_submitted", False):
    # Left-aligned success message
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


