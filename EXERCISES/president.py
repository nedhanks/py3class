"""
class description
"""
from datetime import date

class President():

    _president_data_file = "../DATA/presidents.txt"
    _presidents = []

    def __init__(self, tn):
        if len(self._presidents) == 0:
            self._get_data()
        print(tn)
        if tn > len(self._presidents):
            raise ValueError("Invalid term number")
        else:
            for i in self._presidents:
                print(i['term_num'])
                if i['term_num'] == tn:
                    self._pres = i
#                    self._tnum      = pres['term_num']
#                    self._lname     = pres['last_name']
#                    self._fname     = pres['firs_tname']
#                    self._bdate     = pres['birth_date']
#                    self._ddate     = pres['death_date']
#                    self._bplace    = pres['birth_place']
#                    self._bstate    = pres['birth_state']
#                    self._ts_date   = pres['term_start']
#                    self._te_date   = pres['term_end']
#                    self._party     = pres['party']
                    break
            else:
                raise ValueError("Invalid term number")

    @staticmethod
    def _mkdate(raw_date):
        if raw_date != "NONE":
            raw_year, raw_month, raw_day = raw_date.split('-')
            d = date(int(raw_year), int(raw_month), int(raw_day))
        else:
            d = None
        return d

    def _get_data(self):
        with open(self._president_data_file) as pfile:
            p = {}
            for line in pfile:
                flds = line.rsplit(":")
                p['term_num'] = int(flds[0])
#                self._lname = flds[1]
                p['last_name'] = flds[1]

#                self._fname = flds[2]
                p['first_name'] = flds[2]

#                self._bdate = self._mkdate(flds[3])
                p['birth_date'] = self._mkdate(flds[3])
#                self._ddate = self._mkdate(flds[4])
                p['death_date'] = self._mkdate(flds[4])

#                self._bplace = flds[5]
                p['birth_place'] = flds[5]
#                self._bstate = flds[6]
                p['birth_state'] = flds[6]

#                self._ts_date = self._mkdate(flds[7])
                p['term_start'] =self._mkdate(flds[7])
#                self._te_date = self._mkdate(flds[8])
                p['term_end'] = self._mkdate(flds[8])

#                self._party = flds[9]
                p['party'] = flds[9]
                self._presidents.append(p)
#                print(p)

    @property
    def last_name(self):
        return self._lname

    @property
    def first_name(self):
        return self._fname

    @property
    def birth_date(self):
        return self._bdate

    @property
    def death_date(self):
        return self._ddate

    @property
    def birth_place(self):
        return self._bplace

    @property
    def birth_state(self):
        return self._bstate

    @property
    def term_start_date(self):
        return self._ts_date

    @property
    def term_end_date(self):
        return self._te_date

    @property
    def party(self):
        return self._party

# term_number,
# first_name,
# last_name,
# birth_date,
# death_date,
# birth_place,
# birth_state,
# term_start_date,
# term_end_date,
# party
