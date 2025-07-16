#####Imports####################

from copy import deepcopy
###############################


##function to sort a tuple###
def ts(x):
    return tuple(sorted(x))
#############################

############################################################
############################################################
class DFA:
    def transition_to_next_state(self, current_state, event):
        if (current_state, event) in self.d:  # Check if transition exists
            return self.d[(current_state, event)]  # Return next state
        else:
            print("No valid transition for state:", current_state, "on event:", event)
            return None

    def assign_s_values(self, values_dict):
        for state, distance in values_dict.items():  # `.iteritems()` for Python 2.7
            if state in self.Q:
                self.s[state] = distance
            else:
                print("Warning: State %s not found in the DFA, skipping..." % state)
    
    def enforce_event(self, current_state, event, x, k):
        if current_state not in self.s:
            print("Warning: State", current_state, "has no precomputed s value.")
            return event  # Default to allowing the event if no s value exists
    
        x=x+1
        edit_event = 0
    
        next_state = self.d(current_state, event)    
        s_value = self.s[next_state]  # Get precomputed distance
    
        if x + s_value <= k+1:
            print("x = "+str(x)+"\n")
            print("s = "+str(s_value)+"\n")
            print("Valid event\n")
            return event, edit_event  # Event is valid, return as is

        edit_event = 1
    
        # If constraint is violated, try to find a safe event
        for alt_event in self.S:
            if alt_event is not event:
                next_state = self.d(current_state, alt_event)
                next_s = self.s[next_state]
                if x + next_s <= k+1:
                #print "x+s =  "+str(x+s_value)+"\n"
                    print("x = "+str(x)+"\n")
                    print("s = "+str(s_value)+"\n")
                    print("Alternate event: "+str(alt_event)+"\n")
                    return alt_event, edit_event
            
        return None, None
    def benchmark_enforce(self, current_state, event):
        if self.V(self.d(current_state,event)):
            for alt_event in self.S:
                if alt_event is not event:
                    if not self.V(self.d(current_state, alt_event)):
                        return alt_event, 1
        else:
            return event, 0
    def __init__(self, S, Q, q0, F, V, d, e = ('.l',)):
        self.S = S
        self.Q = Q
        self.q0 = q0
        self.q = q0
        self.F = F
        self.V = V
        self.d = d
        self.e = e # empty word

        self.reset()
    
        self.s = dict((q, None) for q in self.Q)
        
    def complement(self):
        
        newSetF = set()
        
        for q in self.Q:
            if not self.F(q):
                newSetF.add(q)
                
        self.F = lambda q: q in newSetF

    def isEmpty(self):
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            for a in self.S:
                q = self.d(node, a)
                if q and q not in visited:
                    dfs(q)
                    
        dfs(self.q0)
        return all(not self.F(q) for q in visited)

    def show(self):
       
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('alphabet:', sorted(self.S))
        print('\nstates:', sorted(self.Q))
        print('\ninit:', self.q0)
        print('\nfinal:')
        for s in sorted(self.Q):
            if self.F(s):
                print(s)
        print('\ntransitions:')
        for s in sorted(self.Q):
            for a in self.S:
                self.reset(s)
                self.step(a)
                print((s, a), '->', self.q)
            print()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        
        self.graph()

    def graph(self):
        
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print()
        for i, q in enumerate(sorted(self.Q)):
            fill = list('999')
            if q == self.q0:
                fill[1] = 'f'
            if self.F(q):
                fill[0] = 'f'
            if fill == list('999'):
                fill = list('fff')
            print('%s [label="%s" style="fill: #%s"];' % (i, q, ''.join(fill)))
        print()
        sQ = sorted(self.Q)
        for i, s in enumerate(sorted(self.Q)):
            for a in self.S:
                self.reset(s)
                self.step(a)
                print('%s -> %s [labelType = "html" label="<div style=\'width:20px; height:20px; background-color:white; z-index:100; border: 1.5px solid black; text-align: center; border-radius: 5px;\'>%s</div>" lineInterpolate="basis"]' % (i, sQ.index(self.q), a))
                #print '%s -> %s [label="%s"]' % (i, sQ.index(self.q), a)
            print()
        print()
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')

    def reset(self, q = None):
        
        q = q or self.q0
        
        self.q = q


    def step1(self, a):
        #if a != '' and a != self.e:
        if a and a not in self.e:
            self.q = self.d(self.q, a)
            return self.q
            
    def makeInit(self, q):
        #if a != '' and a != self.e:
        #if a and a not in self.e:
        self.q0 = q
        
            
    def step(self, a):
        #if a != '' and a != self.e:
        if a and a not in self.e:
            self.q = self.d(self.q, a)

    def isInAcceptingState(self):
        return self.F(self.q)


    def accepts(self, w):
        
        #w = w.replace(self.e, '')
        
        #if w == '' or w == []:
        if not w or w == self.e:
            return self.F(self.q0)
            
        #if '.d' in w: 
        if w == ('.d',): 
            return False
        
        q = self.q
        
        self.reset()

        for a in w:
            self.step(a)
            
        ret = self.isInAcceptingState()
        
        self.reset(q)

        return ret

