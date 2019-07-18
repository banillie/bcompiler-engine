import json
import os
from pathlib import Path

from ..config import Config
from ..use_cases.parsing import extract_from_multiple_xlsx_files
from ..utils.extraction import _get_xlsx_files
from . import Repo


class FSPopulatedTemplatesRepo(Repo):
    """A repo that is based on a single data file in the .bcompiler-engine directory.
    """

    def __init__(self, directory_path: Path):
        super().__init__(directory_path)

    def list_as_json(self) -> str:
        "Try to open the data file containing populated data as json."
        try:
            with open(
                    os.path.join(Config.BCOMPILER_LIBRARY_DATA_DIR,
                                 "extracted_data.dat")) as f:
                return f.read()
        except FileNotFoundError:
            raise


class InMemoryPopulatedTemplatesRepository(Repo):
    """A repo that does no data file reading or writing - just parsing from excel files.
    """

    def __init__(self, directory_path: Path):
        super().__init__(directory_path)

    def list_as_json(self) -> str:
        "Return data from a directory of populated templates as json."
        excel_files = _get_xlsx_files(self.directory_path)
        data = extract_from_multiple_xlsx_files(excel_files)
        return json.dumps(data)
