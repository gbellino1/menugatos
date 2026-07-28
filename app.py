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
# SECCIÓN 2: MENÚ SEMANAL
# ---------------------------------------------------------
elif opcion_menu == "📅 Menú Semanal":
    st.title("Planificador de Menú Semanal 🗓️")
    st.write("Seleccioná las opciones que vas a preparar o que ya comiste. Los platos tildados se tacharán automáticamente para ayudarte a no repetir preparaciones.")

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
# SECCIÓN 3: RECETARIO INTEGRADO Y AMPLIADO
# ---------------------------------------------------------
elif opcion_menu == "📖 Recetario":
    st.title("Banco de Recetas 📖")
    st.write("Explorá nuestras recetas con ingredientes reales, alta densidad proteica y listas para integrarse a la rutina.")

    recetas = [
        {
            "nombre": "Brownie Proteico de Porotos Negros",
            "desc": "Un clásico denso y chocolatoso. Nadie adivina que está hecho de legumbres.",
            "tags": ["Desayuno", "Merienda", "Freezer", "Proteico"],
            "tiempo": "40 min", "porciones": "9 porciones", "proteina": "Alta", "dificultad": "Muy Fácil",
            "ingredientes": [
                "2 tazas porotos negros cocidos y escurridos", 
                "1/2 taza cacao amargo en polvo", 
                "1/2 taza avena en hojuelas", 
                "1/3 taza miel de caña o sirope", 
                "1/4 taza aceite de coco fundido", 
                "2 cdas semillas de chía hidratadas en 6 cdas de agua", 
                "1 cdita extracto de vainilla", 
                "1 pizca de sal marina",
                "Nueces picadas a gusto"
            ],
            "pasos": [
                "Precalentar el horno a 180°C y engrasar un molde cuadrado de 20x20 cm.",
                "Procesar los porotos cocidos con la chía hidratada y el aceite de coco hasta lograr una crema lisa.",
                "Agregar el cacao, la avena, el endulzante, la vainilla y la sal. Procesar hasta integrar bien.",
                "Volcar la mezcla en el molde, emparejar la superficie y colocar nueces por encima.",
                "Hornear durante 25-30 minutos. Dejar enfriar completamente antes de cortar en cuadrados."
            ],
            "por_que": "Lo preparamos durante el Meal Prep del domingo y nos asegura meriendas nutritivas para toda la semana."
        },
        {
            "nombre": "Escones de Lenteja Turca",
            "desc": "Salados, crocantes por fuera y suaves por dentro. Perfectos para acompañar hummus o palta.",
            "tags": ["Desayuno", "Merienda", "Freezer", "Sin Gluten"],
            "tiempo": "35 min", "porciones": "8 unidades", "proteina": "Alta", "dificultad": "Fácil",
            "ingredientes": [
                "1 taza lentejas turcas (rojas) remojadas 4 horas en agua",
                "1/4 taza aceite de oliva",
                "1/4 taza agua o bebida vegetal",
                "1 cdita polvo de hornear",
                "1 cdita sal fina y provenzal a gusto",
                "2 cdas semillas de sésamo o girasol para espolvorear"
            ],
            "pasos": [
                "Escurrir muy bien las lentejas remojadas.",
                "Procesar las lentejas con el aceite, el agua, la sal y los condimentos hasta obtener una masa pastosa.",
                "Agregar el polvo de hornear y mezclar suavemente.",
                "Formar bollitos sobre una placa de horno con papel manteca o silicona.",
                "Espolvorear con sésamo y hornear a 190°C por 20-25 minutos hasta que estén dorados."
            ],
            "por_que": "Aportan proteína y fibra desde la mañana de forma salada y súper práctica."
        },
        {
            "nombre": "Curry Rápido de Garbanzos",
            "desc": "El salvavidas cremoso y reconfortante para noches cansadas.",
            "tags": ["Almuerzo", "Cena", "Rápida", "Freezer"],
            "tiempo": "20 min", "porciones": "4 porciones", "proteina": "Alta", "dificultad": "Fácil",
            "ingredientes": [
                "2 latas de garbanzos (o 3 tazas cocidos)",
                "1 lata de leche de coco light",
                "2 tazas de espinaca fresca limpia",
                "1 cebolla grande picada fino",
                "2 dientes de ajo y 1 cda de jengibre rallado",
                "1 cda de curry en polvo + 1/2 cdita de comino",
                "Aceite de oliva, sal y pimienta"
            ],
            "pasos": [
                "En una olla, sofreír la cebolla, el ajo y el jengibre con oliva a fuego medio.",
                "Agregar el curry y comino, revolviendo 1 minuto para activar los aromas.",
                "Sumar los garbanzos escurridos y la leche de coco. Cocinar a fuego lento durante 10 minutos.",
                "Apagar el fuego, incorporar la espinaca fresca y revolver hasta que reduzca por el calor residual."
            ],
            "por_que": "Es nuestro 'plato abrazo'. Ensucia una sola olla y rinde impecable al recalentar."
        },
        {
            "nombre": "Fideos con Pestofu Creamy",
            "desc": "Salsa verde rica en proteínas que convierte un plato de pastas clásico en una bomba nutricional.",
            "tags": ["Almuerzo", "Cena", "Rápida", "Proteico"],
            "tiempo": "15 min", "porciones": "3 porciones", "proteina": "Alta", "dificultad": "Muy Fácil",
            "ingredientes": [
                "250g fideos integrales o de legumbres",
                "200g tofu firme",
                "1 taza de albahaca fresca",
                "1/4 taza de nueces o almendras",
                "2 cdas de levadura nutricional",
                "1 diente de ajo",
                "3 cdas de aceite de oliva, sal, pimienta y agua de cocción"
            ],
            "pasos": [
                "Cocinar los fideos en agua hirviendo con sal.",
                "En licuadora o procesadora, colocar el tofu, albahaca, frutos secos, ajo, levadura nutricional, oliva y sal.",
                "Procesar agregando chorritos de agua de la pasta caliente hasta lograr una textura cremosa.",
                "Mezclar el pestofu directamente con la pasta caliente recién escurrida."
            ],
            "por_que": "El tofu pasa desapercibido y le da una textura cremosa al pesto sin necesidad de crema pesada."
        },
        {
            "nombre": "Tacos de Lentejas sazonadas",
            "desc": "Relleno estilo 'carne picada vegetal' con especias intensas.",
            "tags": ["Cena", "Intermedio", "Meal Prep"],
            "tiempo": "25 min", "porciones": "4 porciones", "proteina": "Media-Alta", "dificultad": "Fácil",
            "ingredientes": [
                "2 tazas lentejas cocidas (al dente)",
                "1 cebolla y 1/2 morrón rojo picados",
                "1 cda pimentón ahumado, 1 cdita comino, 1/2 cdita ají molido",
                "2 cdas extracto de tomate",
                "Tortillas de maíz o trigo",
                "Para acompañar: palta, tomate picado y limón"
            ],
            "pasos": [
                "Saltear la cebolla y el morrón en una sartén con aceite de oliva hasta ablandar.",
                "Agregar las especias y el extracto de tomate, cocinando por 1 minuto.",
                "Incorporar las lentejas cocidas y aplastar un tercio de ellas con un tenedor para dar textura.",
                "Cocinar 5-7 minutos hasta que los sabores se integren.",
                "Servir caliente sobre tortillas doradas con palta y tomate fresco."
            ],
            "por_que": "Ideal para cenas divertidas de viernes. La mezcla de especias le da un sabor increíble."
        },
        {
            "nombre": "Falafel Dorado al Horno",
            "desc": "Croquetas tradicionales de garbanzos remojados pero horneadas para menor contenido de aceite.",
            "tags": ["Almuerzo", "Cena", "Freezer", "Sin Gluten"],
            "tiempo": "35 min", "porciones": "12 falafels", "proteina": "Alta", "dificultad": "Intermedio",
            "ingredientes": [
                "2 tazas garbanzos secos (remojados 12 hs, NO cocidos)",
                "1/2 taza cilantro fresco y perejil",
                "1 cebolla chica y 2 dientes de ajo",
                "1 cda comino en polvo, sal y pimienta",
                "1 cdita bicarbonato de sodio",
                "2 cdas aceite de oliva"
            ],
            "pasos": [
                "Escurrir y secar muy bien los garbanzos remojados.",
                "Procesar los garbanzos con cebolla, ajo, hierbas frescas y especias hasta obtener un granulado fino.",
                "Agregar sal y bicarbonato. Dejar reposar la mezcla 15 minutos en heladera.",
                "Formar bolitas ligeramente achatadas con las manos húmedas.",
                "Colocar en placa aceitada, pincelar con aceite de oliva y hornear a 200°C por 20 min girando a mitad de cocción."
            ],
            "por_que": "Se pueden congelar crudos y mandar directo al horno cuando hay poco tiempo."
        },
        {
            "nombre": "Pizza con Base de Garbanzo y Queso de Girasol",
            "desc": "Sin harinas refinadas. Una base crujiente y proteica recubierta de cebolla caramelizada.",
            "tags": ["Cena", "Elaborado", "Sin Gluten"],
            "tiempo": "45 min", "porciones": "2 personas", "proteina": "Alta", "dificultad": "Intermedio",
            "ingredientes": [
                "1 taza harina de garbanzo + 1 taza agua (para la fainá/base)",
                "2 cebollas grandes cortadas en pluma",
                "1/2 taza semillas de girasol remojadas 4 horas",
                "1 cda levadura nutricional, jugo de 1/2 limón, ajo en polvo y sal",
                "Orégano y aceitunas negras"
            ],
            "pasos": [
                "Mezclar la harina de garbanzo con el agua, 1 cda de oliva y sal. Dejar reposar 20 min.",
                "Caramelizar las cebollas a fuego lento en sartén con una pizca de sal.",
                "Procesar el girasol remojado con limón, levadura nutricional, sal y un hilo de agua hasta hacer una crema densa (queso vegetal).",
                "Volcar la mezcla de garbanzo en una pizzera aceitada y hornear a 200°C por 15 min hasta que firme.",
                "Cubrir con la crema de girasol, las cebollas salteadas, orégano y terminar de dorar en el horno."
            ],
            "por_que": "Satisface las ganas de pizza los fines de semana dejando una sensación súper liviana."
        },
        {
            "nombre": "Omelette Proteico",
            "porciones": "1-2 porciones",
            "proteinas": "18g",
            "ingredientes": [
                "1/2 taza de harina de garbanzos",
                "1/2 taza de agua o bebida vegetal sin endulzar",
                "1 cucharadita de cúrcuma",
                "1/2 cucharadita de sal negra Kala Namak (da sabor a huevo)",
                "1/2 taza de verduras picadas (espinaca, tomate, cebolla)",
                "1 cucharadita de aceite de oliva"
            ],
            "pasos": [
                "En un bol, mezclar la harina de garbanzos, el agua, la cúrcuma y la sal negra hasta obtener una mezcla homogénea sin grumos.",
                "Saltar brevemente las verduras elegidas en una sartén antiadherente con una gota de aceite.",
                "Verter la mezcla de garbanzo sobre las verduras repartiendo de manera uniforme.",
                "Cocinar a fuego medio tapado durante 4-5 minutos hasta que la superficie esté firme.",
                "Doblar por la mitad con cuidado, cocinar 1 minuto más y servir caliente."
            ]
        },
        {
            "nombre": "Falafel Crocante",
            "porciones": "12 unidades",
            "proteinas": "15g (por porción)",
            "ingredientes": [
                "1 taza de garbanzos secos (remojados por 12-24 hs, NO cocidos)",
                "1/2 cebolla picada",
                "2 dientes de ajo",
                "1/2 taza de perejil y cilantro fresco picado",
                "1 cucharadita de comino en polvo",
                "2 cucharadas de harina de garbanzo o avena",
                "Sal y pimienta al gusto",
                "1 cucharadita de polvo de hornear"
            ],
            "pasos": [
                "Procesar los garbanzos remojados y escurridos junto con la cebolla, ajo, hierbas y condimentos hasta lograr una pasta granulada.",
                "Agregar la harina de garbanzo y el polvo de hornear. Mezclar bien y dejar reposar en la heladera 30 minutos.",
                "Formar bolitas o hamburguesitas comprimiendo bien con las manos.",
                "Cocinar al horno a 200°C durante 20-25 minutos (girando a la mitad) o en airfryer hasta que estén dorados y crocantes."
            ]
        },
        {
            "nombre": "Tofu Revuelto Proteico",
            "porciones": "2 porciones",
            "proteinas": "22g",
            "ingredientes": [
                "200g de tofu firme",
                "1 cucharada de levadura nutricional",
                "1/2 cucharadita de cúrcuma",
                "1/2 cucharadita de sal negra Kala Namak",
                "2 cucharadas de bebida vegetal sin endulzar",
                "Pimienta negra y comino al gusto",
                "1 cucharada de aceite de oliva"
            ],
            "pasos": [
                "Desmigajar el tofu con las manos o un tenedor logrando trozos irregulares.",
                "En una sartén con aceite de oliva a fuego medio, colocar el tofu y saltear por 3 minutos.",
                "Añadir la cúrcuma, la levadura nutricional, la sal negra y las especias.",
                "Agregar la bebida vegetal para darle cremosidad y revolver durante 2-3 minutos hasta integrar.",
                "Servir solo o sobre tostadas integrales."
            ]
        },
        {
            "nombre": "Fainá Tradicional Proteica",
            "porciones": "4 porciones",
            "proteinas": "12g",
            "ingredientes": [
                "200g de harina de garbanzos",
                "600ml de agua a temperatura ambiente",
                "3 cucharadas de aceite de oliva",
                "1 cucharadita de sal fina",
                "Pimienta negra recién molida"
            ],
            "pasos": [
                "Mezclar la harina de garbanzos con la sal e incorporar el agua progresivamente batiendo con batidor de alambre para evitar grumos.",
                "Dejar reposar la mezcla al menos 1 hora (idealmente 3-4 horas). Retirar la espuma que se forma en la superficie.",
                "Precalentar el horno a 220°C con la pizzera o molde adentro.",
                "Agregar el aceite de oliva a la mezcla y verter con cuidado sobre la pizzera caliente.",
                "Hornear durante 25-30 minutos hasta que los bordes estén dorados y crocantes."
            ]
        },
        {
            "nombre": "Untable de Castañas y Levadura Nutricional",
            "porciones": "1 frasco (250g)",
            "proteinas": "10g (por porción)",
            "ingredientes": [
                "150g de castañas de cajú (remojadas en agua caliente 30 min)",
                "2 cucharadas de levadura nutricional sabor queso",
                "1/4 taza de agua",
                "2 cucharadas de jugo de limón",
                "1 diente de ajo pequeño (opcional)",
                "1/2 cucharadita de sal fina"
            ],
            "pasos": [
                "Escurrir y enjuagar las castañas de cajú remojadas.",
                "Colocar todos los ingredientes en una licuadora o procesadora de alta potencia.",
                "Procesar durante 3-5 minutos raspando los bordes hasta obtener una crema suave y homogénea.",
                "Ajustar sal o limón según el gusto y refrigerar antes de consumir."
            ]
        },
        {
            "nombre": "Pizza Proteica con Base de Legumbres",
            "porciones": "2 porciones",
            "proteinas": "28g",
            "ingredientes": [
                "1 taza de lentejas rojas o garbanzos remojados (4 horas)",
                "1/2 taza de agua",
                "1 cucharadita de orégano y ajo en polvo",
                "1/2 taza de salsa de tomate casera",
                "100g de queso vegetal derritible o tofu rallado",
                "Hojas de albahaca y vegetales a elección"
            ],
            "pasos": [
                "Licuar las lentejas rojas escurridas con el agua y los condimentos hasta obtener una pasta fluida.",
                "Verter sobre una sartén antiadherente o placa para horno con papel manteca formando un disco fino.",
                "Cocinar 7-10 minutos de un lado, dar vuelta y cocinar 3 minutos más.",
                "Cubrir con salsa de tomate, queso vegetal y vegetales. Hornear a 200°C hasta que el queso derrita."
            ]
        },
        {
            "nombre": "Salsa Boloñesa de Soja Texturizada",
            "porciones": "4 porciones",
            "proteinas": "25g",
            "ingredientes": [
                "1 taza de soja texturizada fina",
                "1 taza de caldo vegetal caliente",
                "1 cebolla grande picada",
                "1 zanahoria rallada",
                "1 pimiento rojo picado",
                "500g de tomate triturado",
                "2 dientes de ajo, orégano, pimentón dulce y laurel"
            ],
            "pasos": [
                "Hidratar la soja texturizada en el caldo vegetal durante 10 minutos. Escurrir bien el exceso de líquido.",
                "En una olla, saltear la cebolla, ajo, pimiento y zanahoria con aceite de oliva hasta que estén tiernos.",
                "Agregar la soja texturizada e incorporar el pimentón y orégano salteando 3 minutos.",
                "Verter el tomate triturado, sumar la hoja de laurel y cocinar a fuego lento durante 20 minutos.",
                "Servir sobre pastas integrales o legumbres."
            ]
        },
        {
            "nombre": "Tofu Agridulce Crocante",
            "porciones": "2 porciones",
            "proteinas": "24g",
            "ingredientes": [
                "300g de tofu firme prensado y en cubos",
                "2 cucharadas de fécula de maíz (maizena)",
                "2 cucharadas de salsa de soja",
                "1 cucharada de sirope de arce o agave",
                "2 cucharadas de vinagre de manzana o arroz",
                "1 cucharada de ketchup o concentrado de tomate",
                "1/2 taza de caldo vegetal"
            ],
            "pasos": [
                "Pasar los cubos de tofu por la fécula de maíz asegurando que queden bien cubiertos.",
                "Dorar los cubos en una sartén con aceite a fuego medio-alto hasta que estén crocantes de todos lados.",
                "En un bol pequeño, mezclar salsa de soja, sirope, vinagre, ketchup y el caldo vegetal.",
                "Verter la salsa sobre el tofu en la sartén y saltear a fuego medio hasta que la salsa espese y glacé el tofu."
            ]
        },
        {
            "nombre": "Milanesas de Seitán",
            "porciones": "6 milanesas",
            "proteinas": "32g (por unidad)",
            "ingredientes": [
                "1.5 tazas de gluten puro de trigo",
                "3 cucharadas de levadura nutricional",
                "1 cucharadita de pimentón ahumado y ajo en polvo",
                "1 taza de caldo vegetal sabroso (frío)",
                "Para rebozar: 1/2 taza de harina de garbanzo ligada con agua + pan rallado con semillas"
            ],
            "pasos": [
                "Mezclar el gluten, levadura nutricional y condimentos secos en un bol.",
                "Agregar el caldo vegetal e integrar rápidamente hasta formar una masa elástica.",
                "Cortar en 6 porciones y estirar con palo de amasar formando bifes finos.",
                "Hervir las milanesas en caldo durante 25 minutos. Escurrir y enfriar.",
                "Pasar por la mezcla de harina de garbanzo con agua (ligue) y luego por pan rallado. Hornear o freír hasta dorar."
            ]
        },
        {
            "nombre": "Pan Proteico de Lentejas",
            "porciones": "1 molde mediano",
            "proteinas": "12g (por rebanada)",
            "ingredientes": [
                "2 tazas de lentejas secas (remojadas 8 horas y escurridas)",
                "1/2 taza de agua",
                "1/4 taza de aceite de oliva",
                "1 cucharadita de sal",
                "1 cucharada de polvo de hornear",
                "Mix de semillas (chía, lino, sésamo) para decorar"
            ],
            "pasos": [
                "Procesar las lentejas remojadas con el agua, aceite de oliva y sal hasta obtener una masa homogénea.",
                "Incorporar el polvo de hornear y mezclar suavemente.",
                "Verter la mezcla en un molde para budín enharinado o con papel manteca.",
                "Espolvorear el mix de semillas por encima y hornear a 180°C durante 45-50 minutos."
            ]
        },
        {
            "nombre": "Hummus Clásico de Garbanzos",
            "porciones": "4 porciones",
            "proteinas": "10g",
            "ingredientes": [
                "400g de garbanzos cocidos",
                "2 cucharadas de tahini (pasta de sésamo)",
                "Jugo de 1 limón",
                "1 diente de ajo",
                "1/2 cucharadita de comino",
                "3 cucharadas de agua helada o hielo",
                "Aceite de oliva y pimentón para decorar"
            ],
            "pasos": [
                "Procesar los garbanzos cocidos, el tahini, el jugo de limón, ajo, comino y sal.",
                "Agregar el agua helada o cubitos de hielo mientras se procesa para lograr una textura ultra cremosa.",
                "Servir en un plato hondo con un chorro de aceite de oliva y pimentón ahumado."
            ]
        },
        {
            "nombre": "Guiso Proteico de Legumbres",
            "porciones": "4 porciones",
            "proteinas": "22g",
            "ingredientes": [
                "1 taza de lentejas cocidas",
                "1 taza de garbanzos cocidos",
                "1/2 taza de soja texturizada gruesa hidratada",
                "1 cebolla, 1 pimiento, 2 dientes de ajo",
                "1 batata en cubos y 1/2 taza de calabaza en cubos",
                "400g de tomate triturado y 2 tazas de caldo vegetal"
            ],
            "pasos": [
                "Saltear la cebolla, pimiento y ajo en una olla grande.",
                "Agregar la batata, la calabaza y la soja texturizada hidratada. Cocinar 5 minutos.",
                "Verter el tomate triturado y el caldo vegetal. Tapar y dejar cocinar a fuego medio hasta que los vegetales estén tiernos.",
                "Incorporar las lentejas y garbanzos cocidos. Cocinar 10 minutos más para integrar sabores."
            ]
        },
        {
            "nombre": "Tostada de Palta con Tofu Revuelto",
            "desc": "El reemplazo definitivo del huevo revuelto, lleno de cúrcuma y proteína vegetal.",
            "tags": ["Desayuno", "Merienda", "Rápida", "Proteico"],
            "tiempo": "10 min", "porciones": "2 tostadas", "proteina": "Media-Alta", "dificultad": "Muy Fácil",
            "ingredientes": [
                "150g tofu firme desmenuzado con tenedor",
                "1/2 cdita cúrcuma en polvo",
                "1/4 cdita sal negra (Kala Namak) para sabor ahuevo o sal común",
                "1 cdita levadura nutricional",
                "2 rodajas de pan integral de masa madre",
                "1/2 palta pisada con limón"
            ],
            "pasos": [
                "En sartén con unas gotas de oliva, saltear el tofu desmenuzado durante 3 minutos.",
                "Agregar la cúrcuma, sal negra y levadura nutricional. Revolver bien por 2 minutos más.",
                "Tostar el pan, untar con la palta pisada y colocar el tofu revuelto tibio encima."
            ],
            "por_que": "Aporta energía duradera y saciedad para arrancar mañanas activas."
        }
    ]

    # Controles de Búsqueda y Filtro en el Recetario
    col_busq, col_tag = st.columns([2, 2])
    with col_busq:
        search_query = st.text_input("🔍 Buscar por nombre o ingrediente:", "")
    with col_tag:
        tag_filtro = st.multiselect(
            "Filtrar por Etiqueta:",
            options=["Desayuno", "Merienda", "Almuerzo", "Cena", "Freezer", "Rápida", "Proteico", "Sin Gluten"],
            default=[]
        )

    # Filtrado lógico
    recetas_filtradas = []
    for r in recetas:
        coincide_texto = search_query.lower() in r['nombre'].lower() or search_query.lower() in r['desc'].lower() or any(search_query.lower() in ing.lower() for ing in r['ingredientes'])
        coincide_tag = True if not tag_filtro else any(t in r['tags'] for t in tag_filtro)
        
        if coincide_texto and coincide_tag:
            recetas_filtradas.append(r)

    st.divider()

    if not recetas_filtradas:
        st.info("No se encontraron recetas que coincidan con tu búsqueda.")
    else:
        for r in recetas_filtradas:
            with st.expander(f"🍲 {r['nombre']} — ⏱️ {r['tiempo']}"):
                st.write(f"*{r['desc']}*")
                
                # Badges de tags
                tags_html = " ".join([f"`{t}`" for t in r['tags']])
                st.markdown(f"**Etiquetas:** {tags_html} | **Dificultad:** {r['dificultad']} | **Proteína:** {r['proteina']} | **Rinde:** {r['porciones']}")
                
                col_ing, col_paso = st.columns(2)
                with col_ing:
                    st.markdown("#### 🛒 Ingredientes")
                    for ing in r['ingredientes']:
                        st.markdown(f"- {ing}")
                with col_paso:
                    st.markdown("#### 👨‍🍳 Preparación Paso a Paso")
                    for idx, paso in enumerate(r['pasos'], 1):
                        st.markdown(f"**{idx}.** {paso}")
                
                st.info(f"💡 **¿Por qué está en nuestro manual?:** {r['por_que']}")

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
        {"Alimento": "Panes y Escones", "Duración": "2-3 meses", "Método Recalentado": "Tostadora o sartén directo"},
        {"Alimento": "Legumbres cocidas", "Duración": "3 meses", "Método Recalentado": "Directo a sopas o sartén caliente"},
        {"Alimento": "Tofu prensado/marinado", "Duración": "3-5 meses", "Método Recalentado": "Descongelar y dorar en sartén"}
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
