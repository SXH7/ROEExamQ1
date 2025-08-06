class PaymentException extends Exception {
   public PaymentException(String msg) {
     super(msg);
   }
}
public class PaymentProcessor {
     public static void validatePayment(String method, double amount) throws PaymentException {
    if (amount <= 0) {
        throw new PaymentException("Invalid payment amount");
   }
   System.out.println("Payment validated");
}
public static void main(String[] args) {
   try {
       	try {
             validatePayment("card", 0.0);
      } catch (PaymentException e) {
       System.out.println("Inner catch: " + e.getMessage());
       throw e;
    }
} catch (PaymentException e) {
          System.out.println("Outer catch: Transaction failed - " + e.getMessage());
      }
    }
 }