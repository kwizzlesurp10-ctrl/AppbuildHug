#!/bin/bash

# Antigravity Project Builder - Automation Script
# This script runs all available tests and quality checks.

echo "🚀 Starting Automations..."

# 1. Run Functional Tests
echo -e "\n🔍 Running Functional Tests..."
python3 tests/test_functional.py

if [ $? -eq 0 ]; then
    echo "✅ Functional tests passed!"
else
    echo "❌ Functional tests failed!"
    exit 1
fi

# 2. Check App Process
echo -e "\n📋 Checking Application Process..."
if lsof -i :7860 > /dev/null; then
    echo "✅ Application is running on port 7860."
else
    echo "⚠️ Application is NOT running on port 7860. Attempting to restart..."
    nohup python3 app.py > app.log 2>&1 &
    sleep 5
    if lsof -i :7860 > /dev/null; then
        echo "✅ Application restarted successfully."
    else
        echo "❌ Failed to restart application."
    fi
fi

# 3. Verify GEMINI.md exists
echo -e "\n📄 Verifying documentation..."
if [ -f "GEMINI.md" ]; then
    echo "✅ GEMINI.md exists."
else
    echo "❌ GEMINI.md is missing!"
fi

echo -e "\n✨ All automations completed!"
