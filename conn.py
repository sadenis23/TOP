import streamlit as st
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import text


def get_sql_connection():
    f_server = 'qpuyr2s222zuplnuhyog2iiq2i-qjnq56ukjhuu7pslxusprbzoly.datawarehouse.fabric.microsoft.com'
    f_database = 'TOP_Ataskaitos'
    f_driver='ODBC Driver 18 for SQL Server'
    f_user= 'sys-reportimport%40eso.lt' # use %40 inplace of @
    f_pass1='5ccM&TgZ2p^k%40ywv' # use %40 inplace of @
    f_connection_string = f'mssql+pyodbc://{f_user}:{f_pass1}@{f_server}/{f_database}?driver={f_driver}&Trusted_Connection=no&Authentication=ActiveDirectoryPassword'
    f_engine = sa.create_engine(f_connection_string, echo=True, connect_args={'autocommit': True}, fast_executemany=True)

    try:
        # Create SQLAlchemy engine with the connection string
        f_engine = sa.create_engine(f_connection_string, echo=True, connect_args={'autocommit': True}, fast_executemany=True)
        return f_engine
    except Exception as e:
        st.error(f"Error creating SQLAlchemy engine: {e}")
        return None

# Function to insert data into Azure SQL
def insert_report_data(report_data):
    engine = get_sql_connection()
    
    if engine is None:
        st.error("Failed to create the connection. Please check your settings.")
        return

    try:
        # Insert the report data into the table using SQLAlchemy
        with engine.connect() as conn:
            query = text("""
                INSERT INTO ataskaitos_duomenys_1 
                (Vardas, Pavarde, EL_Pastas, Pavadinimas, Savininkas, Tema, Kategorija, Skyrius, Kiti_Skyriai, Naudojimo_Daznumas, Naudojama_ESO_BL_Lentoje, Iseina_I_Isore, Komentarai_Pastabos)
                VALUES (:Vardas, :Pavarde, :EL_Pastas, :Pavadinimas, :Savininkas, :Tema, :Kategorija, :Skyrius, 
                        :Kiti_Skyriai, :Naudojimo_Daznumas, :Naudojama_ESO_BL_Lentoje, :Iseina_I_Isore, :Komentarai_Pastabos)
            """)
            conn.execute(query, report_data)
        st.success("Data successfully inserted into Azure SQL.")
    except Exception as e:
        st.error(f"Error inserting data: {e}")

# Function to submit the form data
def submit_form_data():
    if st.session_state.is_form_submitted:
        for report in st.session_state.reports:
            # Combine personal info with report data
            full_report_data = {**st.session_state.user_info, **report}
            insert_report_data(full_report_data)
        st.success("Ataskaitos sėkmingai pateiktos ir išsaugotos į Azure SQL!")


#------------------------------------------------------------------------------------------------------------------------------------------------------
# Set page layout and title
st.set_page_config(page_title="Power BI Dokumentacija", layout="centered")

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
        Pavadinimas = st.text_input("Ataskaitos pavadinimas *", key=f"pavadinimas_{report_index}", disabled=disabled_state)
        Savininkas = st.text_input("Ataskaitos savininkas *", key=f"savininkas_{report_index}", disabled=disabled_state)
        Tema = st.text_area("Ataskaitos tema *", key=f"tema_{report_index}", height=100, disabled=disabled_state)

        # Predefined multiselect categories with an option to add custom ones
        predefined_categories = ["SMART'ai", "GV", "Finansai", "Dujos", "Neeilinė situacija", "Kita"]
        Kategorija = st.multiselect("Kategorijos *", predefined_categories, key=f"kategorija_{report_index}", disabled=disabled_state)

        custom_categories = []
        if "Kita" in Kategorija:
            custom_categories = st_tags(label="Papildomos kategorijos", key=f"custom_category_{report_index}")
            Kategorija.extend(custom_categories)

        Skyrius = st.text_input("Skyrius *", key=f"skyrius_{report_index}", disabled=disabled_state)
        Skyriai = st.text_input("Kiti skyriai *", key=f"skyriai_{report_index}", disabled=disabled_state)
        NaudojimoDaznumas = st.selectbox("Naudojimo dažnumas *", ['Dažnai', 'Retai', 'Labai dažnai'], key=f"naudojimo_daznumas_{report_index}", disabled=disabled_state)
        EsoBLNaudojimas = st.radio("Naudojama ESO BL lentoje?", ['Taip', 'Ne'], key=f"eso_bl_{report_index}", disabled=disabled_state)
        Isore = st.radio("Ar išeina į išorę?", ['Taip', 'Ne'], key=f"isore_{report_index}", disabled=disabled_state)
        KomentaraiPastabos = st.text_area("Komentarai / Pastabos", key=f"komentarai_{report_index}", height=150, disabled=disabled_state)

        return {
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

# Function to check for missing fields in all reports
def check_for_missing_fields():
    missing_fields = []
    for i, report in enumerate(st.session_state.reports):
        fields = []
        for key, value in report.items():
            if not value:
                fields.append(key)
        if fields:
            missing_fields.append((i + 1, fields))
    return missing_fields

# Main form logic
display_personal_info()

# Display report forms
for i in range(len(st.session_state.reports)):
    report_data = display_report_form(i)
    if report_data:
        st.session_state.reports[i] = report_data

# Button to add a new report
if is_personal_info_filled():
    if st.button("Pridėti naują ataskaitą"):
        st.session_state.reports.append(display_report_form(len(st.session_state.reports)))
else:
    st.button("Pridėti naują ataskaitą", disabled=True)

# Button to submit the form
if is_personal_info_filled() and st.session_state.reports:
    st.markdown("---")
    if st.button("Baigti pildyti formą ir siųsti duomenis"):
        missing_fields = check_for_missing_fields()
        if missing_fields:
            st.warning("Nepavyko pateikti duomenų, nes kai kurių ataskaitų laukų trūksta:")
            for report_index, fields in missing_fields:
                st.warning(f"Ataskaita {report_index}: trūksta laukų: {', '.join(fields)}")
        else:
            st.session_state.is_form_submitted = True
            submit_form_data()

