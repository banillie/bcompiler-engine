import json
import shutil
from pathlib import Path

import pytest

from engine.repository.templates import (FSPopulatedTemplatesRepo,
                                         InMemoryPopulatedTemplatesRepository)
from engine.use_cases.parsing import ParsePopulatedTemplatesUseCase


def test_template_parser_use_case(resources):
    repo = InMemoryPopulatedTemplatesRepository(resources)
    parse_populated_templates_use_case = ParsePopulatedTemplatesUseCase(repo)
    result = parse_populated_templates_use_case.execute()
    assert (json.loads(result)["test_template.xlsx"]["data"]["Summary"]["B3"]
            ["value"] == "This is a string")


@pytest.mark.skip("Wait until we have BCOMPILER_IO_LIBRARY in config file")
def test_query_data_from_data_file(mock_config, dat_file,
                                   spreadsheet_same_data_as_dat_file):
    mock_config.initialise()
    shutil.copy2(dat_file, mock_config.BCOMPILER_LIBRARY_DATA_DIR)
    shutil.copy2(spreadsheet_same_data_as_dat_file,
                 mock_config.BCOMPILER_IO_LIBRARY)
    repo = FSPopulatedTemplatesRepo(Path.home() / "Desktop")
    parse_populated_templates_use_case = ParsePopulatedTemplatesUseCase(repo)
    result = parse_populated_templates_use_case.execute()
    assert (json.loads(result)["test.xlsx"]["data"]["new sheet"]["A1"]["value"]
            == "Project/Programme Name")
