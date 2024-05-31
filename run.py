from prefect import flow, serve, task, deploy
from datetime import datetime

testFlow = flow.from_source(
    source="https://github.com/DanRunfola/testPrefect.git",
    entrypoint="testDeploy.py:testFlow"
)

testFlow.deploy(name="testDeploy", work_pool_name="process-agent-GPU")