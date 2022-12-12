# Getting Started with the Quantum Collaborative's IBM Quantum Network #

1. If you have not already done so, request to have your IBM Quantum Cloud account added to the Hub using the form.
2. Login to the IBM Quantum Cloud and copy your API Access Token: [https://quantum-computing.ibm.com/account](https://quantum-computing.ibm.com/account)
2. Replace **TOKEN** with your API Key in *1-store_credentials.py*
3. Replace **PROJECT** with your Project Name (typically "institution-PI_lastname" such as "ASU-Smith") in *2-test_access.py* and *3-simple_circuit.py* - this is sent to you in email when your account is approved.
4. Install qiskit: [https://qiskit.org/documentation/getting_started.html](https://qiskit.org/documentation/getting_started.html)
5. Run *1-store_credentials.py* once to store your API Access Token on disk.
6. Run *2-test_access.py* to test - the script will report the available backends if successful.
7. Run *3-simple_circuit.py* to verify submissions to the Hub work

## Useful Links ##

* Qiskit Overview: [https://qiskit.org/documentation/index.html](https://qiskit.org/documentation/index.html)
* Qiskit Installation: [https://qiskit.org/documentation/getting_started.html](https://qiskit.org/documentation/getting_started.html)
* Qiskit Tutorials: [https://qiskit.org/documentation/tutorials.html](https://qiskit.org/documentation/tutorials.html)



