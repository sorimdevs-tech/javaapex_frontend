# 🚀 Java Migration Accelerator

**End-to-End Java 7 → Java 21 Migration Automation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-18+-61dafb.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)

## 🌟 Overview

Java Migration Accelerator is a comprehensive, enterprise-grade solution for automating Java version migrations. It intelligently analyzes Java projects, applies complex migration rules, and delivers production-ready code with full traceability.

### ✨ Key Features

- **🔄 Multi-Version Support**: Java 7 → Java 8/11/17/18/21
- **📦 Framework Migrations**: Spring Boot 2→3, Jakarta EE, JUnit 4→5
- **🎯 Smart Code Analysis**: Detects deprecated APIs, security issues, performance problems
- **🔧 Automated Fixes**: 18+ comprehensive business logic improvements
- **🌐 Multi-Platform**: GitHub & GitLab support
- **📊 Migration Reports**: Detailed HTML reports with change tracking
- **🧪 Quality Assurance**: SonarQube integration, JMeter test generation
- **📧 Email Notifications**: Migration summaries and alerts
- **🚀 Cloud Deployment**: Railway, Render, Vercel ready

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git
- GitHub/GitLab Personal Access Token

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/java-migration-accelerator.git
cd java-migration-accelerator

# Backend Setup
cd java-migration-backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your tokens
python main.py

# Frontend Setup (new terminal)
cd ../java-migration-frontend
npm install
npm run dev
```

Visit `http://localhost:5173` for the web interface and `http://localhost:8001` for API docs.

## 🎯 Core Capabilities

### Java Version Migrations
- **Java 7 → 8**: Lambda expressions, Stream API, Optional
- **Java 8 → 11**: String methods, Collections, Files API
- **Java 11 → 17**: Text blocks, records, sealed classes
- **Java 17 → 21**: Virtual threads, pattern matching, sequenced collections

### Framework Migrations
- **Spring Boot 2 → 3**: Jakarta EE, security config updates
- **JUnit 4 → 5**: Annotations, assertions, extensions
- **javax → jakarta**: Complete Jakarta EE migration
- **Log4j → SLF4J**: Logging framework modernization

### Code Quality Improvements
- **Null Safety**: Objects.equals(), Optional usage
- **Performance**: StringBuilder optimizations
- **Thread Safety**: Concurrent collections
- **Exception Handling**: Specific exception types
- **Resource Management**: Try-with-resources patterns

## 🏗️ Architecture

```
java-migration-accelerator/
├── java-migration-backend/          # FastAPI Backend
│   ├── services/                    # Business Logic
│   │   ├── migration_service.py     # Core Migration Logic
│   │   ├── github_service.py        # GitHub Integration
│   │   ├── gitlab_service.py        # GitLab Integration
│   │   ├── email_service.py         # Email Notifications
│   │   └── sonarqube_service.py     # Code Quality
│   ├── main.py                      # FastAPI Application
│   └── requirements.txt             # Python Dependencies
├── java-migration-frontend/         # React Frontend
│   ├── src/
│   │   ├── components/              # React Components
│   │   └── services/                # API Integration
│   └── package.json                 # Node Dependencies
└── deployment/                      # Cloud Deployment
    ├── Dockerfile                   # Container Config
    ├── railway.toml                # Railway Config
    └── render.yaml                  # Render Config
```

## 📡 API Endpoints

### Migration Operations
- `POST /api/migration/start` - Start migration job
- `GET /api/migration/{job_id}` - Get migration status
- `POST /api/migration/preview` - Preview migration changes

### Repository Operations
- `GET /api/github/repos` - List GitHub repositories
- `GET /api/gitlab/repos` - List GitLab repositories
- `GET /api/github/analyze-url` - Analyze repository by URL

### Reports & Testing
- `GET /api/migration/{job_id}/report` - Download HTML report
- `GET /api/migration/{job_id}/jmeter` - Generate JMeter tests

## 🚀 Deployment Options

### Railway (Recommended)
```bash
# Deploy backend to Railway
railway login
railway init
railway up
```

### Render
```bash
# Deploy full-stack app to Render
# Use render.yaml configuration
```

### Docker
```bash
# Build and run with Docker
docker build -t java-migration .
docker run -p 8001:8001 -p 5173:5173 java-migration
```

### Vercel (Frontend Only)
```bash
# Deploy frontend to Vercel
cd java-migration-frontend
vercel --prod
```

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Git Platform Tokens
GITHUB_TOKEN=ghp_your_github_token_here
GITLAB_TOKEN=glpat_your_gitlab_token_here

# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_app_password

# SonarQube Configuration
SONARQUBE_URL=https://sonarcloud.io
SONARQUBE_TOKEN=your_sonar_token

# Application Settings
WORK_DIR=/tmp/migrations
GITLAB_URL=https://gitlab.com
```

## 📊 Migration Examples

### Basic Java Version Migration
```json
{
  "platform": "github",
  "source_repo_url": "https://github.com/company/legacy-app",
  "target_repo_name": "migrated-legacy-app",
  "source_java_version": "8",
  "target_java_version": "17",
  "token": "ghp_...",
  "conversion_types": ["java_version"],
  "fix_business_logic": true
}
```

### Complete Framework Migration
```json
{
  "platform": "gitlab",
  "source_repo_url": "https://gitlab.com/company/spring-app",
  "target_repo_name": "modernized-spring-app",
  "source_java_version": "8",
  "target_java_version": "17",
  "token": "glpat_...",
  "conversion_types": ["java_version", "spring_boot_2_to_3", "javax_to_jakarta"],
  "run_tests": true,
  "run_sonar": true,
  "email": "team@company.com"
}
```

## 🎨 User Interface

### Migration Wizard
1. **Repository Selection**: Choose GitHub/GitLab repository
2. **Migration Configuration**: Select target Java version and conversions
3. **Preview Changes**: Review planned modifications
4. **Execute Migration**: Run automated migration
5. **Download Reports**: Get detailed migration documentation

### Dashboard Features
- Real-time migration progress
- Detailed logs and error tracking
- File-by-file change summaries
- Dependency upgrade reports
- Quality gate results

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenRewrite for Java transformation recipes
- FastAPI for the robust backend framework
- React for the modern frontend experience
- GitHub/GitLab APIs for repository integration

## 📞 Support

- 📧 Email: support@java-migration-accelerator.com
- 📖 Documentation: [docs.java-migration-accelerator.com](https://docs.java-migration-accelerator.com)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/java-migration-accelerator/issues)

---

**Built with ❤️ for the Java community**