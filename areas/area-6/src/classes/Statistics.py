
class Statistic:
    def __init__(self, user_name, work_name, deadline, all_point, do_point, **kwargs):
        self.user_name = user_name
        self.work_name = work_name
        self.all_point = all_point
        self.do_point = do_point
        self.deadline = deadline
        if not (
                isinstance(id, int) and isinstance(user_name, str)
                and isinstance(work_name, str)
                and isinstance(all_point, int)
                and isinstance(do_point, int)
                and isinstance(deadline, bool)
        ):
            raise TypeError

