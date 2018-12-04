public class NumberCruncherTest {

	public static void main(String [] args) {
		NumberCruncher num = new NumberCruncher();

		String results = "";

		int successes = 0;
		int tests = 0;

        try {
            if(num.sumInts(5) != 15) {
                results += "Failed sumInts(5) == 15\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumInts(5): " + e.toString() + "\n";
        }
        tests++;
		
        try {
            if(num.sumInts(0) != 0) {
                results += "Failed sumInts(0) == 0\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumInts(0): " + e.toString() + "\n";
        }
        tests++;
		

        try {
            if(num.raiseToPower(2, 2) != 4) {
                results += "Failed raiseToPower(2, 2) == 4\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed raiseToPower(2, 2): " + e.toString() + "\n";
        }
		tests++;


        try {
            if(num.raiseToPower(2, 3) != 8) {
                results += "Failed raiseToPower(2, 3) == 8\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed raiseToPower(2, 3): " + e.toString() + "\n";
        }
		tests++;

        try {
            if(num.sumSquares(3) != 14) {
                results += "Failed sumSquares(3) == 14\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumSquares(3): " + e.toString() + "\n";
        }
		tests++;

        try {
            if(num.sumSquares(2) != 5) {
                results += "Failed sumSquares(2) == 5\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumSquares(2): " + e.toString() + "\n";
        }
		tests++;
        
        try {
            if(num.sumSquares(3) != 14) {
                results += "Failed sumSquares(3) == 14\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumSquares(3): " + e.toString() + "\n";
        }
		tests++;
        
        try {
            if(num.sumRecips(3) > 1.9 || num.sumRecips(3) < 1.8) {
                results += "Failed num.sumRecips(3) < 1.9 && num.sumRecips(3) > 1.8\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed num.sumRecips(3): " + e.toString() + "\n";
        }
		tests++;
        
        try {
            if(num.sumRecips(5) < 2.25 || num.sumRecips(5) > 2.3) {
                results += "Failed sumRecips(5) > 2.25 && num.sumRecips(5) < 2.3\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed sumRecips(5): " + e.toString() + "\n";
        }
		tests++;

        try {
            if(!num.isPerfSquare(4)){
                results += "Failed isPerfSquare(4)\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed isPerfSquare(4): " + e.toString() + "\n";
        }
		tests++;
        
        try {
            if(num.isPerfSquare(3)) {
                results += "Failed num.isPerfSquare(3)\n";
            }
            else
                successes++;
        } catch (Exception e) {
            results += "Failed num.isPerfSquare(3): " + e.toString() + "\n";
        }
        tests++;
        
        
		if(successes == tests)
			System.out.println("All Tests Passed");
		else {
			System.out.println("Passed " + 1.0*successes/tests * 100 + "% of tests.  The following tests failed:\n");
			System.out.println(results);
		}
	}
}
