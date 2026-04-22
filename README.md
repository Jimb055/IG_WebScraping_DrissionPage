# Instagram Web Scraper - Proyecto de Ingeniería 🚀

Este proyecto es una herramienta de Web Scraping desarrollada en Python
para extraer de forma automatizada las últimas 10 publicaciones de
cualquier perfil público de Instagram.

A diferencia de los métodos tradicionales (como Selenium o Wrappers de
API), este script utiliza **DrissionPage** para interactuar directamente
con el navegador, lo que permite evadir sistemas de detección de bots y
muros de seguridad (WAF) como Cloudflare.

------------------------------------------------------------------------

##  Tecnologías Utilizadas

-   **Lenguaje:** Python 3.9+
-   **Automatización:** DrissionPage (Control directo de navegador sin
    WebDriver)
-   **Navegador:** Microsoft Edge (Motor Chromium)
-   **Fuente de Datos:** Mirror público (Imginn) para garantizar
    disponibilidad sin requerir login

------------------------------------------------------------------------

##  Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

-   Python 3.9 o superior
-   Microsoft Edge (instalado por defecto en Windows)
-   El gestor de paquetes pip

------------------------------------------------------------------------

##  Instalación y Configuración

### 1. Clonar el repositorio

``` bash
git clone https://github.com/tu-usuario/Web_scraping_ig.git
cd Web_scraping_ig
```

### 2. Instalar dependencias

``` bash
pip install DrissionPage
```

### 3. Configurar la ruta del navegador (Crítico)

``` python
# Ruta estándar en Windows 10/11
ruta_edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
```

------------------------------------------------------------------------

##  Ejecución

``` bash
python script.py
```

El script solicitará el nombre del usuario (ejemplo: `leomessi`) y
procederá a abrir una instancia de Edge para recolectar los datos.

------------------------------------------------------------------------

##  Salida (Output)

``` json
[
  {
    "id": 1,
    "caption": "Descripción del post...",
    "url_img": "https://url-de-la-imagen.jpg"
  },
  ...
]
```

------------------------------------------------------------------------

##  Notas

-   **Bypass de Seguridad:**\
    Se optó por DrissionPage para evitar la variable
    `navigator.webdriver`, la cual suele ser detectada por los firewalls
    de Instagram/Cloudflare en herramientas como Selenium o Playwright.

-   **Resiliencia:**\
    El script utiliza esperas inteligentes (`wait.ele_displayed`) para
    manejar el renderizado asíncrono de imágenes (lazy loading).
