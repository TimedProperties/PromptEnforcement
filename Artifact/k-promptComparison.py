#######imports###########
import sys
sys.path.append("Properties/")
#import Enforcer
from Properties import Automata3
import copy
#########################

phi = Automata3.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4'],
'q0',
lambda q: q in ['q3', 'q2'],
lambda q: q in ['q3', 'q4'],
lambda q, a: {
        ('q0', 'a') : 'q0',
        ('q0', 'b') : 'q1',
        ('q0', 'c') : 'q3',
        ('q1', 'a') : 'q1',
        ('q1', 'b') : 'q1',
        ('q1', 'c') : 'q2',
        ('q2', 'a') : 'q0',
        ('q2', 'b') : 'q2',
        ('q2', 'c') : 'q2',
        ('q3', 'a') : 'q4',
        ('q3', 'b') : 'q4',
        ('q3', 'c') : 'q4',
    ('q4', 'a') : 'q4',
        ('q4', 'b') : 'q4',
        ('q4', 'c') : 'q4',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 2,
    'q1': 1,
    'q2': 0,
    'q3': 50,
    'q4': 50  # Accepting state
}

phi.assign_s_values(dist_value)
with open("word2.txt", "r") as f:
    content = f.read().strip()

# Support space or comma separated input
if "," in content:
    word = content.split(",")
else:
    word = content.split()

word_length = len(word)

enf_word=[]
benchmark_word=[]
current_state = phi.q0
unedited_state = phi.q0
benchmark_state = phi.q0
#violation_state = phi.q3

edit_event = 0
benchmark_edit = 0
edit_counter = 0
acc_counter = 0
x = 0
unedit_acc = 0
benchmark_acc = 0
violation_counter = 0
benchmark_counter = 0

if phi.F(current_state):
    x=0
else:
    x=x+1

for event in word:
    print("Current state: "+str(current_state))
    print("Current event: "+str(event))
    new_event, edit_event = phi.enforce_event(current_state,event,x,3)
    edit_counter = edit_counter + edit_event

    benchmark_event, benchmark_edit = phi.benchmark_enforce(benchmark_state, event)
    benchmark_counter = benchmark_counter+benchmark_edit
    #print "Type (event): "+str(type(event))
    #print "Type (new_event): "+str(type(new_event))
    unedited_state = phi.d(unedited_state, event)
    if str(unedited_state) == "q3":
        violation_counter = violation_counter +1
    if phi.F(unedited_state):
        unedit_acc = unedit_acc +1
    current_state = phi.d(current_state,new_event)
    benchmark_state = phi.d(benchmark_state, benchmark_event)
    #print "Next state: "+str(current_state)
    enf_word.append(new_event)
    benchmark_word.append(benchmark_event)
    #q = lambda current
    if phi.F(current_state):
        x=0
        acc_counter = acc_counter+1
    else:
        x=x+1
    if phi.F(benchmark_state):
        benchmark_acc = benchmark_acc+1
#v_sat = acc_counter/word_length
#v_edited = edit_counter/word_length
#v_unedited = 1 - v_edited

print("Original Word:    "+str(word))
print("\nEnforced Word:    "+str(enf_word))
print("\n\n-------------k-prompt enforcer------------")
print("\nNo of edits:    "+str(edit_counter))
print("\nPolicy Satisfaction:    "+str(acc_counter))
print("\n------------------------------------------")
print("\n\n------------benchmark enforcer------------")
print("\n No of edits by benchmark enforcer: "+str(benchmark_counter))
print("\n Policy satisfaction by benchmark enforcer: "+str(benchmark_acc))
print("-------------------------------------------")
print("\n\nPolicy Satisfaction without any enforcer:    "+str(unedit_acc))