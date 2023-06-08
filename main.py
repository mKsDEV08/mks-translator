from googletrans import  Translator
import PySimpleGUI as sg

translator = Translator()
languages = ['Português', 'Inglês', 'Esperanto', 'Latim']


sg.theme('Reddit')

col1 = [
    [sg.Text('Texto a ser traduzido:', font='arial 20')],
    [sg.Text('Selecione a linguagem: ', font='arial 12')],
    [sg.Combo(languages, size=(15, 30), font='arial 12', enable_events=True, key='-LANG_INPUT1-')],
    [sg.Multiline(size=(50, 10), font='arial 10',  key='-TEXT_INPUT-')]
]

col2 = [
    [sg.Text('Texto traduzido:', font='arial 20')],
    [sg.Text('Selecione a linguagem:', font='arial 12')],
    [sg.Combo(languages, size=(15, 30), font='arial 12', enable_events=True, key='-LANG_INPUT2-')],
    [sg.Text('', size=(50, 10), key='-TEXT_OUTPUT-', font='arial 10', enable_events=True)]
]

layout = [
    [sg.Text('Tradutor', font='arial 24 bold')],
    [sg.Column(col1, element_justification='center'), sg.VerticalSeparator(), sg.Column(col2, element_justification='center')],
    [sg.Button('Traduzir', size=(75, 0), font='arial 12 bold', key='-TRANSLATE-')],
]

window = sg.Window(
    "Tradutor",
    element_justification="center",
    layout=layout,
    finalize=True,
    resizable=True
)

while True:
    event, values = window.Read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-TRANSLATE-':
        lang1 = values['-LANG_INPUT1-']
        lang2 = values['-LANG_INPUT2-']
        text_in = values['-TEXT_INPUT-']
        text_out = window['-TEXT_OUTPUT-']

        if lang1 == 'Português':
            lang1 = 'pt'

        elif lang1 == 'Inglês':
            lang1 = 'en'

        elif lang1 == 'Esperanto':
            lang1 = 'eo'

        elif lang1 == 'Latim':
            lang1 = 'la'

        else:
            sg.popup('ERRO! Por favor selecione as duas linguagens')


        if lang2 == 'Português':
            lang2 = 'pt'

        elif lang2 == 'Inglês':
            lang2 = 'en'

        elif lang2 == 'Esperanto':
            lang2 = 'eo'

        elif lang2 == 'Latim':
            lang2 = 'la'

        else:
            sg.popup('ERRO! Por favor selecione as duas linguagens')

        if (lang1 != 'None') and (lang2 != 'None'):
            if lang1 != lang2:
                translate = translator.translate(text_in, src=lang1, dest=lang2)
                text_out.update(translate.text)
            else:
                sg.popup('ERRO! As linguagens devem ser diferentes')
        else:
            sg.popup('ERRO! Por favor selecione as duas linguagens')

window.Close()