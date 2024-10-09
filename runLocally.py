#!/usr/bin/env python3

from autogenstudio import WorkflowManager
# load workflow from exported json workflow file.
workflow_manager = WorkflowManager(workflow="Research_and_Summarize_Workflow.json")

# run the workflow on a task
task_query = "Selena Gomez"
workflow_manager.run(message=task_query)
