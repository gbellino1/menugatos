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

# ---------------------------------------------------------
# DICCIONARIO DE RECETAS (CONSERVADAS + NUEVAS AGREGADAS)
# ---------------------------------------------------------
RECETAS = {
    "Saladas": [
        # --- Recetas previas ---
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
        # --- Nuevas recetas agregadas ---
        {
            "nombre": "Pastel de Papas y Lentejas",
            "porciones": "4 porciones",
            "proteinas": "22g",
            "ingredientes": [
                "1 kg de papas peladas y hervidas",
                "2 tazas de lentejas cocidas",
                "1 cebolla grande y 1/2 pimiento picados",
                "1/2 taza de puré de tomate",
                "2 cucharadas de aceite de oliva, nuez moscada, sal y pimienta",
                "Levadura nutricional o queso vegetal para gratinar"
            ],
            "pasos": [
                "Hacer un puré suave con las papas hervidas, un chorrito de aceite de oliva, sal y nuez moscada.",
                "En una sartén, rehogar la cebolla y el pimiento. Agregar las lentejas cocidas y el puré de tomate. Condimentar al gusto y cocinar 5 minutos.",
                "En una fuente para horno, colocar la base de relleno de lentejas y cubrir de manera pareja con el puré de papas.",
                "Espolvorear levadura nutricional o queso vegetal por encima.",
                "Gratinar al horno a 200°C durante 15-20 minutos hasta que la superficie esté dorada."
            ]
        },
        {
            "nombre": "Lasagna de Verduras y Tofu",
            "porciones": "6 porciones",
            "proteinas": "20g",
            "ingredientes": [
                "Placas de lasagna precocidas",
                "300g de tofu firme desmenuzado",
                "2 tazas de espinaca picada cocida",
                "2 zucchinis cortados a lo largo en láminas finas",
                "3 tazas de salsa de tomate casera",
                "1/2 taza de levadura nutricional sabor queso",
                "Ajo en polvo, orégano, sal y pimienta"
            ],
            "pasos": [
                "Mezclar el tofu desmenuzado con la espinaca, levadura nutricional, ajo en polvo, sal y pimienta para crear el relleno cremoso.",
                "En un molde rectangular para horno, colocar una capa de salsa de tomate en el fondo.",
                "Alternar capas de placas de lasagna, láminas de zucchini, relleno de tofu y salsa.",
                "Finalizar con abundante salsa de tomate por encima y un toque de levadura nutricional.",
                "Cubrir con papel aluminio y hornear a 190°C durante 30 minutos; retirar el aluminio los últimos 10 minutos para dorar."
            ]
        },
        {
            "nombre": "Musaka de Berenjena",
            "porciones": "4 porciones",
            "proteinas": "18g",
            "ingredientes": [
                "2 berenjenas grandes cortadas en rodajas de 1 cm",
                "1.5 tazas de soja texturizada hidratada",
                "1 cebolla y 2 dientes de ajo picados",
                "400g de tomate triturado",
                "1/2 cucharadita de canela en polvo",
                "Salsa bechamel vegetal (2 cdas harina de avena, 1 cda aceite, 1.5 tazas leche vegetal, nuez moscada)"
            ],
            "pasos": [
                "Dorar las rodajas de berenjena al horno con apenas aceite durante 15 minutos hasta que estén tiernas.",
                "Saltear la cebolla, ajo y la soja texturizada. Incorporar el tomate y la canela, y cocinar 10 minutos.",
                "Preparar la bechamel vegetal revolviendo la harina y aceite a fuego medio, sumando la leche vegetal gradualmente hasta espesar.",
                "En una fuente, alternar capas de berenjena y boloñesa de soja. Cubrir con la salsa bechamel.",
                "Gratinar en el horno a 200°C por 20 minutos hasta dorar la superficie."
            ]
        },
        {
            "nombre": "Curry de Garbanzos y Coco",
            "porciones": "4 porciones",
            "proteinas": "16g",
            "ingredientes": [
                "2 tazas de garbanzos cocidos",
                "1 lata (400ml) de leche de coco",
                "1 cebolla picada y 1 taza de zapallo en cubos",
                "2 cucharadas de pasta de curry rojo o curry en polvo",
                "1 taza de espinacas frescas",
                "Aceite de coco, jengibre rallado, sal y cilantro"
            ],
            "pasos": [
                "Saltear la cebolla y los cubos de zapallo con un poco de aceite de coco y jengibre rallado en una olla.",
                "Agregar la pasta de curry y revolver durante 1 minuto para activar sus aromas.",
                "Verter la leche de coco y los garbanzos cocidos. Tapar y cocinar a fuego medio durante 15 minutos hasta que el zapallo esté tierno.",
                "Agregar las espinacas frescas sobre el final y revolver hasta que se marchiten.",
                "Servir bien caliente decorado con cilantro fresco picado y acompañado de arroz."
            ]
        },
        {
            "nombre": "Tarta de Verduras y Tofu",
            "porciones": "4 porciones",
            "proteinas": "17g",
            "ingredientes": [
                "1 tapa de tarta integral",
                "250g de tofu firme",
                "1 atado de acelga o espinaca rehogada",
                "1 cebolla y 1/2 pimiento salteados",
                "2 cdas de levadura nutricional",
                "1 cda de fécula de maíz disuelta en 3 cdas de agua",
                "Nuez moscada, sal y pimienta"
            ],
            "pasos": [
                "Procesar o licuar el tofu firme con la fécula disuelta, la levadura nutricional y los condimentos hasta obtener una crema espesa.",
                "Mezclar el tofu licuado con las verduras salteadas (acelga/espinaca, cebolla, pimiento).",
                "Forrar un molde de tarta con la masa integral y verter el relleno de verduras y tofu de forma pareja.",
                "Hornear a 190°C durante 30 a 35 minutos hasta que la masa esté crocante y el relleno firme."
            ]
        }
    ],
    "Dulces": [
        # --- Recetas previas ---
        {
            "nombre": "Pancakes Proteicos de Avena",
            "porciones": "2 porciones (6 pancakes)",
            "proteinas": "20g",
            "ingredientes": [
                "1 taza de harina de avena",
                "1 scoop (30g) de proteína vegetal en polvo (vainilla o neutra)",
                "1 banana madura pisada",
                "1 taza de bebida vegetal",
                "1 cucharadita de polvo de hornear",
                "1 cucharadita de canela"
            ],
            "pasos": [
                "Mezclar la banana pisada con la bebida vegetal.",
                "Agregar la harina de avena, la proteína vegetal, el polvo de hornear y la canela.",
                "Calentar una sartén antiadherente con unas gotas de aceite de coco.",
                "Verter porciones de mezcla y cocinar a fuego medio hasta que salgan burbujas, dar vuelta y dorar 1 minuto más."
            ]
        },
        {
            "nombre": "Bowl Desayuno Proteico de Frutos Rojos",
            "porciones": "1 porción",
            "proteinas": "24g",
            "ingredientes": [
                "200g de yogur vegetal espeso (o tofu sedoso batido)",
                "1 scoop de proteína vegetal sabor frutos rojos o vainilla",
                "1/2 taza de frutos rojos congelados",
                "Toppings: Granola casera, semillas de chía y manteca de maní"
            ],
            "pasos": [
                "Licuar el yogur vegetal con la proteína y los frutos rojos congelados hasta obtener una consistencia cremosa y firme.",
                "Servir en un bowl y decorar con la granola, las semillas de chía y una cucharada de manteca de maní."
            ]
        },
        {
            "nombre": "Mousse de Chocolate Proteico",
            "porciones": "2 porciones",
            "proteinas": "15g",
            "ingredientes": [
                "250g de tofu sedoso (silken tofu)",
                "3 cucharadas de cacao amargo en polvo",
                "3 cucharadas de sirope de arce, agave o endulzante a gusto",
                "1 cucharadita de extracto de vainilla",
                "50g de chocolate amargo derretido"
            ],
            "pasos": [
                "Colocar el tofu sedoso en la licuadora o procesadora.",
                "Añadir el cacao amargo, el endulzante, la vainilla y el chocolate derretido.",
                "Licuar a alta velocidad durante 2-3 minutos hasta que esté completamente suave.",
                "Verter en vasos individuales y refrigerar al menos 2 horas antes de servir."
            ]
        },
        {
            "nombre": "Cookies Proteicas de Maní y Chocolate",
            "porciones": "8 galletas",
            "proteinas": "8g (por galleta)",
            "ingredientes": [
                "1/2 taza de manteca de maní natural",
                "1/4 taza de sirope de agave o miel de caña",
                "1/2 taza de harina de avena",
                "1 scoop de proteína vegetal de chocolate o vainilla",
                "1/4 taza de chispas de chocolate amargo"
            ],
            "pasos": [
                "Mezclar la manteca de maní con el sirope hasta integrar bien.",
                "Agregar la harina de avena y la proteína vegetal formando una masa maleable.",
                "Incorporar las chispas de chocolate.",
                "Formar 8 bolitas, aplastarlas sobre una placa para horno con papel manteca y hornear a 180°C durante 10-12 minutos."
            ]
        },
        {
            "nombre": "Rolls de Canela Proteicos",
            "porciones": "6 rolls",
            "proteinas": "14g (por unidad)",
            "ingredientes": [
                "1.5 tazas de harina integral o de avena",
                "1 scoop de proteína de vainilla",
                "1 cucharada de polvo de hornear",
                "3/4 taza de yogur vegetal firme",
                "Relleno: 2 cucharadas de aceite de coco, 2 cucharadas de azúcar mascabo y 1 cucharada de canela"
            ],
            "pasos": [
                "Mezclar la harina, proteína, polvo de hornear y yogur vegetal hasta formar una masa suave.",
                "Estirar la masa con palo de amasar formando un rectángulo.",
                "Pincelar con el aceite de coco derretido y espolvorear la mezcla de azúcar mascabo y canela.",
                "Enrollar a lo largo y cortar en 6 rodajas.",
                "Colocar en un molde redondo y hornear a 180°C durante 20 minutos."
            ]
        },
        # --- Nuevas recetas agregadas ---
        {
            "nombre": "Brownie Proteico de Chocolate",
            "porciones": "8 cuadrados",
            "proteinas": "10g (por porción)",
            "ingredientes": [
                "1 taza de porotos negros o rojos cocidos (bien enjuagados)",
                "1/2 taza de cacao amargo en polvo",
                "1 scoop de proteína vegetal de chocolate",
                "1/3 taza de sirope de arce o endulzante a elección",
                "1/4 taza de manteca de maní",
                "1/2 taza de bebida vegetal",
                "1/2 taza de chispas de chocolate amargo"
            ],
            "pasos": [
                "Procesar los porotos cocidos junto con la bebida vegetal, la manteca de maní y el sirope hasta lograr una crema lisa.",
                "Incorporar el cacao amargo y el scoop de proteína vegetal, procesando nuevamente hasta integrar.",
                "Pasar la mezcla a un bol e incorporar con espátula las chispas de chocolate amargo.",
                "Verter en un molde cuadrado con papel manteca y hornear a 180°C durante 20-25 minutos.",
                "Dejar enfriar completamente antes de cortar en 8 porciones."
            ]
        },
        {
            "nombre": "Brownie Proteico Carrot Cake",
            "porciones": "8 cuadrados",
            "proteinas": "9g (por porción)",
            "ingredientes": [
                "1.5 tazas de zanahoria rallada finamente",
                "1 taza de harina de avena",
                "1 scoop de proteína vegetal sabor vainilla",
                "1/4 taza de nueces picadas",
                "1/3 taza de sirope o endulzante",
                "1/2 taza de leche vegetal",
                "1 cdita de canela y 1/2 cdita de jengibre en polvo"
            ],
            "pasos": [
                "Mezclar la harina de avena, la proteína de vainilla, la canela y el jengibre en un bol.",
                "Añadir la leche vegetal y el endulzante mezclando con batidor.",
                "Incorporar la zanahoria rallada y las nueces picadas envolviendo suavemente.",
                "Colocar la preparación en un molde antiadherente y hornear a 180°C por 25 minutos.",
                "Enfriar y cortar en barritas o cuadrados."
            ]
        },
        {
            "nombre": "Escones de Lenteja Turca",
            "porciones": "6 unidades",
            "proteinas": "11g (por unidad)",
            "ingredientes": [
                "1 taza de lentejas turcas (rojas) remojadas por 4 horas y escurridas",
                "1/2 taza de harina de avena",
                "2 cdas de aceite de oliva o coco",
                "1 cdita de polvo de hornear",
                "1 cda de endulzante o pizca de sal (según versión dulce o salada)",
                "Ralladura de 1 limón o naranja (para versión dulce)"
            ],
            "pasos": [
                "Procesar las lentejas turcas remojadas con el aceite y la ralladura cítrica hasta tener una pasta uniforme.",
                "Transferir a un bol y agregar la harina de avena, el polvo de hornear y el endulzante.",
                "Formar discos gruesos de masa de 2 cm de alto y cortar en triángulos (tipo scones).",
                "Ubicar en una placa para horno y hornear a 180°C durante 18-20 minutos hasta que estén dorados."
            ]
        },
        {
            "nombre": "Muffins Proteicos de Fruta",
            "porciones": "6 muffins",
            "proteinas": "8g (por unidad)",
            "ingredientes": [
                "1 taza de harina integral o de avena",
                "1 scoop de proteína vegetal de vainilla",
                "1 banana madura pisada",
                "1/2 taza de arándanos o manzanas picadas",
                "1/2 taza de leche vegetal",
                "1 cdita de polvo de hornear y 1 cdita de canela"
            ],
            "pasos": [
                "Integrar la banana pisada con la leche vegetal.",
                "Sumar la harina, la proteína en polvo, el polvo de hornear y la canela.",
                "Agregar la fruta elegida (arándanos o manzana) con movimientos envolventes.",
                "Repartir la masa en pirotines o molde para muffins y hornear a 180°C durante 18-20 minutos."
            ]
        }
    ],
    "Recetas Estrella": [
        # --- Recetas previas ---
        {
            "nombre": "Bao Buns Rellenos de Tofu Glaseado",
            "porciones": "4 panes",
            "proteinas": "22g",
            "ingredientes": [
                "Para los panes: 250g de harina 0000, 1/2 cucharadita de levadura seca, 150ml de agua tibia, 1 cda de azúcar",
                "Relleno: 250g de tofu firme salteado y glaseado con salsa barbacoa/soja",
                "Acompañamiento: Zanahoria y pepino encurtido, cilantro fresco"
            ],
            "pasos": [
                "Amasar los ingredientes del pan y dejar leudar 1 hora.",
                "Dividir en bollos, estirar en óvalos, doblar por la mitad con papel manteca en el centro y cocinar al vapor durante 10-12 minutos.",
                "Dorar el tofu en sartén y pincelar con el glaseado agridulce.",
                "Rellenar los panes bao tibios con el tofu, los vegetales encurtidos y cilantro."
            ]
        },
        {
            "nombre": "Niños Envueltos Proteicos",
            "porciones": "4 porciones",
            "proteinas": "20g",
            "ingredientes": [
                "8 hojas grandes de acelga o repollo blanco blanqueadas",
                "1 taza de soja texturizada fina hidratada",
                "1/2 taza de arroz integral cocido",
                "1 cebolla y 1 diente de ajo picados",
                "2 tazas de salsa de tomate casera"
            ],
            "pasos": [
                "Saltear la cebolla y el ajo, mezclar con la soja texturizada y el arroz cocido. Condimentar bien.",
                "Colocar una porción de relleno en cada hoja de acelga/repollo y doblar los bordes hacia adentro formando rollitos.",
                "Disponer los rollitos en una fuente para horno, cubrir con la salsa de tomate y hornear a 180°C durante 25 minutos."
            ]
        },
        {
            "nombre": "Tiramisú Proteico en Vaso",
            "porciones": "2 vasos",
            "proteinas": "18g",
            "ingredientes": [
                "100g de tostadas de arroz o vainillas caseras integrales",
                "1 taza de café expreso cargado sin azúcar",
                "200g de tofu sedoso o yogur griego vegetal",
                "1 scoop de proteína vegetal sabor vainilla",
                "2 cucharadas de endulzante a gusto",
                "Cacao amargo en polvo para espolvorear"
            ],
            "pasos": [
                "Procesar el tofu sedoso con la proteína de vainilla y el endulzante hasta obtener una crema suave.",
                "Humedecer las tostadas/vainillas en el café preparado.",
                "En vasos individuales, alternar capas de galletas humedecidas y crema proteica.",
                "Espolvorear cacao amargo en la superficie y enfriar en la heladera mínimo 1 hora."
            ]
        }
    ]
}

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
# SECCIÓN 3: RECETARIO COMPLETO (CONSERVADO + AMPLIADO)
# ---------------------------------------------------------
elif opcion_menu == "📖 Recetario":
    st.title("Banco de Recetas 📖")
    st.write("Explorá nuestras preparaciones divididas por categorías. Podés buscar por nombre o ingredientes.")

    # Filtros y Búsqueda
    col_busq, col_cat = st.columns([2, 2])
    with col_busq:
        search_query = st.text_input("🔍 Buscar por nombre o ingrediente:", "")
    with col_cat:
        cat_seleccionadas = st.multiselect(
            "Filtrar por Categoría:",
            options=list(RECETAS.keys()),
            default=list(RECETAS.keys())
        )

    st.divider()

    encontrados = 0

    for cat in cat_seleccionadas:
        recetas_categoria = RECETAS.get(cat, [])
        
        # Filtrado de recetas según el texto de búsqueda
        recetas_filtradas = []
        for r in recetas_categoria:
            coincide_nombre = search_query.lower() in r['nombre'].lower()
            coincide_ingrediente = any(search_query.lower() in ing.lower() for ing in r['ingredientes'])
            if coincide_nombre or coincide_ingrediente:
                recetas_filtradas.append(r)
        
        if recetas_filtradas:
            st.subheader(f"📌 {cat}")
            for r in recetas_filtradas:
                encontrados += 1
                with st.expander(f"🍲 {r['nombre']} — ⚡ Proteínas: {r['proteinas']}"):
                    st.markdown(f"**Rinde:** {r['porciones']} | **Aporte Proteico:** {r['proteinas']}")
                    st.markdown("---")
                    
                    col_ing, col_pasos = st.columns(2)
                    with col_ing:
                        st.markdown("#### 🛒 Ingredientes")
                        for ing in r['ingredientes']:
                            st.markdown(f"- {ing}")
                    
                    with col_pasos:
                        st.markdown("#### 👨‍🍳 Preparación Paso a Paso")
                        for idx, paso in enumerate(r['pasos'], 1):
                            st.markdown(f"**{idx}.** {paso}")
            st.markdown("<br>", unsafe_allow_html=True)

    if encontrados == 0:
        st.info("No se encontraron recetas que coincidan con la búsqueda.")

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
