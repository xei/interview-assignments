package fsm;

public interface State {
    State onInput(char input);
    int getValue();  // For mod-3: 0, 1, or 2
}