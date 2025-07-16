#######imports###########
import sys
sys.path.append("Properties/")
#import Enforcer
from Properties import prop
import copy
#########################

phi_options = {
    "1": (prop.phi1, prop.dist_value1),
    "2": (prop.phi2, prop.dist_value2),
    "3": (prop.phi3, prop.dist_value3),
    "4": (prop.phi4, prop.dist_value4),
    "5": (prop.phi5, prop.dist_value5),
    "6": (prop.phi6, prop.dist_value6),
    "7": (prop.phi7, prop.dist_value7),
    # Add more if defined in prop.py
}

print("Choose a property:")
for key in sorted(phi_options):
    print(f"  {key}: phi{key}")

choice = input("Enter your choice (e.g., 1): ").strip()

if choice not in phi_options:
    print("Invalid choice. Exiting.")
    sys.exit(1)

phi, dist_value = phi_options[choice]
phi.assign_s_values(dist_value)
#word = ['b'] + ['a']*850 +['c']*149
enf_word=[]
current_state = phi.q0
edit_event = 0
edit_counter = 0
acc_counter = 0
x = 0
k = int(input("Enter k =  "))

with open("word.txt", "r") as f:
    content = f.read().strip()

# Support space or comma separated input
if "," in content:
    word = content.split(",")
else:
    word = content.split()

word_length = len(word)

if phi.F(current_state):
    x=0
else:
    x=x+1

for event in word:
    #print ("Current state: "+str(current_state))
    #print ("Current event: "+str(event))
    new_event, edit_event = phi.enforce_event(current_state,event,x,k)
    if new_event == None :
        print("k too small, try again with greater k value")
        sys.exit()
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
v_sat = acc_counter/word_length
v_edited = edit_counter/word_length
v_unedited = 1 - v_edited

print ("Original Word:    "+str(word))
print ("\nEnforced Word:    "+str(enf_word))
#print ("\nNo of edits:	"+str(edit_counter))
#print ("\nPolicy Satisfaction:	"+str(acc_counter))
print ("\nFrequency of policy satisfaction (v_sat):	"+str(v_sat))
print ("\nFrequency of edited event (v_edited):	"+str(v_edited))
print ("\nFrequency of unedited event (v_unedited):	"+str(v_unedited))