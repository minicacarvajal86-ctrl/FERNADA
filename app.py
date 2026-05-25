from flask import Flask, render_template


app = Flask(__name__)


TOP_BRANDS = ["Aurora Cinema", "Aurora Screens", "Aurora Gold", "AURORA VIP"]

SIDEBAR_LINKS = [
    {"label": "Inicio", "icon": "icons-home.svg"},
    {"label": "Peliculas", "icon": "icons-movie.svg"},
    {"label": "Estrenos", "icon": "icons-megaphone.svg"},
    {"label": "Cartelera", "icon": "icons-ticket.svg"},
    {"label": "Mi lista", "icon": "icons-bookmark.svg"},
    {"label": "Aurora VIP", "icon": "icons-card.svg"},
    {"label": "Promociones", "icon": "icons-offer.svg"},
    {"label": "Configuracion", "icon": "icons-settings.svg"},
]

RECENT_RELEASES = [
    {
        "title": "Mortal Kombat II",
        "meta": "Accion intensa",
        "tag": "Recien agregada",
        "image": "https://p16-cc-image-search-sign-sg.ibyteimg.com/tos-alisg-i-h9hire4aei-sg/image/c429d8418ce3b3486fe51469ff96e5dc~tplv-h9hire4aei-image.jpeg?rk3s=add9cc80&x-expires=1784857055&x-signature=XzIm6sDi60YAmYq69QaVRTPNY20%3D",
    },
    {
        "title": "The Mandalorian and Grogu",
        "meta": "Sci-fi premium",
        "tag": "Top estreno",
        "image": "https://p16-cc-image-search-sign-sg.ibyteimg.com/tos-alisg-i-h9hire4aei-sg/image/59d6c6d75e57f3106389694b6e94b12a~tplv-h9hire4aei-image.jpeg?rk3s=add9cc80&x-expires=1784857090&x-signature=ahmdnQMOAZ2u59MoaCBgveVMQEk%3D",
    },
    {
        "title": "The Mummy",
        "meta": "Terror de estreno",
        "tag": "Lanzamiento",
        "image": "https://www.alamy.com/aggregator-api/download?url=https://h7.alamy.com/comp/3DFJKHJ/the-mummy-2026-directed-by-lee-cronin-and-starring-jack-reynor-laia-costa-and-may-calamawy-a-modern-expedition-awakens-an-ancient-evil-unleashing-a-curse-that-binds-a-fractured-family-to-a-vengeful-supernatural-force-us-teaser-poster-editorial-use-only-credit-bfa-warner-bros-3DFJKHJ.jpg",
    },
    {
        "title": "Undertone",
        "meta": "Suspenso A24",
        "tag": "Tendencia",
        "image": "https://i.ytimg.com/vi/j6uDeBYDHu4/maxresdefault.jpg",
    },
    {
        "title": "In the Grey",
        "meta": "Thriller de autor",
        "tag": "Nueva llegada",
        "image": "https://i.ytimg.com/vi/IH0jGUjaiuI/maxresdefault.jpg",
    },
    {
        "title": "Michael",
        "meta": "Evento musical",
        "tag": "Proximamente",
        "image": "/static/posters/michael.svg",
    },
]

FEATURED_PREMIERE = {
    "title": "Mortal Kombat II",
    "tag": "Estreno cinematografico",
    "headline": "Mortal Kombat II llega con acceso VIP temprano",
    "description": (
        "Aurora VIP, una experiencia unica con acceso preferencial, beneficios "
        "premium y una forma mas exclusiva de vivir cada estreno."
    ),
    "meta": ["Acceso anticipado", "Sala VIP", "Combos premium"],
    "schedule": "Preestreno 8:30 PM",
    "image": "https://p16-cc-image-search-sign-sg.ibyteimg.com/tos-alisg-i-h9hire4aei-sg/image/c429d8418ce3b3486fe51469ff96e5dc~tplv-h9hire4aei-image.jpeg?rk3s=add9cc80&x-expires=1784857055&x-signature=XzIm6sDi60YAmYq69QaVRTPNY20%3D",
}

LAUNCH_CALENDAR = [
    {
        "title": "Avatar: Fire and Ash",
        "date": "12 Jun",
        "format": "IMAX Laser",
        "image": "https://upload.wikimedia.org/wikipedia/en/9/95/Avatar_Fire_and_Ash_poster.jpeg",
    },
    {
        "title": "TRON: Ares",
        "date": "18 Jun",
        "format": "4DX",
        "image": "https://upload.wikimedia.org/wikipedia/en/0/06/Tron_Ares_poster.jpg",
    },
    {
        "title": "Batman Beyond",
        "date": "24 Jun",
        "format": "VIP Hall",
        "image": "https://image.tmdb.org/t/p/original/3hsxYIV0uJDK2eHVZgrv0z0PLHd.jpg",
    },
    {
        "title": "How to Train Your Dragon",
        "date": "02 Jul",
        "format": "Family Night",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/80/How_To_Train_Your_Dragon_2025_Poster.jpg",
    },
]

VIP_PLANS = [
    {
        "theme": "gold",
        "name": "Oro",
        "price": "$35.000",
        "caption": "Perfecto para cinéfilos frecuentes",
        "features": ["2 entradas al mes", "Fila preferencial", "10% en confiteria"],
        "featured": False,
    },
    {
        "theme": "diamond",
        "name": "Diamante",
        "price": "$66.000",
        "caption": "Experiencia premium total Aurora VIP",
        "features": ["4 entradas premium", "Sala VIP y preventas", "15% en combos y lounge"],
        "featured": True,
    },
]

VIP_EXCLUSIVES = [
    {
        "title": "Premier Aurora Originals",
        "tag": "Solo VIP",
        "caption": "Funciones de lanzamiento con acceso limitado antes del estreno general.",
        "theme": "premiere",
    },
    {
        "title": "Maraton Midnight Gold",
        "tag": "Noches exclusivas",
        "caption": "Sesiones especiales con cocteleria, lounge y experiencia inmersiva.",
        "theme": "midnight",
    },
    {
        "title": "Director's Cut Sessions",
        "tag": "Contenido premium",
        "caption": "Versiones extendidas, material inedito y conversatorios para miembros.",
        "theme": "director",
    },
]

VIP_BENEFITS = [
    {"title": "Asientos reclinables", "value": "Zona lounge", "kind": "lounge"},
    {"title": "Preventa anticipada", "value": "48 horas antes", "kind": "preventa"},
    {"title": "Combos premium", "value": "Hasta 15% OFF", "kind": "combo"},
    {"title": "Acumulacion de puntos", "value": "2X puntos", "kind": "points"},
]

SHOWCASE_METRICS = [
    {"label": "Pantalla principal", "value": "Portada cinematografica"},
    {"label": "Planes VIP", "value": "Oro / Diamante"},
    {"label": "Experiencia visual", "value": "Negro + dorado"},
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        featured_premiere=FEATURED_PREMIERE,
        top_brands=TOP_BRANDS,
        sidebar_links=SIDEBAR_LINKS,
        recent_releases=RECENT_RELEASES,
        launch_calendar=LAUNCH_CALENDAR,
        vip_plans=VIP_PLANS,
        vip_exclusives=VIP_EXCLUSIVES,
        vip_benefits=VIP_BENEFITS,
        showcase_metrics=SHOWCASE_METRICS,
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
