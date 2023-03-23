
class Battery(object):
    __spend_value = 5
    group = {}

    def __init__(self):
        pass

    def getGroup(self, group_id):
        if not self.group.has_key(group_id):
            self.group[group_id] = 100

        return self.group[group_id]

    def getBattery(self, group_id):
        return self.getGroup(group_id)

    def spendBattery(self, group_id):
        self.group[group_id] -= self.__spend_value
        if self.group[group_id] < 0:
            self.group[group_id] = 0

        return self.group[group_id]

    def getMessage(self, group_id):
        return f'剩余电量：{self.group[group_id]}%'

    def toString(self, value):
        if value > 80:
            return ""
        elif value > 60:
            return ""
        elif value > 40:
            return ""
        elif value > 20:
            return ""
        else:
            return ""