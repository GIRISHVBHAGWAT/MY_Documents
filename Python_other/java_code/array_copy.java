import java.util.ArrayList;
import java.util.Scanner;

class array_copy {
    public static void main(String[] args) {
        System.out.println("hari om");
        ArrayList<CharSequence> om = new ArrayList<CharSequence>();
        om.add("hari1");
        om.add("hari2");
        om.add("hari3");
        om.add("hari4");
        om.remove("hari1");
        om.remove("hari2");
        om.remove("hari3");
        om.remove("hari4");
        for (CharSequence a : om) {
            if (om != null) {
                System.out.println(a);
            }

        }
    }
}