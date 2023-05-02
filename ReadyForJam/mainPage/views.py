from jam.utils import GetCurrentDate
from jam.views import JamListView
from tzlocal import get_localzone_name

class MainPageView(JamListView):

    __cardsLimit = 10

    _query = JamListView._query + \
            f"WHERE (CAST(jam_jamdate.start_date AS timestamp) " \
            f"AT TIME ZONE '{get_localzone_name()}') > '{GetCurrentDate()}' " +\
             "ORDER BY jam_jamdate.start_date" \
             + f" LIMIT {__cardsLimit}"

    _href = '/mainPage/MainPage.html'