from models.study import Study
import requests

class MetadataGetter:
    def __init__(self):
        self._connection = None
        self._data = None
        self._database = None
        self._url = "https://osdr.nasa.gov/osdr/data/osd/meta/"

    def navigateStudy(self, studyID):
        url = self._url + str(studyID)
        self._connection = requests.get(url)
        if self._connection.status_code == 200:
            self._data = self._connection.json()
            study = self._data.get('study', {})
            osd = study.get(f'OSD-{studyID}', {})
            self._database = osd.get('studies', {})[0]
            return self._database
        else:
            return None

    def get_title(self):
        if self._database != None:
            return self._database["title"]

    def get_description(self):
        if self._database != None:
            return self._database["description"]

    def get_tech(self):
        if self._database != None:
            assays = self._database["assays"]
            return assays[0]["technologyPlatform"]

    # def get_links(self):  # pending
    #     return self._links

    def get_database(self):
        return self._database

    def set_database(self, database):
        self._database = database
