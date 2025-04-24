#######imports###########
import sys
sys.path.append("../")
import Enforcer
import Automata2
import copy
#########################


#########################################################################################
###Define DFA describing input property psi##############################################
######### (actions, states, initial state, final states, transition function)############
##This DFA defines "There should be atleast two a|b actions, followed by a "c" action.###
#########################################################################################
psi = Automata2.DFA(
['a', 'b', 'c'],
['q0'],
'q0',
lambda q: q in ['q0'],
lambda q, a: {
        ('q0', 'a') : 'q0',
        ('q0', 'b') : 'q0',
        ('q0', 'c') : 'q0',
    }[(q, a)]
)
###############################################################################

###############################################################################
###Define DFA describing property to enforcer phi##############################
######### (actions, states, initial state, final states, transition function)###
##This DFA defines "There should be atleast one "a|b" action, before action "c" can occur. 
###The sequence should end with a "c" action.####################################
###############################################################################
"""
#########################################phi-1######################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4'],
'q0',
lambda q: q in ['q3'],
lambda q, a: {
        ('q0', 'a') : 'q1',
        ('q0', 'b') : 'q0',
        ('q0', 'c') : 'q0',
        ('q1', 'a') : 'q1',
        ('q1', 'b') : 'q2',
        ('q1', 'c') : 'q4',
        ('q2', 'a') : 'q1',
        ('q2', 'b') : 'q2',
        ('q2', 'c') : 'q3',
        ('q3', 'a') : 'q1',
        ('q3', 'b') : 'q3',
        ('q3', 'c') : 'q3',
	('q4', 'a') : 'q1',
        ('q4', 'b') : 'q4',
        ('q4', 'c') : 'q4',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 3,
    'q1': 2,
    'q2': 1,
    'q3': 0,
    'q4': 3  # Accepting state
}

phi.assign_s_values(dist_value)
"""
"""
########################################phi-2#########################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4'],
'q0',
lambda q: q in ['q1', 'q3'],
lambda q, a: {
        ('q0', 'a') : 'q1',
        ('q0', 'b') : 'q2',
        ('q0', 'c') : 'q0',
        ('q1', 'a') : 'q2',
        ('q1', 'b') : 'q3',
        ('q1', 'c') : 'q1',
        ('q2', 'a') : 'q2',
        ('q2', 'b') : 'q3',
        ('q2', 'c') : 'q0',
        ('q3', 'a') : 'q2',
        ('q3', 'b') : 'q4',
        ('q3', 'c') : 'q3',
	('q4', 'a') : 'q4',
        ('q4', 'b') : 'q4',
        ('q4', 'c') : 'q4',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 1,
    'q1': 0,
    'q2': 1,
    'q3': 0,
    'q4': 50  # Accepting state
}

phi.assign_s_values(dist_value)
"""
"""
#######################################phi-3##########################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4'],
'q0',
lambda q: q in ['q2'],
lambda q, a: {
        ('q0', 'a') : 'q3',
        ('q0', 'b') : 'q3',
        ('q0', 'c') : 'q1',
        ('q1', 'a') : 'q2',
        ('q1', 'b') : 'q4',
        ('q1', 'c') : 'q4',
        ('q2', 'a') : 'q1',
        ('q2', 'b') : 'q2',
        ('q2', 'c') : 'q2',
        ('q3', 'a') : 'q1',
        ('q3', 'b') : 'q4',
        ('q3', 'c') : 'q4',
	('q4', 'a') : 'q3',
        ('q4', 'b') : 'q4',
        ('q4', 'c') : 'q4',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 2,
    'q1': 1,
    'q2': 0,
    'q3': 2,
    'q4': 3  # Accepting state
}

phi.assign_s_values(dist_value)
"""
#"""
##################################phi-4###############################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3'],
'q0',
lambda q: q in ['q3'],
lambda q, a: {
        ('q0', 'a') : 'q1',
        ('q0', 'b') : 'q0',
        ('q0', 'c') : 'q2',
        ('q1', 'a') : 'q1',
        ('q1', 'b') : 'q3',
        ('q1', 'c') : 'q2',
        ('q2', 'a') : 'q1',
        ('q2', 'b') : 'q2',
        ('q2', 'c') : 'q2',
        ('q3', 'a') : 'q1',
        ('q3', 'b') : 'q3',
        ('q3', 'c') : 'q2',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 2,
    'q1': 1,
    'q2': 2,
    'q3': 0  # Accepting state
}

