package com.example;

import org.springframework.stereotype.Service;
import java.util.List;
import java.util.ArrayList;
import java.util.Optional;

@Service
public class UserService {

    private List<User> users = new ArrayList<>();

    public UserService() {
        // Add some sample data
        users.add(new User("John Doe", "john@example.com"));
        users.add(new User("Jane Smith", "jane@example.com"));
    }

    public List<User> findUsers(String filter) {
        if (filter == null || filter.trim().isEmpty()) {
            return new ArrayList<>(users);
        }

        List<User> filtered = new ArrayList<>();
        for (User user : users) {
            if (user.getName().toLowerCase().contains(filter.toLowerCase())) {
                filtered.add(user);
            }
        }
        return filtered;
    }

    public User findById(Long id) {
        for (User user : users) {
            if (user.getId() != null && user.getId().equals(id)) {
                return user;
            }
        }
        throw new RuntimeException("User not found: " + id);
    }

    public User save(User user) {
        if (user.getId() == null) {
            // New user
            user.setId((long) (users.size() + 1));
            users.add(user);
        } else {
            // Update existing
            for (int i = 0; i < users.size(); i++) {
                if (users.get(i).getId() != null && users.get(i).getId().equals(user.getId())) {
                    users.set(i, user);
                    break;
                }
            }
        }
        return user;
    }

    public void deleteById(Long id) {
        users.removeIf(user -> user.getId() != null && user.getId().equals(id));
    }
}