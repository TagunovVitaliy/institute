from ..classes.Individual_plans import IndividualPlan

class User:

    def __init__(self, id, name, individual_plans):
        self.id = id
        self.name = name
        self.individual_plans = individual_plans
        if not (
                isinstance(id, int) and isinstance(name, str)
                and isinstance(individual_plans, list)
        ):
            raise TypeError

    def get_user_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_i_plans(self):
        return self.individual_plans

    def set_user_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_i_plans(self, i_plans):
        self.individual_plans = i_plans

    def add_i_plan(self, individual_plan: IndividualPlan):
        self.individual_plans.append(individual_plan)
        return True


"""    def get_individual_plan(self):
        return self.individual_plan"""

"""    def set_individual_plan(self, individual_plan):
        self.individual_plan = individual_plan"""