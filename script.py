import json
from DrissionPage import ChromiumPage, ChromiumOptions
import re


def parse_number(text):
    """Convierte strings tipo '500M' o '10.5K' en enteros."""
    if not text: return 0
    text = text.upper().replace(',', '').strip()
    multiplier = 1
    if 'M' in text:
        multiplier = 1_000_000
        text = text.replace('M', '')
    elif 'K' in text:
        multiplier = 1_000
        text = text.replace('K', '')
    try:
        return int(float(text) * multiplier)
    except:
        return 0
    

def scrape_mirrors_indetectable(usuario):

    co = ChromiumOptions()
    
    ruta_chrome = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' 
    co.set_browser_path(ruta_chrome)
    
    # 
    page = ChromiumPage(addr_or_opts=co)
    
    try:
        url = f"https://imginn.com/user/{usuario}/"
        print(f"Accediendo a: {url}")
        
        page.get(url)
        
        if page.wait.ele_displayed('.item', timeout=10):
            print(" Contenido renderizado correctamente.")
            
            posts = []
            items = page.eles('.item')[:10]
            
            for i, item in enumerate(items):
                img = item.ele('tag:img')
                caption = item.ele('tag:img').attr('alt') or ""
                fecha_relativa = item.ele('.time').text if item.ele('.time') else "Desconocida"
                hashtags = re.findall(r'#\w+', caption)
                mentions = re.findall(r'@\w+', caption)
                posts.append({
                    "id": i + 1,
                    "caption": caption,
                    "url_img": img.attr('data-src') or img.attr('src'),
                    "fecha": fecha_relativa,
                    "hashtags": hashtags,
                    "mentions": mentions
                })
                print(f"  → Post {i+1} capturado.")
                
            return posts
        else:
            print(" El sitio no responde.")
            return None
            
    finally:
        page.quit()

if __name__ == "__main__":
    target = input("Usuario(perfil público): ")
    data = scrape_mirrors_indetectable(target)
    
    if data:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("\nPublicaciones registradas.")