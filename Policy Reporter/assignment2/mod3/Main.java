package mod3;

public class Main {
    public static final String DEFAULT_BINARY_INPUT = "1011";

    public static void main(String[] args) {
        String input = args.length > 0 ? args[0] : DEFAULT_BINARY_INPUT;
        if (!input.matches("[01]+")) {
            System.out.println("Error: Input must be a binary string.");
            return;
        }

        Mod3FSM mod3FSM = new Mod3FSM();
        int result = mod3FSM.mod3(input);

        System.out.println(input + " % 3 = " + result);
    }
}
