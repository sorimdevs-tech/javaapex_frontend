import React from "react";

interface HeaderProps {
  showBackButton?: boolean;
  onBackToHome?: () => void;
}

export default function Header({ showBackButton = false, onBackToHome }: HeaderProps) {
  const styles: { [key: string]: React.CSSProperties } = {
    navbar: {
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "16px 40px",
      borderBottom: "1px solid #1e293b",
      backgroundColor: "rgba(15, 20, 25, 0.95)",
      backdropFilter: "blur(10px)",
      position: "relative",
    },
    logoContainer: {
      display: "flex",
      alignItems: "center",
      gap: 12,
    },
    logoIcon: {
      fontSize: 28,
      fontWeight: 700,
      background: "linear-gradient(135deg, #3b82f6 0%, #60a5fa 100%)",
      WebkitBackgroundClip: "text",
      WebkitTextFillColor: "transparent",
      backgroundClip: "text",
    },
    logoText: {
      fontSize: 18,
      fontWeight: 700,
      color: "#3b82f6",
      margin: 0,
    },
    tagline: {
      fontSize: 11,
      color: "#64748b",
      fontStyle: "italic",
      margin: "2px 0 0 0",
      fontWeight: 400,
    },
    navLinks: {
      display: "flex",
      gap: 30,
      alignItems: "center",
      flex: 1,
      justifyContent: "center",
    },
    navLink: {
      color: "#e2e8f0",
      textDecoration: "none",
      fontSize: 14,
      fontWeight: 500,
      cursor: "pointer",
      transition: "color 0.3s ease",
    },
    ctaButton: {
      backgroundColor: "#3b82f6",
      color: "#fff",
      padding: "10px 22px",
      borderRadius: 8,
      border: "none",
      fontWeight: 700,
      cursor: "pointer",
      fontSize: 14,
      transition: "all 0.3s ease",
      boxShadow: "0 4px 12px rgba(59, 130, 246, 0.3)",
    },
    backButton: {
      position: "absolute",
      right: 40,
      backgroundColor: "#f1f5f9",
      color: "#1e293b",
      border: "1.5px solid #cbd5e1",
      borderRadius: 8,
      padding: "10px 20px",
      fontWeight: 600,
      cursor: "pointer",
      fontSize: 14,
      transition: "all 0.3s ease",
    },
  };

  return (
    <nav style={styles.navbar}>
      <div style={styles.logoContainer}>
        <div style={styles.logoIcon}>{ }</div>
        <div>
          <p style={styles.logoText}>javaAPEX</p>
          <p style={styles.tagline}>Accelerating Java Modernization</p>
        </div>
      </div>

      <div style={styles.navLinks}>
        <a
          style={styles.navLink}
          onMouseEnter={(e) => (e.currentTarget.style.color = "#3b82f6")}
          onMouseLeave={(e) => (e.currentTarget.style.color = "#e2e8f0")}
        >
          Features
        </a>
        <a
          style={styles.navLink}
          onMouseEnter={(e) => (e.currentTarget.style.color = "#3b82f6")}
          onMouseLeave={(e) => (e.currentTarget.style.color = "#e2e8f0")}
        >
          Documentation
        </a>
        <a
          style={styles.navLink}
          onMouseEnter={(e) => (e.currentTarget.style.color = "#3b82f6")}
          onMouseLeave={(e) => (e.currentTarget.style.color = "#e2e8f0")}
        >
          Support
        </a>
      </div>

      {showBackButton && onBackToHome ? (
        <button
          style={styles.backButton}
          onClick={onBackToHome}
          onMouseEnter={(e) => {
            e.currentTarget.style.backgroundColor = "#e2e8f0";
            e.currentTarget.style.borderColor = "#64748b";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.backgroundColor = "#f1f5f9";
            e.currentTarget.style.borderColor = "#cbd5e1";
          }}
        >
          ← Back to Home
        </button>
      ) : (
        <button
          style={styles.ctaButton}
          onMouseEnter={(e) => {
            e.currentTarget.style.backgroundColor = "#2563eb";
            e.currentTarget.style.boxShadow = "0 8px 16px rgba(59, 130, 246, 0.5)";
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.backgroundColor = "#3b82f6";
            e.currentTarget.style.boxShadow = "0 4px 12px rgba(59, 130, 246, 0.3)";
          }}
        >
          Start Migration
        </button>
      )}
    </nav>
  );
}
