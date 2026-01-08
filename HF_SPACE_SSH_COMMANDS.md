# Hugging Face Space SSH Commands & Actions Guide

Once connected via SSH to your Hugging Face Space (`ssh hf-space`), here are useful commands and actions you can take:

## 🔍 System Information & Environment

```bash
# Check current directory
pwd

# List files and directories
ls -la

# Check disk space
df -h

# Check memory usage
free -h

# Check running processes
ps aux

# Check system info
uname -a

# Check Python version
python --version
python3 --version

# Check pip packages
pip list

# Check environment variables
env
printenv

# Check Hugging Face specific environment
echo $HF_USERNAME
echo $HF_SPACE_ID
```

## 📁 File System Navigation

```bash
# Navigate to your Space root
cd /home/user

# List all files (including hidden)
ls -lah

# Find files by name
find . -name "*.py"
find . -name "*.txt"

# View file contents
cat filename.py
less filename.py
head -n 20 filename.py
tail -n 20 filename.py

# Edit files (nano is usually available)
nano app.py
# Or use vi/vim if available
vi app.py

# Create directories
mkdir -p new_directory

# Copy files
cp source.py dest.py

# Move/rename files
mv old_name.py new_name.py

# Delete files (careful!)
rm filename.py
rm -rf directory_name
```

## 🐍 Python & Dependencies

```bash
# Check Python path
which python
which python3

# Run Python scripts
python app.py
python3 app.py

# Install packages
pip install package_name
pip install -r requirements.txt

# Upgrade pip
pip install --upgrade pip

# Check installed packages
pip show package_name
pip list | grep package_name

# Create virtual environment (if needed)
python3 -m venv venv
source venv/bin/activate
```

## 🔧 Gradio & App Management

```bash
# Check if Gradio is running
ps aux | grep gradio
ps aux | grep python

# View Gradio logs
# Logs are usually in /tmp or check with:
journalctl -u gradio 2>/dev/null || echo "Check logs directory"

# Restart your app (if you have restart script)
# Usually handled by Hugging Face, but you can:
pkill -f gradio
python app.py &

# Test your app locally
python app.py
```

## 📦 Git Operations

```bash
# Check git status
git status

# View git log
git log --oneline -10

# Check git remotes
git remote -v

# View changes
git diff

# Stage and commit changes
git add .
git commit -m "Your commit message"

# Push to Hugging Face (if configured)
git push origin main

# Pull latest changes
git pull origin main

# View git config
git config --list
```

## 🔐 Hugging Face CLI

```bash
# Check if HF CLI is installed
huggingface-cli --version

# Login to Hugging Face
huggingface-cli login

# Upload files
huggingface-cli upload username/model-name ./file.txt

# Download files
huggingface-cli download username/model-name

# List your spaces
huggingface-cli repo list --type space
```

## 📊 Monitoring & Debugging

```bash
# Monitor system resources in real-time
top
htop  # if available

# Check network connections
netstat -tuln
ss -tuln

# Check disk I/O
iostat  # if available

# View system logs
dmesg | tail
journalctl -n 50

# Check error logs
tail -f /var/log/syslog  # if accessible
```

## 🧪 Testing & Validation

```bash
# Test Python imports
python3 -c "import gradio; print('Gradio OK')"
python3 -c "import google.generativeai; print('Gemini OK')"

# Run syntax check
python3 -m py_compile app.py

# Test HTTP endpoints (if your app exposes them)
curl http://localhost:7860
curl http://127.0.0.1:7860/health

# Check port availability
netstat -tuln | grep 7860
```

## 🔄 Environment & Configuration

```bash
# Check Space secrets/environment variables
# These are usually set by Hugging Face
env | grep HF_
env | grep GEMINI
env | grep DEMO

# View Space configuration
cat .env  # if exists
cat README.md
cat requirements.txt

# Check Space metadata
cat .hf/config.json  # if exists
```

## 📝 File Editing Tips

```bash
# Quick edits with nano
nano app.py
# Ctrl+O to save, Ctrl+X to exit

# View and edit with vi/vim
vi app.py
# Press 'i' to insert, ESC then ':wq' to save and quit

# Create backup before editing
cp app.py app.py.backup

# Compare files
diff file1.py file2.py
```

## 🚀 Quick Actions for Your Antigravity Project

```bash
# Check your app.py
cat app.py | head -50

# Verify requirements
cat requirements.txt

# Test if app runs
python3 -c "import app; print('App imports OK')"

# Check Gradio version
python3 -c "import gradio; print(gradio.__version__)"

# View preview HTML
cat preview.html | head -50

# Check for syntax errors
python3 -m py_compile app.py && echo "No syntax errors!"
```

## 🔍 Troubleshooting Commands

```bash
# Check if app is running
ps aux | grep -E "(gradio|python.*app)"

# Find error logs
find /tmp -name "*.log" -type f
find /var/log -name "*gradio*" -type f 2>/dev/null

# Check file permissions
ls -la app.py
chmod +x app.py  # if needed

# Verify file integrity
md5sum app.py
sha256sum app.py

# Check Python path issues
python3 -c "import sys; print('\n'.join(sys.path))"
```

## 📤 Exporting & Backing Up

```bash
# Create a backup of your files
tar -czf backup.tar.gz *.py *.txt *.html requirements.txt

# List files to backup
ls -lah

# Copy files locally (from your machine, not SSH)
# Use scp from your local terminal:
# scp hf-space:/home/user/app.py ./app.py.backup
```

## 🎯 Common Workflows

### Update Your App
```bash
# 1. Edit your code
nano app.py

# 2. Test it
python3 -m py_compile app.py

# 3. Commit changes
git add app.py
git commit -m "Updated app"
git push origin main

# 4. Hugging Face will rebuild automatically
```

### Debug Issues
```bash
# 1. Check logs
tail -f /tmp/gradio.log  # or wherever logs are

# 2. Test imports
python3 -c "import app"

# 3. Run app manually to see errors
python3 app.py

# 4. Check environment
env | grep -E "(HF_|GEMINI|DEMO)"
```

### Install New Dependencies
```bash
# 1. Add to requirements.txt
echo "new-package==1.0.0" >> requirements.txt

# 2. Install locally to test
pip install new-package==1.0.0

# 3. Commit and push
git add requirements.txt
git commit -m "Added new dependency"
git push origin main
```

## ⚠️ Important Notes

- **File Changes**: Changes made via SSH are temporary unless committed to git
- **Auto-rebuild**: Hugging Face rebuilds your Space when you push to git
- **Resource Limits**: Spaces have resource limits (CPU, memory, disk)
- **Persistence**: Some directories may be ephemeral; check `/home/user` for persistent storage
- **Permissions**: You may have limited permissions; some system commands might not work

## 🆘 Getting Help

```bash
# Check Hugging Face documentation
# Visit: https://huggingface.co/docs/hub/spaces

# View Space settings
# Go to: https://huggingface.co/spaces/onyxmunk/antigravity-project-builder/settings
```

---

**Pro Tip**: Keep a terminal open with `tail -f` on log files to monitor your app in real-time while making changes!
