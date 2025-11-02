from automata.fa.dfa import DFA

dfa = DFA(
    states={'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q2', 'b': 'q3'},
        'q3': {'a': 'q2', 'b': 'q1'}
    },
    initial_state='q1',
    final_states={'q3'}
)

# Testing
print(dfa.accepts_input('aab'))   # True
print(dfa.accepts_input('baba'))  # False
print(dfa.accepts_input('aabb'))  # False
