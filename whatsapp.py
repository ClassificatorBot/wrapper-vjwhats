import os
import time
from vjwhats import WhatsApp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

BASE_PATH = "C:\\Users\\User\\Desktop\\robo_class_cam\\Robo_de_classificacao\\resources\\relatorios"


class Whatsapp:
    user_data_dir = os.path.join(
        os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User", "Data"
    )
    # Intanciando minhas Options do Chrome
    chrome_options = Options()
    # Adicionando as opções do Chrome, meu diretório de usuário e o perfil
    chrome_options.add_argument(f"user-data-dir={user_data_dir}")
    chrome_options.add_argument("profile-directory=Developer")

    def __init__(self):
        # Criando um webdriver com as opções configuradas
        self.driver = None
        # Acessando o WhatsApp Web
        self.whatsapp = None

    def __enter__(self):
        # Intanciando meu WhatsApp Web
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.whatsapp = WhatsApp(self.driver)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fechando o webdriver
        self.driver.quit()

    def send_message_attachment(self, full_path_file):

        # Sending a file to a contact
        self.whatsapp.send_file(Path(full_path_file), which=1)

    def send_message_image(self, full_path_file):

        # Sending a file to contact
        self.whatsapp.send_file(Path(full_path_file), which=2)

    def send_whatsapp_text(self, contact, text):
        # Sending a message to Contact 1
        self.whatsapp.find_by_username(contact)
        self.whatsapp.send_message(text)

    def clear_messages(self, contact):
        # Clear all messages from the contact
        self.whatsapp.clear_messages(contact)

    def get_all_images(self):
        # Get all images from the conversation
        self.whatsapp.get_images_sent()

    def find_contact(self, contact):
        # Find a contact
        self.whatsapp.find_by_username(contact)


with Whatsapp() as whats:
    contact = {
        "name": "+5519998722472",  # DESV Robo Classif Cams Concepcion
        "image": "relatorio",
        "pdf": "Relatorio_Final",
    }
    print("Iniciando envio de mensagem para", contact)
    whats.find_contact(contact=contact["name"])

    print(f"Enviando mensagem image relatorio.png ...")

    whats.send_message_image(full_path_file=os.path.join(BASE_PATH, contact["image"]))
    for i in range(1, 4):
        filename = f'{contact["pdf"]}_{i}'
        print(f"Enviando mensagem attachment {i} {filename}.pdf ...")
        whats.send_message_attachment(
            full_path_file=os.path.join(BASE_PATH, f"{filename}.pdf")
        )
