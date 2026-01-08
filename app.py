"""
Antigravity Project Builder
A beautiful Gradio app for visualizing project architectures with zero-gravity animations.
Supports both demo mode (static) and Gemini-powered dynamic blueprint generation.
"""

import os
import gradio as gr
from typing import Optional

# Try to import Gemini (optional)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# Configuration
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
DEMO_MODE = os.environ.get("DEMO_MODE", "true").lower() == "true"

# Placeholder blueprint for demo mode
DEMO_BLUEPRINT = """
# Project Blueprint: {project_name}

## Tech Stack
- **Frontend**: React 19 + TypeScript + Tailwind CSS
- **Backend**: Next.js 15 App Router + tRPC
- **Database**: PostgreSQL with Drizzle ORM
- **Authentication**: NextAuth.js with OAuth providers
- **AI Integration**: OpenAI API / Anthropic Claude
- **Deployment**: Vercel (Frontend) + Railway (Backend)

## Architecture Overview
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   Backend   │────▶│  Database   │
│   (React)   │     │  (Next.js)  │     │ (PostgreSQL)│
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       └───────────────────┴───────────────────┘
                          │
                   ┌──────▼──────┐
                   │  AI Service │
                   │  (OpenAI)   │
                   └─────────────┘
```

## Key Files Structure
```
project-root/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── api/
│       └── trpc/
│           └── [trpc]/
├── components/
│   ├── ui/
│   └── features/
├── server/
│   ├── routers/
│   └── db/
├── lib/
│   └── utils.ts
└── package.json
```

## Next Steps
1. Initialize Next.js project with TypeScript
2. Set up Drizzle ORM and database schema
3. Configure tRPC endpoints
4. Implement authentication flow
5. Build core features iteratively
"""


