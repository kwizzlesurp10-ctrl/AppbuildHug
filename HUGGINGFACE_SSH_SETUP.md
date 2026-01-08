# Hugging Face SSH Key Setup

## Your SSH Public Key (add this to Hugging Face)

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINwfk3hxTrO0Lj1Rpq4eth/r9UJJkyx+QGEbouY5v5Ab huggingface-developer
```

## Steps to Add SSH Key to Hugging Face

1. **Copy your public key** (shown above)

2. **Go to Hugging Face Settings:**
   - Visit: https://huggingface.co/settings/keys
   - Or navigate: Profile → Settings → SSH Keys

3. **Add the SSH key:**
   - Click "New SSH Key"
   - Give it a name (e.g., "My Development Machine")
   - Paste the public key above
   - Click "Add SSH Key"

## SSH Configuration

Your SSH key is located at:
- **Private Key:** `~/.ssh/id_ed25519_hf`
- **Public Key:** `~/.ssh/id_ed25519_hf.pub`

## Using Git with Hugging Face

After adding the key, you can clone repositories using SSH:

```bash
# Clone a model repository
git clone git@hf.co:username/model-name.git

# Or clone your space
git clone git@hf.co:spaces/username/space-name.git
```

## Testing the Connection

Test your SSH connection:

```bash
ssh -T git@hf.co
```

You should see: `"Welcome to Hugging Face. You are authenticated as <your-username>"`

## Connecting to Hugging Face Space via SSH

To connect to your Space's development environment:

```bash
ssh -i ~/.ssh/id_ed25519_hf onyxmunk-antigravity-project-builder@ssh.hf.space
```

**Important:** Make sure:
1. Your SSH key is added to your Hugging Face account (see steps above)
2. SSH access is enabled for your Space (Settings → SSH Access)
3. Your Space is running (not paused)

You can also add this to your SSH config for easier access:

```bash
# Add to ~/.ssh/config
Host hf-space
    HostName ssh.hf.space
    User onyxmunk-antigravity-project-builder
    IdentityFile ~/.ssh/id_ed25519_hf
    IdentitiesOnly yes
```

Then connect with: `ssh hf-space`

## Commands & Actions Once Connected

See **[HF_SPACE_SSH_COMMANDS.md](./HF_SPACE_SSH_COMMANDS.md)** for a comprehensive guide of commands and actions you can take once connected via SSH to your Space.

## For Your AppbuildHug Project

If you want to push this project to Hugging Face Spaces:

```bash
# Initialize git if not already done
git init

# Add Hugging Face remote (replace with your username/space-name)
git remote add origin git@hf.co:spaces/YOUR_USERNAME/AppbuildHug.git

# Push your code
git add .
git commit -m "Initial commit"
git push origin main
```

## Troubleshooting

If you encounter permission issues:
```bash
chmod 600 ~/.ssh/id_ed25519_hf
chmod 644 ~/.ssh/id_ed25519_hf.pub
```

If SSH agent isn't running:
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519_hf
```
