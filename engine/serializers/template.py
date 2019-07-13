import json

from engine.domain.template import TemplateCell


class TemplateCellSerializer(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "file_name": o.file_name,
                "sheet_name": o.sheet_name,
                "cellref": o.cell_ref,
                "data_type": o.data_type.name,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)


class ParsedTemplatesSerializer(json.JSONEncoder):
    pass


#    # TODO write this so that it encodes the data format currently
#    # produced by parse_multiple_xlsx_files()
#
#    def default(self, o):
#        try:
#            to_serialize = {[]}
#        except AttributeError:
#            return super().default(o)