
class Battery(object):
    groups = {}

    def __init__(self):
        pass

    def getGroup(self, group_id):
        if group_id not in self.groups:
            self.groups[group_id] = 100

        return self.groups[group_id]

    def getBattery(self, group_id):
        return self.getGroup(group_id)

    def spendBattery(self, group_id, value=3):
        self.groups[group_id] -= value
        if self.groups[group_id] < 0:
            self.groups[group_id] = 0

        return self.groups[group_id]

    def charge(self, group_id, num=10):
        for key in self.groups.keys():
            self.groups[key] += num
            if self.groups[key] > 100:
                self.groups[key] = 100

    def getMessage(self, group_id):
        return f'剩余电量：{self.groups[group_id]}%'

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