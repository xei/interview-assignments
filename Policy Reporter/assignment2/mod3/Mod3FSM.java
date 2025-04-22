package mod3;

import fsm.FSM;

public class Mod3FSM {
    private FSM fsm = new FSM(Mod3State.S0);

    public int mod3(String binary) {
        if (!binary.matches("[01]*")) {
            throw new IllegalArgumentException("Input must be a binary string containing only '0' and '1'");
        }

        fsm.reset(Mod3State.S0);
        for (char c : binary.toCharArray()) {
            fsm.transition(c);
        }
        return fsm.getStateValue();
    }
}
