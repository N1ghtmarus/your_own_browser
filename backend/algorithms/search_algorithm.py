from thefuzz import process
from django.db.models import Case, When

from .soundex_algorithm import obj_to_soundex


def search_notes(query: str, notes_qs):
    """
    Функция поиска наиболее похожих
    заметок в Queryset по заданному запросу
    """
    # convert query to soundex form and getting all authors soundexed notes
    soundexed_query = obj_to_soundex(query)
    soundexes_qs = list(notes_qs.values_list('soundex', flat=True))

    # search query in soundexed notes and build a response sorted by matching
    response = process.extract(soundexed_query, soundexes_qs, limit=50)

    # remove matcing coefficient from response
    response_cleared = [i[0] for i in response]

    # use "Django Case-When" for match our response with soundex in db
    # and then order queryset results in right order by this preserve
    preserved = Case(*[When(soundex=soundex, then=pos) for pos, soundex in enumerate(response_cleared)])
    queryset = notes_qs.filter(soundex__in=response_cleared).order_by(preserved)
    return queryset
