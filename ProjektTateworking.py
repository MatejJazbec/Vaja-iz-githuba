import re
import orodja

#
# regex_filma = re.compile(
#     r'href="/title/tt(?P<id>\d+)/\?ref_=adv_li_tt"[^>]*?'
#     r'>(?P<naslov>.+?)</a>.*?'
#     r'lister-item-year text-muted unbold">.*?\((?P<leto>\d{4})\)</span>.*?'
#     r'runtime">(?P<dolzina>\d+?) min</.*?'
#     r'<span class="genre">(?P<zanri>.*?)</span>.*?'
#     r'<strong>(?P<ocena>.+?)</strong>.*?'
#     r'<p class="text-muted">(?P<opis>.+?)<.*?'
#     r'Directors?:(?P<reziserji>.+?)<span class="ghost">.*?'
#     r'Stars:(?P<igralci>.+?)</p>',
#     flags=re.DOTALL
# )
#
#
# regex_osebe = re.compile(
#     r'href="/name/nm(?P<id>\d+)/[^>]*?>(?P<ime>.+?)</a>',
#     flags=re.DOTALL
# )


def zajemi_spletne_strani():
    for stran in range(1, 62):
        osnovni_naslov = 'http://www.tate.org.uk/search'
        parametri = 'era=20th century 1900-1945&type=artwork'
        naslov = '{}?{}&page={}'.format(osnovni_naslov, parametri, stran)
        datoteka = 'tate/{:02}.html'.format(stran)
        orodja.shrani(naslov, datoteka)
        with open(datoteka) as f:
            vsebina = f.read()
            for ujemanje in re.finditer('\(\d{4}\)', vsebina):
                print(ujemanje)

zajemi_spletne_strani()
