import pytest
import threading
import time
from app import app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 1. Uygulamayı arka planda çalıştıracak mekanizma
@pytest.fixture(scope="module")
def server():
    # HATA GİDERİLDİ: run_server yerine yeni standart olan run kullanıldı
    web_server = threading.Thread(
        target=lambda: app.run(debug=False, port=8050, use_reloader=False)
    )
    web_server.daemon = True
    web_server.start()
    time.sleep(3)  # Sunucunun tam hazır olması için süreyi biraz artırdım
    yield "http://127.0.0.1:8050"

# 2. Tarayıcı ayarları
@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Elemanların bulunması için tarayıcıya tolerans tanıyalım
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# --- TESTLER ---

def test_header_exists(server, browser):
    browser.get(server)
    header = browser.find_element("tag name", "h1")
    assert header.text == "Pink Morsel Visualiser"

def test_visualisation_exists(server, browser):
    browser.get(server)
    # Grafiğin yüklenmesini bekle
    time.sleep(1)
    graph = browser.find_element("id", "sales-line-chart")
    assert graph is not None

def test_region_picker_exists(server, browser):
    browser.get(server)
    picker = browser.find_element("id", "region-filter")
    assert picker is not None