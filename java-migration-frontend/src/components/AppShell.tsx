import React from "react";

const shellStyles: { [key: string]: React.CSSProperties } = {
  root: {
    minHeight: "100vh",
    background: "#f8fafc",
    display: "flex",
    flexDirection: "column",
  },
  header: {
    background: "#fff",
    borderBottom: "1px solid #e5e7eb",
    padding: "24px 0",
    textAlign: "center",
    boxShadow: "0 1px 4px rgba(0,0,0,0.03)",
  },
  headerTitle: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 12,
    fontSize: 28,
    fontWeight: 700,
    color: "#1f2937",
    margin: 0,
  },
  headerLogo: {
    fontSize: 32,
    color: "#2563eb",
  },
  headerSubtitle: {
    fontSize: 16,
    color: "#6b7280",
    margin: "8px 0 0 0",
    fontWeight: 400,
  },
  main: {
    flex: 1,
    display: "flex",
    justifyContent: "center",
    alignItems: "flex-start",
    padding: "48px 20px 64px 20px",
  },
  content: {
    width: "100%",
    maxWidth: 900,
  },
  footer: {
    background: "#fff",
    borderTop: "1px solid #e5e7eb",
    textAlign: "center",
    padding: "24px 20px",
    color: "#6b7280",
    fontSize: 14,
  },
  footerContent: {
    maxWidth: 900,
    margin: "0 auto",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  footerLeft: {
    fontSize: 15,
    fontWeight: 600,
    color: "#374151",
  },
  footerRight: {
    fontSize: 13,
    color: "#9ca3af",
  },
};

const AppShell: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={shellStyles.root}>
    <header style={shellStyles.header}>
      <img src="src\assets\javapexfinal.png" width = "180px" height = "60px"alt="" />
      <p style={shellStyles.headerSubtitle}>
        <i>Accelerating Java Modernization</i>
      </p>
    </header>

    <main style={shellStyles.main}>
      <div style={shellStyles.content}>
        {children}
      </div>
    </main>

    <footer style={shellStyles.footer}>
      <div style={shellStyles.footerContent}>
        <div style={shellStyles.footerLeft}>
          Java Migration Accelerator
        </div>
        <div style={shellStyles.footerRight}>
          © {new Date().getFullYear()} All rights reserved
        </div>
      </div>
    </footer>
  </div>
);

export default AppShell;