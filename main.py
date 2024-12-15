import streamlit as st
from streamlit_tags import st_tags
import pandas as pd
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
from sqlalchemy import create_engine
import urllib
from sqlalchemy import VARCHAR
from sqlalchemy import text
from datetime import datetime
from typing import Dict
from urllib.parse import urlencode, quote_plus, unquote_plus
import re

st.set_page_config(page_title="📚 ESO Dokumentacija", layout="centered")

# Define function for each page
def pagrindinis_page():
    st.markdown("<h1 style='text-align: center;'>ESO dokumentacijos sistema</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 32px !important;
        font-weight: bold;
        color: #000000 !important;  /* Force green color */
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
                    <li><b>Ataskaitų tvarkymas ir dokumentacija</b> - Kiekvieną ataskaitą ar įrankį dokumentuokite aiškiai, nurodydami, kas ją sukūrė, kokie duomenys naudojami ir kokiam tikslui ji tarnauja. Tai užtikrina, kad svarbiausia informacija bus lengvai pasiekiama ir ateityje.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)


# TOP ATASKAITOS ------------------------------------------------------------------------------------------------------------------------------------------
def top_ataskaitos_page():
    # Set page layout and title
    st.markdown("<h1 style='text-align: center;'>TOP ataskaitos forma</h1>", unsafe_allow_html=True)


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
            color: #000000!important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Kodėl yra reikalinga turėti svarbiausių (TOP) Power BI ataskaitų sąrašą?", expanded=False):
        st.markdown("""
            <div style="background-color: #f0f4f7; padding: 20px; border-radius: 8px; border-left: 4px solid #32CD32;">
                <ol style="font-size: 16px; color: #333;">
                    <li><b>Suteikti aukštesnį prioritetą</b>, ypač kai jos neatsinaujina laiku.</li>
                    <li><b>DWH galės sparčiau atnaujinti</b> lentas šioms ataskaitoms.</li>
                    <li><b>Galimybė perkelti ataskaitas</b> į naują „capacity“ erdvę, kas pagerintų jų prieinamumą ir veikimo greitį.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

    def store_to_sql(df):
        # Connection details
        f_server = 'qpuyr2s222zuplnuhyog2iiq2i-qjnq56ukjhuu7pslxusprbzoly.datawarehouse.fabric.microsoft.com'
        f_database = 'Streamlit'
        f_driver = 'ODBC Driver 17 for SQL Server'
        f_user = 'sys-reportimport%40eso.lt'  # %40 represents @
        f_pass1 = '5ccM&TgZ2p^k%40ywv'  # %40 represents @

        # Create a connection string for SQLAlchemy
        connection_string = f'mssql+pyodbc://{f_user}:{f_pass1}@{f_server}/{f_database}?driver={f_driver}&Trusted_Connection=no&Authentication=ActiveDirectoryPassword'

        # Create a SQLAlchemy engine
        engine = create_engine(connection_string)

        # Use the correct table name with schema [TOP].[TOPAtaskaitos]
        table_name = '[TOP].[TOPAtaskaitos]'

        insert_query = f"""
        INSERT INTO {table_name} 
        (Vardas, Pavarde, El_Pastas, Pavadinimas, Savininkas, Tema, Kategorija, Papildoma_Kategorija, Skyrius, Kiti_Skyriai, Naudojimo_Daznumas, Naudojama_ESO_BL_Lentoje, Iseina_I_Isore, Komentarai_Pastabos, DateAdded)
        VALUES (:Vardas, :Pavarde, :El_Pastas, :Pavadinimas, :Savininkas, :Tema, :Kategorija, :Papildoma_Kategorija, :Skyrius, :Kiti_Skyriai, :Naudojimo_Daznumas, :Naudojama_ESO_BL_Lentoje, :Iseina_I_Isore, :Komentarai_Pastabos, :DateAdded)
        """

        try:
            with engine.begin() as connection:  # This will handle commits automatically
                for _, row in df.iterrows():
                    # Process categories: Use the first item as 'Kategorija' and the rest as 'Papildoma_Kategorija'
                    kategorijos = row['Kategorijos'] if isinstance(row['Kategorijos'], list) else [row['Kategorijos']]
                    primary_category = kategorijos[0] if kategorijos else ''
                    additional_category = ', '.join(kategorijos[1:]) if len(kategorijos) > 1 else ''

                    # Insert data into the table
                    connection.execute(text(insert_query), {
                        "Vardas": row['Vardas'],
                        "Pavarde": row['Pavarde'],
                        "El_Pastas": row['El. Paštas'],
                        "Pavadinimas": row['Pavadinimas'],
                        "Savininkas": row['Savininkas'],
                        "Tema": row['Tema'],
                        "Kategorija": primary_category,
                        "Papildoma_Kategorija": additional_category,
                        "Skyrius": row['Skyrius'],
                        "Kiti_Skyriai": row['Kiti skyriai'],
                        "Naudojimo_Daznumas": row['Naudojimo dažnumas'],
                        "Naudojama_ESO_BL_Lentoje": row['Naudojama ESO BL lentoje'],
                        "Iseina_I_Isore": row['Išeina į išorę'],
                        "Komentarai_Pastabos": row['Komentarai/Pastabos'],
                        "DateAdded": datetime.now()  # Insert current timestamp
                    })
        except Exception as e:
            st.error(f"Duomenų nepavyko išsiųsti: {e}")


    # Load report titles from Excel
    @st.cache_data
    def load_data_from_excel(file_path):
       return pd.read_excel(file_path, engine='openpyxl')

    file_path = r"//Users//nedasvaitkus//Desktop//AtaskaituDuomenis.xlsx"  # Replace with your actual path
    df = load_data_from_excel(file_path)

    # Assuming the report titles are in a column named 'Pavadinimas'
    report_titles = ["Pasirinkite..."] + df['Pavadinimas'].tolist()

    # Predefined categories for "Ataskaitos kategorija"
    predefined_categories = ["SMART'ai", "GV", "TP apkrovos" "Finansai", "Dujos", "Neeilinė situacija", "Kita"]

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
    if is_personal_info_filled() and not st.session_state.is_form_submitted:
        st.markdown("---")
        st.markdown('<div class="submit-button">', unsafe_allow_html=True)
        if st.button("Baigti pildyti formą ir siųsti duomenis"):
            missing_fields = check_for_missing_fields()
            if missing_fields:
                missing_fields_str = ', '.join(missing_fields)
                st.info(f"Neužpildyti šie laukai: {missing_fields_str}")
            else:
                # Create a placeholder for the status messages
                status_message = st.empty()

                # Show "Please wait" message
                status_message.info("Palaukite, duomenys yra siunčiami...")

                # Set flag to prevent further submissions
                st.session_state.is_form_submitted = True

                # Display submitted information
                st.markdown("## Jūsų pateikta informacija:")
                st.subheader("Asmeninė informacija")
                st.write(f"**Vardas:** {st.session_state.user_info['Vardas']}")
                st.write(f"**Pavardė:** {st.session_state.user_info['Pavarde']}")
                st.write(f"**El. Paštas:** {st.session_state.user_info['El. Paštas']}")

                st.markdown("## Ataskaita:")
                for key, value in st.session_state.report_data.items():
                    st.write(f"**{key}:** {value}")
                
                # Create a DataFrame and store to SQL
                combined_data = {**st.session_state.user_info, **st.session_state.report_data}
                df = pd.DataFrame([combined_data])

                # Store to SQL
                store_to_sql(df)

                # After storing the data, update the placeholder with success message
                status_message.success("✅ Duomenys pateikti sėkmingai!")
                st.balloons()
        
        st.markdown('</div>', unsafe_allow_html=True)

    # If the form is already submitted, show a warning
    elif st.session_state.is_form_submitted:
        st.warning("Ataskaita jau buvo pateikta šios sesijos metu. Negalima pateikti antrą kartą.")
                
# IRANKIO DOKUMENTACIJA--------------------------------------------------------------------------
def ataskaitos_dokumentacija_page():
    # Set page layout and title
    st.markdown("<h1 style='text-align: center;'>Dokumentacijos forma</h1>", unsafe_allow_html=True)

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
            color: #000000 !important;  /* Force green color */
            text-align: center;
            margin-bottom: 10px;
        }
        </style>
        <div class='sidebar-title'>Naudingos nuorodos</div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------------------
    def store_to_sql():
        # Connection details
        f_server = 'qpuyr2s222zuplnuhyog2iiq2i-qjnq56ukjhuu7pslxusprbzoly.datawarehouse.fabric.microsoft.com'
        f_database = 'Streamlit'
        f_driver = 'ODBC Driver 17 for SQL Server'
        f_user = 'sys-reportimport%40eso.lt'  # %40 represents @
        f_pass1 = '5ccM&TgZ2p^k%40ywv'  # %40 represents @

        # Create a connection string for SQLAlchemy
        connection_string = f'mssql+pyodbc://{f_user}:{f_pass1}@{f_server}/{f_database}?driver={f_driver}&Trusted_Connection=no&Authentication=ActiveDirectoryPassword'

        # Create a SQLAlchemy engine
        engine = create_engine(connection_string)

        # Use the correct table name with schema [TOP].[Dokumentacija]
        table_name = '[TOP].[Dokumentacija]'

        insert_query = f"""
        INSERT INTO {table_name} 
        (
            Pavadinimas, Tool_Name, Tool_URL, Workspace_URL, Executor, Clients, Tool_Type, 
            Purpose, Selected_Processes, Topics, Tags, Orchestrator, GitLab_Integration, 
            External_Tool, Data_Gateway, RLS, Fabric_Elements, Comments, 
            DataSource_Type, Details, Code_Fragment, Code_Comment, DateAdded
        ) 
        VALUES 
        (
            :Pavadinimas, :Tool_Name, :Tool_URL, :Workspace_URL, :Executor, :Clients, :Tool_Type, 
            :Purpose, :Selected_Processes, :Topics, :Tags, :Orchestrator, :GitLab_Integration, 
            :External_Tool, :Data_Gateway, :RLS, :Fabric_Elements, :Comments, 
            :DataSource_Type, :Details, :Code_Fragment, :Code_Comment, :DateAdded
        )
        """

        # Convert list of values into a comma-separated string for multiselect fields
        tool_type_str = ','.join(st.session_state['tool_type'])
        selected_processes_str = ','.join(st.session_state['selected_processes'])
        topics_str = ','.join(st.session_state['topics'])
        tags_str = ','.join([tema.strip() for tema in st.session_state['tags'].split(',')]) if 'tags' in st.session_state else ""
        fabric_elements_str = ','.join(st.session_state['fabric'])

        try:
            # Begin transaction and insert data
            with engine.begin() as conn:
                for i in range(st.session_state['data_sources_count']):
                    conn.execute(text(insert_query), {
                        'Pavadinimas': st.session_state.get('pavadinimas'),                   # Pavadinimas (Report Title)
                        'Tool_Name': st.session_state.get('tool_name'),                       # Tool_Name
                        'Tool_URL': st.session_state.get('tool_url'),                         # Tool_URL
                        'Workspace_URL': st.session_state.get('workspace'),                   # Workspace_URL
                        'Executor': st.session_state.get('executor'),                         # Executor
                        'Clients': st.session_state.get('clients'),                           # Clients
                        'Tool_Type': tool_type_str,                                           # Tool_Type (list -> str)
                        'Purpose': st.session_state.get('purpose'),                           # Purpose
                        'Selected_Processes': selected_processes_str,                         # Selected_Processes (list -> str)
                        'Topics': topics_str,                                                 # Topics (list -> str)
                        'Tags': tags_str,                                                     # Tags (from text input)
                        'Orchestrator': st.session_state.get('orchestrator'),                 # Orchestrator (Yes/No)
                        'GitLab_Integration': st.session_state.get('gitlab'),                 # GitLab_Integration (Yes/No)
                        'External_Tool': st.session_state.get('external'),                    # External_Tool (Yes/No)
                        'Data_Gateway': st.session_state.get('data_gateway'),                 # Data_Gateway (Yes/No)
                        'RLS': st.session_state.get('rls'),                                   # RLS (Yes/No)
                        'Fabric_Elements': fabric_elements_str,                               # Fabric_Elements (list -> str)
                        'Comments': st.session_state.get('comments'),                         # Comments (from text area),
                        'DataSource_Type': st.session_state.get(f'type_{i}'),                 # DataSource_Type
                        'Details': st.session_state.get(f'details_{i}'),                      # Details (Server/Database/Schema/Name)
                        'Code_Fragment': st.session_state.get(f'code_fragment_{i}'),          # Code_Fragment
                        'Code_Comment': st.session_state.get(f'code_comment_{i}'),            # Code_Comment
                        'DateAdded': datetime.now()                                           # DateAdded (current timestamp)
                    })

                # Show success message to the user after successful insertion
                st.success("✅ Duomenys pateikti sėkmingai!")

        except Exception as e:
            # Handle any exceptions that occur during the database operation
            st.error(f"Įvyko klaida siunčiant duomenis į duomenų bazę: {str(e)}")
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Initialize session state variables if not already present
    def initialize_session_state():
        if 'current_step' not in st.session_state:
            st.session_state['current_step'] = 1
        if 'section_completed' not in st.session_state:
            st.session_state['section_completed'] = {
                'section1': False,
                'section2': False,
                'section3': False,
                'section4': False
            }
        if 'form_in_progress' not in st.session_state:
            st.session_state['form_in_progress'] = False  # Track if form submission is in progress
        if 'attempted_section' not in st.session_state:
            st.session_state['attempted_section'] = {
                'section1': False,
                'section2': False,
                'section3': False,
                'section4': False
            }

    # Initialize session state variables
    initialize_session_state()

    # Function to proceed to the next section
    def next_section(section_key: str):
        # Mark the current section as completed
        st.session_state['section_completed'][section_key] = True
        st.session_state['attempted_section'][section_key] = True

        # Ensure current_step doesn't go beyond 4
        if st.session_state['current_step'] < 4:
            st.session_state['current_step'] += 1
            st.success(f"Perėjote į kitą žingsnį!")


    @st.cache_data
    def load_data_from_excel(file_path):
        return pd.read_excel(file_path, engine='openpyxl')

    file_path = r"//Users//nedasvaitkus//Desktop//AtaskaituDuomenis.xlsx"  # Replace with your actual path
    df = load_data_from_excel(file_path)
    # Assuming the report titles are in a column named 'Pavadinimas'
    report_titles = ["Pasirinkite..."] + df['Pavadinimas'].tolist()
    
    # Section 1: Pagrindinė įrankio informacija (Step 1)
    if st.session_state['current_step'] >= 1:
        with st.expander("1. Pagrindinė įrankio informacija", expanded=True):
            Pavadinimas = st.selectbox("Pasirinkite įrankio pavadinimą *", report_titles, key="pavadinimas")
            st.session_state['tool_name'] = st.text_input("Jei neradote įrankio pavadinimo, įrašykite", placeholder="Įrašykite įrankio pavadinimą")
            st.session_state['tool_url'] = st.text_input("Įrankio nuoroda", placeholder="Įklijuokite įrankio nuorodą")
            st.session_state['workspace'] = st.text_input("Įrankio workspace nuoroda (jei patalpintas)",
                                                        placeholder="Įklijuokite įrankio workspace nuorodą")

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

            tags = st.text_input("Jei galite priskirti daugiau įrankio tematikų, prašome jas įrašyti:", placeholder="Įrašykite temas atskirtas kableliais")
            if tags:
                temas_list = [tema.strip() for tema in tags.split(',')]
                st.write("**Pateiktos temos:**", ", ".join(temas_list))

            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            if st.button("Tęsti", key="section1"):
                st.session_state['attempted_section']['section1'] = True
                next_section('section1')
            st.markdown('</div>', unsafe_allow_html=True)

    # Section 2: Duomenų šaltiniai (Step 2)
    # Section 2: Duomenų šaltiniai (Step 2)
    if st.session_state['current_step'] >= 2:
        with st.expander("2. Duomenų šaltiniai", expanded=False):
            
            # Initialize session state for data sources
            if 'data_sources_count' not in st.session_state:
                st.session_state['data_sources_count'] = 1

            if 'data_sources' not in st.session_state:
                st.session_state['data_sources'] = [{"type": "", "details": "", "code_language": "", "code_fragment": ""}]
            
            # Add new data source
            def add_data_source():
                st.session_state['data_sources'].append({"type": "", "details": "", "code_language": "", "code_fragment": ""})
                st.session_state['data_sources_count'] += 1
                st.rerun()  # Use st.rerun to refresh the UI

            # Delete a specific data source
            def delete_data_source(index):
                if st.session_state['data_sources_count'] > 1:
                    st.session_state['data_sources'].pop(index)
                    st.session_state['data_sources_count'] -= 1
                    st.rerun()  # Use st.rerun to refresh the UI

            for i in range(st.session_state['data_sources_count']):
                st.subheader(f"Duomenų šaltinis {i + 1}")
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.selectbox(f"Tipas", options=["DWH", "Sharepoint", "Excel", "API", "Kita"], 
                                key=f"type_{i}", index=0 if st.session_state['data_sources'][i]['type'] == "" else st.session_state['data_sources'][i]['type'])
                with col2:
                    st.text_input(f"Serveris/Duomenų bazė/Schema/Lenta/Pavadinimas", 
                                placeholder="Pateikite detales apie šaltinį", 
                                value=st.session_state['data_sources'][i]['details'], 
                                key=f"details_{i}")

                # Code-related input
                st.text_area(f"Komentaras apie šaltinį ir jo ypatumus", 
                            placeholder="Pateikite komentarą apie šaltinį", 
                            value=st.session_state['data_sources'][i]['code_fragment'], 
                            key=f"code_fragment_{i}")

                # Comment for code explanation
                st.text_input(f"Naudinga nuoroda (pvz. Gitlab nuoroda į atlitkas šaltinio transformacijas)", 
                            placeholder="Pridėkite šaltinio naudingą nuorodoą", 
                            value=st.session_state['data_sources'][i]['code_language'], 
                            key=f"code_comment_{i}")

                if st.session_state['data_sources_count'] > 1 and i > 0:
                    if st.button(f"Pašalinti šaltinį {i + 1}", key=f"delete_{i}"):
                        delete_data_source(i)

                if i < st.session_state['data_sources_count'] - 1:
                    st.markdown("---")

            # Add new data source button
            if st.button("Pridėti naują duomenų šaltinį"):
                add_data_source()

            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            if st.button("Tęsti", key="section2"):
                st.session_state['attempted_section']['section2'] = True
                st.session_state['current_step'] += 1
                st.success("Perėjote į kitą žingsnį!")
            st.markdown('</div>', unsafe_allow_html=True)


    # Section 3: Įrankio konfiguracija (Step 3)
    if st.session_state['current_step'] >= 3:
        with st.expander("3. Įrankio konfiguracija", expanded=False):
            st.subheader("Įrankio konfiguracija")

            col1, col2 = st.columns(2)

            with col1:
                st.session_state['orchestrator'] = st.radio("Ar naudojamas kodo orchestratorius?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['gitlab'] = st.radio("Ar yra GitLab integracija?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['external'] = st.radio("Ar įrankis išeina į išorę?", options=["Taip", "Ne"], index=1, horizontal=False)

            with col2:
                st.session_state['data_gateway'] = st.radio("Ar naudojamas Data Gateway?", options=["Taip", "Ne"], index=1, horizontal=False)
                st.session_state['rls'] = st.radio("Ar yra įdiegta duomenų saugos sistema (RLS)?", options=["Taip", "Ne"], index=1, horizontal=False)

            st.session_state['fabric'] = st.multiselect("Microsoft naudojami elementai", 
                options=[
                    "Data Factory", 
                    "Data Lake", 
                    "Lakehouse", 
                    "Data Warehouse", 
                    "Notebooks", 
                    "Spark Jobs", 
                    "Power BI", 
                    "Pipelines", 
                    "Real-time Analytics", 
                    "Synapse Data Explorer", 
                    "Dataflow Gen2", 
                    "Kusto Query Language (KQL)"
                ]
            )

            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            if st.button("Tęsti", key="section3"):
                st.session_state['attempted_section']['section3'] = True
                next_section('section3')
            st.markdown('</div>', unsafe_allow_html=True)

    # Section 4: Komentarai / Pastabos (Step 4)
    if st.session_state['current_step'] >= 4:
        with st.expander("4. Papildoma informacija", expanded=False):
            st.subheader("Papildoma informacija")
            st.session_state['comments'] = st.text_area("Pateikite pagrindinius įrankio iššūkius ar komentarus", placeholder="Pateikite papildomus komentarus arba pastabas")

            st.markdown('<div class="center-button">', unsafe_allow_html=True)
            
            # Check if the form has already been submitted
            if not st.session_state.get('form_submitted', False):
                if st.button("Baigti pildyti ir pateikti duomenis", key="section4"):
                    st.session_state['attempted_section']['section4'] = True
                    st.session_state['form_submitted'] = True  # Mark the form as submitted

                    # Show the blue info message while data is being sent
                    sending_message = st.info("Palaukite, siunčiami duomenys...")

                    # Trigger the SQL insertion process
                    store_to_sql()

                    # Replace the blue message with a success message
                    sending_message.empty()
                    st.balloons()

                    # Move to the next section or indicate completion
                    next_section('section4')
            else:
                st.warning("Dokumentacija jau buvo pateikta šios sesijos metu. Negalima pateikti antrą kartą.")  # Display a message if already submitted

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
        Jei turite klausimų ar kažkas neveikia, praneškite DAS komandai arba Nedui Vaitkui | © 2024 ESO.
    </div>
    """, unsafe_allow_html=True)
    
    

