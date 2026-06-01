// Refactored code for better testability

public class RetryUtility {
    public static void retry(Runnable task, int maxAttempts) {
        for (int attempt = 0; attempt < maxAttempts; attempt++) {
            try {
                task.run();
                return;
            } catch (Exception e) {
                if (attempt == maxAttempts - 1) throw e;
            }
        }
    }
}