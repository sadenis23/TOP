import streamlit as st
from streamlit_tags import st_tags
import pandas as pd
from streamlit_navigation_bar import st_navbar
import pyodbc

# Define function for each page
def pagrindinis_page():
    st.title("Sveiki atvykę į ESO ataskaitų dokumentacijos puslapį!")

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
            color: #28a745 !important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Kaip pildyti TOP ataskaitų formą?", expanded=False):
        st.markdown("""
            <div class="sidebar-content">
                <ol style="font-size: 16px; color: #333;">
                    <li><b>Asmeninės informacijos pildymas</b>: Užpildykite visus asmeninės informacijos laukus.</li>
                    <li><b>Ataskaitos pildymas</b>: Pasirinkite ataskaitos pavadinimą ir užpildykite visus laukus pažymėtus žvaigždute (*).</li>
                    <li><b>Pateikti ataskaitą</b>: Kai baigsite, paspauskite <b>„Baigti pildyti formą“</b>, kad pateiktumėte ataskaitą.</li>
                </ol>
            </div>
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

    file_path = r"C:\DAS server data\TOP_forma\AtaskaituDuomenis.xlsx"  # Replace with your actual path
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
    st.title("Įrankio perdavimas")

    # Custom CSS to center buttons
    st.markdown("""
        <style>
        .center-button {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state for progress tracking and visibility control
    if 'current_step' not in st.session_state:
        st.session_state['current_step'] = 1

    if 'section_completed' not in st.session_state:
        st.session_state['section_completed'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False,
            'section5': False,
            'section6': False
        }

    if 'attempted_section' not in st.session_state:
        st.session_state['attempted_section'] = {
            'section1': False,
            'section2': False,
            'section3': False,
            'section4': False,
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
        if not st.session_state.get('owner'):
            missing_fields.append("Savininkas")
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
        if not st.session_state.get('type_0'):
            missing_fields.append("Tipas 1")
        if not st.session_state.get('details_0'):
            missing_fields.append("Detalės 1")
        
        # Check for additional data sources if added (dynamic indexing)
        for i in range(1, st.session_state['data_sources_count']):
            if not st.session_state.get(f'type_{i}'):
                missing_fields.append(f"Tipas {i + 1}")
            if not st.session_state.get(f'details_{i}'):
                missing_fields.append(f"Detalės {i + 1}")
        
        return missing_fields

    def check_for_missing_fields_section3():
        missing_fields = []
        # Assuming there are steps for transformations
        for i in range(st.session_state['transformations_count']):
            if not st.session_state.get(f'steps_{i}'):
                missing_fields.append(f"Transformacija {i + 1}")
        
        return missing_fields

    def check_for_missing_fields_section4():
        missing_fields = []
        if not st.session_state.get('frequency'):
            missing_fields.append("Atnaujinimų dažnumas")
        if not st.session_state.get('update_time'):
            missing_fields.append("Naujinimosi laikas")
        
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


    # Section 1: Įrankio dokumentacija (Step 1)
    if st.session_state['current_step'] >= 1:
        with st.expander("Pagrindinė ataskaitos informacija", expanded=True):
            st.session_state['report_name'] = st.text_input("Ataskaitos pavadinimas", placeholder="Įrašykite ataskaitos pavadinimą")

            col1, col2 = st.columns(2)
            with col1:
                st.session_state['executor'] = st.text_input("Projekto vykdytojas", placeholder="Įrašykite projekto vykdytoją")
            with col2:
                st.session_state['clients'] = st.text_input("Projekto užsakovai", placeholder="Nurodykite projekto užsakovus")

            st.session_state['owner'] = st.text_input("Savininkas", placeholder="Nurodykite atsakingą asmenį")
            st.session_state['tool_type'] = st.multiselect("Įrankio tipas", options=["Power BI", "Python", "Power Apps", "Excel", "Kita"])
            st.session_state['purpose'] = st.text_area("Paskirtis", placeholder="Apibrėžkite ataskaitos paskirtį ir jos naudą")
            st.session_state['topics'] = st.multiselect("Ataskaitos tematika", options=["Finansai", "IT", "GV", "SMART"])

           # Simple text area for adding themes (temos kategorijas)
            tags = st.text_area(
                label="Pridėkite savo temų kategorijas:",
                placeholder="Įrašykite temas atskirtas kableliais, pvz., Finansai, IT, Analitika",
                height=10
            )

            # Display the entered themes
            if tags:
                # Split the input string by commas and display as a list
                temas_list = [tema.strip() for tema in tags.split(',')]
                st.write("**Pateiktos temos:**", ", ".join(temas_list))


            # Show the Continue button only for the current step
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
        with st.expander("Duomenų šaltiniai", expanded=False):

            if 'data_sources_count' not in st.session_state:
                st.session_state['data_sources_count'] = 1

            if 'data_sources' not in st.session_state:
                st.session_state['data_sources'] = [{"type": "", "details": ""}]

            def add_data_source():
                st.session_state['data_sources'].append({"type": "", "details": ""})

            def delete_data_source(index):
                if st.session_state['data_sources_count'] > 1 and index > 0:
                    st.session_state['data_sources'].pop(index)
                    st.session_state['data_sources_count'] -= 1

            for i in range(st.session_state['data_sources_count']):
                st.subheader(f"Duomenų šaltinis {i + 1}")
                col1, col2 = st.columns([1, 3])

                with col1:
                    # Set key for automatic session state syncing
                    st.selectbox(
                        f"Tipas {i + 1}",
                        options=["DWH", "Sharepoint", "Excel", "API", "Kita"],
                        key=f"type_{i}"
                    )
                with col2:
                    # Set key for automatic session state syncing
                    st.text_area(
                        f"Detalės {i + 1}",
                        placeholder="Įrašykite detales apie šaltinį",
                        key=f"details_{i}"
                    )

                if st.session_state['data_sources_count'] > 1 and i > 0:
                    if st.button(f"Pašalinti šaltinį {i + 1}", key=f"delete_{i}"):
                        delete_data_source(i)

                if i == st.session_state['data_sources_count'] - 1:
                    if st.session_state.get(f'type_{i}') and st.session_state.get(f'details_{i}'):
                        if st.button("Pridėti naują duomenų šaltinį"):
                            add_data_source()
                            st.session_state['data_sources_count'] += 1
            
            # Show the Continue button only for the current step
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

    # Section 3: Transformacijos Sekcija (Step 3)
    if st.session_state['current_step'] >= 3:
        with st.expander("Svarbios atliktos transformacijos", expanded=False):

            if 'transformations_count' not in st.session_state:
                st.session_state['transformations_count'] = 1

            if 'transformations' not in st.session_state:
                st.session_state['transformations'] = [{"steps": ""}]

            def add_transformation():
                st.session_state['transformations'].append({"steps": ""})

            for i in range(st.session_state['transformations_count']):
                st.subheader(f"Transformacija {i + 1}")
                st.text_area(
                    f"Pagrindiniai punktai {i + 1}",
                    placeholder="Pateikite pagrindinius duomenų transformacijos veiksmus",
                    key=f"steps_{i}"
                )

                if i > 0:
                    if st.button(f"Pašalinti transformaciją {i + 1}", key=f"delete_transform_{i}"):
                        st.session_state['transformations'].pop(i)
                        st.session_state['transformations_count'] -= 1

                if i == st.session_state['transformations_count'] - 1:
                    if st.session_state.get(f'steps_{i}'):
                        if st.button("Pridėti naują transformaciją"):
                            add_transformation()
                            st.session_state['transformations_count'] += 1
            
            # Show the Continue button only for the current step
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

    # Section 4: Ataskaitos naujinimasis (Step 4)
    if st.session_state['current_step'] >= 4:
        with st.expander("Naujinimosi informacija", expanded=False):
            st.subheader("Naujinimosi informacija")

            st.session_state['frequency'] = st.radio("Atnaujinimų dažnumas", options=["Kasdien", "Kas savaitę", "Kas mėnesį"])
            st.session_state['update_time'] = st.time_input("Pasirinkite naujinimosi laiką", value=None)

            # Show the Continue button only for the current step
            if st.session_state['current_step'] == 4:
                missing_fields = check_for_missing_fields_section4()
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Tęsti", key="section4"):
                    st.session_state['attempted_section']['section4'] = True
                    if not missing_fields:
                        next_section('section4')
                if st.session_state['attempted_section']['section4'] and missing_fields:
                    st.warning(f"Prašome užpildyti šiuos laukus: {', '.join(missing_fields)}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Section 5: Priskirtas Procesas (Step 5)
    if st.session_state['current_step'] >= 5:
        with st.expander("Įrankio konfiguracija", expanded=False):
            st.subheader("Įrankio konfiguracija")
            
            # Using st.columns for a more organized layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.session_state['orchestrator'] = st.radio("1. Ar naudojamas kodo orchestratorius?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['gitlab'] = st.radio("2. Ar yra GitLab integracija?", options=["Taip", "Ne"], index=1, horizontal=False)
            
            with col2:
                st.session_state['data_gateway'] = st.radio("3. Ar naudojamas Data Gateway?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['rls'] = st.radio("4. Ar yra įdiegta duomenų saugos sistema, pvz.: (RLS)?", options=["Taip", "Ne"], index=1, horizontal=False)

            process_options = [
                "L3 PROCESŲ GRUPĖ. ELEKTROS SKIRSTOMŲJŲ TINKLŲ VYSTYMAS",
                "L3 PROCESŲ GRUPĖ. GAMTINIŲ DUJŲ SKIRSTOMŲJŲ DUOJETIEKIŲ VYSTYMAS",
                "TBD"
            ]
            st.session_state['selected_processes'] = st.multiselect(
                "5. Kokiems procesams priklauso įrankis?",
                options=process_options,
                placeholder="Nurodykite, prie kokio proceso ar verslo srities priskirta ataskaita"
            )

            # Show the Continue button only for the current step
            if st.session_state['current_step'] == 5:
                missing_fields = check_for_missing_fields_section5()
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Tęsti", key="section5"):
                    st.session_state['attempted_section']['section5'] = True
                    if not missing_fields:
                        next_section('section5')
                if st.session_state['attempted_section']['section5'] and missing_fields:
                    st.warning(f"Prašome užpildyti šiuos laukus: {', '.join(missing_fields)}")
                st.markdown('</div>', unsafe_allow_html=True)

    # Section 6: Komentarai / Pastabos (Step 6)
    if st.session_state['current_step'] >= 6:
        with st.expander("Komentarai / Pastabos", expanded=False):
            st.subheader("Komentarai / Pastabos")
            st.session_state['comments'] = st.text_area("Komentarai / Pastabos", placeholder="Pateikite papildomus komentarus arba pastabas")

            # Show the Submit button at the end
            if st.session_state['current_step'] == 6:
                st.markdown('<div class="center-button">', unsafe_allow_html=True)
                if st.button("Baigti pildyti ir pateikti duomenis", key="section6"):
                    st.session_state['attempted_section']['section6'] = True
                    next_section('section6')
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

def main():
    # Create a navbar with custom page names
    page = st_navbar(["Pagrindinis", "TOP ataskaitos", "Įrankio perdavimas"], styles=styles)

    # Display selected page content
    if page == "Pagrindinis":
        pagrindinis_page()
    elif page == "TOP ataskaitos":
        top_ataskaitos_page()
    elif page == "Įrankio perdavimas":
        ataskaitos_dokumentacija_page()

if __name__ == "__main__":
    main()

