from qiskit import IBMQ

# Assumes that credentials are stored in $HOME/.qiskit/qiskitrc - see 1-store_credentials.py
IBMQ.load_account()

# Select the ASU Quantum Hub Provider (Hub, Group, and Project) - change PROJECT to your assigned project
provider = IBMQ.get_provider(hub="ibm-q-asu", group="main", project="PROJECT")

# Get and print available backends in the Project
ibmq_backends = provider.backends()
print("Remote backends: ", ibmq_backends)
