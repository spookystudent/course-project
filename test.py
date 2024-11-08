opts = {
    "alias": ("айрис", "арис", "рис", "аис", "iris", "airis", "ириска", 'олег'),
    "tbr": (
        "скажи",
        "расскажи",
        "покажи",
        "сколько",
        "произнеси",
        "как",
        "сколько",
        "поставь",
        "переведи",
        "засеки",
        "запусти",
        "сколько будет",
    ),
    "cmds": {
        "ctime": (
            "текущее время",
            "сейчас времени",
            "который час",
            "время",
            "какое сейчас время",
        ),
        "startStopwatch": ("запусти секундомер", "включи секундомер", "засеки время"),
        "stopStopwatch": ("останови секундомер", "выключи секундомер", "останови"),
        "stupid1": (
            "расскажи анекдот",
            "рассмеши меня",
            "ты знаешь анекдоты",
            "шутка",
            "прикол",
        ),
        "calc": (
            "прибавить",
            "умножить",
            "разделить",
            "степень",
            "вычесть",
            "поделить",
            "х",
            "+",
            "-",
            "/",
        ),
        "shutdown": (
            "выключи",
            "выключить",
            "отключение",
            "отключи",
            "выключи компьютер",
        ),
        "conv": ("валюта", "конвертер", "доллар", "руб", "евро"),
        "internet": ("открой", "вк", "гугл", "сайт", "вконтакте", "ютуб"),
        "translator": ("переводчик", "переведи", "translate"),
        "deals": ("дела", "делишки", "как сам", "как дела"),
    },
}

def recogniseVoice(voice: str):
    """Распознаем комманду из строки голоса
        Например    voice = "<Имя> <Команда> <Параметры....>"\n
        Или         voice = "<Распознанный голос> <Имя> <Команда> <Параметры....>"

    Args:
        voice (str): строка голоса
    """
    
    splited_voice = voice.split(' ')
    recognised_alias = [alias for alias in opts["alias"] if alias in splited_voice]
    prepared_voice = splited_voice
    
    recoginesed_command = ''
    
    alias_ids = []

    if recognised_alias:
        for alias in recognised_alias:
            alias_ids += [index for index, word in enumerate(splited_voice) if word == alias]

        prepared_voice = prepared_voice[alias_ids[-1]:][1:] # Убираем все лишнее, берем последнее обращение без имени
        
    for command in opts['cmds']:
        command_words = opts['cmds'][command]
        
        if prepared_voice[0] in command_words: # Смотри есть ли глагол в списке комманд, если да, возвращаем
            recoginesed_command = command
            prepared_voice = ' '.join(prepared_voice[1:])
            break
        
    if recoginesed_command:
        return  [recoginesed_command, prepared_voice]
    else:
        return None
    

voice1 = 'олег hello world'
voice2 = 'сплошной шум много слов мы арис переведи ай блять не знаем что говорим а потом случается аис переведи hello world'
command1 = recogniseVoice(voice1)
command2 = recogniseVoice(voice2)

print(command1)
print(command2)