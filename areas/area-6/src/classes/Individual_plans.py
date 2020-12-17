from .Scientific_works import ScientificWork

class IndividualPlan:

    def __init__(self, id, name, start_date, scientific_works):
        self.i_plan_id = id
        self.name = name
        self.start_date = start_date
        if not (
                isinstance(name, str)
        ):
            raise TypeError
        self.scientific_works = scientific_works

    def get_i_plan_id(self):
        return self.i_plan_id

    def get_name(self):
        return self.name

    def get_start_date(self):
        return self.start_date

    def get_scientific_works(self):
        return self.scientific_works

    def set_name(self, name):
        self.name = name

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_scientific_works(self, scientific_works):
        self.scientific_works = scientific_works

    def add_scientific_work(self, scientific_work: ScientificWork):
        self.scientific_works.append(scientific_work)
        return True

    def get_statistic(self):
        pass