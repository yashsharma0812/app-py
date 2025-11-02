from automata.fa.nfa import NFA

nfa = NFA(
    states={'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q1': {'a': {'q1', 'q2'}, 'b': {'q1'}},
        'q2': {'b': {'q3'}},
        'q3': {'a': {'q2'}, 'b': {'q1'}}
    },
    initial_state='q1',
    final_states={'q3'}
)

# Testing
print(nfa.accepts_input('aab'))   # True
print(nfa.accepts_input('baba'))  # False
print(nfa.accepts_input('aaab'))  # True
print(nfa.accepts_input('abb'))   # False
