Azul Process Reporter CLI Tool

This is a cross-platform CLI utility that generates a detailed report of running processes on your system. It was built as a portable, secure, and user-friendly tool with support for CI/CD, automated testing, and optional Ansible-based setup.

Features

- Lists running processes including:
  - PID (Process ID)
  - Name
  - User
  - CPU usage
  - Memory usage (in MB)
- Outputs report in `CSV` or `JSON`
- Can be executed from any directory
- Easy to use: no external dependencies beyond Python and `psutil`
- CI pipeline via Jenkins (Linux and Windows support)
- Environment setup automation via Ansible (Linux) or batch script (Windows)

---

Installation & Setup

# Linux/macOS (with Ansible)

1. Ensure you have Python 3 and Ansible installed.
2. Run the Ansible playbook to set up the environment:

   ```bash
   ansible-playbook setup_azul_env.yml
   ```

[GitHub Repository](https://github.com/Rokoshik/azul_project)
