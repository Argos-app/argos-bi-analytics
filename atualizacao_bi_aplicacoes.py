# Upgrade Databricks SDK to the latest version and restart Python to see updated packages
%pip install --upgrade databricks-sdk==0.70.0
%restart_python

from databricks.sdk.service.jobs import JobSettings as Job


Atualização_BI_Aplicações_Argos = Job.from_dict(
    {
        "name": "Atualização BI - Aplicações Argos",
        "trigger": {
            "pause_status": "UNPAUSED",
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        "tasks": [
            {
                "task_key": "atualizar_pipeline_aplicacoes",
                "pipeline_task": {
                    "pipeline_id": "942eb27f-1d7f-4b65-87f3-09d34a5a7b08",
                },
            },
            {
                "task_key": "atualizar_pipeline_estoque",
                "depends_on": [
                    {
                        "task_key": "atualizar_pipeline_aplicacoes",
                    },
                ],
                "pipeline_task": {
                    "pipeline_id": "4fe452d8-f0c9-4974-9be4-55eab983d17e",
                },
            },
        ],
        "queue": {
            "enabled": True,
        },
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()
w.jobs.reset(new_settings=Atualização_BI_Aplicações_Argos, job_id=719848862917210)
# or create a new job using: w.jobs.create(**Atualização_BI_Aplicações_Argos.as_shallow_dict())
