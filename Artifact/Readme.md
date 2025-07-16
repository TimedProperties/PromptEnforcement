# ATVA'25 Artifact: `Prompt Runtime Enforcement`
**`Ayush	Anand	Indian Institute of Technology Bhubaneswar`**	
**`Loïc Germerie Guizouarn		Univ Rennes, Inria, CNRS, IRISA, France`**		
**`Thierry	Jéron	Univ Rennes, Inria, CNRS, IRISA, France`**	
**`Sayan	Mukherjee	Inria, France	`**	
**`Srinivas	Pinisetty	Indian Institute of Technology Bhubaneswar`**
**`Ocan	Sankur	Univ Rennes, Inria, CNRS, IRISA, France`**

This artifact serves as a demonstration of 'k-prompt enforcer' in the paper titled `Prompt Runtime Enforcement`. The paper was submitted as *Research Paper* to *ATVA 2025*.
The artifact aims at replicating the results discussed in **Section 7** of the paper. 
The results of the paper can be categorized into two main groups:
  ### Behaviour of k-prompt enforcer with varying k
        a. v_edited monotonically decreases with increasing k
        b. v_unedited increases with increasing k
        c. v_sat is inversly proportional to k for words that have no prefix satisfying the property
      where v_sat = frequency of property satisfaction = number of accepting prefixes / word length ,
            v_edted = frequency of edited events (by the enforcer) = number of edited events / word length ,
            and v_unedited =  frequency of unedited events νunedited = 1 − νedited.
  ### Comparison with enforcer in [A]
        a. the k-prompt enforcer guarantees property satisfaction at regular intervals, while enforcer in [A] does not.
        Reference:
        [A] Pinisetty, S., Roop, P.S., Smyth, S., Allen, N., Tripakis, S., von Hanxleden, R.: Runtime enforcement of cyber-physical systems. ACM Trans. Embed. Comput. Syst. 16(5s), 178:1–178:25 (2017), https://doi.org/10.1145/3126500

# Quickstart

## Setup Steps
- Install VM as described at https://zenodo.org/records/10928976.

- Download the artifact `atva25-artifact.zip `
  from the given url

- Unzip the artifact:

  **Note:** This will unzip the artifact directory structure and files into the
  current working directory


## Smoke Test Steps

### For first category of results
  Step 1 - Run python script k-promptEnforcer.py ($ python3 k-promptEnforcer.py)
  Step 2 - It will show a list of properties - 1. phi1 2. ph2 ... etc. Enter 4.
  Step 3 - It will ask to enter k value. Enter 3.

  **Output of Smoke Test Execution**
    <summary>After you enter the k value, the code must generate the following results</summary>

    ```
    Frequency of policy satisfaction (v_sat):       0.25

    Frequency of edited event (v_edited):   0.287

    Frequency of unedited event (v_unedited):       0.7130000000000001

    ```

### For second category of results
  Step 1 - Run python script k-promptComparison.py

  **Output of Smoke Test Execution**
    <summary>Execution of k-promptComparison.py will produce following results</summary>

    ```
    .
    .
    .

    -------------k-prompt enforcer------------

    No of edits:    28

    Policy Satisfaction:    51

    ------------------------------------------


    ------------benchmark enforcer------------

    No of edits by benchmark enforcer: 6

    Policy satisfaction by benchmark enforcer: 29
    -------------------------------------------


    Policy Satisfaction without any enforcer:    2

    ```



The following sections are intended for the full review phase.

---

# Available Bagde

The artifact was uploaded to Zenodo and is available at
https://zenodo.org/record/`<record>` (DOI: `xx.xxxx/zenodo.xxxxxxx`).

# Functional Badge

## Steps to repplicate the results and observations discussed in the paper

