# digital_wallet
Digital Wallet Code Submitted to InsightDataScience

# Table of Contents

1. [Summary] (README.md#summary)
2. [Data structure and algorithm] (README.md#data-structure-and-algorithm)
3. [Description of Data] (README.md#description-of-data)
4. [Description of the code](README.md#description-of-the-code)
5. [Testing directory structure and output format] (README.md#testing-directory-structure-and-output-format)
6. [A simple add-on and further thoughts](README.md#a-simple-addon-and-further-thoughts)

## Summary
[Back to Table of Contents] (README.md#summary)

This project called "digital-wallet"is requested by "InsightDataScience", the detail can be found in https://github.com/InsightDataScience/digital-wallet

* The source code, `antifraud.py`, is under the `./src` fold.

* Some of the following content are directly copied from the request source to be highlighted for being better understood


## Data structure and algorithm
[Back to Table of Contents] (README.md#data-structure-and-algorithm)

The basic idea used here is to find the shortest path between two nodes in a network.

The shortest path algorithm (e.g. Dijkstra's algorithm', whose run time time for "worst-case performance" can be O(|E| + |V|log|V|)) is necessary to build a suitable data structure to solve the problem.

An efficient computing process is needed for big data base. A pygraph packaged published by Pedro matiello, etc., is applied for this purpose, by which the programming can also be in a relatively clean style.

* To install pygraph package
    '''
    1) download python-graph-master from https://github.com/pmatiello/python-graph.git
    2) run: make install-core and make install-dot
    '''
* Module graph and minmax are used here


## Description of Data
[Back to Table of Contents] (README.md#description-of-data)

** Please download `batch_payment.csv` at [https://www.dropbox.com/s/y6fige3w1ohksbd/batch_payment.csv?dl=0], change the extention to .txt and save it (`batch_payment.txt`) under the `./paymo_input` folder because the arguments in `run_sh` is based on '.txt';

** Please download `stream_payment.csv` at [https://www.dropbox.com/s/vrn4pjlypwa2ki9/stream_payment.csv?dl=0], change the extention to .txt, and save it (`stream_payment.txt`) under the `./paymo_input` folder because the arguments in `run_sh` is based on '.txt';

###Input

The first file, `batch_payment.txt` or `batch_payment.csv`, is used to build the initial state of the entire user network, graph. The file format should be double checked, and `batch_payment.txt` would be a better choice for this program to open the file, and the possible format change once saved by excel need to be considered.

The second file, `stream_payment.txt` or `stream_payment.csv` should be used to determine whether there's a possibility of fraud and a warning should be triggered.

Each line of `stream_payment.txt` corresponds to a new, valid PayMo payment record. 

###Output

For each line of transaction/payment in `stream_payment.txt`, two words, `trusted` or `unverified` is printed in each line for information 

`trusted` means the two users involved in the transaction have previously paid one another (when implementing Feature 1) or are part of the "friends network" (when implementing Feature 2 and 3).

`unverified` means the two users have not previously been involved in a transaction (when implementing Feature 1) or are outside of the "friends network" (when implementing Features 2 and 3)

The outputs are written to a text file in the `paymo_output` directory. Each output file will be named after the applicable feature, such as `output1.txt`, `output2.txt` and `output3.txt`.


##Description of the code

[Back to Table of Contents] (README.md#description-of-the-code)

Python language is used in the source code, `antifraud.py`, under the `./src` fold. 

The top-most directory is called `digital-wallet-master`, which include the `src`, `paymo_input`, `paymo_output`,`insight_testsuite` and `images` directories, and a shell script named `run.sh`, as well as a `README.md` file.

Pygragh package need to be installed and the correspoding modules are imported at the beginning of the code.

* To install pygraph package
'''
1) download python-graph-master from https://github.com/pmatiello/python-graph.git
2) run: make install-core and make install-dot
'''
* Module graph and minmax are used here


##Testing directory structure and output format
[Back to Table of Contents] (README.md#testing-directory-structure-and-output-format)

There is a test code offered by "Insight" to make sure that the code has the correct directory structure and the format of the output data in `output1.txt`, `output2.txt` and `output3.txt` is correct.

From the `insight_testsuite` folder, run the test with the following command:

    insight_testsuite$ bash run_tests.sh

    or

	insight_testsuite$ ./run_tests.sh 

The output of `run_tests.sh` should look like:
	
	[PASS]: test-1-paymo-trans (output1.txt)
	[PASS]: test-1-paymo-trans (output2.txt)
	[PASS]: test-1-paymo-trans (output3.txt)
	[Fri Nov  4 13:20:25 PDT 2016] 3 of 3 tests passed
on success.


##A simple add-on and further thoughts
[Back to Table of Contents] (README.md#a-simple-addon-and-further-thoughts)

**A simple add-on feature to warn a payment exceeding the maximum limit is added. The code is inherited in the function "get_payment_notice". The max_payment_amount can be set up in the argument.

There are also other potential features that can be added on:
1) The directed relationship can be configured according to "Who pay Whom";
2) The weight can be put on the edge depending on how much the payment is;
etc.
