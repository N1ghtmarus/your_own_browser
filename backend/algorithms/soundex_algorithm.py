from fonetika.soundex import RussianSoundex


def obj_to_soundex(*args: tuple) -> str:
    """Функция перевода текста в фонетический вид"""
    soundex = RussianSoundex()
    return ' '.join(str(soundex.transform(el)) for el in args)
