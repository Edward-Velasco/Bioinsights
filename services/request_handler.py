from models.study import Study
from services.metadata_getter import MetadataGetter

class RequestHandler:
    @staticmethod
    def handleRequest(data):
        id = data['id']
        metadata = MetadataGetter()
        study = Study()
        if id == 379:
            print('Obtaining data...')
            metadata.navigateStudy(id)
            study.set_title(metadata.get_title())
            study.set_description(metadata.get_description())
            study.set_subjects('x')
            study.set_travel('x')
            study.set_control('x')
            study.set_tech(metadata.get_tech())
            study.set_links('x')
            return {'data': study.to_dict(), 'status': 200}
        elif id == 665:
            print('Obtaining data...')
            metadata.navigateStudy(id)
            study.set_title(metadata.get_title())
            study.set_description(metadata.get_description())
            study.set_subjects('x')
            study.set_travel('x')
            study.set_control('x')
            study.set_tech(metadata.get_tech())
            study.set_links('x')
            return {'data': study.to_dict(), 'status': 200}
        else:
            return {'error': 'study is not supported yet', 'status': 400}
