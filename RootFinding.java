

public class RootFinding {
	public static void main(String[] args) {
	NewtonsMethod(1, 0.0001, 50);
	}
/*	public static void main(String[] args) {
		BisectionMethod(0, 15, 1, 0);
		System.out.println();
		NewtonsMethod(1, 0.0001, 50);
		System.out.println();
		SecantMethod(1, 0.99, 0.0001, 50);
	}*/

	private static void BisectionMethod(double a, double b, int it, double prev_p) {
		double p = (a+b)/2;
		double f_a = Math.pow(a, 3) - 16*Math.pow(a, 2) + 5*a + 5.5;
		double f_p = Math.pow(p, 3) - 16*Math.pow(p, 2) + 5*p + 5.5;
		if(p - prev_p < 0.0000000000000000000000001) {
			System.out.println("Bisection Method");
			System.out.println("------------------");
			System.out.println("p = " + Double.toString(p));
			System.out.println("f(p) = " + Double.toString(f_p));
			System.out.println("|p - p_(n-1)|: " + Double.toString(Math.abs(p-prev_p)) + ".");
			System.out.println("Found after " + Integer.toString(it) + " iterations.");
		}
		else if(f_a/Math.abs(f_a) != f_p/Math.abs(f_p)) {
			BisectionMethod(a, p, it+1, p);
			System.out.println("|p - p_(n-1)|: " + Double.toString(Math.abs(p-prev_p)) + ".");
		}
		else {
			BisectionMethod(p, b, it+1, p);
			System.out.println("|p - p_(n-1)|: " + Double.toString(Math.abs(p-prev_p)) + ".");
		}
	}
	
	private static void NewtonsMethod(double p_0, double tol, double N_max) {
		System.out.println("Newton's Method");
		System.out.println("-----------------");
		double i = 1;
		double f_p_0 ;
		double df_p_0;
		while (i <= N_max) {
			f_p_0 = Math.pow(p_0, 3) - 5*p_0;
			df_p_0 = 3*Math.pow(p_0, 2) - 5;
			double p = p_0 - f_p_0/df_p_0;
			if(Math.abs(p-p_0) < tol) {
				System.out.println("p_0 = " + Double.toString(p_0));
				System.out.println("p-p_0 = " + Double.toString(Math.abs(p-p_0)));
				System.out.println("Found root after " + Double.toString(i) + " iterations.");
				i = N_max + 1;
			}
			p_0 = p;
			i = i + 1;
			System.out.println(p_0);
			if(i == N_max + 1) {
				System.out.println("Failed to find the root after " + Double.toString(N_max) + " iterations.");
			}
		}
	}
	
	private static void SecantMethod(double p_0, double p_1, double tol, double N_max) {
		System.out.println("Secant Method");
		System.out.println("--------------");
		double i = 1;
		double f_p_0;
		double f_p_1;
		while (i <= N_max) {
			f_p_0 = 3*Math.pow(p_0, 3) - 2*Math.pow(p_0, 2) + 5*p_0 - 2*Math.exp(p_0) + 1;
			f_p_1 = 3*Math.pow(p_1, 3) - 2*Math.pow(p_1, 2) + 5*p_1 - 2*Math.exp(p_1) + 1;
			double p = p_1 - (f_p_1 * (p_1 - p_0))/(f_p_1 - f_p_0);
			if(Math.abs(p-p_1) < tol) {
				System.out.println("p = " + Double.toString(p_0));
				System.out.println("p-p_nmin1 = " + Double.toString(Math.abs(p-p_1)));
				System.out.println("Found root after " + Double.toString(i) + " iterations.");
				i = N_max + 1;
			}
			p_0 = p_1;
			p_1 = p;
			i = i + 1;
			if(i == N_max + 1) {
				System.out.println("Failed to find the root after " + Double.toString(N_max) + " iterations.");
			}
		}
	}
}