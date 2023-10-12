from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

# Stworzenie klasy apki Formularz, której układ strony wykorzystuje GridLayout
class Formularz(GridLayout):
    #Inicjalizacjas apki
    def __init__(self, **kwargs):
        # Call grid layout konstruktor
        super(Formularz, self).__init__(**kwargs)

        # Wstaw kolumny
        self.cols = 2

        # Dodaj widget z Label (etykieta)
        self.label = self.add_widget(Label(text="To jest ETYKIETA", font_size = "30sp"))

        # Dodaj Pole Input (Box)
        self.name = TextInput(multiline=False)
        self.name.background_color = [1, 1, 0, 1]

        # Dodaj widget z obiektem - polem input
        self.add_widget(self.name)

        # Dodaj Image
        self.img = Image(source="rys.jpg")
        # Dodaj widget z obiektem obrazkowym
        self.add_widget(self.img)

        # Przycisk do wysyłania (Submit Button)
        self.submit = Button(text="Wyślij", font_size=32)
        self.submit.background_color = [1, 0, 0, 1]

        # Dodanie obsługi kliknięcia (czyli zdarzenia) do przycisku - po kliknięciu zostanie wywołana funkcja o nazwie wypiszTekst
        self.submit.bind(on_press=self.nacisnij)

        #Dodaj widget - przycisk do wysyłania (Submit Button)
        self.add_widget(self.submit)

        # Dodaj widget z label (etykieta)
        self.label = self.add_widget(Label(text="Kliknij Wyślij, aby potwierdzić Twój wpis",font_size="13sp"))

    # Funkcja obsługująca kliknięcie
    def nacisnij(self, instance):
        # przechwyć wpisany tekst do Inputa do nowej zmiennej
        namePrzechwycone = self.name.text

        # stworzymy nowy element strony Label, w którym wyświetlimy przechwycony twkst (ze zmiennej namePrzechwycone)
        self.add_widget(Label(text=f'Napisałeś: {namePrzechwycone}'))

        # Dodajmy jeszcze jedną funkcjonalność - wyczyszczenie pola Input po przechwyceniu wiadomości
        self.name.text= ""

class MobileApp(App):
    def build(self):
        return Formularz()

if __name__ == '__main__':
    MobileApp().run()

