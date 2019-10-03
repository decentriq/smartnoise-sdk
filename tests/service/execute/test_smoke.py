import json

import pytest

from burdock.restclient.models.project_run_details import ProjectRunDetails

@pytest.mark.parametrize("project", [{"params": {"alpha": .4}, "uri": "https://github.com/mlflow/mlflow-example"},
                                     {"params": {"text": "this text"}, "uri": "modules/module-example"},
                                     {"params": {"dataset_name": "example", "column_name": "a", "budget": .2},
                                      "uri": "modules/psi-count-module"}])
def test_execute_run(client, project):
    details = ProjectRunDetails(params=json.dumps(project["params"]),
                                project_uri=project["uri"])
    client.executerun(details)

