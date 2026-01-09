"""
Antigravity Project Builder
A beautiful Gradio app for visualizing project architectures with zero-gravity animations.
Supports both demo mode (static) and Gemini-powered dynamic blueprint generation.
"""

import os
import gradio as gr
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

# Try to import Gemini (optional)
try:
    from google import genai
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
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
                touch-action: none;
            }

            #canvas-container {
                width: 100%;
                height: clamp(300px, 50vh, 450px);
                position: relative;
                background: radial-gradient(circle at center, #1a0035 0%, #0a0015 100%);
                border-radius: 12px;
                overflow: hidden;
                cursor: pointer;
                min-height: 300px;
                max-height: 450px;
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
            
            .orb-frontend { background: linear-gradient(135deg, #10b981, #059669); color: #10b981; width: clamp(35px, 8vw, 50px); height: clamp(35px, 8vw, 50px); }
            .orb-backend { background: linear-gradient(135deg, #8b5cf6, #7c3aed); color: #8b5cf6; width: clamp(40px, 9vw, 55px); height: clamp(40px, 9vw, 55px); }
            .orb-db { background: linear-gradient(135deg, #f59e0b, #d97706); color: #f59e0b; width: clamp(34px, 7.5vw, 48px); height: clamp(34px, 7.5vw, 48px); }
            .orb-ai { background: linear-gradient(135deg, #3b82f6, #2563eb); color: #3b82f6; width: clamp(37px, 8.2vw, 52px); height: clamp(37px, 8.2vw, 52px); }
            .orb-auth { background: linear-gradient(135deg, #ec4899, #db2777); color: #ec4899; width: clamp(33px, 7.2vw, 46px); height: clamp(33px, 7.2vw, 46px); }
            .orb-api { background: linear-gradient(135deg, #06b6d4, #0891b2); color: #06b6d4; width: clamp(35px, 7.7vw, 49px); height: clamp(35px, 7.7vw, 49px); }
            .orb-deploy { background: linear-gradient(135deg, #6366f1, #4f46e5); color: #6366f1; width: clamp(36px, 8vw, 51px); height: clamp(36px, 8vw, 51px); }
            .orb-test { background: linear-gradient(135deg, #14b8a6, #0d9488); color: #14b8a6; width: clamp(33px, 7.3vw, 47px); height: clamp(33px, 7.3vw, 47px); }

            @media (max-width: 768px) {
                .orb {
                    font-size: 8px !important;
                }
            }

            @media (max-width: 480px) {
                .orb {
                    font-size: 7px !important;
                }
            }
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
                
                // Responsive orb configurations
                const containerWidth = container.offsetWidth;
                const containerHeight = container.offsetHeight;
                const minDimension = Math.min(containerWidth, containerHeight);
                const scale = Math.min(minDimension / 400, 1); // Scale based on 400px reference

                // Orb configurations: [label, class, radius, duration, delay, direction]
                const orbConfigs = [
                    ['FE', 'orb-frontend', 120 * scale, 6000, 0, 1],
                    ['BE', 'orb-backend', 140 * scale, 7500, 300, -1],
                    ['DB', 'orb-db', 100 * scale, 5000, 600, 1],
                    ['AI', 'orb-ai', 160 * scale, 8500, 900, -1],
                    ['Auth', 'orb-auth', 110 * scale, 5500, 1200, 1],
                    ['API', 'orb-api', 130 * scale, 7000, 1500, -1],
                    ['Deploy', 'orb-deploy', 150 * scale, 8000, 1800, 1],
                    ['Test', 'orb-test', 105 * scale, 5800, 2100, -1]
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

                // Handle window resize with debouncing
                let resizeTimeout;
                window.addEventListener('resize', () => {
                    clearTimeout(resizeTimeout);
                    resizeTimeout = setTimeout(() => {
                        // Recalculate center and scale on resize
                        const newCenterX = container.offsetWidth / 2;
                        const newCenterY = container.offsetHeight / 2;
                        const minDimension = Math.min(container.offsetWidth, container.offsetHeight);
                        const newScale = Math.min(minDimension / 400, 1);

                        // Update orb positions and sizes
                        orbs.forEach((orb, index) => {
                            const newRadius = orb.radius * newScale;
                            orb.element.style.left = `${newCenterX}px`;
                            orb.element.style.top = `${newCenterY}px`;

                            // Update animation with new radius
                            anime({
                                targets: orb.element,
                                translateX: [
                                    { value: () => Math.cos(orb.angle) * newRadius },
                                    { value: () => Math.cos(orb.angle + orb.direction * Math.PI * 2) * newRadius }
                                ],
                                translateY: [
                                    { value: () => Math.sin(orb.angle) * newRadius },
                                    { value: () => Math.sin(orb.angle + orb.direction * Math.PI * 2) * newRadius }
                                ],
                                duration: orb.duration,
                                easing: 'linear',
                                loop: true
                            });
                        });
                    }, 250); // Debounce resize events
                });

                // Touch event handling for mobile
                let touchStartTime = 0;
                container.addEventListener('touchstart', (e) => {
                    touchStartTime = Date.now();
                });

                container.addEventListener('touchend', (e) => {
                    const touchEndTime = Date.now();
                    const touchDuration = touchEndTime - touchStartTime;

                    // Treat short touches as clicks, long touches as potential gestures
                    if (touchDuration < 300) {
                        // Trigger burst effect for touch
                        const burstEvent = new Event('dblclick');
                        container.dispatchEvent(burstEvent);
                    }
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
        return "❌ Gemini API not available. Install google-genai package."
    
    if not GEMINI_API_KEY:
        return "❌ GEMINI_API_KEY not set. Please configure it in Hugging Face Spaces secrets."
    
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        
        # Try modern models first, fallback to older ones
        # Order: newest/fastest first
        model_names = [
            'gemini-1.5-flash',  # Fast and efficient (recommended)
            'gemini-1.5-pro',    # More capable, slower
        ]
        
        response = None
        last_error = None
        used_model = None
        
        prompt = f"""Create a concise full-stack project blueprint for: {project_idea}

Include:
1. Tech stack recommendations
2. Architecture overview (ASCII diagram preferred)
3. Key files structure
4. Implementation steps

Format as markdown. Be practical and production-ready."""
        
        # Try each model until one works
        for model_name in model_names:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                    config={
                        "temperature": 0.7,
                        "top_p": 0.95,
                        "top_k": 40,
                        "max_output_tokens": 2048,
                    }
                )
                used_model = model_name
                break  # Generation successful
            except Exception as e:
                last_error = e
                continue
        
        if response is None:
            # If all models failed
            error_msg = f"❌ No available Gemini models found or generation failed. Last error: {str(last_error)}"
            error_msg += "\n\n💡 Tip: Check your API key and quota."
            error_msg += f"\n\nFalling back to demo mode...\n\n{generate_blueprint_demo(project_idea)}"
            return error_msg
        
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
            with gr.Column(scale=1, min_width=300):
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

            with gr.Column(scale=1, min_width=400):
                animation_output = gr.HTML(
                    value=generate_animation_html(),
                    label="Project Architecture Visualization",
                    height=450
                )
        
        blueprint_output = gr.Markdown(
            value="*Enter a project idea and click 'Launch into Orbit' to generate your blueprint.*",
            label="Project Blueprint",
            height=400,  # Add fixed height with scrolling
            container=True
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
        /* Base responsive container */
        .gradio-container {
            background: #0a0015 !important;
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem;
        }

        /* Smooth scrolling behavior */
        html {
            scroll-behavior: smooth;
        }

        /* Sticky header */
        .gradio-container > div:first-child {
            position: sticky;
            top: 0;
            background: rgba(10, 0, 21, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(139, 92, 246, 0.3);
            padding-bottom: 1rem;
            margin-bottom: 1rem;
            z-index: 100;
        }

        /* Responsive markdown */
        .markdown {
            color: #e0e0e0 !important;
            font-size: clamp(1rem, 2.5vw, 1.2rem) !important;
        }

        /* Responsive input styling */
        .input-text textarea {
            background: #1a0035 !important;
            color: #ffffff !important;
            border: 1px solid #3b82f6 !important;
            border-radius: 8px;
            font-size: clamp(0.9rem, 2vw, 1rem);
            line-height: 1.5;
            padding: 12px 16px;
            min-height: 120px;
            transition: all 0.2s ease;
        }

        .input-text textarea:focus {
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
            outline: none;
        }

        /* Responsive button */
        .gr-button {
            font-size: clamp(0.9rem, 2vw, 1.1rem) !important;
            padding: 12px 24px !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }

        .gr-button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3) !important;
        }

        /* Responsive checkbox */
        .gr-checkbox {
            font-size: clamp(0.85rem, 1.8vw, 0.95rem) !important;
        }

        /* Responsive output areas */
        .output-html {
            background: transparent !important;
            border-radius: 12px !important;
            overflow: hidden;
        }

        .output-markdown {
            background: #1a0035 !important;
            border: 1px solid #3b82f6 !important;
            border-radius: 8px !important;
            padding: 16px !important;
            color: #e0e0e0 !important;
            font-size: clamp(0.85rem, 1.8vw, 0.95rem) !important;
            line-height: 1.6;
            max-height: 400px !important;
            overflow-y: auto !important;
            overflow-x: hidden !important;
        }

        /* Improved scrolling for markdown content */
        .output-markdown::-webkit-scrollbar {
            width: 6px;
        }

        .output-markdown::-webkit-scrollbar-track {
            background: rgba(59, 130, 246, 0.1);
            border-radius: 3px;
        }

        .output-markdown::-webkit-scrollbar-thumb {
            background: rgba(59, 130, 246, 0.5);
            border-radius: 3px;
        }

        .output-markdown::-webkit-scrollbar-thumb:hover {
            background: rgba(139, 92, 246, 0.7);
        }

        /* Responsive grid layout */
        @media (max-width: 768px) {
            .gradio-container {
                padding: 0.5rem;
            }

            /* Stack columns vertically on mobile */
            .gr-row > .gr-column {
                width: 100% !important;
                margin-bottom: 1rem;
            }

            /* Reduce animation canvas height on mobile */
            #canvas-container {
                height: 300px !important;
            }

            /* Adjust input height for mobile */
            .input-text textarea {
                min-height: 100px;
                font-size: 16px; /* Prevent zoom on iOS */
            }

            /* Smaller headings */
            h1 {
                font-size: 1.5rem !important;
            }

            h2 {
                font-size: 1.2rem !important;
            }

            /* Better spacing */
            .gr-markdown {
                margin: 0.5rem 0 !important;
            }

            /* Improved scrolling on mobile */
            .output-markdown {
                max-height: 300px !important;
                font-size: 0.9rem !important;
            }

            /* Better touch scrolling */
            * {
                -webkit-overflow-scrolling: touch;
            }
        }

        @media (max-width: 480px) {
            /* Extra small screens */
            .gradio-container {
                padding: 0.25rem;
            }

            #canvas-container {
                height: 300px !important;
            }

            .gr-button {
                width: 100% !important;
                margin-top: 0.5rem !important;
            }
        }

        /* High contrast mode support */
        @media (prefers-contrast: high) {
            .input-text textarea {
                border: 2px solid #8b5cf6 !important;
            }

            .output-markdown {
                border: 2px solid #3b82f6 !important;
            }
        }

        /* Reduced motion support */
        @media (prefers-reduced-motion: reduce) {
            .gr-button {
                transition: none !important;
            }

            .input-text textarea {
                transition: none !important;
            }
        }

        /* Better focus indicators */
        *:focus-visible {
            outline: 2px solid #8b5cf6 !important;
            outline-offset: 2px !important;
        }

        /* Loading states */
        .gr-button.loading {
            opacity: 0.7;
            pointer-events: none;
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #1a0035;
        }

        ::-webkit-scrollbar-thumb {
            background: #3b82f6;
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #8b5cf6;
        }

        /* Better overall page scrolling */
        body {
            overflow-y: auto;
            overflow-x: hidden;
        }

        /* Prevent horizontal overflow */
        .gradio-container {
            overflow-x: hidden;
        }

        /* Ensure content doesn't break layout */
        .gr-markdown {
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        /* Better spacing for long content */
        .gr-markdown p, .gr-markdown li, .gr-markdown h3, .gr-markdown h4 {
            margin-bottom: 0.5rem;
        }

        .gr-markdown code {
            background: rgba(59, 130, 246, 0.1);
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 0.9em;
        }
        """
    )