def generate_animation_html() -> str:
    """Generate the HTML for the animated orbiting orbs canvas."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js"></script>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                background: #0a0015;
                overflow: hidden;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            }
            
            #canvas-container {
                width: 100%;
                height: 450px;
                position: relative;
                background: radial-gradient(circle at center, #1a0035 0%, #0a0015 100%);
                border-radius: 12px;
                overflow: hidden;
                cursor: pointer;
            }
            
            #central-core {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 80px;
                height: 80px;
                background: radial-gradient(circle, #a855f7 0%, #3b82f6 50%, #0a0015 100%);
                border-radius: 50%;
                box-shadow: 0 0 40px rgba(168, 85, 247, 0.6),
                            0 0 80px rgba(59, 130, 246, 0.4),
                            inset 0 0 20px rgba(255, 255, 255, 0.1);
                z-index: 10;
            }
            
            .orb {
                position: absolute;
                border-radius: 50%;
                box-shadow: 0 0 20px currentColor;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 10px;
                font-weight: bold;
                color: rgba(255, 255, 255, 0.9);
                text-shadow: 0 0 10px currentColor;
                user-select: none;
            }
            
            .orb-frontend { background: linear-gradient(135deg, #10b981, #059669); color: #10b981; width: 50px; height: 50px; }
            .orb-backend { background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: #8b5cf6; width: 55px; height: 55px; }
            .orb-db { background: linear-gradient(135deg, #f59e0b, #d97706); color: #f59e0b; width: 48px; height: 48px; }
            .orb-ai { background: linear-gradient(135deg, #3b82f6, #2563eb); color: #3b82f6; width: 52px; height: 52px; }
            .orb-auth { background: linear-gradient(135deg, #ec4899, #db2777); color: #ec4899; width: 46px; height: 46px; }
            .orb-api { background: linear-gradient(135deg, #06b6d4, #0891b2); color: #06b6d4; width: 49px; height: 49px; }
            .orb-deploy { background: linear-gradient(135deg, #6366f1, #4f46e5); color: #6366f1; width: 51px; height: 51px; }
            .orb-test { background: linear-gradient(135deg, #14b8a6, #0d9488); color: #14b8a6; width: 47px; height: 47px; }
        </style>
    </head>
    <body>
        <div id="canvas-container" aria-label="Animated project architecture visualization">
            <div id="central-core"></div>
            <!-- Orbs will be dynamically created -->
        </div>
        
        <script>
            console.log("Floating free... 🚀");
            
            if (typeof anime === 'undefined') {
                console.error("Anime.js not loaded");
            } else {
                const container = document.getElementById('canvas-container');
                const core = document.getElementById('central-core');
                const centerX = container.offsetWidth / 2;
                const centerY = container.offsetHeight / 2;
                
                // Orb configurations: [label, class, radius, duration, delay, direction]
                const orbConfigs = [
                    ['FE', 'orb-frontend', 120, 6000, 0, 1],
                    ['BE', 'orb-backend', 140, 7500, 300, -1],
                    ['DB', 'orb-db', 100, 5000, 600, 1],
                    ['AI', 'orb-ai', 160, 8500, 900, -1],
                    ['Auth', 'orb-auth', 110, 5500, 1200, 1],
                    ['API', 'orb-api', 130, 7000, 1500, -1],
                    ['Deploy', 'orb-deploy', 150, 8000, 1800, 1],
                    ['Test', 'orb-test', 105, 5800, 2100, -1]
                ];
                
                const orbs = [];
                
                // Create orbs
                orbConfigs.forEach(([label, className, radius, duration, delay, direction], index) => {
                    const orb = document.createElement('div');
                    orb.className = `orb ${className}`;
                    orb.textContent = label;
                    orb.style.left = `${centerX}px`;
                    orb.style.top = `${centerY}px`;
                    container.appendChild(orb);
                    orbs.push({ element: orb, radius, duration, delay, direction, angle: (index * 45) * Math.PI / 180 });
                });
                
                // Animate orbiting
                function animateOrbits() {
                    orbs.forEach(({ element, radius, duration, delay, direction, angle }) => {
                        anime({
                            targets: element,
                            translateX: [
                                { value: () => Math.cos(angle) * radius },
                                { value: () => Math.cos(angle + direction * Math.PI * 2) * radius }
                            ],
                            translateY: [
                                { value: () => Math.sin(angle) * radius },
                                { value: () => Math.sin(angle + direction * Math.PI * 2) * radius }
                            ],
                            rotate: direction * 360,
                            scale: [
                                { value: 0.8, duration: duration / 2 },
                                { value: 1.2, duration: duration / 2 }
                            ],
                            opacity: [
                                { value: 0.7, duration: duration / 3 },
                                { value: 1, duration: duration / 3 },
                                { value: 0.7, duration: duration / 3 }
                            ],
                            duration: duration,
                            delay: delay,
                            easing: 'linear',
                            loop: true
                        });
                    });
                }
                
                // Central core breathing animation
                anime({
                    targets: core,
                    scale: [
                        { value: 1, duration: 2000 },
                        { value: 1.15, duration: 2000 }
                    ],
                    opacity: [
                        { value: 0.9, duration: 2000 },
                        { value: 1, duration: 2000 }
                    ],
                    loop: true,
                    easing: 'easeInOutSine'
                });
                
                // Start orbiting animation
                animateOrbits();
                
                // Double-click burst effect
                let burstTimeout;
                container.addEventListener('dblclick', () => {
                    // Clear any existing burst
                    if (burstTimeout) clearTimeout(burstTimeout);
                    
                    // Random spin and scale burst
                    orbs.forEach(orb => {
                        anime({
                            targets: orb.element,
                            rotate: () => anime.random(360, 720),
                            scale: [1, 1.5, 1],
                            duration: 800,
                            easing: 'easeOutElastic(1, .8)'
                        });
                    });
                    
                    // Core pulse
                    anime({
                        targets: core,
                        scale: [1, 1.3, 1],
                        duration: 600,
                        easing: 'easeOutElastic(1, .6)'
                    });
                });
            }
        </script>
    </body>
    </html>
    """


