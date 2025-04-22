package tests;

import mod3.Mod3FSM;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Mod3FSMTest {

    @Test
    void testBinaryInputs() {
        Mod3FSM mod3FSM = new Mod3FSM();

        assertEquals(0, mod3FSM.mod3("0"));
        assertEquals(1, mod3FSM.mod3("1"));
        assertEquals(2, mod3FSM.mod3("10"));
        assertEquals(0, mod3FSM.mod3("11"));
        assertEquals(1, mod3FSM.mod3("100"));
        assertEquals(2, mod3FSM.mod3("101"));
        assertEquals(0, mod3FSM.mod3("110"));
        assertEquals(1, mod3FSM.mod3("111"));
        assertEquals(2, mod3FSM.mod3("1001"));
    }

    @Test
    void testEmptyInput() {
        Mod3FSM mod3FSM = new Mod3FSM();
        // TODO: Return 0 or any desired behavior
        assertEquals(0, mod3FSM.mod3(""));
    }

    @Test
    void testInvalidInput() {
        Mod3FSM mod3FSM = new Mod3FSM();
        // Ensure IllegalArgumentException is thrown for invalid input
        assertThrows(IllegalArgumentException.class, () -> {
            mod3FSM.mod3("10a1");
        });
    }

    @Test
    void testEdgeCases() {
        Mod3FSM mod3FSM = new Mod3FSM();
        // Additional edge case test for large input
        assertEquals(0, mod3FSM.mod3("111111111111111111111111111111111111"));
    }
}