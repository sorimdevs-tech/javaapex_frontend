"""
Git Service - Handles GitHub and GitLab API interactions
"""
import os
import tempfile
import shutil
from typing import List, Dict, Any
from github import Github, GithubException
import git
import httpx


class GitHubService:
    def __init__(self):
        self.work_dir = os.getenv("WORK_DIR", tempfile.gettempdir() + "/migrations")
        os.makedirs(self.work_dir, exist_ok=True)
    
    async def list_repositories(self, token: str) -> List[Dict[str, Any]]:
        """List all repositories accessible with the token"""
        try:
            if not token or len(token) < 10:
                raise Exception("Invalid GitHub token format")
            
            g = Github(token)
            user = g.get_user()
            
            # Test authentication by accessing login
            _ = user.login
            
            repos = []
            
            # Get user's own repos
            for repo in user.get_repos():
                repos.append({
                    "name": repo.name,
                    "full_name": repo.full_name,
                    "url": repo.html_url,
                    "default_branch": repo.default_branch,
                    "language": repo.language,
                    "description": repo.description or ""
                })
            
            return repos
        except GithubException as e:
            error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
            raise Exception(f"GitHub API error: {error_msg}")
        except Exception as e:
            raise Exception(f"Failed to connect to GitHub: {str(e)}")
    
    async def analyze_repository(self, token: str, owner: str, repo: str) -> Dict[str, Any]:
        """Analyze a repository to detect Java version, build tool, and structure"""
        try:
            # Allow public repo analysis without token
            if token and len(token.strip()) > 0:
                g = Github(token.strip())
            else:
                g = Github()
            repository = g.get_repo(f"{owner}/{repo}")
            
            analysis = {
                "name": repository.name,
                "full_name": repository.full_name,
                "default_branch": repository.default_branch,
                "language": repository.language,
                "build_tool": None,
                "java_version": None,
                "has_tests": False,
                "dependencies": [],
                "api_endpoints": [],
                "structure": {
                    "has_pom_xml": False,
                    "has_build_gradle": False,
                    "has_src_main": False,
                    "has_src_test": False
                }
            }
            
            # Check for build files
            try:
                contents = repository.get_contents("")
                file_names = [c.name for c in contents]
                
                if "pom.xml" in file_names:
                    analysis["build_tool"] = "maven"
                    analysis["structure"]["has_pom_xml"] = True
                    # Parse pom.xml for Java version
                    pom_content = repository.get_contents("pom.xml").decoded_content.decode()
                    analysis["java_version"] = self._detect_java_version_from_pom(pom_content)
                    analysis["dependencies"] = self._parse_pom_dependencies(pom_content)
                
                elif "build.gradle" in file_names:
                    analysis["build_tool"] = "gradle"
                    analysis["structure"]["has_build_gradle"] = True
                    gradle_content = repository.get_contents("build.gradle").decoded_content.decode()
                    analysis["java_version"] = self._detect_java_version_from_gradle(gradle_content)
                
                # Check for src directory structure
                try:
                    repository.get_contents("src/main")
                    analysis["structure"]["has_src_main"] = True
                except:
                    pass
                
                try:
                    repository.get_contents("src/test")
                    analysis["structure"]["has_src_test"] = True
                    analysis["has_tests"] = True
                except:
                    pass
                
            except GithubException:
                pass
            
            return analysis
            
        except GithubException as e:
            raise Exception(f"GitHub API error: {e.data.get('message', str(e))}")
    
    async def parse_repo_url(self, repo_url: str) -> tuple:
        """Parse GitHub URL to extract owner and repo name"""
        import re
        # Handle various GitHub URL formats
        patterns = [
            r'github\.com[:/]+([^/]+)/([^/\s]+)',  # https://github.com/owner/repo or github.com/owner/repo
            r'^([^/]+)/([^/]+)$',  # owner/repo format
        ]
        for pattern in patterns:
            match = re.search(pattern, repo_url)
            if match:
                return match.group(1), match.group(2).replace('.git', '')
        raise Exception("Invalid GitHub repository URL. Use format: owner/repo or https://github.com/owner/repo")
    
    async def get_repo_info(self, token: str, owner: str, repo: str) -> Dict[str, Any]:
        """Get repository information (works with or without token for public repos)"""
        try:
            if token:
                g = Github(token)
            else:
                g = Github()
            
            repository = g.get_repo(f"{owner}/{repo}")
            
            return {
                "name": repository.name,
                "full_name": repository.full_name,
                "url": repository.html_url,
                "default_branch": repository.default_branch,
                "language": repository.language,
                "description": repository.description or "",
                "is_private": repository.private,
                "owner": repository.owner.login,
            }
        except GithubException as e:
            error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
            raise Exception(f"GitHub API error: {error_msg}")
        except Exception as e:
            raise Exception(f"Failed to get repository info: {str(e)}")
    
    async def list_repo_files(self, token: str, owner: str, repo: str, path: str = "") -> List[Dict[str, Any]]:
        """List all files and directories in a repository"""
        try:
            if token and len(token.strip()) > 0:
                g = Github(token.strip())
            else:
                g = Github()
            
            repository = g.get_repo(f"{owner}/{repo}")
            contents = repository.get_contents(path)
            
            files = []
            for item in contents:
                files.append({
                    "name": item.name,
                    "path": item.path,
                    "type": "file" if not item.type == "dir" else "dir",
                    "size": item.size if hasattr(item, 'size') else 0,
                    "url": item.html_url,
                })
            
            return files
        except GithubException as e:
            error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
            raise Exception(f"GitHub API error: {error_msg}")
        except Exception as e:
            raise Exception(f"Failed to list files: {str(e)}")
    
    async def get_file_content(self, token: str, owner: str, repo: str, path: str) -> str:
        """Get the content of a file from the repository"""
        try:
            if token:
                g = Github(token)
            else:
                g = Github()
            
            repository = g.get_repo(f"{owner}/{repo}")
            file_content = repository.get_contents(path)
            
            if hasattr(file_content, 'decoded_content'):
                return file_content.decoded_content.decode('utf-8')
            return ""
        except GithubException as e:
            error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
            raise Exception(f"GitHub API error: {error_msg}")
        except Exception as e:
            raise Exception(f"Failed to get file content: {str(e)}")
    
    async def clone_repository(self, token: str, repo_url: str) -> str:
        """Clone a repository to local filesystem"""
        # Create unique directory for this clone
        import uuid
        clone_dir = os.path.join(self.work_dir, str(uuid.uuid4()))
        os.makedirs(clone_dir, exist_ok=True)

        # Add token to URL for authentication
        if "github.com" in repo_url:
            auth_url = repo_url.replace("https://", f"https://{token}@")
        else:
            auth_url = repo_url

        try:
            # Use subprocess for better control over git clone with config
            import subprocess

            # Clone with config to handle Windows Zone.Identifier files
            result = subprocess.run([
                'git', 'clone',
                '-c', 'core.protectNTFS=false',  # Allow files with colons in names
                auth_url, clone_dir
            ], capture_output=True, text=True, cwd=os.path.dirname(clone_dir))

            if result.returncode == 0:
                return clone_dir
            else:
                # If clone fails due to Zone.Identifier files, try recovery
                error_msg = result.stderr
                if "Zone.Identifier" in error_msg and "invalid path" in error_msg:
                    # Try clone with --no-checkout first
                    result2 = subprocess.run([
                        'git', 'clone', '--no-checkout', auth_url, clone_dir
                    ], capture_output=True, text=True, cwd=os.path.dirname(clone_dir))

                    if result2.returncode == 0:
                        # Configure the repo and try checkout
                        result3 = subprocess.run([
                            'git', 'config', 'core.protectNTFS', 'false'
                        ], capture_output=True, text=True, cwd=clone_dir)

                        # Try checkout
                        result4 = subprocess.run([
                            'git', 'checkout'
                        ], capture_output=True, text=True, cwd=clone_dir)

                        # Even if checkout fails, return the directory
                        # The migration service can work with partial checkouts
                        return clone_dir
                    else:
                        raise Exception(f"Failed to clone repository (recovery): {result2.stderr}")
                else:
                    raise Exception(f"Failed to clone repository: {error_msg}")
        except Exception as e:
            raise Exception(f"Failed to clone repository: {str(e)}")
    

    async def create_and_push_repo(self, token: str, repo_name: str, local_path: str, description: str) -> str:
        """Create a new repository and push the migrated code"""
        try:
            print(f"DEBUG: Starting repository creation process")
            print(f"DEBUG: Token provided: {'Yes' if token else 'No'} (length: {len(token) if token else 0})")
            print(f"DEBUG: Repo name: {repo_name}")
            print(f"DEBUG: Local path exists: {os.path.exists(local_path)}")

            if not token or len(token.strip()) == 0:
                raise Exception("GitHub token is required to create and push repositories. Please provide a valid Personal Access Token with repo or public_repo scope.")

            g = Github(token)
            user = g.get_user()
            print(f"DEBUG: Authenticated as user: {user.login}")

            # Check if repo already exists
            try:
                existing = user.get_repo(repo_name)
                print(f"DEBUG: Repo {repo_name} already exists, renaming...")
                # If exists, delete it first or use a different name
                repo_name = f"{repo_name}-{int(__import__('time').time())}"
                print(f"DEBUG: New repo name: {repo_name}")
            except GithubException as e:
                print(f"DEBUG: Repo {repo_name} does not exist, proceeding with creation")

            # Create new repository
            try:
                print(f"DEBUG: Creating repo {repo_name}...")
                new_repo = user.create_repo(
                    name=repo_name,
                    description=description,
                    private=False,
                    auto_init=False
                )
                print(f"DEBUG: Repo created successfully: {new_repo.html_url}")
            except GithubException as e:
                error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
                print(f"DEBUG: Repo creation failed: {error_msg}")
                if 'name already exists' in error_msg.lower():
                    # Try with timestamp suffix
                    repo_name = f"{repo_name}-{int(__import__('time').time())}"
                    print(f"DEBUG: Retrying with name: {repo_name}")
                    new_repo = user.create_repo(
                        name=repo_name,
                        description=description,
                        private=False,
                        auto_init=False
                    )
                    print(f"DEBUG: Repo created on retry: {new_repo.html_url}")
                else:
                    raise Exception(f"Repository creation failed: {error_msg}")

            # Initialize git in local path and push
            try:
                print(f"DEBUG: Initializing git repo in {local_path}")
                repo = git.Repo(local_path)
                print("DEBUG: Git repo initialized")
            except git.InvalidGitRepositoryError:
                # Initialize new repo if not already a git repo
                print("DEBUG: Local path not a git repo, initializing...")
                repo = git.Repo.init(local_path)
                print("DEBUG: Git repo initialized from scratch")

            # Remove old remote if exists
            if "origin" in [remote.name for remote in repo.remotes]:
                print("DEBUG: Removing old origin remote")
                repo.delete_remote("origin")

            # Add new remote with token
            auth_url = new_repo.clone_url.replace("https://", f"https://{token}@")
            print(f"DEBUG: Adding remote origin: {auth_url[:50]}...")
            origin = repo.create_remote("origin", auth_url)

            # Check git status before staging
            print("DEBUG: Checking git status...")
            status = repo.git.status(porcelain=True)
            print(f"DEBUG: Git status: {status}")

            if not status.strip():
                print("DEBUG: No changes to commit - creating initial commit")
                # Create a .gitkeep file if directory is empty
                gitkeep_path = os.path.join(local_path, ".gitkeep")
                with open(gitkeep_path, 'w') as f:
                    f.write("# Migration placeholder\n")
                repo.git.add(A=True)

            # Stage and commit all changes
            print("DEBUG: Staging changes...")
            repo.git.add(A=True)

            # Check if there are staged changes
            staged = repo.git.diff("--cached", "--name-only")
            print(f"DEBUG: Staged files: {staged}")

            if staged.strip():
                try:
                    print("DEBUG: Committing changes...")
                    commit_msg = "Java migration completed - upgraded Java version, dependencies, and code quality"
                    repo.index.commit(commit_msg)
                    print(f"DEBUG: Commit successful: {commit_msg}")

                    # Show commit details
                    commit = repo.head.commit
                    print(f"DEBUG: Commit hash: {commit.hexsha}")
                    print(f"DEBUG: Files changed: {len(commit.stats.files)}")
                    print(f"DEBUG: Commit stats: {commit.stats.total}")

                except git.GitCommandError as e:
                    print(f"DEBUG: Commit failed: {str(e)}")
                    print(f"DEBUG: Git status: {repo.git.status()}")
                    raise Exception(f"Git commit failed: {str(e)}")
            else:
                print("DEBUG: No staged changes to commit")
                # Still create an empty commit to establish the repo
                try:
                    repo.index.commit("Migration setup - no source changes detected")
                    print("DEBUG: Empty commit created")
                except git.GitCommandError:
                    print("DEBUG: Could not create empty commit")

            # Push to new repo - try main first, then master
            try:
                print("DEBUG: Checking current branch...")
                current_branch = repo.active_branch.name if repo.heads else None
                print(f"DEBUG: Current branch: {current_branch}")

                if not repo.heads:
                    print("DEBUG: No branches exist, creating main...")
                    repo.git.checkout('-b', 'main')
                    current_branch = 'main'
                    print("DEBUG: Created main branch")
                else:
                    current_branch = repo.active_branch.name

                print(f"DEBUG: Pushing to {current_branch} branch...")
                push_result = origin.push(refspec=f"HEAD:{current_branch}", set_upstream=True, force=True)
                print(f"DEBUG: Push to {current_branch} successful")
                print(f"DEBUG: Push result: {push_result}")

            except git.GitCommandError as e:
                print(f"DEBUG: Push to {current_branch} failed: {str(e)}")

                # Try alternative branch names
                for alt_branch in ['main', 'master']:
                    if alt_branch != current_branch:
                        try:
                            print(f"DEBUG: Retrying push to {alt_branch}...")
                            push_result = origin.push(refspec=f"HEAD:{alt_branch}", force=True)
                            print(f"DEBUG: Push to {alt_branch} successful")
                            break
                        except git.GitCommandError as alt_error:
                            print(f"DEBUG: Push to {alt_branch} also failed: {str(alt_error)}")
                            continue
                else:
                    # All push attempts failed
                    raise Exception(f"Failed to push to repository on any branch: {str(e)}")

            print(f"DEBUG: Migration completed successfully: {new_repo.html_url}")
            return new_repo.html_url

        except GithubException as e:
            error_msg = e.data.get('message', str(e)) if hasattr(e, 'data') else str(e)
            print(f"DEBUG: GitHub API error: {error_msg}")
            raise Exception(f"GitHub API error: {error_msg}")
        except Exception as e:
            import traceback
            error_msg = str(e)
            print(f"DEBUG: Unexpected error: {error_msg}")
            print(f"DEBUG: Full traceback: {traceback.format_exc()}")

            # Provide more specific error messages for common issues
            if "Bad credentials" in error_msg or "401" in error_msg:
                raise Exception("GitHub authentication failed. Please check your token is valid and has the required permissions (repo or public_repo scope).")
            elif "403" in error_msg or "Forbidden" in error_msg:
                raise Exception("GitHub API access forbidden. Your token may not have permission to create repositories. Please check token scopes.")
            elif "name already exists" in error_msg.lower():
                raise Exception("Repository name already exists. The system tried to create a unique name but it still conflicts.")
            elif "Validation Failed" in error_msg:
                raise Exception("Repository validation failed. The repository name may be invalid or you may have reached GitHub's repository limits.")
            elif "git" in error_msg.lower() and ("push" in error_msg.lower() or "remote" in error_msg.lower()):
                raise Exception(f"Git operation failed during repository push: {error_msg}")
            else:
                raise Exception(f"Repository creation failed: {error_msg}")
    
    def _detect_java_version_from_pom(self, pom_content: str) -> str:
        """Detect Java version from pom.xml"""
        import re
        
        # Check for maven.compiler.source
        match = re.search(r'<maven\.compiler\.source>(\d+)</maven\.compiler\.source>', pom_content)
        if match:
            return match.group(1)
        
        # Check for java.version property
        match = re.search(r'<java\.version>(\d+)</java\.version>', pom_content)
        if match:
            return match.group(1)
        
        # Check for source in compiler plugin
        match = re.search(r'<source>(\d+\.?\d*)</source>', pom_content)
        if match:
            version = match.group(1)
            return version.replace("1.", "") if version.startswith("1.") else version
        
        return "unknown"
    
    def _detect_java_version_from_gradle(self, gradle_content: str) -> str:
        """Detect Java version from build.gradle"""
        import re
        
        # Check for sourceCompatibility
        match = re.search(r"sourceCompatibility\s*=\s*['\"]?(\d+)['\"]?", gradle_content)
        if match:
            return match.group(1)
        
        # Check for JavaVersion enum
        match = re.search(r"JavaVersion\.VERSION_(\d+)", gradle_content)
        if match:
            return match.group(1)
        
        return "unknown"
    
    def _parse_pom_dependencies(self, pom_content: str) -> List[Dict[str, str]]:
        """Parse dependencies from pom.xml"""
        import re
        
        dependencies = []
        dep_pattern = re.compile(
            r'<dependency>\s*'
            r'<groupId>([^<]+)</groupId>\s*'
            r'<artifactId>([^<]+)</artifactId>\s*'
            r'(?:<version>([^<]+)</version>)?',
            re.DOTALL
        )
        
        for match in dep_pattern.finditer(pom_content):
            dependencies.append({
                "group_id": match.group(1),
                "artifact_id": match.group(2),
                "current_version": match.group(3) or "inherited",
                "new_version": None,
                "status": "analyzing"
            })
        
        return dependencies
        