############################################################
############################################################


############################################################
############################################################
class DFAProduct:
        
    #def __init__(self, dfas, outFun = None, e = '.l'):
    def __init__(self, dfas, outFun = None, e = ('.l',)):
        
        outFun = outFun or str
        
        self.e = e
        
        self.S = dfas[0].S
        
        assert all(self.S == dfa.S for dfa in dfas)
        
        self.q0 = tuple(dfa.q0 for dfa in dfas)
        self.q = self.q0
        
        def d(q, a):
            return tuple(dfa.d(qi, a) for qi, dfa in zip(q, dfas))
        
        self.d = d

        def g(q):
            return outFun(tuple({False : 0, True : 1}[dfa.F(qi)] for qi, dfa in zip(q, dfas)))

        self.g = g
        
        self.reset()
        
        ## All loc
        states = set()
        for state1 in dfas[0].Q:
            for state2 in dfas[1].Q:
                states.add((state1,state2))
         
        #print states    
        self.Q = states
        # TODO: perform a DFS in order to identify Q (reachable product states) - DONE!
#
#        visited = set()
#        
#        def dfs(node):
#            visited.add(node)
#            for a in self.S:
#                q = self.d(node, a)
#                if q and q not in visited:
#                    dfs(q)
#
#        dfs(self.q0)
#
#        self.Q = visited

    def getDFA(self):
        
        deltaDict = {}
        
        for q in self.Q:
            for a in self.S:
                deltaDict[(q, a)] = self.d(q, a)
        
        finalSet = set()
        
        for q in self.Q:
            if self.g(q): # self.g must return True / False
                finalSet.add(q)
        
        #print deltaDict
        return DFA( self.S,
                    self.Q,
                    self.q0,
                    lambda q: q in finalSet, 
                    lambda q, a: deltaDict[(q, a)])
        
    def show(self):
       
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('alphabet:', sorted(self.S))
        print('\nstates:', sorted(self.Q))
        print('\ninit:', self.q0)
        print('\noutput:')
        for so in sorted(zip(self.Q, list(map(self.g, self.Q))), key = lambda q_g: (q_g[1], q_g[0])):
            print(so)
        print('\ntransitions:')
        for s in sorted(self.Q):
            for a in self.S:
                self.reset(s)
                self.step(a)
                print((s, a), '->', self.q)
            print()
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        
        self.graph()
        
    def graph(self):
        
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        print()
        for i, q in enumerate(sorted(self.Q)):
            fill = list('999')
            if q == self.q0:
                fill[1] = 'f'
            if self.g(q):
                fill[0] = 'f'
            if fill == list('999'):
                fill = list('fff')
            print('%s [label="%s" style="fill: #%s"];' % (i, '(' + ', '.join(q) + ')', ''.join(fill)))
        print()
        sQ = sorted(self.Q)
        for i, s in enumerate(sorted(self.Q)):
            for a in self.S:
                self.reset(s)
                self.step(a)
                print('%s -> %s [labelType = "html" label="<div style=\'width:20px; height:20px; background-color:white; z-index:100; border: 1.5px solid black; text-align: center; border-radius: 5px;\'>%s</div>" lineInterpolate="basis"]' % (i, sQ.index(self.q), a))
            print()
        print()
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
        
    def reset(self, q = None):
        
        q = q or self.q0
        
        self.q = q
        self.o = self.g(q)

    def step(self, a):
        #if a != '' and a != self.e:
        if a and a != self.e:
            self.q = self.d(self.q, a)
            self.o = self.g(self.q)
             
    def transduce(self, w):
        
        if w == self.e:
            return self.o
        
        q = self.q
        
        self.reset()
        
        #ret = self.o
        ret = [self.o]
        
        for a in w:
            self.step(a)
            #ret += self.o
            ret.append(self.o)
            
        self.reset(q)

        return tuple(ret)

    
##################################################################################
##################################################################################





##################################################################################
    # return True if L(dfa1) includes L(dfa2)
    # and False otherwise
###################################################################################
def includesLang(dfa1, dfa2):
    dfa1c = deepcopy(dfa1)
    dfa1c.complement()
    diff = DFAProduct([dfa1c, dfa2], lambda o1_o2 : o1_o2[0] and o1_o2[1]).getDFA()
    return diff.isEmpty()
##################################################################################
##################################################################################


#def set_distance(self, distance):
#    for 
