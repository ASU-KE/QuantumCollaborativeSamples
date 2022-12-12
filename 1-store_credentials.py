from qiskit import IBMQ

# Replace TOKEN with your API token available from here: https://quantum-computing.ibm.com/account
# Do not remove the single quotes
token = 'TOKEN'

# By default, credentials are stored in $HOME/qiskit/qiskitrc
IBMQ.save_account(token)

# Load the credentials to verify - if this fails with a python error the TOKEN (or something else) is wrong
IBMQ.load_account()

print('If this script  exists without an error, the TOKEN was accepted and valid.')

