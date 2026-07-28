import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA Y ESTILOS
# ---------------------------------------------------------
st.set_page_config(
    page_title="Nuestro Manual de Cocina",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para mantener la paleta original
st.markdown("""
    <style>
    /* Paleta: Armonía Natural */
    :root {
        --verde: #8A9A86;
        --arena: #E8E2DA;
        --terracota: #C97A63;
        --fondo: #FAF8F5;
    }
    
    .stApp {
        background-color: var(--fondo);
    }
    
    /* Títulos con estilo serif elegante */
    h1, h2, h3 {
        font-family: 'Playfair Display', Georgia, serif;
    }
    
    /* Badges para complejidad de menú */
    .badge-rapido {
        background-color: #D1E7DD;
        color: #0F5132;
        padding: 4px 10px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .badge-intermedio {
        background-color: #FFF3CD;
        color: #664D03;
        padding: 4px 10px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .badge-elaborado {
        background-color: #F8D7DA;
        color: #842029;
        padding: 4px 10px;
        border-radius: 12px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    
    /* Estilo de la tarjeta */
    .card-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #EAEAEA;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BASE DE DATOS DE MENÚ SEMANAL
# ---------------------------------------------------------
menu_data = [
    # Desayunos y Meriendas
    {"categoria": "Desayunos y Meriendas", "plato": "Batido de leche + fruta + proteína", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Tostadas + hummus + tomate + nueces", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Tostadas + pasta de mani + fruta + nueces", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Yogur + fruta + granola", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Barrita de cereal + fruta + nueces", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Galletitas + frutos secos y frutas", "tiempo": "Rápido"},
    {"categoria": "Desayunos y Meriendas", "plato": "Tostada con palta y tofu revuelto", "tiempo": "Intermedio"},
    {"categoria": "Desayunos y Meriendas", "plato": "Helado protéico + quinoa pop + nuces", "tiempo": "Intermedio"},
    {"categoria": "Desayunos y Meriendas", "plato": "Brownie protéico chocolate", "tiempo": "Intermedio"},
    {"categoria": "Desayunos y Meriendas", "plato": "Brownie protéico carrot", "tiempo": "Intermedio"},
    {"categoria": "Desayunos y Meriendas", "plato": "Escones de lenteja turca", "tiempo": "Elaborado"},
    {"categoria": "Desayunos y Meriendas", "plato": "Panqueques protéicos", "tiempo": "Elaborado"},
    {"categoria": "Desayunos y Meriendas", "plato": "Muffins proteicos + fruta", "tiempo": "Elaborado"},
    
    # Almuerzos y Cenas
    {"categoria": "Almuerzos y Cenas", "plato": "Milanesas + ensaladas", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Hambuguesas + ensalada", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Tofu + ensalada", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Tofu + verduras al horno", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Ensalada + legumbres", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Tarta de verduras + tofu", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Sopa de arvejas", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Arroz + verduras al horno", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Arroz con tomate y arvejas", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Milanesas + ensalada de papa zanahoria y arvejas", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Hamburguesas con verduras al vapor o puré", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Tofu + verduras al vapor", "tiempo": "Rápido"},
    {"categoria": "Almuerzos y Cenas", "plato": "Falafel con ensalada", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Ravioles con salsa bolognesa/blanca con hongos", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Omelette con cebolla y queso + ensalada", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Fideos de arroz + verduras salteadas", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Quinoa + verduras salteadas", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Tacos de lentejas", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Guiso de lentejas", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Fideos con pestofu", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Revuelto de tofu con zapallitos", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Curry de garbanzos", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Sopa de verduras con quinoa", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Brochete de tofu y verduras", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Zapallitos rellenos con quinoa", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Fideos de zucchini con bolognesa de soja", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Empanadas", "tiempo": "Intermedio"},
    {"categoria": "Almuerzos y Cenas", "plato": "Gnocchi di patate de gatitos", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Pastel de papas + lenteja/soja", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Arepas de porotos y hongos", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Lasagna de verduras", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Musaka de berenjena", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Sushi de pepino y tofu", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Pizza de garbanzos con verduras", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Bollitos de soja + verduras + papas al horno", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Pizza de garbanzos con cebolla y queso de girasol", "tiempo": "Elaborado"},
    {"categoria": "Almuerzos y Cenas", "plato": "Milanesa de coliflor con tofu", "tiempo": "Elaborado"}
]

# Inicializar Session State para checkboxes del menú
if "selected_meals" not in st.session_state:
    st.session_state.selected_meals = set()

# ---------------------------------------------------------
# MENÚ LATERAL DE NAVEGACIÓN
# ---------------------------------------------------------
st.sidebar.title("Nuestro Manual")
st.sidebar.markdown("*Versión Digital 2.0*")
st.sidebar.divider()

opcion_menu = st.sidebar.radio(
    "Navegación",
    [
        "🏠 Inicio", 
        "📅 Menú Semanal", 
        "📖 Recetario", 
        "⏳ Meal Prep", 
        "❄️ Freezer", 
        "🌱 Nutrición"
    ]
)

st.sidebar.divider()
st.sidebar.caption('"Que siempre encontremos disfrute en nutrirnos."')

# ---------------------------------------------------------
# SECCIÓN 1: INICIO
# ---------------------------------------------------------
if opcion_menu == "🏠 Inicio":
    st.title("Bienvenidos a nuestra cocina 🌿")
    st.markdown("""
    Este espacio es la extensión digital de nuestro manual físico. Aquí centralizamos la organización para que cocinar 
    no sea una carga, sino un acto de cuidado. Una guía viva, flexible y enfocada en la nutrición basada en plantas sin la 
    rigidez de las dietas convencionales.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-box">
            <h3 style="color: #8A9A86;">Filosofía Diaria</h3>
            <p>No buscamos la perfección. Buscamos reducir la fatiga de decisión. Si tenemos bases listas, comer bien es inevitable.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-box">
            <h3 style="color: #C97A63;">El Método</h3>
            <p>Cocinamos bases el domingo, congelamos el excedente y ensamblamos bowls o platos rápidos en minutos durante la semana.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("💡 **Sistema de Libertad:** Ingredientes Reales • Proteína Vegetal • Calma")

# ---------------------------------------------------------
# SECCIÓN 2: MENÚ SEMANAL (NUEVO MÓDULO)
# ---------------------------------------------------------
elif opcion_menu == "📅 Menú Semanal":
    st.title("Planificador de Menú Semanal 🗓️")
    st.write("Seleccioná las opciones que vas a preparar o que ya comiste. Los platos tildados se tacharán automáticamente para ayudarte a no repetir preparaciones.")

    # Filtros y controles top
    col_f1, col_f2, col_f3 = st.columns([2, 2, 1])
    
    with col_f1:
        cat_filtro = st.multiselect(
            "Filtrar por Categoría:",
            options=["Desayunos y Meriendas", "Almuerzos y Cenas"],
            default=["Desayunos y Meriendas", "Almuerzos y Cenas"]
        )
    with col_f2:
        tiempo_filtro = st.multiselect(
            "Filtrar por Tiempo/Elaboración:",
            options=["Rápido", "Intermedio", "Elaborado"],
            default=["Rápido", "Intermedio", "Elaborado"]
        )
    with col_f3:
        st.write(" ")
        st.write(" ")
        if st.button("🔄 Reiniciar Semana", use_container_width=True):
            st.session_state.selected_meals = set()
            st.rerun()

    st.divider()

    # Muestreo de datos por categoría
    for categoria in ["Desayunos y Meriendas", "Almuerzos y Cenas"]:
        if categoria in cat_filtro:
            st.subheader(f"🥣 {categoria}" if categoria == "Desayunos y Meriendas" else f"🍲 {categoria}")
            
            platos_cat = [m for m in menu_data if m["categoria"] == categoria and m["tiempo"] in tiempo_filtro]
            
            if not platos_cat:
                st.caption("No hay opciones que coincidan con los filtros elegidos.")
            
            for item in platos_cat:
                plato_id = f"{item['categoria']}_{item['plato']}"
                is_checked = plato_id in st.session_state.selected_meals
                
                col_check, col_plato, col_badge = st.columns([0.5, 4, 1.5])
                
                with col_check:
                    checked = st.checkbox("", value=is_checked, key=plato_id)
                    if checked:
                        st.session_state.selected_meals.add(plato_id)
                    else:
                        st.session_state.selected_meals.discard(plato_id)
                        
                with col_plato:
                    if checked:
                        st.markdown(f"~~{item['plato']}~~", unsafe_allow_html=True)
                    else:
                        st.markdown(f"**{item['plato']}**")
                        
                with col_badge:
                    if item['tiempo'] == 'Rápido':
                        st.markdown('<span class="badge-rapido">⚡ Rápido</span>', unsafe_allow_html=True)
                    elif item['tiempo'] == 'Intermedio':
                        st.markdown('<span class="badge-intermedio">⏱️ Intermedio</span>', unsafe_allow_html=True)
                    else:
                        st.markdown('<span class="badge-elaborado">👨‍🍳 Elaborado</span>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# SECCIÓN 3: RECETARIO
# ---------------------------------------------------------
elif opcion_menu == "📖 Recetario":
    st.title("Banco de Recetas 📖")
    
    recetas = [
        {
            "nombre": "Brownie Proteico de Porotos Negros",
            "desc": "Un clásico denso y chocolatoso. Nadie adivina que está hecho de legumbres.",
            "tags": ["Desayuno", "Merienda", "Freezer"],
            "tiempo": "40 min", "porciones": "9 porciones", "proteina": "Alta", "dificultad": "Muy Fácil",
            "ingredientes": ["2 tazas porotos negros cocidos", "1/2 taza cacao amargo", "1/2 taza avena", "1/3 taza sirope", "1/4 taza aceite coco", "2 cdas semillas chía", "Vainilla", "Pizca sal"],
            "pasos": ["Precalentar horno a 180°C.", "Procesar todos los ingredientes.", "Verter en molde 20x20.", "Hornear 25-30 min.", "Enfriar antes de cortar."],
            "por_que": "Lo hacemos el domingo y tenemos desayunos listos para toda la semana."
        },
        {
            "nombre": "Curry Rápido de Garbanzos",
            "desc": "El salvavidas cremoso y reconfortante para noches cansadas.",
            "tags": ["Almuerzo", "Cena", "Rápida", "Freezer"],
            "tiempo": "20 min", "porciones": "4 porciones", "proteina": "Alta", "dificultad": "Fácil",
            "ingredientes": ["2 latas garbanzos", "1 lata leche coco", "2 tazas espinaca", "1 cebolla", "Especias curry", "Jengibre y ajo"],
            "pasos": ["Sofreír cebolla, ajo y jengibre.", "Agregar especias y garbanzos.", "Incorporar leche de coco y cocinar 10 min.", "Apagar y sumar espinaca fresca."],
            "por_que": "Es nuestro 'plato abrazo'. Ensucia una sola olla y reconforta siempre."
        }
    ]
    
    for r in recetas:
        with st.expander(f"🍲 {r['nombre']} ({r['tiempo']})"):
            st.write(f"*{r['desc']}*")
            st.caption(f"**Etiquetas:** {', '.join(r['tags'])} | **Dificultad:** {r['dificultad']} | **Proteína:** {r['proteina']}")
            
            col_ing, col_paso = st.columns(2)
            with col_ing:
                st.markdown("**Ingredientes:**")
                for ing in r['ingredientes']:
                    st.markdown(f"- {ing}")
            with col_paso:
                st.markdown("**Pasos:**")
                for idx, paso in enumerate(r['pasos'], 1):
                    st.markdown(f"{idx}. {paso}")
            
            st.info(f"**¿Por qué nos encanta?:** {r['por_que']}")

# ---------------------------------------------------------
# SECCIÓN 4: MEAL PREP
# ---------------------------------------------------------
elif opcion_menu == "⏳ Meal Prep":
    st.title("Nuestras 2 Horas del Domingo ⏳")
    st.write("Checklist interactiva para dejar listos los bloques de construcción de la semana.")
    
    prep_items = [
        "Hervir legumbres (lentejas o garbanzos)",
        "Cocinar tanda de hummus base",
        "Preparar 2 tazas de quinoa o arroz integral",
        "Asar bandeja de calabaza y zanahoria",
        "Lavar y secar hojas verdes (rúcula/espinaca)",
        "Hornear snack dulce (Brownie o Muffins)",
        "Preparar aderezo base de tahini"
    ]
    
    completados = 0
    for item in prep_items:
        if st.checkbox(item, key=f"prep_{item}"):
            completados += 1
            
    progreso = completados / len(prep_items)
    st.progress(progreso)
    st.write(f"**Progreso:** {int(progreso * 100)}% completado")

# ---------------------------------------------------------
# SECCIÓN 5: FREEZER
# ---------------------------------------------------------
elif opcion_menu == "❄️ Freezer":
    st.title("Guía del Freezer ❄️")
    st.write("Consulta rápida para congelar y recalentar conservando sabor y textura.")
    
    freezer_df = pd.DataFrame([
        {"Alimento": "Hamburguesas Veggie", "Duración": "3-4 meses", "Método Recalentado": "Directo a sartén u horno"},
        {"Alimento": "Guisos y Currys", "Duración": "3 meses", "Método Recalentado": "Bajar a heladera noche anterior"},
        {"Alimento": "Panes y Masas", "Duración": "2-3 meses", "Método Recalentado": "Tostadora directo"},
        {"Alimento": "Legumbres cocidas", "Duración": "3 meses", "Método Recalentado": "Directo a sopas o agua caliente"},
        {"Alimento": "Tofu prensado", "Duración": "3-5 meses", "Método Recalentado": "Descongelar y marinar"}
    ])
    
    busqueda = st.text_input("🔍 Buscar alimento en el freezer:")
    if busqueda:
        freezer_df = freezer_df[freezer_df['Alimento'].str.contains(busqueda, case=False)]
        
    st.dataframe(freezer_df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# SECCIÓN 6: NUTRICIÓN Y GRÁFICOS
# ---------------------------------------------------------
elif opcion_menu == "🌱 Nutrición":
    st.title("Inteligencia Nutricional 🌱")
    
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        st.subheader("Densidad Proteica (g por porción)")
        df_prot = pd.DataFrame({
            'Alimento': ['Seitán', 'Tofu', 'Tempeh', 'Lentejas', 'Garbanzos', 'Cáñamo'],
            'Proteína (g)': [25, 20, 18, 9, 8, 10]
        })
        
        chart_prot = alt.Chart(df_prot).mark_bar(color='#8A9A86', cornerRadius=6).encode(
            x='Proteína (g):Q',
            y=alt.Y('Alimento:N', sort='-x')
        ).properties(height=300)
        
        st.altair_chart(chart_prot, use_container_width=True)
        
    with col_g2:
        st.subheader("Anatomía del Bowl Perfecto")
        df_bowl = pd.DataFrame({
            'Componente': ['Verdes', 'Carbohidratos', 'Proteína', 'Grasas'],
            'Porcentaje': [30, 30, 25, 15]
        })
        
        chart_bowl = alt.Chart(df_bowl).mark_arc(innerRadius=60).encode(
            theta=alt.Theta(field="Porcentaje", type="quantitative"),
            color=alt.Color(field="Componente", type="nominal", 
                            scale=alt.Scale(range=['#A3B19B', '#E8E2DA', '#8A9A86', '#C97A63']))
        ).properties(height=300)
        
        st.altair_chart(chart_bowl, use_container_width=True)
