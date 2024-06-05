from prefect import flow, serve, task, deploy
from datetime import datetime

testFlow = flow.from_source(
    source="https://github.com/DanRunfola/testPrefect.git",
    entrypoint="testDeploy.py:testFlow"
)

testFlow.deploy(name="testDeploy", 
                work_pool_name="generic-cpu-8GB", 
                parameters=dict(testParameter="Test Parameter Value"),
                cron="*/10 * * * *")