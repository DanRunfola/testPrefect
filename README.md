Notes:
First, a work pool needs to be created.  
Second, you need to configure Prefect to the correct API.
Third, you need to spin up the workers to add them to the work pool.
Finally, you populate your flows and deployments to run based on relevant triggers.

##For setting up k8s workers in non-root settings:
curl -L -o virtualenv.pyz https://bootstrap.pypa.io/virtualenv.pyz
python virtualenv.pyz env
bash
source env/bin/activate
pip install prefect
prefect config set PREFECT_API_URL="http://128.239.58.222:4200/api"
prefect worker start --pool "k8s-pool"

Note that the place where the k8s submissions run from must have this set to avoid errors:
PREFECT_KUBERNETES_CLUSTER_UID = dsmillerrunfol