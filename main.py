import streamlit as st
from streamlit_tags import st_tags
import pandas as pd

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
            <div class="card-title">Instrukcijos</div>
            <div class="card-content">
                Sveiki atvykę į DAS komandos Power BI ataskaitų dokumentacijos ir svarbiausių (TOP) ataskaitų identifikavimo sistemą.
                Šioje aplikacijoje galite užpildyti TOP Ataskaitos formą, kad Jūsų ataskaita būtų priskirta prie prioritetinių.
                Taip pat suteikiama galimybė užpildyti ataskaitos dokumentaciją, kuri padės pagerinti duomenų valdymą bei jų prieinamumą.
            </div>
        </div>
    """, unsafe_allow_html=True)

def top_ataskaitos_page():
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
            background-color: #343a40;  /* grey background */
            color: white;  /* White text */
            font-size: 22px;  /* Adjust font size */
            border-radius: 8px;  /* Optional: Add rounded corners */
            padding: 10px 20px;  /* Optional: Add padding */
        }
        .stButton > button:hover {
            background-color: #23272b;  /* Darker green on hover */
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
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
                <ol style="font-size: 16px; color: #333;">
                    <li><b>Suteikti aukštesnį prioritetą</b>, ypač kai jos neatsinaujina laiku.</li>
                    <li><b>DWH galės sparčiau atnaujinti</b> lentas šioms ataskaitoms.</li>
                    <li><b>Galimybė perkelti ataskaitas</b> į naują „capacity“ erdvę, kas pagerintų jų prieinamumą ir veikimo greitį.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
    st.sidebar.markdown(
        """
        <style>
        .sidebar .bottom-image {
            position: absolute;
            bottom: 0;
            width: 100%;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.markdown("<div style='height: 50px !important;'></div>", unsafe_allow_html=True)  # Optional spacer to push the image to the bottom

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
        import streamlit as st

    # Set page layout and title
    #st.set_page_config(page_title="Power BI Dokumentacija", layout="centered")

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

    # Show personal info section and allow report input
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
        if st.button("Baigti pildyti formą ir siųsti duomenis"):
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


#--------------------------------------------------------------------------
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

            tags = st_tags(
                label="Jei nėra, pridėkite savo temų kategorijas:",
                text="Pridėkite temas",
                value=[],
                suggestions=["Finansai", "IT", "Analitika"],
            )
            st.write("**Pateiktos temos:**", ", ".join(tags))

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
# Main app logic
def main():
    st.sidebar.title("Navigacija")
    page = st.sidebar.selectbox(
        "Pasirinkite puslapį",
        ("Pagrindinis", "TOP ataskaitos", "Ataskaitos dokumentacija")
    )

    # Navigation logic
    if page == "Pagrindinis":
        pagrindinis_page()
    elif page == "TOP ataskaitos":
        top_ataskaitos_page()
    elif page == "Ataskaitos dokumentacija":
        ataskaitos_dokumentacija_page()

if __name__ == "__main__":
    main()
