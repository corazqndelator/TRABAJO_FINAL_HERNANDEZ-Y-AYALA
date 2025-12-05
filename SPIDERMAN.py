import streamlit as st #Importamos esta librería para que nuestra página web se muestre
import random #Esta nos servirá para el juego del ahorcado, donde se debe elegir una palabra al azar de una lista
import streamlit.components.v1 as components #Estos los componentes de streamlit
import pandas as pd #Y por último, esto nos sirve para muchas cosas, para leer archivos y más
#Configuración previa: Lo primero que haremos será crear una lista de 5 páginas que tendrá nuestra web
paginas = ["Conoce a Spiderman", "Películas y Series", "Conoce a los actores" ,"Mapa de Tiendas","Juega con los villanos"]
pagina = st.sidebar.selectbox("Elige una página", paginas) #Luego, crearemos una barra lateral que le permitirá al usuario elegir la sección a la que quiere ingresar
#Primera sección: Conoce a spiderman. Usamos bucle if para que cuando el usuario elija la página de conoce a spiderman, pueda ver esta sección y si no es así, ver otra
if pagina == "Conoce a Spiderman": 
    #lo primero que vamos a hacer es configurar el título con 
    st.markdown(#usamos markdown para poder personalizar nuestro título y colocar un texto, para eso importamos una fuente que queramos usar, lo alineamos, ponemos el tamaño y ponemos letras en color blanco
        """
        <style> 
        /* Fuente tipo Spider-Man */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');

        .spider-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 80px;
            text-align: center;
            color: white;  /* Letras blancas */
            text-shadow: 3px 3px 5px black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
#luego solo lo guardamos y colocamos el título que vamos a utilizar que es: 🕸️ Conoce el Spiderverse 
    st.markdown('<div class="spider-title">🕸️ Conoce el Spiderverse</div>', unsafe_allow_html=True)

    #ahora vamos con la división de columnas, usamos dos una para el texto de presentación y otra para las dos fotos que queremos poner
    col1, col2 = st.columns([2, 1]) #aqui dividimos en dos columnas 

    #la función with la usamos para utilizar la primera columna, esta es solo para el texto
    with col1:
        st.write("""
        **Peter Benjamin Parker**, reconocido como Spider-Man, es uno de los personajes más icónicos de Marvel Comics. 
        Apareció por primera vez en *Amazing Fantasy #15* en 1962, siendo creación de Stan Lee y Steve Ditko. 
        Originario de Queens y criado por sus tíos Ben y May tras la pérdida de sus padres, Peter destacó desde pequeño por su elevada inteligencia y amor por la ciencia, aunque era tímido y sufría acoso en la escuela. 
        Su existencia se transformó cuando una araña radioactiva lo picó mientras estaba en un laboratorio, otorgándole facultades sobrehumanas tales como fuerza, agilidad, reflejos mejorados, aptitud para escalar paredes y un “sentido arácnido”. 
        Inicialmente aprovechó estos dones para su propio interés, pero después de dejar escapar a un ladrón que más tarde asesinó a su tío Ben, entendió que “un gran poder implica una gran responsabilidad”, lema que orientaría toda su vida como héroe. 
        Desde entonces ha protegido Nueva York enfrentándose a villanos icónicos como el Duende Verde, Doctor Octopus, Venom y el Hombre de Arena, mientras lidia con su vida como estudiante, fotógrafo del Daily Bugle, científico y pareja de Mary Jane Watson, equilibrando siempre su identidad secreta con la protección de los inocentes.
        """) #ponemos tres comillas pq así funciona en visual studio code 

    #seguimos los mismos pasos para colocar las dos fotos, con width ponemos el tamaño que queremos
    with col2:
        #se importa las dos fotos que ya estaban en nuestra carpeta
        st.image("spiderman logo.jpg", width=300)
        st.image("spidermancito.jpg", width=300)

    #ahora con la función subheader lo que vamos a hacer es crear un subtitulo para la sección en donde crearemos el multiverso
    st.subheader("Explicando el multiverso") #y escribimos la explicación del multiverso
    st.write("""
    En la azotea de Nueva York, los tres Spider-Man, Tobey, Andrew y Tom, se encuentran por primera vez, sorprendidos pero unidos por un objetivo común. 
    Los amigos de Peter (Tom) se ven sumamente asustados. Mientras intentan organizarse, los villanos regresan por el portal interdimensional, desatando el caos en la ciudad. 
    Entre bromas y miradas cómplices, los tres héroes combinan sus estilos de lucha únicos, saltando entre edificios y lanzando telarañas, enfrentando juntos a los villanos. Podría ser la escena más icónica de la película *No Way Home*.
    """)

    #ahora dentro de esta misma condicional de la página, crearemos un botón para ver la escena del multiverso, cuando se juntan los tres, ahi le haremos click y nos abrirá el video de youtube que copiamos abajo
    if st.button("Ver escena multiverso"):
        st.video("https://www.youtube.com/watch?v=z8SoP46g5OY")

    st.markdown("---") #esta función de nuevo nos va ayudar a separar las secciones

    #ahora para mostrar escenas lo que vamos a hacer es crear secciones con una barra expander, un boton donde vas a clickear y aparecerá la información
    with st.expander("La muerte de Gwen Stacy"):
        st.image("gwen y peter.jpg", width=600) #ponemos dentro la imagen, que también está en la carpeta y escribimos la descripción
        st.write("""
        La noche en que murió Gwen Stacy es uno de los momentos más importantes y trágicos en la historia de Spider-Man. 
        En esta escena de The Amazing Spider-Man, el Duende Verde secuestra a Gwen Stacy, la novia de Peter Parker, y la arroja desde lo alto de un puente. 
        Spider-Man intenta salvarla lanzando una telaraña, pero el impacto repentino detiene su caída tan bruscamente que le rompe el cuello, causando su muerte. 
        Devastado y culpándose por no haberla podido salvar, Peter enfrenta al Duende Verde en una batalla final donde el villano termina muriendo accidentalmente empalado por su propio planeador. 
        Esta historia marcó un antes y un después en los cómics, mostrando que incluso los héroes pueden perder a las personas que aman.
        """)
        st.video("https://www.youtube.com/watch?v=euK99ix7CVU") #añadimos el video de la escena, solo con el link de youtube

    with st.expander("La muerte del Tío Ben"): #ahora con la misma función, lo hacemos con la muerte del tio ben exportando la foto, poniendo el texto y poniendo el link de youtube
        st.image("tio ben je.jpg", width=600)
        st.write("""
        La muerte del tío Ben ocurre cuando Peter Parker, todavía joven y recién obtenido sus poderes, decide no detener a un ladrón porque piensa que no es su responsabilidad. 
        Ese criminal termina escapando y, poco después, asesina al tío Ben durante un robo en su casa. 
        Al descubrir que él mismo dejó libre al asesino, Peter queda devastado por la culpa y entiende finalmente la lección que su tío siempre le enseñó: “un gran poder conlleva una gran responsabilidad”. 
        Ese error marca para siempre su vida y se convierte en el origen real de Spider-Man, impulsándolo a usar sus poderes para ayudar a los demás y evitar que alguien más sufra la misma pérdida que él.
        """)
        st.video("https://www.youtube.com/watch?v=wCh34ewYKFo")
#son funciones propias de streamlit, ppor eso todo comienza con st 
    with st.expander("Peter Parker reportero"):#hacemos lo mismo para peter parker reportero, exportamos la foto, colocamos el texto y subimos el video de youtube
        st.image("peter reportero.jpg", width=600)
        st.write("""
        El trabajo de Peter Parker como reportero fotográfico para el Daily Bugle le permite combinar su vida cotidiana con su identidad como Spider-Man. 
        Su labor consiste principalmente en capturar imágenes de su alter ego en acción para venderlas al periódico, enfrentándose a menudo al escepticismo y las críticas de J. Jonah Jameson, quien retrata al héroe como una amenaza. 
        Más allá del aspecto económico, este rol lo coloca en el centro de los eventos que sacuden Nueva York, le da acceso a información privilegiada y le permite difundir la verdad detrás de los superhéroes y los villanos.
        """)
        st.video("https://www.youtube.com/watch?v=sYekLbgY080")
#ACA FINALIZA LA SECCIÓN 1
#Seguimos con la sección 2, películas y series, lo hacemos con la condicional elife en donde nos dará la opción para acceder a otra sección de la página, cuando seleccionemos Películas y series, se abrirá este contenido
elif pagina == "Películas y Series":
    st.title("🎥 Películas y Series de Spiderman") #Colocamos el título con emojis 
    st.markdown(""" Estamos en la sección de Películas y Series, aquí, podrás encontrar todo el material audiovisual del universo de Spider-Man en orden para que sea más fácil verlas en pantalla. Solo avanza el círculo sobre la línea y las películas se mostrarán. Puedes también colocar un click sobre el círculo y avanzar con la flecha de tu teclado.
    """) #Y de nuevo, con la misma función cargamos la descripción
    #ahora lo diferente es que debemos desarrollar una forma de abrir el excel donde están todos nuestros datos
    df = pd.read_excel("pelis y series.xlsx") #usamos la función de read que lee archivos y los convierte en data frames una forma de limpiar los datos

    df.columns = df.columns.str.strip() #devuelve los nombres de las columnas del data frame y lo ponemos para solo mantener las 16 filas que queremos
    df = df.head(16) #usamos la función head que muestra solo los primeros datos hasta el 16 que es el rango colocado

    #convertimos los años a integrers o decimales para que no haya problemas al ordenarlos de menor a mayor. colocamos la fila de error para que cualquier cosa, si hay una celda vacía se ponga NAN
    df["Año"] = pd.to_numeric(df["Año"], errors="coerce").fillna(0).astype(int)

    #ahora con nuestra función de sort_values vamos a ordenar por año por defecto ordena de menor a mayor, 
    df = df.sort_values(by="Año").reset_index(drop=True)

    total = len(df)  #vemos que el total de columnas sea 16 con len que es para contar
#ahora procedemos a crear nuestra barra slider, guiados de los ejemplos dados. primero usamos la función de streamlit slider
    indice = st.slider(
        "Selecciona posición", #luego colocamos el texto donde se le indica al usuario que eliga la posición
        min_value=1,#empezamos en posición 1 
        max_value=total,#terminamos en el total de columnas
        value=1,
        step=1 #y vamos de uno en uno 
    )

    peli = df.iloc[indice - 1] #ahora usamos iloc para obtener los datos de cada producto audiovisual, normalmente contamos desde 1 pero pandas desde 0 por eso se le resta 1 al índice, así si el usuario, elige la tercera película accederá a la columna 2 y así

    año = peli["Año"] #primero configuramos que se vea el año de la película 

    st.write(f"### Posición: {indice}/{total}")
    st.markdown(f"## 🎬 {peli['Películas y series']} ({año})") #ahora colocamos esto para que nos salga el nombre de la película y al lado su año

    col1, col2 = st.columns([1, 2]) #nuevamente creamos dos columnas, para separar al poster de su texto

    with col1:
        poster = peli["Poster"] #añadimos la columna de poster en la columna 1, colocamos el nombre de la columna, 
        if isinstance(poster, str) and poster.strip() != "": #comprueba que sea realmente un string y por lo tanto una foto
            st.image(poster, width=300)

    with col2: #en la segunda columna, colocaremos todos los datos de nuestro excel, la forma con f string es para que nos salgan todos los datos en la misma línea
        st.write(f"### Director: {peli['Director']}") #primero colocamos el director
        st.write(f"### Spider-Man: {peli['Spider-Man (actor)']}") #luego  el actor que hace de spiderman
        st.write(f"### Villano(s): {peli['Villano(s)']}") #luego el villano
        st.write("### Resumen:") #ponemos el subtitulo resumen y abajo el texto respectivo
        st.write(peli["Resumen"]) 
        st.write(f"### 🎵 Canción: {peli['Canción']}") #colocamos la canción en link de youtube
        st.write(f"### Tipo: {peli['Película o serie']}") #colocamos si es serie o película
#todo esto lo hacemos dentro de la barra o slider para que mientras el usuario lo mueva la información vaya cambiando
#ACÁ FINALIZA LA SEGUNDA SECCIÓN 
# Tercera página: Conoce a los actores
elif pagina == "Conoce a los actores":#continuamos usando los condicionales para que cuando el usuario seleccione la seccion de conoce a los actores, le aparezca la información sobre estos
    st.title("🎭 Conoce a los Actores de Spider-Man") #ponemos el título como lo hemos hecho y añadimos una pequeña bievenidaa a la sección

    st.write("""
    Bienvenidos a la sección de **Conoce a los actores de Spider-Man**.  
    Aquí podrás ver a algunos de los actores principales de las películas, 
    junto con su personaje y una breve información.
    """)

    df = pd.read_excel("actores.xlsx") #nuevamente usamos la función de read para usar nuestra segunda base de datos, que son, los actores 

#para el buscador nos hemos guiado del modelo de paideia, donde puedes buscar a las personas de una lista por la inicial de su nombre o apellido
    st.subheader("🔎 Busca actores por inicial") #colocamos el título al buscador 

    letras = ["Todos"] + [chr(i) for i in range(ord("A"), ord("Z") + 1)] + ["Ñ"] #generamos todas las letras del abecedario e incluimos la ñ. se convierte con ord las letras a números, y luego de vuelta a letras solo para poder odenarlas

    colA, colB = st.columns(2) #hacemos nuevamente otras columnas, ahora a y b

    #en la columna a ponemos un select box para seleccionar la inicial del nombre de la lista letras
    with colA:
        inicial_nombre = st.selectbox("Inicial del Nombre:", letras)

    #hacemos lo mismo con el apellido, siguiendo los mismos pasos para que el usuario escoja que letra elegir
    with colB:
        inicial_apellido = st.selectbox("Inicial del Apellido:", letras)

    #ahora vamos a necesitar hacer una copia de 
    df_filtrado = df.copy()

    # primero vamos a filrar por nombre. ponemos todo en mayúsculas con upper para que no importa si está con mayúscula o minúscula
    if inicial_nombre != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["Nombre"].str.upper().str.startswith(inicial_nombre)
        ]

    #hacemos lo mismo para el apellido 
    if inicial_apellido != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["Nombre"].str.split().str[-1].str.upper().str.startswith(inicial_apellido)#starts with se utiliza para ver con qué inicia el apellido y filtrar el data frame para que solamente se muestre el actor que tenga como inicial la letra elegida
        ]

    #y ahora solo mostramos  cuantos actores se encontraron bajo los criterios seleccionados por el usuario
    st.write(f"🎬 **{len(df_filtrado)} actores encontrados**")
    st.markdown("---") #y añadimos una separación 

    for index, row in df_filtrado.iterrows(): #usamos esto para que iterrows itere sobre cada fila del excel y nos brinde los datos de todos los actores

        st.markdown("### ⭐ " + row["Nombre"]) #añadimos el nombre del actor junto a un emoji de estrella
        
        col1, col2 = st.columns([1, 2]) #nuevamente creamos dos columnas para separar la foto del texto

        #hacemos que en la primera columna se muestre la fotografía con la función with
        with col1:
            st.image(row["Foto"], width=180)


        #en la segunda columna, colocamos la información de los actores: nacionalidad, año de nacimiento, personaje
        with col2:
            st.write(f"**Nacionalidad:** {row['Nacionalidad']}") #primero colocamos la nacionalidad
            st.write(f"**Año de nacimiento:** {row['Año de nacimiento']}") #luego su año de nacimiento
            st.write(f"**Personaje:** {row['Personaje']}") #por último el personaje que interpreta
#ACÁ TERMINA LA TERCERA SECCIÓN 

#Cuarta página: Mapa de tiendas 
elif pagina == "Mapa de Tiendas":#volvemos a utilizar el condicional para que cuando el usuario abra la página de mapa de tiendas, aparezca la información correspondiente
    st.title("🗺️ Mapa de Tiendas") #añadimos un título
    st.markdown("""
    ¡Bienvenidos a la sección de tiendas! Este mapa muestra la ubicación de varias tiendas en Lima relacionadas a Spider-Man.
    Para ver la información de las tiendas, haz click en los íconos del mapa. Luego, si quieres conocer más información de esa tienda en específico, busca su nombre en el buscador de tiendas de la parte inferior. Esperamos que lo disfrutes.
    """) #y una pequeña introducción con los pasos a seguir para usar el mapa y el motor de búsqueda
    with open("mapa_tiendas.html", "r", encoding="utf-8") as f: #con la función with abrimos el mapa que descargamos en html
        html_map = f.read() #con esta función podemos leer el contenido del mapa que hicimos previamente en collab
    components.html(html_map, height=600) #ahora descargamos los componentes del mapa y le asignamos un tamaño
#ahora creamos un diccionario con todos los datos de las tiendas, su nombre, dirección, red social, número de teléfono, etc
    datos_tiendas = {
        "Tienda": [
            "Toy D Coleccion Juguetes y Figuras Lima Perú",
            "Akabane Comics",
            "Factory Comics Store",
            "Level 100 Store",
            "Origin Toys",
            "The best Collections",
            "Anime Import Perú",
            "Pierre Toys",
            "S Geek",
            "Blue Star Comics",
            "RED DE COLECCIONISTAS DEL PERÚ",
            "Librería Communitas",
            "Toy Master",
            "Game Center"
        ],
        "Direccion": [
            "Av. Gral. Juan Antonio Álvarez de Arenales 1700 - C, Lince 15046",
            "Av. Arenales 1737, Tienda 1-21 CC Arenales Plaza, Lince 15046",
            "Av. Gral. Juan Antonio Álvarez de Arenales 1624, Lince 15073",
            "Av. La Mar 2275, San Miguel 15088",
            "CC Caminos del Inca, Jr. Monterrey 170, Surco 15038",
            "Av. Arenales 1737, tda 3-25 2do nivel, Lince",
            "CC Arenales, Av. Arenales 1737, Lince 15046",
            "Av. Arenales 1737, Lince 15046",
            "Av. Arenales 1701, Lince 15046",
            "Jr. Camaná 964, Lima 15001",
            "Jirón Carabaya 1150, Lima 15001",
            "Av. Dos de Mayo 1690, San Isidro 15076",
            "Av. la Paz 138, Miraflores 15074",
            "Av. Aviación 5087 Polvos Rosados stand 76/29"
        ],
        "Red social": [
            "https://www.instagram.com/toydcoleccion/?hl=es",
            "https://www.facebook.com/pabloakabanecoleccionables/?locale=es_LA",
            "https://www.instagram.com/factory_comics/?hl=es",
            "https://www.instagram.com/level100store/",
            "https://www.instagram.com/origintoys/?hl=es",
            "https://www.instagram.com/explore/locations/263122847512850/the-best-collections/?hl=es#",
            "https://www.instagram.com/anime_import_peru/?hl=es-la",
            "https://www.facebook.com/PierreToys/?locale=es_LA",
            "https://www.facebook.com/sgeekcomic/?locale=es_LA",
            "https://www.instagram.com/bluestarcomics/",
            "https://www.instagram.com/rcp.sac/?hl=es",
            "https://www.instagram.com/libreriacommunitas/?hl=es",
            "https://www.instagram.com/toysmaster.pe/",
            "https://www.instagram.com/gamecenterlatam/?hl=es"
        ],
        "Telefono": [
            "997 336 926", "", "915 088 664", "942 403 965", "942 403 965",
            "(01) 4716612", "958 133 718", "922 563 111", "994 985 009",
            "994 564 514", "993 604 280", "965 433 850", "966 323 587", "931 464 789"
        ]
    }
#al finalizar, lo vamos a convertir en un data frame para poder utilizarlo en el motor de búsqueda
    df_tiendas = pd.DataFrame(datos_tiendas)
    st.header("🛒 Buscador de tiendas") #creamos un subtítulo para nombrar al buscador 
    busqueda = st.text_input("🔎 Escribe el nombre de la tienda: ").lower() #y colocamos un espacio para que el usuario coloque el nombre de la tienda, para esto usamos input
#y dentro del elif creamos un condicional para sistematizar el motor de búsqueda
    if busqueda:
        encontrado = False #crea una bandera que indica si se encontró una tienda que coincida con la búsqueda, como condición previa coloca que es falso y luego si encuentra un resultado válido entonces lo mostrará

        for i in range(len(df_tiendas)): #con len se obtiene el número de filas del data frame
            nombre = df_tiendas.loc[i, "Tienda"] #itera sobre cada fila y nos muestra los datos
#con búsqueda in se verifica si el texto buscado está dentro del nombre de la tienda como tal 
            if busqueda in nombre.lower(): #convierte el nombre de la tienda a minúsculas para que la búsqueda no se altere
                direccion = df_tiendas.loc[i, "Direccion"] #obtiene la dirección de la columna 
                red = df_tiendas.loc[i, "Red social"] #obtiene la red social de la columna y por último el teléfono
                telefono = df_tiendas.loc[i, "Telefono"]

                st.subheader(nombre) #muestra el nombre de la tienda como subtítulo en Streamlit.
                st.markdown(f"📍 **Dirección:** {direccion}")  #muestra la dirección
                st.markdown(f"🌐 **Red social:** [Visitar]({red})") #muestra la red social 
                st.markdown(f"📞 **Teléfono:** {telefono if telefono else 'No disponible'}") #muestra el teléfono si existe i está vacíomuestra no disponible

                encontrado = True #porque ya encontramos al menos una tienda

        if not encontrado: #si no se encuentra entonces alertará que no hay nada disponible 
            st.warning("😢 No se encontró ninguna tienda con ese nombre.")
#ACÁ TERMINA LA CUARTA SECCIÓN 
#Quinta página: Juega con los villanos donde vamos a crear un juego de ahorcado 
elif pagina == "Juega con los villanos": #por último, usamos nuestro último elif para que cuando el usuario escoja la sección de juego con villanos entonces se abrirá el contenido de está página
    st.title("🕸️ Juega con los villanos – Ahorcado") #creamos el título de la sección y generamos las indicaciones para utilizar el juego 
    st.write(
        "¡Bienvenido al juego del ahorcado! El juego consiste en adivinar el nombre del villano "
        "a partir de una pista dada con emojis y la cantidad de letras que tiene su nombre. "
        "Recuerda poner una letra por intento y que solo tienes 4 oportunidades"
    )
#vamos a crear un diccionario con los datos de todos los villanos, su nombre, descripción, foto y una pista dada cn emojis 
    villanos = {
        "duendeverde": {
            "descripcion": "El Duende Verde, cuyo portador principal es Norman Osborn, es uno de los enemigos más importantes y peligrosos de Spider-Man. Norman, un brillante pero ambicioso científico y empresario, desarrolla un suero experimental destinado a mejorar las capacidades humanas; al probarlo en sí mismo obtiene fuerza, velocidad y resistencia sobrehumanas, además de una capacidad de regeneración acelerada.",
            "foto": "DUENDE VERDE.jpg",
            "pista": "🟢🎃💣🛩️"
        },
        "octopus": {
            "descripcion": "El Doctor Octopus, cuyo nombre real es Otto Octavius, es uno de los villanos con cuatro brazos mecánicos altamente avanzados, diseñados para manipular materiales peligrosos y realizar experimentos de alta precisión. Durante un accidente en el laboratorio, una explosión fusiona permanentemente estos brazos a su cuerpo y, además, afecta su mente, volviéndolo más agresivo.",
            "foto": "octopus.jpg",
            "pista": "🐙🦾🦾🦾🦾"
        },
        "lagarto": {
            "descripcion": "El Lagarto en realidad es Dr. Curt Connors. Connors es un brillante científico y cirujano que pierde un brazo durante su servicio militar, lo que lo impulsa a investigar la regeneración de extremidades tomando como modelo a los reptiles. Prueba el ADN de lagarto y decide probarlo en sí mismo. El experimento funciona al principio y su brazo vuelve a crecer, pero pronto se desencadena un efecto secundario terrible: Curt se transforma en el Lagarto.",
            "foto": "lagarto.jpg",
            "pista": "🦎🧪🧬"
        },
        "el buitre": {
            "descripcion": "El Buitre, cuyo nombre real es Adrian Toomes, es un ingeniero brillante que se vuelve criminal después de ser estafado y perder todo lo que había construido. Usando un traje especial con alas mecánicas de su propio diseño, obtiene la capacidad de volar.",
            "foto": "buitre.jpg",
            "pista": "🦅⚙️🛩️"
        },
        "mysterio": {
            "descripcion": "Mysterio, cuyo nombre real es Quentin Beck, es un experto en efectos especiales, ilusionismo y trucos cinematográficos que decide usar su talento para el crimen. Beck crea ilusiones tan realistas que puede hacerle creer a cualquiera que ve monstruos, desastres o enemigos inexistentes, convirtiendo cada pelea en un engaño psicológico. Él es el villano que revelará la identidad de Spiderman como Peter Parker.",
            "foto": "mysterio.jpg",
            "pista": "🟣🎭✨"
        },
        "escorpión": {
            "descripcion": "El Escorpión, cuyo nombre real es Mac Gargan, fue originalmente un investigador contratado para descubrir cómo funcionaban las habilidades de Spider-Man. Pero, tras someterse a un experimento diseñado para darle poderes similares a los de un escorpión, obtiene una fuerza enorme, agilidad aumentada y un traje equipado con una cola mecánica extremadamente peligrosa.",
            "foto": "escorpión.jpg",
            "pista": "🦂🤖"
        },
        "rhino": {
            "descripcion": "Rhino, cuyo nombre real es Aleksei Sytsevich, es un criminal ruso que acepta someterse a un experimento para obtener fuerza sobrehumana. El procedimiento recubre su cuerpo con un traje casi indestructible fusionado a su piel, dándole una resistencia brutal y una velocidad de embestida que lo convierte en un “rinoceronte humano”",
            "foto": "rhino.jpg",
            "pista": "🦏💪"
        },
        "sandman": {
            "descripcion": "Sandman, cuyo nombre real es Flint Marko, obtiene sus poderes cuando un accidente con partículas experimentales transforma su cuerpo en arena viviente. Puede cambiar de forma, endurecerse, volverse gigante y convertir cualquier parte de su cuerpo en un arma. Aunque suele delinquir, Sandman no es completamente malvado, solo quiere ayudar a su familia",
            "foto": "sandman.jpg",
            "pista": "🏜️👊"
        },
        "electro": {
            "descripcion": "Electro, o Max Dillon, es un trabajador de una compañía eléctrica que adquiere la capacidad de generar y manipular electricidad tras ser alcanzado por un rayo durante un accidente laboral. Con sus nuevos poderes, desarrolla una personalidad arrogante y peligrosa, usando descargas, campos eléctricos y ataques de alta tensión para enfrentarse a Spider-Man.",
            "foto": "electro.jpg",
            "pista": "⚡⚡⚡"
        },
        "venom": {
            "descripcion": "Venom es un simbionte alienígena que primero se une a Spider-Man, otorgándole fuerza aumentada y un traje negro viviente, pero al sentir el rechazo de Peter termina fusionándose con Eddie Brock, un reportero resentido con él. La unión perfecta entre el odio de Eddie y el rencor del simbionte crea a Venom.",
            "foto": "venom.jpg",
            "pista": "🖤👅🕷️"
        }
    }
#terminamos con el diccionario y vamos a crear una forma de que el usuario pueda jugar al ahorcado
    if "palabra_secreta" not in st.session_state: #es un diccionario especial de sreamlit que permite guardar variables entre interacciones de usuario
        st.session_state.palabra_secreta = random.choice(list(villanos.keys())) #ahora usamos random choice  que elegirá un nombre random de la lista de villanos
        st.session_state.letras_adivinadas = []
        st.session_state.intentos = 0 #inicia en 0 intentos 
        st.session_state.intentos_maximos = 4 #y hay 4 inentos máximos 
        st.session_state.terminado = False
#esto hace que el juego solamente se desarrolla una vez, evitando reinicios cada vez que el usuario interactúa
    palabra = st.session_state.palabra_secreta #diccionario  de streamlit que guarda interacciones del usuario cada vez que juega 
    letras_adivinadas = st.session_state.letras_adivinadas #accede a cada clave que guardamos antes 
    intentos = st.session_state.intentos
    intentos_max = st.session_state.intentos_maximos
    progreso = "" #se crea una cadena vacía de progreso para que se represente la palabra a adivinar, solo saldrán los guiones de la cantidad de letras que tienen la palabra
    for letra in palabra: #recorre cada letra de la palabra secreta 
        if letra in letras_adivinadas: #ve si está en la lista de letras adivinadas
            progreso += f"{letra} "
        else:
            progreso += "_ " #si la letra fue adivinada, se coloca, sino solo un guión bajo 
#al inicio se mostrará que nuestro villano tiene una cantidad de letras específicas, luego mostrará el progreso 
    st.markdown(f"🔮 Tu villano misterioso tiene {len(palabra)} letras: {progreso.strip()}")
    st.markdown(f"**Pista:** {villanos[palabra]['pista']}") #además abajo saldrá la pista que asignamos a cada uno de los villanos
    st.markdown(f"Intentos restantes: {intentos_max - intentos}") #luego abajo también saldrá la cantidad de intentos que quedan que es 4 - los que ya intentó el usuario
    st.markdown(f"Letras intentadas: {', '.join(letras_adivinadas) if letras_adivinadas else '—'}") #si la letra aún no se adivina entonces aparecerá un guión

    if not st.session_state.terminado: #variable booleana que indica si el juego ya terminó
        intento = st.text_input("Adivina una letra:", max_chars=1).lower() #se usa input para que el usuario pueda escribir
#asegura que el bloque solo se ejecute mientras el juego no haya terminado
        if intento: #si el usuario escribe 
            if intento in letras_adivinadas: #si la letra adivinada ya fue intentada entonces se mostrará un mensaje afirmandolo
                st.info("🔁 Ya intentaste con esa letra.")
            else: 
                letras_adivinadas.append(intento) #agrega la letra a la lista de letras ya intentadas
                if intento in palabra:
                    st.success("🎯 ¡Sí! Esa letra está en el villano.") #comprueba que la letra que se colocó si está en la palabra 
                else:
                    st.session_state.intentos += 1
                    st.error(f"💔 Letra incorrecta. Te quedan {intentos_max - st.session_state.intentos} intento(s)...") #incrementa el número de intentos usados si la letra no está en la palabra

    if all(letra in letras_adivinadas for letra in palabra): #si el jugador adivina todas las letras
        st.balloons() #se muestran globlos
        st.success(f"🎉 ¡Ganaste! El villano era: {palabra.upper()} 🎉") #y el mensaje que afirma que ganó junto al nombre del villano
        st.write(villanos[palabra]["descripcion"]) #muestra la descripción del villano y una foto
        st.image(villanos[palabra]["foto"], width=300)
        st.session_state.terminado = True #aquí termina la sesión o el juego

    elif intentos >= intentos_max:#se ejecuta si no se ganó, pero se superaron los intentos máximos
        st.error(f"💀 Se acabaron los intentos. El villano era: {palabra.upper()}") #muestra un mensaje de error mostrando que perdió y que el villano era realmente: Nombre del villano
        st.write(villanos[palabra]["descripcion"]) #genera la descripción del villano no adivinado
        st.image(villanos[palabra]["foto"], width=300) #pone su foto
        st.session_state.terminado = True #termina la sesión

    if st.session_state.terminado: #crea un botón interactivo en la página y al presionarlo se elimina la sesión iniciada y puedes volver a jugar
        if st.button("🔄 Jugar otra vez"):
            for key in ["palabra_secreta", "letras_adivinadas", "intentos", "terminado"]:
                del st.session_state[key]

#acá termina la página
