import streamlit as st
from streamlit_tags import st_tags

# Set page layout and title
st.set_page_config(page_title="Įrankio Dokumentacija", layout="centered")

# Custom CSS to center buttons
st.markdown("""
    <style>
    .center-button {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Įrankio dokumentacija")
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

# Initialize attempt flags for all sections (tracks if "Continue" was clicked)
if 'attempted_section' not in st.session_state:
    st.session_state['attempted_section'] = {
        'section1': False,
        'section2': False,
        'section3': False,
        'section4': False,
        'section5': False,
        'section6': False
    }

# Function to handle progression
def next_section(section_key):
    st.session_state['section_completed'][section_key] = True
    st.session_state['current_step'] += 1
    st.success(f"Automatiškai išsaugota! Galite tęsti toliau. ")

# Validation functions for each section
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
    for i in range(st.session_state['data_sources_count']):
        if not st.session_state.get(f'type_{i}'):
            missing_fields.append(f"Tipas {i + 1}")
        if not st.session_state.get(f'details_{i}'):
            missing_fields.append(f"Detalės {i + 1}")
    return missing_fields

def check_for_missing_fields_section3():
    missing_fields = []
    for i in range(st.session_state['transformations_count']):
        if not st.session_state.get(f'steps_{i}'):
            missing_fields.append(f"Pagrindiniai punktai {i + 1}")
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
    if not st.session_state.get('data_gateway'):
        missing_fields.append("Data Gateway")
    if not st.session_state.get('gitlab'):
        missing_fields.append("GitLab integracija")
    if not st.session_state.get('rls'):
        missing_fields.append("Saugos sistema (RLS)")
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
