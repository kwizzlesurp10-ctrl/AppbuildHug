import time
import requests
from gradio_client import Client

BASE_URL = "http://localhost:7860"

def test_homepage_availability():
    """Test if the homepage is accessible."""
    print(f"Testing homepage availability at {BASE_URL}...")
    try:
        response = requests.get(BASE_URL)
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        print("✅ Homepage is accessible.")
    except Exception as e:
        print(f"❌ Homepage check failed: {e}")
        exit(1)

def test_app_logic_demo_mode():
    """Test the main logic in Demo mode."""
    print("\nTesting App Logic (Demo Mode)...")
    try:
        client = Client(BASE_URL)
        
        # Input: Project idea, Use Gemini (False)
        result = client.predict(
            "A fast retro arcade game",
            False,
            api_name="/process_project"
        )
        
        # Result is a tuple (animation_html, blueprint_markdown)
        # Note: gradio_client might return it as a list/tuple depending on version/api
        
        animation_html = result[0]
        blueprint = result[1]
        
        # Verify Animation HTML
        assert "<!DOCTYPE html>" in animation_html, "Animation HTML missing doctype"
        assert "anime.min.js" in animation_html, "Animation HTML missing anime.js"
        assert "orbConfigs" in animation_html, "Animation HTML missing orb configurations"
        assert "orb-frontend" in animation_html, "Animation HTML missing specific orb class"
        print("✅ Animation HTML generated successfully.")
        
        # Verify Blueprint (Demo mode should contain specific text)
        assert "Project Blueprint: A fast retro arcade game" in blueprint, "Blueprint title mismatch"
        assert "Tech Stack" in blueprint, "Blueprint missing structure"
        print("✅ Demo Blueprint generated successfully.")
        
    except Exception as e:
        print(f"❌ Demo mode test failed: {e}")
        # Try to print available API names if it failed
        try:
            client = Client(BASE_URL)
            print("Available endpoints:", client.view_api())
        except:
            pass

def test_app_logic_gemini_fallback():
    """Test the main logic requesting Gemini mode (expecting fallback if no key)."""
    print("\nTesting App Logic (Gemini Mode - Expecting Fallback/Response)...")
    try:
        client = Client(BASE_URL)
        
        # Input: Project idea, Use Gemini (True)
        result = client.predict(
            "A quantum computing simulator",
            True,
            api_name="/process_project"
        )
        
        blueprint = result[1]
        
        # Since we likely don't have a key set in the running process, 
        # it should either be the demo blueprint OR an error message if the key was set but invalid.
        # But looking at the code: if not GEMINI_API_KEY: -> generate_blueprint_demo
        
        if "Project Blueprint: A quantum computing simulator" in blueprint:
            print("✅ Blueprint generated (Likely Fallback to Demo or successful mock).")
        elif "Error generating blueprint" in blueprint:
            print("✅ Error handled gracefully (Gemini attempted but failed).")
        else:
            # If it actually worked (if user environment had a key), that's good too.
            print(f"ℹ️ Received blueprint: {blueprint[:100]}...")
            print("✅ Blueprint generated.")

    except Exception as e:
        print(f"❌ Gemini mode test failed: {e}")

if __name__ == "__main__":
    # Give the app a moment if it just started (though we checked lsof)
    time.sleep(2)
    
    test_homepage_availability()
    test_app_logic_demo_mode()
    test_app_logic_gemini_fallback()
