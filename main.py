import streamlit as st
from streamlit_tags import st_tags
import pandas as pd
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

st.set_page_config(page_title="📚 ESO Dokumentacija", layout="centered")

# Define function for each page
def pagrindinis_page():
    st.title("ESO dokumentacijos sistema")
    st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 32px !important;
        font-weight: bold;
        color: #FF4B4B !important;  /* Force green color */
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    <div class='sidebar-title'>Naudingos nuorodos</div>
""", unsafe_allow_html=True)

    # Adding custom CSS for card-like styling
    st.markdown("""
        <style>
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
        }
        .card-title {
            font-size: 22px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        .card-content {
            font-size: 16px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    # Card-like widget with a title and content
    st.markdown("""
        <div class="card">
            <div class="card-title">Kaip efektyviai naudotis šia sistema?</div>
            <div class="card-content">
                Ši sistema sukurta tam, kad padėtume Jums ne tik tvarkyti ir dokumentuoti ESO Power BI ataskaitas, 
                bet ir užtikrinti, jog svarbiausi duomenys niekada nebūtų prarasti ar nepasiekiami. Čia galite:
                <ul>
                    <li><b>Identifikuoti prioritetines ataskaitas</b> - pasinaudodami TOP ataskaitos forma, galite nurodyti, kurios ataskaitos yra ypatingai svarbios Jūsų skyriui ar projektui.</li>
                    <li><b>Perduoti sukurtus įrankius</b> - sistema padės lengvai dokumentuoti ir perduoti svarbią informaciją apie sukurtą įrankį, užtikrinant, kad visi kolegos turėtų prieigą prie reikalingos informacijos ir galėtų efektyviai juo naudotis.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)


# TOP ATASKAITOS ------------------------------------------------------------------------------------------------------------------------------------------
def top_ataskaitos_page():
    # Set page layout and title
    st.title("TOP Power BI ataskaitos forma")


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

    # Sidebar content and styling
    st.sidebar.markdown("""
        <style>
        .sidebar-title {
            font-size: 32px !important;
            font-weight: bold;
            color: #FF4B4B !important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Kodėl yra reikalinga turėti svarbiausių (TOP) Power BI ataskaitų sąrašą?", expanded=False):
        st.markdown("""
            <div style="background-color: #f0f4f7; padding: 20px; border-radius: 8px; border-left: 4px solid #007BFF;">
                <ol style="font-size: 16px; color: #333;">
                    <li><b>Suteikti aukštesnį prioritetą</b>, ypač kai jos neatsinaujina laiku.</li>
                    <li><b>DWH galės sparčiau atnaujinti</b> lentas šioms ataskaitoms.</li>
                    <li><b>Galimybė perkelti ataskaitas</b> į naują „capacity“ erdvę, kas pagerintų jų prieinamumą ir veikimo greitį.</li>
                </ol>
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

    # Initialize session state for storing user info and report data
    if 'user_info' not in st.session_state:
        st.session_state.user_info = {
            "Vardas": "",
            "Pavarde": "",
            "El. Paštas": ""
        }
    if 'report_data' not in st.session_state:
        st.session_state.report_data = {}
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

    # Function to display the report input form with collapsible sections (for a single report)
    def display_report_form():
        disabled_state = not is_personal_info_filled()  # Disable fields if personal info is not filled

        with st.expander("Ataskaitos duomenys", expanded=True):
            st.subheader("Ataskaitos informacija")
            Pavadinimas = st.selectbox("Pasirinkite ataskaitos pavadinimą *", report_titles, key="pavadinimas", disabled=disabled_state)

            Savininkas = st.text_input("Ataskaitos savininkas *", placeholder="Įveskite savininką", key="savininkas", disabled=disabled_state)

            Tema = st.text_area("Ataskaitos tema *", placeholder="Įveskite ataskaitos temą", key="tema", height=100, disabled=disabled_state)

            Kategorija = st.multiselect(
                "Kuriai kategorijai priskirtumėte ataskaitą? *", 
                options=predefined_categories, 
                default=None, 
                help="Pasirinkite vieną ar daugiau kategorijų. Jei pasirinksite 'Kita', turėsite įvesti papildomą kategoriją.",
                key="kategorija",
                disabled=disabled_state
            )

            if "Kita" in Kategorija:
                # Input field for entering additional categories separated by commas
                custom_categories_input = st.text_input("Įveskite papildomą kategoriją (-as):", 
                                                        placeholder="Atskirkite kategorijas kableliais", 
                                                        key="custom_category_input",
                                                        disabled=disabled_state)
                # Split the input into a list of categories by commas
                custom_categories = [cat.strip() for cat in custom_categories_input.split(',') if cat.strip()]
                Kategorija.extend(custom_categories)

            st.subheader("Skyrių informacija")
            Skyrius = st.text_input("Skyrius *", placeholder="Skyrius, kuriam buvo kurta ataskaita", key="skyrius", disabled=disabled_state)

            Skyriai = st.text_input("Kiti skyriai *", placeholder="Skyriai, kurie naudojasi ataskaita", key="skyriai", disabled=disabled_state)

            st.subheader("Naudojimo informacija")
            NaudojimoDaznumas = st.selectbox("Kiek dažnai ataskaita yra naudojama? *", 
                                        ['Pasirinkite...', 'Naudojama tik išimtiniais atvejais', 'Labai retai', 'Kartais', 'Dažnai', 'Labai dažnai', 'Nuolat'],
                                        key="naudojimo_daznumas", disabled=disabled_state)

            EsoBLNaudojimas = st.radio("Ar naudojama ESO BL rodiklių lentoje? *", 
                                    ['Pasirinkite...', 'Taip', 'Ne', 'Nežinau'], key="eso_bl", disabled=disabled_state)

            Isore = st.radio("Ar išeina į išorę? *", ['Pasirinkite...', 'Taip', 'Ne', 'Nežinau'], key="isore", disabled=disabled_state)

            st.subheader("Komentarai ir pastabos")
            KomentaraiPastabos = st.text_area("Komentarai / Pastabos *", 
                                            placeholder="Įveskite kitus komentarus arba pastabas apie ataskaitą", 
                                            height=150, key="komentarai", disabled=disabled_state)

            st.session_state.report_data = {
                "Pavadinimas": Pavadinimas,
                "Savininkas": Savininkas,
                "Tema": Tema,
                "Kategorijos": Kategorija,
                "Skyrius": Skyrius,
                "Kiti skyriai": Skyriai,
                "Naudojimo dažnumas": NaudojimoDaznumas,
                "Naudojama ESO BL lentoje": EsoBLNaudojimas,
                "Išeina į išorę": Isore,
                "Komentarai/Pastabos": KomentaraiPastabos
            }

    # Function to check for missing fields
    def check_for_missing_fields():
        missing_fields = []
        for key, value in st.session_state.report_data.items():
            if not value or (isinstance(value, str) and value == 'Pasirinkite...'):
                missing_fields.append(key)
        return missing_fields

    # Main page logic
    display_personal_info()
    display_report_form()

    # Show button to submit the form only if personal info is filled
    if is_personal_info_filled():
        st.markdown("---")
        st.markdown('<div class="submit-button">', unsafe_allow_html=True)
        if st.button("Baigti pildyti formą ir siųsti duomenis"):
            missing_fields = check_for_missing_fields()
            if missing_fields:
                missing_fields_str = ', '.join(missing_fields)
                st.info(f"Neužpildyti šie laukai: {missing_fields_str}")
            else:
                st.session_state.is_form_submitted = True
                st.success("Ataskaita sėkmingai pateikta!")

                # Display submitted information
                st.markdown("## Jūsų pateikta informacija:")
                st.subheader("Asmeninė informacija")
                st.write(f"**Vardas:** {st.session_state.user_info['Vardas']}")
                st.write(f"**Pavardė:** {st.session_state.user_info['Pavarde']}")
                st.write(f"**El. Paštas:** {st.session_state.user_info['El. Paštas']}")

                st.markdown("## Ataskaita:")
                for key, value in st.session_state.report_data.items():
                    st.write(f"**{key}:** {value}")
        st.markdown('</div>', unsafe_allow_html=True)
        
 # IRANKIO DOKUMENTACIJA--------------------------------------------------------------------------
def ataskaitos_dokumentacija_page():
    # Set page layout and title
    st.title("Įrankio dokumentacija")

    # Custom CSS to center buttons
    st.markdown("""
        <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar content and styling
    st.sidebar.markdown("""
        <style>
        .sidebar-title {
            font-size: 32px !important;
            font-weight: bold;
            color: #FF4B4B !important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
    """, unsafe_allow_html=True)
    
    with st.sidebar.expander("Perdavimo instrukcijos", expanded=False):
        st.markdown("""
        <div style="background-color: #f0f4f7; padding: 20px; border-radius: 8px; border-left: 4px solid #28a745;">
            <ol style="font-size: 16px; color: #333;">
                <li><b>Surinkite visą reikiamą informaciją</b>, įskaitant ataskaitos pavadinimą, projekto vykdytoją, užsakovus, savininką, ir pagrindinį ataskaitos tikslą.</li>
                <li><b>Nurodykite duomenų šaltinius</b> ir pateikite išsamią informaciją apie jų tipus, pvz.: DWH, SharePoint, Excel, ar API. Jei yra daugiau nei vienas šaltinis, pridėkite juos.</li>
                <li><b>Aptarkite atliktas transformacijas</b> – nurodykite, kokios transformacijos buvo atliekamos su duomenimis (pvz., valymo veiksmai, duomenų transformavimas).</li>
                <li><b>Pateikite atnaujinimo dažnumą</b> – nustatykite, kaip dažnai atnaujinami duomenys (pvz.: kasdien, kas savaitę) ir kada vyksta atnaujinimai.</li>
                <li><b>Įrašykite įrankio konfiguraciją</b>, įskaitant kodo orchestratorių, GitLab integraciją, Data Gateway naudojimą, bei RLS (saugos sistemos) taikymą.</li>
                <li><b>Papildomi komentarai ir pastabos</b> – pateikite bet kokią papildomą informaciją ar rekomendacijas ateičiai.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    # Adjust session state initialization for section tracking
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    # Adjust section tracking state for 4 sections only
    if 'section_completed' not in st.session_state:
        st.session_state['section_completed'] = {
            'section1': False,
            'section2': False,
            'section5': False,
            'section6': False
        }

    if 'attempted_section' not in st.session_state:
        st.session_state['attempted_section'] = {
            'section1': False,
            'section2': False,
            'section5': False,
            'section6': False
        }

    def next_section(section_key):
        st.session_state['section_completed'][section_key] = True
        st.session_state['current_step'] += 1
        st.success(f"Automatiškai išsaugota! Galite tęsti toliau.")

    def check_for_missing_fields_section1():
        missing_fields = []
        if not st.session_state.get('report_name'):
            missing_fields.append("Ataskaitos pavadinimas")
        if not st.session_state.get('executor'):
            missing_fields.append("Projekto vykdytojas")
        if not st.session_state.get('clients'):
            missing_fields.append("Projekto užsakovai")
        if not st.session_state.get('tool_type'):
            missing_fields.append("Įrankio tipas")
        if not st.session_state.get('purpose'):
            missing_fields.append("Paskirtis")
        if not st.session_state.get('topics'):
            missing_fields.append("Ataskaitos tematika")

        return missing_fields

    def check_for_missing_fields_section2():
        missing_fields = []
        # Assuming there are data fields like type_0, details_0, etc.
        for i in range(st.session_state['data_sources_count']):
            if not st.session_state.get(f'type_{i}'):
                missing_fields.append(f"Tipas {i + 1}")
            if not st.session_state.get(f'details_{i}'):
                missing_fields.append(f"Detalės {i + 1}")
            if not st.session_state.get(f'transformation_{i}'):
                missing_fields.append(f"Transformacija {i + 1}")
        
        return missing_fields

    def check_for_missing_fields_section5():
        missing_fields = []
        if not st.session_state.get('orchestrator'):
            missing_fields.append("Kodo orchestratorius")
        if not st.session_state.get('gitlab'):
            missing_fields.append("GitLab integracija")
        if not st.session_state.get('data_gateway'):
            missing_fields.append("Data Gateway")
        if not st.session_state.get('rls'):
            missing_fields.append("Duomenų saugos sistema (RLS)")
        if not st.session_state.get('selected_processes'):
            missing_fields.append("Procesai")
        
        return missing_fields

# IRANKIO DOKUMENTACIJA--------------------------------------------------------------------------


def ataskaitos_dokumentacija_page():
    # Set page layout and title
    st.title("Įrankio dokumentacija")

    # Custom CSS to center buttons
    st.markdown("""
        <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar content and styling
    st.sidebar.markdown("""
        <style>
        .sidebar-title {
            font-size: 32px !important;
            font-weight: bold;
            color: #FF4B4B !important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
    """, unsafe_allow_html=True)

    # Adjust session state initialization for section tracking
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    # Adjust section tracking state for 4 sections only
    if 'section_completed' not in st.session_state:
        st.session_state['section_completed'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False
        }

    if 'attempted_section' not in st.session_state:
        st.session_state['attempted_section'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False
        }

        # Function to proceed to the next section
    def next_section(section_key):
        st.session_state['section_completed'][section_key] = True
        st.session_state['current_step'] += 1
        st.success(f"Automatiškai išsaugota! Galite tęsti toliau.")

    # Function to check for missing fields in Section 1
    def check_for_missing_fields_section1():
        missing_fields = []
        if not st.session_state.get('report_name'):
            missing_fields.append("Įrankio pavadinimas")
        if not st.session_state.get('tool_name'):
            missing_fields.append("Įrankio nuoroda")
        if not st.session_state.get('executor'):
            missing_fields.append("Projekto vykdytojas")
        if not st.session_state.get('clients'):
            missing_fields.append("Projekto užsakovai")
        if not st.session_state.get('tool_type'):
            missing_fields.append("Įrankio tipas")
        if not st.session_state.get('purpose'):
            missing_fields.append("Paskirtis")
        if not st.session_state.get('selected_processes'):
            missing_fields.append("Procesai")
        if not st.session_state.get('topics'):
            missing_fields.append("Tematika")

        return missing_fields

    # Function to check for missing fields in Section 2
    def check_for_missing_fields_section2():
        missing_fields = []
        for i in range(st.session_state['data_sources_count']):
            if not st.session_state.get(f'type_{i}'):
                missing_fields.append(f"Tipas {i + 1}")
            if not st.session_state.get(f'details_{i}'):
                missing_fields.append(f"Serveris/Duomenų bazė/Schema {i + 1}")
            if not st.session_state.get(f'transformation_{i}'):
                missing_fields.append(f"Transformacija {i + 1}")
            if not st.session_state.get(f'link_{i}'):
                missing_fields.append(f"Nuoroda {i + 1}")

        return missing_fields

    # Function to check for missing fields in Section 3
    def check_for_missing_fields_section3():
        missing_fields = []
        if not st.session_state.get('orchestrator'):
            missing_fields.append("Kodo orchestratorius")
        if not st.session_state.get('gitlab'):
            missing_fields.append("GitLab integracija")
        if not st.session_state.get('data_gateway'):
            missing_fields.append("Data Gateway")
        if not st.session_state.get('rls'):
            missing_fields.append("Duomenų saugos sistema (RLS)")

        return missing_fields

    # Initialize session state for the progress and sections
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    if 'section_completed' not in st.session_state:
        st.session_state['section_completed'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False
        }

    if 'attempted_section' not in st.session_state:
        st.session_state['attempted_section'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False
        }

    # Section 1: Pagrindinė įrankio informacija (Step 1)
    if st.session_state['current_step'] >= 1:
        with st.expander("1. Pagrindinė įrankio informacija", expanded=True):
            st.session_state['report_name'] = st.text_input("Įrankio pavadinimas", placeholder="Įrašykite įrankio pavadinimą")
            st.session_state['tool_name'] = st.text_input("Įrankio nuoroda", placeholder="Įklijuokite įrankio nuorodą")

            col1, col2 = st.columns(2)
            with col1:
                st.session_state['executor'] = st.text_input("Projekto vykdytojas", placeholder="Įrašykite projekto vykdytoją")
            with col2:
                st.session_state['clients'] = st.text_input("Projekto užsakovai / Atsakingi asmenys", placeholder="Nurodykite projekto užsakovus")

            st.session_state['tool_type'] = st.multiselect("Įrankio tipas", options=["Power BI", "Python", "Power Apps", "Excel", "Power Automate", "Kita"])
            if "Kita" in st.session_state['tool_type']:
                custom_tool_type = st.text_input("Įrašykite savo įrankio tipą", placeholder="Įrašykite kitą įrankio tipą")
                if custom_tool_type:
                    st.session_state['tool_type'].append(custom_tool_type)

            st.session_state['purpose'] = st.text_area("Paskirtis", placeholder="Apibrėžkite ataskaitos paskirtį ir jos naudą")
            process_options = ["L3 PROCESŲ GRUPĖ. ELEKTROS SKIRSTOMŲJŲ TINKLŲ VYSTYMAS", "L3 PROCESŲ GRUPĖ. GAMTINIŲ DUJŲ SKIRSTOMŲJŲ DUOJETIEKIŲ VYSTYMAS", "TBD"]
            st.session_state['selected_processes'] = st.multiselect("Kokiems procesams priklauso įrankis?", options=process_options, placeholder="Nurodykite procesą")
            st.session_state['topics'] = st.multiselect("Tematika", options=["Finansai", "IT", "GV", "SMART", "TBD"])

            tags = st.text_input("Pridėkite savo temų kategorijas", placeholder="Įrašykite temas atskirtas kableliais")
            if tags:
                temas_list = [tema.strip() for tema in tags.split(',')]
                st.write("**Pateiktos temos:**", ", ".join(temas_list))

            if st.session_state['current_step'] == 1:
                missing_fields = check_for_missing_fields_section1()
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Tęsti", key="section1"):
                    st.session_state['attempted_section']['section1'] = True
                    if not missing_fields:
                        next_section('section1')
                if st.session_state['attempted_section']['section1'] and missing_fields:
                    st.warning(f"Prašome užpildyti šiuos laukus: {', '.join(missing_fields)}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Section 2: Duomenų šaltiniai (Step 2)
    if st.session_state['current_step'] >= 2:
        with st.expander("2. Duomenų šaltiniai", expanded=False):

            if 'data_sources_count' not in st.session_state:
                st.session_state['data_sources_count'] = 1

            if 'data_sources' not in st.session_state:
                st.session_state['data_sources'] = [{"type": "", "details": "", "transformation": "", "link": ""}]

            def add_data_source():
                st.session_state['data_sources'].append({"type": "", "details": "", "transformation": "", "link": ""})

            def delete_data_source(index):
                if st.session_state['data_sources_count'] > 1 and index > 0:
                    st.session_state['data_sources'].pop(index)
                    st.session_state['data_sources_count'] -= 1

            for i in range(st.session_state['data_sources_count']):
                st.subheader(f"Duomenų šaltinis {i + 1}")
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.selectbox(f"Tipas", options=["DWH", "Sharepoint", "Excel", "API", "Kita"], key=f"type_{i}")
                with col2:
                    st.text_input(f"Serveris/Duomenų bazė/Schema/Lenta", placeholder="Įrašykite detales apie šaltinį", key=f"details_{i}")

                st.text_area(f"Transformacija", placeholder="Įrašykite transformaciją (jei taikoma)", key=f"transformation_{i}")
                st.text_input(f"Kur atliekamos transformacijos (jei taikoma)?", placeholder="Pateikite nuorodą (jei taikoma)", key=f"link_{i}")

                if st.session_state['data_sources_count'] > 1 and i > 0:
                    if st.button(f"Pašalinti šaltinį {i + 1}", key=f"delete_{i}"):
                        delete_data_source(i)

                if i < st.session_state['data_sources_count'] - 1:
                    st.markdown("---")

                if i == st.session_state['data_sources_count'] - 1:
                    if st.session_state.get(f'type_{i}') and st.session_state.get(f'details_{i}') and st.session_state.get(f'transformation_{i}') and st.session_state.get(f'link_{i}'):
                        if st.button("Pridėti naują duomenų šaltinį"):
                            add_data_source()
                            st.session_state['data_sources_count'] += 1

            if st.session_state['current_step'] == 2:
                missing_fields = check_for_missing_fields_section2()
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Tęsti", key="section2"):
                    st.session_state['attempted_section']['section2'] = True
                    if not missing_fields:
                        next_section('section2')
                if st.session_state['attempted_section']['section2'] and missing_fields:
                    st.warning(f"Prašome užpildyti šiuos laukus: {', '.join(missing_fields)}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Section 3: Įrankio konfiguracija (Step 3)
    if st.session_state['current_step'] >= 3:
        with st.expander("3. Įrankio konfiguracija", expanded=False):
            st.subheader("Įrankio konfiguracija")

            col1, col2 = st.columns(2)

            with col1:
                st.session_state['orchestrator'] = st.radio("Ar naudojamas kodo orchestratorius?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['gitlab'] = st.radio("Ar yra GitLab integracija?", options=["Taip", "Ne"], index=1, horizontal=False)

            with col2:
                st.session_state['data_gateway'] = st.radio("Ar naudojamas Data Gateway?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['rls'] = st.radio("Ar yra įdiegta duomenų saugos sistema (RLS)?", options=["Taip", "Ne"], index=1, horizontal=False)

            if st.session_state['current_step'] == 3:
                missing_fields = check_for_missing_fields_section3()
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Tęsti", key="section3"):
                    st.session_state['attempted_section']['section3'] = True
                    if not missing_fields:
                        next_section('section3')
                if st.session_state['attempted_section']['section3'] and missing_fields:
                    st.warning(f"Prašome užpildyti šiuos laukus: {', '.join(missing_fields)}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Section 4: Komentarai / Pastabos (Step 4)
    if st.session_state['current_step'] >= 4:
        with st.expander("4. Komentarai / Pastabos", expanded=False):
            st.subheader("Komentarai / Pastabos")
            st.session_state['comments'] = st.text_area("Komentarai / Pastabos", placeholder="Pateikite papildomus komentarus arba pastabas")

            if st.session_state['current_step'] == 4:
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Baigti pildyti ir pateikti duomenis", key="section4"):
                    st.session_state['attempted_section']['section4'] = True
                    next_section('section4')
                    st.success("Pateikimas baigtas. Visi duomenys automatiškai išsaugoti!")
                st.markdown('</div>', unsafe_allow_html=True)


#------------------------------------------------------------------------------------------------------
# Main app logic
styles = {
    "nav": {
        "background-color": "rgb(123, 209, 146)",  # Light green background for the navbar
    },
    "div": {
        "max-width": "32rem",  # Set max-width for the navbar content
    },
    "span": {
        "border-radius": "0.5rem",  # Rounded corners for the tabs
        "color": "rgb(49, 51, 63)",  # Text color
        "margin": "0 0.125rem",  # Margin between tabs
        "padding": "0.4375rem 0.625rem",  # Padding for the tabs
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",  # Background for the active tab
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",  # Background for the hovered tab
    },
}


def show_footer():
    st.markdown("""
    <style>
    .footer {
        text-align: center;
        font-size: 12px;
        color: gray;
        padding: 10px;
        margin-top: 50px;
        border-top: 1px solid #f0f0f0;
    }
    </style>
    <div class="footer">
        © 2024 ESO.
    </div>
    """, unsafe_allow_html=True)
    


def main():
    # Create a longer navbar with additional padding, spacing, and custom styles
    page = option_menu(
        menu_title=None,  # Hide the menu title
        options=["Pagrindinis", "TOP ataskaitos", "Dokumentacija"],  # Added more options for longer bar
        icons=["house", "clipboard", "book"],  # Add custom icons (optional)
        menu_icon="cast",  # Optional menu icon
        default_index=0,  # Set the default selected index
        orientation="horizontal",  # Horizontal orientation
        styles={
            "container": {"padding": "0!important", "background-color": "#FF4B4B"},  # Primary Red background for the navbar
            "icon": {"color": "white", "font-size": "25px"},  # White icons with larger font size
            "nav-link": {
                "font-size": "18px",  # Larger font size for navigation items
                "text-align": "center",
                "margin": "0px 10px",  # Add margin between items for a wider layout
                "padding": "12px 20px",  # Add padding for a larger clickable area
                "color": "white",
                "background-color": "#FF4B4B",  # Primary Red background for unselected links
                "border-radius": "5px",  # Add some rounding to the edges
            },
            "nav-link-selected": {"background-color": "#D32F2F"},  # Dark Red for the selected link
            "hover": {"background-color": "#FF6E6E"},  # Secondary Red on hover
        },
    )
    
    # Display selected page content
    if page == "Pagrindinis":
        pagrindinis_page()
    elif page == "TOP ataskaitos":
        top_ataskaitos_page()
    elif page == "Dokumentacija":
        ataskaitos_dokumentacija_page()
    show_footer()

if __name__ == "__main__":
    main()
