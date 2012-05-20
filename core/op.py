#!/usr/bin/python

from core.yamlagent import YamlAgent

data = {
    "MAOV": ["Model As Oracle Verification",],
    }

class Data(YamlAgent):
    """Data class defines the main data structure, includes the major
       methods to manipulate the data including merge and export.

       #Data Structure
            {Term: [Def1, ...],}
    """
    def __init__(self, data_format, path='./data/glossary.yml'):
        self.data_format = data_format

        self.glossary = load_data(path)

    def merge(self, files):
        """merge files, dump the merged glossary data

        """
        [self.merge_file(file_) for file_ in files if is_valid(file_)]


    def compare_datum(self, current, merging):
        """return True if two data set have intersection"""
        return set(current.keys()).intersection(merging.keys())

    def merge_file(self, file_):
        """glossary data is merged with file_

        solve two problems: key conflicts and value update

        Args:
            file_: merging file path

        Returns:
            None
        """
        self.merging_data = getattr(self, 'get_%s' % self.data_format)(file_)

        if self.compare_datum(self.glossary,
