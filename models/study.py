class Study:
    def __init__(self, title='', description='', name='BALB/cAnNTac (mice)', subjects=-1, travel=-1, control=-1, tech=-1, links={}):
        self._title = title,
        self._description = description,
        self._name = name
        self._subjects = subjects
        self._travel = travel
        self._control = control
        self._tech = tech
        self._links = links

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_name(self):
        return self._name

    def get_subjects(self):
        return self._subjects

    def get_travel(self):
        return self._travel

    def get_control(self):
        return self._control
    
    def get_tech(self):
        return self._tech

    def get_links(self):
        return self._links

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_name(self, name):
        self._name = name

    def set_subjects(self, subjects):
        self._subjects = subjects

    def set_travel(self, travel):
        self._travel = travel

    def set_control(self, control):
        self._control = control

    def set_tech(self, tech):
        self._tech = tech

    def set_links(self, links):
        self._links = links

    def to_dict(self):
        return {
            'title': self._title,
            'description': self._description,
            'name': self._name,
            'subjects': self._subjects,
            'travel': self._travel,
            'control': self._control,
            'tech': self._tech,
            'links': self._links
        }
