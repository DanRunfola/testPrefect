#First, you must create a conda environment with prefect:
#conda create -n pT
#conda activate pT
#conda install -c conda-forge prefect

#After the install, you must then configure prefect from CLI.
#In a local install, the API is set to http://127.0.0.1:4200/api
#We must change to point at our API server:
#https://docs.prefect.io/2.10.12/host/
#prefect config set PREFECT_API_URL="http://128.239.58.222:4200/api"

#Once the above is run, you should be able to type
#"python testFlow.py", and the below should appear on the user interface.

from prefect import flow, serve, task, deploy
from datetime import datetime
import time

@flow(name="Test Flow",
      description="A test flow for Prefect",
      log_prints=True)
def testFlow(testParameter):
    start_time = time.time()
    TIMESTAMP = str(datetime.now())
    print("This is a test flow, executed at time " + TIMESTAMP)
    n = 10**7
    primes = [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    print(f"Computed {len(primes)} primes in {time.time() - start_time:.2f} seconds")
    print("Incoming parameter was: " + str(testParameter))
    return(primes)

