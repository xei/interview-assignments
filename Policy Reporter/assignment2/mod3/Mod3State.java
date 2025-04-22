package mod3;

import fsm.State;

public enum Mod3State implements State {
    S0 {
        public State onInput(char input) {
            return switch (input) {
                case '0' -> S0;
                case '1' -> S1;
                default -> throw new IllegalArgumentException("Invalid input: " + input);
            };
        }
        public int getValue() { return 0; }
    },
    S1 {
        public State onInput(char input) {
            return switch (input) {
                case '0' -> S2;
                case '1' -> S0;
                default -> throw new IllegalArgumentException("Invalid input: " + input);
            };
        }
        public int getValue() { return 1; }
    },
    S2 {
        public State onInput(char input) {
            return switch (input) {
                case '0' -> S1;
                case '1' -> S2;
                default -> throw new IllegalArgumentException("Invalid input: " + input);
            };
        }
        public int getValue() { return 2; }
    };
}