phi.assign_s_values(dist_value)
#"""
"""
##################################phi5###############################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3'],
'q0',
lambda q: q in ['q1'],
lambda q, a: {
        ('q0', 'a') : 'q1',
        ('q0', 'b') : 'q3',
        ('q0', 'c') : 'q3',
        ('q1', 'a') : 'q1',
        ('q1', 'b') : 'q2',
        ('q1', 'c') : 'q1',
        ('q2', 'a') : 'q3',
        ('q2', 'b') : 'q2',
        ('q2', 'c') : 'q1',
        ('q3', 'a') : 'q3',
        ('q3', 'b') : 'q3',
        ('q3', 'c') : 'q3',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 1,
    'q1': 0,
    'q2': 1,
    'q3': 50 # Accepting state
}

phi.assign_s_values(dist_value)
"""
"""
################################phi-6#################################################

phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4', 'q5'],
'q0',
lambda q: q in ['q0', 'q3'],
lambda q, a: {
        ('q0', 'a') : 'q5',
        ('q0', 'b') : 'q1',
        ('q0', 'c') : 'q1',
        ('q1', 'a') : 'q4',
        ('q1', 'b') : 'q5',
        ('q1', 'c') : 'q2',
        ('q2', 'a') : 'q5',
        ('q2', 'b') : 'q5',
        ('q2', 'c') : 'q3',
        ('q3', 'a') : 'q4',
        ('q3', 'b') : 'q5',
        ('q3', 'c') : 'q3',
	('q4', 'a') : 'q4',
        ('q4', 'b') : 'q5',
        ('q4', 'c') : 'q1',
	('q5', 'a') : 'q5',
        ('q5', 'b') : 'q5',
        ('q5', 'c') : 'q5',
    }[(q, a)]
)
###############################################################################


dist_value = {
    'q0': 3,
    'q1': 2,
    'q2': 1,
    'q3': 0,
    'q4': 3,
    'q5': 50  # Accepting state
}

phi.assign_s_values(dist_value)
"""
"""
################################phi-7#################################################
phi = Automata2.DFA(
['a', 'b', 'c'],
['q0', 'q1', 'q2', 'q3',  'q4'],
'q0',
lambda q: q in ['q3', 'q2'],
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
"""
###############################################################################
###Invoke the enforcer with properties psi, phi, and some test input sequence #
######### (psi, phi, input sequence sigma)#######################################
###############################################################################
#word = ['b', 'c', 'a', 'a', 'a', 'a', 'b', 'c']
#word = ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'c']
#word = ['b', 'c', 'a', 'b', 'a', 'c', 'b', 'a']
#word = ['b', 'c', 'b', 'a', 'a', 'a', 'a', 'a']
word = ['b'] + ['c']*99
enf_word=[]
current_state = phi.q0
edit_event = 0
edit_counter = 0
acc_counter = 0
x = 0

if phi.F(current_state):
    x=0
else:
    x=x+1

for event in word:
    print "Current state: "+str(current_state)
    print "Current event: "+str(event)
    new_event, edit_event = phi.enforce_event(current_state,event,x,10)
    edit_counter = edit_counter + edit_event
    #print "Type (event): "+str(type(event))
    #print "Type (new_event): "+str(type(new_event))
    current_state = phi.d(current_state,new_event)
    #print "Next state: "+str(current_state)
    enf_word.append(new_event)
    #q = lambda current
    if phi.F(current_state):
    	x=0
	acc_counter = acc_counter+1
    else:
	x=x+1

print "Original Word:    "+str(word)
print "\nEnforced Word:    "+str(enf_word)
print "\nNo of edits:	"+str(edit_counter)
print "\nPolicy Satisfaction:	"+str(acc_counter)



"""
####Input sigma = aac#####
print "input sequence is aac"  
#Enforcer.enforcer(copy.copy(psi), copy.copy(phi), ['a', 'a', 'c'])
Enforcer.enforcer(copy.copy(psi), copy.copy(phi), ['a', 'a', 'c'])
print "######################" 

####Input sigma = bbc#####
print "input sequence is bbc"
Enforcer.enforcer(copy.copy(psi), copy.copy(phi), ['b', 'b', 'c'])
print "######################" 

####Input sigma = abc#####
print "input sequence is abc"
Enforcer.enforcer(copy.copy(psi), copy.copy(phi), ['a', 'b', 'b', 'c'])
print "######################" 


####Input sigma = bac#####
print "input sequence is bac"
Enforcer.enforcer(copy.copy(psi), copy.copy(phi), ['b', 'a', 'c'])
print "######################" 
###############################################################################

"""







