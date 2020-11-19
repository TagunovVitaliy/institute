from ..classes.Individual_plans import IndividualPlan

class User:

    def __init__(self, id, name, **kwargs):
        self.id = id
        self.name = name
        if not (
                isinstance(id, int) and isinstance(name, str)
        ):
            raise TypeError
        if 'individual_plans' in kwargs:
            self.individual_plans = kwargs['individual_plans']

    def get_user_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def add_i_plan(self, individual_plan: IndividualPlan):
        self.individual_plans.append(individual_plan)


"""    def get_individual_plan(self):
        return self.individual_plan"""

"""    def set_individual_plan(self, individual_plan):
        self.individual_plan = individual_plan"""