def generate_blueprint_demo(project_idea: str) -> str:
    """Generate a demo blueprint with the project idea."""
    project_name = project_idea.strip()[:50] if project_idea.strip() else "Your Dream Project"
    return DEMO_BLUEPRINT.format(project_name=project_name)


def generate_blueprint_gemini(project_idea: str) -> str:
    """Generate a blueprint using Gemini API."""
    if not GEMINI_AVAILABLE:
        return "❌ Gemini API not available. Install google-generativeai package."
    
    if not GEMINI_API_KEY:
        return "❌ GEMINI_API_KEY not set. Please configure it in Hugging Face Spaces secrets."
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Create a concise full-stack project blueprint for: {project_idea}

Include:
1. Tech stack recommendations
2. Architecture overview (ASCII diagram preferred)
3. Key files structure
4. Implementation steps

Format as markdown. Be practical and production-ready."""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating blueprint: {str(e)}\n\nFalling back to demo mode...\n\n{generate_blueprint_demo(project_idea)}"


def process_project(project_idea: str, use_gemini: bool) -> tuple[str, str]:
    """Process the project idea and return animation HTML and blueprint."""
    # Always return the same animation HTML
    animation_html = generate_animation_html()
    
    # Generate blueprint based on mode
    if use_gemini and GEMINI_AVAILABLE and GEMINI_API_KEY:
        blueprint = generate_blueprint_gemini(project_idea)
    else:
        blueprint = generate_blueprint_demo(project_idea)
    
    return animation_html, blueprint


def create_interface():
    """Create and configure the Gradio interface."""
    with gr.Blocks() as app:
        gr.Markdown(
            "# 🚀 Antigravity Project Builder\n\n"
            "Describe your dream project and watch it assemble in zero-gravity space."
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                project_input = gr.Textbox(
                    label="Describe your dream project...",
                    placeholder="e.g., A social media platform for developers with AI-powered code reviews",
                    lines=4,
                    value=""
                )
                
                use_gemini_checkbox = gr.Checkbox(
                    label="Use Gemini AI (requires GEMINI_API_KEY)",
                    value=not DEMO_MODE and GEMINI_AVAILABLE and bool(GEMINI_API_KEY),
                    interactive=GEMINI_AVAILABLE and bool(GEMINI_API_KEY)
                )
                
                launch_btn = gr.Button(
                    "Launch into Orbit 🚀",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                animation_output = gr.HTML(
                    value=generate_animation_html(),
                    label="Project Architecture Visualization",
                    height=450
                )
        
        blueprint_output = gr.Markdown(
            value="*Enter a project idea and click 'Launch into Orbit' to generate your blueprint.*",
            label="Project Blueprint"
        )
        
        # Event handlers
        launch_btn.click(
            fn=process_project,
            inputs=[project_input, use_gemini_checkbox],
            outputs=[animation_output, blueprint_output]
        )
        
        # Auto-update animation on input change (optional)
        project_input.submit(
            fn=process_project,
            inputs=[project_input, use_gemini_checkbox],
            outputs=[animation_output, blueprint_output]
        )
        
        gr.Markdown(
            "---\n"
            "### 💡 Tips\n"
            "- **Double-click the animation** for a burst effect\n"
            "- Each orb represents a different component (Frontend, Backend, Database, etc.)\n"
            "- Enable Gemini mode for AI-powered blueprint generation\n"
            "- Configure `GEMINI_API_KEY` in Hugging Face Spaces secrets for dynamic mode"
        )
    
    return app


if __name__ == "__main__":
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        theme=gr.themes.Soft(primary_hue="purple"),
        css="""
        .gradio-container {
            background: #0a0015 !important;
        }
        .markdown {
            color: #e0e0e0 !important;
        }
        .input-text textarea {
            background: #1a0035 !important;
            color: #ffffff !important;
            border: 1px solid #3b82f6 !important;
        }
        .output-html {
            background: transparent !important;
        }
        """
    )