### Behaviour of k-prompt enforcer with varying k
  Step 1 - Run python script k-promptEnforcer.py ($ python3 k-promptEnforcer.py)
  Step 2 - It will show a list of properties - 1. phi1 2. ph2 ... etc. Enter 4.
  Step 3 - It will ask to enter k value. Enter 3.
  
  Repeat steps 1,2 and 3 for k = 4, 5, 7, 10 and note down the corresponding v_sat, v_edited and v_unedited.
  You will get the following results:
  | k  | v_sat | v_edited | v_unedited |
  |----|-------|----------|------------|
  | 3  | 0.25  | 0.287    | 0.713      |
  | 4  | 0.2   | 0.23     | 0.77       |
  | 5  | 0.166 | 0.191    | 0.809      |
  | 7  | 0.125 | 0.144    | 0.856      |
  | 10 | 0.091 | 0.105    | 0.895      |

  --You can repeat the experiments with different properties (phi1 ... phi7) and different values of k. You will notice that v_sat and v_edited monotonically increases with incrreasingk, while v_unedited monotonically decreases with increasing k. Also k must be greater than or equal to dist_value(q0) where q0 is the initial state (k-enforceability condition).

  --Please note that, for this experiment, we only consider words that have no accepting prefixes that satisfy the property. The word used in this experiment is read from word.txt, and it satisfies the criteria of having no accepting prefixes for properties phi2, phi4 and phi6.

  --You may run the experiment with word of your choice by replacing the contents of word.txt with word of your choice. A word is a sequence of input events separated by comma or space.

  --All the properties given in this experiment have input alphabet set = {a, b, c}.

  --You may add a property of your choice with different alphabet set. Please note that the property must be k-enforceable.

  --To add a property of your choice, you may replace any property phi1 or phi2 ...phi7 with property of your choice in `Properties/prop.py`, and also precompute the distance of each state from Z and replace the corresponding dist_value. Properties are defined as objects DFA class from Automata2.py.  

### Comparison with benchmark enforcer
  Step 1 Replace contents of word2.txt with random_word1.txt.
  Step 2 Run python script k-promptComparison.py, and note down number of edits and policy satisfaction by 3-prompt enforcer (k=3) and benchmark enforcer

  Repeat steps 1 and 2 with words in random_word2, ..., random_word5.
  You will get the following results:

  |     |           3-prompt enforcer               |           Benchmark Enforcer              |
  |     | No. of Edits | No. of Policy Satisfaction | No. of Edits | No. of Policy Satisfaction |
  |-----|--------------|----------------------------|--------------|----------------------------|
  | rw1 | 28           | 51                         | 6            | 29                         |
  | rw2 | 26           | 49                         | 10           | 29                         |
  | rw3 | 28           | 53                         | 14           | 38                         |
  | rw4 | 25           | 52                         | 10           | 33                         |
  | rw5 | 20           | 57                         | 8            | 44                         |

  --You can repeat the experiment with other randomly generated words. You will notice that policy is satisfied more often by the 3-prompt enforcer.

  --When no prefix of a word satisfies the given property, then the number of policy satisfaction by benchmark enforcer is zero, while 3-prompt enforcer gurantees property satisfaction, every 4 steps. This can be verified by replacing the word in word2.txt by that in word3.txt.   


## Artifact Directory Structure

  - `k-promptEnforcer.py` : Script to run first set of results
  - `k-promptEnforcer.py` : Script to run second set of results
  - `word_generator.py` : Script to generate a random word
  - `word.txt` : Text file containing input word
  - `word2.txt` : Text file containing input word
  - `word3.txt` : Text file containing input word
  - `random_word.txt` : Text file containing word generated by executing word_generator.py
  - `random_word1.txt` : Text file containing random word
  - `random_word2.txt` : Text file containing random word
  - `random_word3.txt` : Text file containing random word
  - `random_word4.txt` : Text file containing random word
  - `random_word5.txt` : Text file containing random word
  - `paper.pdf` : The submitted paper titled *Prompt Runtime Enforcement*
  - Directory `Properties`
    - `Automata2.py` : Python code defining DFA class and related functionalities
    - `Automata3.py` : Python code defining DFA class and related functionalities
    - `prop.py` : Definition of properties
