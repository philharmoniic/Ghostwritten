init python:
    import datetime
    class Date(datetime.date):

        @property
        def day(self):
            return _strftime("%A", self.timetuple())
        @property
        def day_short(self):
            return _strftime("%a", self.timetuple())
        @property
        def month(self):
            return _strftime("%B", self.timetuple())
        @property
        def month_short(self):
            return _strftime("%b", self.timetuple())

default cal = Date(2024, 11, 1)
define day_inc = datetime.timedelta(days=1)

    