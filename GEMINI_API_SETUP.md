# Setting up Gemini API Key

## Get Your API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API key"
4. Copy the generated API key

## Set the Environment Variable
Replace `your_gemini_api_key_here` with your actual API key:

```bash
export GEMINI_API_KEY="your_actual_api_key_here"
```

## Restart the Application
After setting the API key, restart the app:

```bash
python3 app.py
```

## Features Unlocked
Once the API key is set:
- ✅ Gemini AI mode becomes available
- ✅ Dynamic project blueprint generation
- ✅ AI-powered architecture suggestions
- ✅ Custom project recommendations

## Troubleshooting
- If Gemini mode still doesn't work, check that your API key is valid
- Ensure you have sufficient API quota/credits
- The app will fall back to demo mode if the API key is invalid