import json
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

ARQUIVO = 'livros.json'

class MeuApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.94, 0.9, 1)

        self.carregar_livros()

        layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        titulo_app = Label(
            text = 'Minhas Leituras',
            font_size = 28,
            color = (0.2, 0.15, 0.1, 1),
            size_hint_y = None,
            height = 50
        )

        self.campo_titulo = TextInput(hint_text = "Digite o Título", font_size = 18, size_hint_y = None, height = 45)
        self.campo_autor = TextInput(hint_text = "Digite o Autor", font_size = 18, size_hint_y = None, height = 45)
        self.campo_genero = TextInput(hint_text = "Digite o Gênero", font_size = 18, size_hint_y = None, height = 45)

        botao_salvar = Button(
            text = 'Salvar',
            font_size = 18,
            background_color = (0.3, 0.6, 0.3, 1),
            background_normal = '',
            size_hint_y = None,
            height = 50,
            on_press = self.salvar_livro
        )
        botao_titulo = Button(
            text = 'Ordenar por Título',
            background_color = (0.4, 0.5, 0.7, 1),
            background_normal = '',
            size_hint_y = None,
            height = 45,
            on_press = self.ordenar_por_titulo
        )
        botao_autor = Button(
            text = 'Ordenar por Autor',
            background_color = (0.4, 0.5, 0.7, 1),
            background_normal = '',
            size_hint_y = None,
            height = 45,
            on_press = self.ordenar_por_autor
        )
        botao_genero = Button(
            text = 'Ordenar por Gênero',
            background_color = (0.4, 0.5, 0.7, 1),
            background_normal = '',
            size_hint_y = None,
            height = 45,
            on_press = self.ordenar_por_genero
        )

        self.label_lista = Label(
            text = '',
            font_size = 16,
            color = (0.2, 0.15, 0.1, 1),
            markup = True,
            size_hint_y = None,
            halign = 'left',
            valign = 'top'
        )
        self.label_lista.bind(texture_size = self.label_lista.setter('size'))

        scroll = ScrollView()
        scroll.add_widget(self.label_lista)

        layout.add_widget(titulo_app)
        layout.add_widget(self.campo_titulo)
        layout.add_widget(self.campo_autor)
        layout.add_widget(self.campo_genero)
        layout.add_widget(botao_salvar)
        layout.add_widget(botao_titulo)
        layout.add_widget(botao_autor)
        layout.add_widget(botao_genero)
        layout.add_widget(scroll)

        self.atualizar_lista()

        return layout

    def carregar_livros(self):
        try:
            arquivo = open(ARQUIVO, 'r')
            self.livros = json.load(arquivo)
            arquivo.close()
        except:
            self.livros = []

    def salvar_no_arquivo(self):
        arquivo = open(ARQUIVO, 'w')
        json.dump(self.livros, arquivo)
        arquivo.close()

    def atualizar_lista(self):
        texto = ''
        numero = 1
        for l in self.livros:
            texto += '[b]' + str(numero) + '. ' + l['Título'] + '[/b]\n'
            texto += l['Autor'] + ' _ ' + l['Gênero'] + '\n\n'
            numero += 1
        self.label_lista.text = texto

    def salvar_livro(self, instance):
        livro = {
            'Título': self.campo_titulo.text,
            'Autor' : self.campo_autor.text,
            'Gênero' : self.campo_genero.text
        }
        self.livros.append(livro)
        self.salvar_no_arquivo()
        self.atualizar_lista()

    def ordenar_por_titulo(self, instance):
        self.livros = sorted(self.livros, key = lambda l: l['Título'])
        self.atualizar_lista()

    def ordenar_por_autor(self, instance):
        self.livros = sorted(self.livros, key = lambda l: l['Autor'])
        self.atualizar_lista()

    def ordenar_por_genero(self, instance):
        self.livros = sorted(self.livros, key = lambda l: l['Gênero'])
        self.atualizar_lista()

if __name__ == '__main__':
    MeuApp().run()
