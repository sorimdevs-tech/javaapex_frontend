package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import javax.servlet.http.HttpServletRequest;
import javax.persistence.Entity;
import javax.persistence.Id;
import org.apache.log4j.Logger;

@SpringBootApplication
public class Application {

    private static final Logger logger = Logger.getLogger(Application.class);

    public static void main(String[] args) {
        // Deprecated primitive wrapper constructors
        Integer oldInt = new Integer(42);
        Long oldLong = new Long(123L);
        Double oldDouble = new Double(3.14);

        // Old date/time usage
        long timestamp = new java.util.Date().getTime();

        // String concatenation in loop (should use StringBuilder)
        String result = "";
        for (int i = 0; i < 10; i++) {
            result += "item" + i;
        }

        // Dangerous String comparison
        String input = null;
        if (input.equals("test")) {
            System.out.println("This will NPE!");
        }

        // Old logging
        System.out.println("Using System.out.println instead of logger");

        SpringApplication.run(Application.class, args);
    }

    // Method with null-unsafe parameter
    public String processUser(String userId) {
        // No null check - potential NPE
        return userId.toUpperCase();
    }

    // Generic exception handling
    public void riskyOperation() {
        try {
            // Some risky code
            throw new RuntimeException("Something went wrong");
        } catch (Exception e) {
            // Too generic - should be more specific
            throw new RuntimeException("Operation failed", e);
        }
    }
}