def main():
    # Define a compact, responsive navbar with refined styles
    page = option_menu(
        menu_title=None,  # Hide the menu title
        options=["Namai", "Forma", "Dokumentacija"],  # Navbar options
        icons=["house", "clipboard", "book"],  # Icons for each option
        menu_icon="cast",  # Optional menu icon
        default_index=0,  # Default selected index
        orientation="horizontal",  # Horizontal layout
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#FF4B4B",
                "width": "100%",  # Set full width for responsiveness
                "overflow": "hidden",  # Prevent overflow
            },
            "icon": {"color": "white", "font-size": "18px"},  # Smaller icons
            "nav-link": {
                "font-size": "14px",  # Slightly smaller font size
                "text-align": "center",
                "margin": "0px 5px",  # Reduce space between items
                "padding": "8px 10px",  # Adjust padding to fit longer text
                "color": "white",
                "background-color": "#FF4B4B",  # Red background for unselected links
                "border-radius": "5px",  # Rounded corners
            },
            "nav-link-selected": {
                "background-color": "#D32F2F",  # Dark Red for selected link
                "color": "white",
            },
            "nav-link:hover": {
                "background-color": "#FF6E6E",  # Hover color
                "color": "white",
            },
        },
    )


    # Display selected page content
    if page == "Namai":
        pagrindinis_page()
    elif page == "Forma":
        top_ataskaitos_page()
    elif page == "Dokumentacija":
        ataskaitos_dokumentacija_page()  
    show_footer()

if __name__ == "__main__":
    main()
