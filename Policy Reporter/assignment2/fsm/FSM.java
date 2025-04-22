package fsm;

public class FSM {
    private State currentState;

    public FSM(State initialState) {
        this.currentState = initialState;
    }

    public void reset(State initialState) {
        this.currentState = initialState;
    }

    public void transition(char input) {
        this.currentState = currentState.onInput(input);
    }

    public int getStateValue() {
        return currentState.getValue();
    }
}