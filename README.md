
# AutoIDE Project

Full-scale automation IDE full-with browser extensions (mini + full), deep learning methods, admin control panel, and code generation.

- Supports Chrome & Firefox additions
- Flask-based backend with admin UI
- Deep Learning MODULEs for automation code generation
- User panel with balance, serials, and download flow tracking

Project Structure:
```\nAutoIDE/\l‛mini_addon/\n |  ’manifest.json\n |  ₼pbackground.js\n |  ₯popup.html / popup.js\n |  ₯token_extractor.js\n\lキfull_addon/ (more features)\n ```\```\bbackend/\napp.py\ntemplates/                       # login.html, dashboard.html, userpanel.html\nstatic/                          # css, js\ngenerator/ - python_generator.py, dom_predictor.py\nusers.json + db.json\n ```\n\nFeatures to come:\n- Telegram bot notifications\n- Auto-upgrade via Replit cron\n- OpenAI fine-tuning module focused on web automation\n 