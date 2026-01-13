package com.example;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import org.junit.Ignore;
import static org.junit.Assert.*;
import java.util.List;

public class UserServiceTest {

    private UserService userService;

    @Before
    public void setUp() {
        userService = new UserService();
    }

    @After
    public void tearDown() {
        userService = null;
    }

    @Test
    public void testFindAllUsers() {
        List<User> users = userService.findUsers(null);
        assertNotNull(users);
        assertTrue(users.size() >= 2); // Should have sample data
    }

    @Test
    public void testFindUsersWithFilter() {
        List<User> users = userService.findUsers("John");
        assertNotNull(users);
        assertEquals(1, users.size());
        assertEquals("John Doe", users.get(0).getName());
    }

    @Test
    public void testCreateUser() {
        User newUser = new User("Test User", "test@example.com");
        User saved = userService.save(newUser);

        assertNotNull(saved.getId());
        assertEquals("Test User", saved.getName());
        assertEquals("test@example.com", saved.getEmail());
    }

    @Test(expected = RuntimeException.class)
    public void testFindNonExistentUser() {
        userService.findById(999L);
    }

    @Ignore("This test is temporarily disabled")
    @Test
    public void testDisabledTest() {
        // This test should be ignored
        fail("This test should not run");
    }
}