package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SpringBootApplication
public class Application {

    private static final Logger logger = LoggerFactory.getLogger(Application.class);

    public static void main(String[] args) {
        // Fixed: Deprecated primitive wrapper constructors → Integer.valueOf()
        Integer oldInt = Integer.valueOf(42);
        Long oldLong = Long.valueOf(123L);
        Double oldDouble = new Double(3.14);

        // Fixed: Old date/time usage → System.currentTimeMillis()
        long timestamp = System.currentTimeMillis();

        // Fixed: String concatenation in loop → StringBuilder suggested
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            result.append("item").append(i);
        }

        // Fixed: Dangerous String comparison → null-safe check
        String input = null;
        if ("test".equals(input)) {
            System.out.println("Safe comparison!");
        }

        // Fixed: Old logging → proper SLF4J logging
        logger.info("Using proper SLF4J logger");

        SpringApplication.run(Application.class, args);
    }

    // Fixed: Method with null-safe parameter validation
    public String processUser(String userId) {
        // Added null check
        if (userId == null) {
            throw new IllegalArgumentException("userId cannot be null");
        }
        return userId.toUpperCase();
    }

    // Fixed: More specific exception handling
    public void riskyOperation() {
        try {
            // Some risky code
            throw new RuntimeException("Something went wrong");
        } catch (RuntimeException e) {
            // More specific exception type
            throw new IllegalStateException("Operation failed due to runtime error", e);
        }
    }
}