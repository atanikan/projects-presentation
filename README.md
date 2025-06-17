# 🚀 Technical Presentation - Data Services Architecture

A professional technical presentation built with Quarto and reveal.js, showcasing expertise in scientific computing, HPC, and data services architecture.

## 📋 Prerequisites

- **Node.js** (v16 or higher) - for Mermaid diagram rendering
- **Python** (v3.8 or higher) - for Quarto
- **Git** - for version control

## 🛠️ Installation

### 1. Install Quarto

#### macOS
```bash
# Using Homebrew (recommended)
brew install quarto

# Or download from official website
# https://quarto.org/docs/get-started/
```

#### Linux
```bash
# Download and install the latest release
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-amd64.deb
sudo dpkg -i quarto-1.4.550-linux-amd64.deb

# Or using conda
conda install -c conda-forge quarto
```

#### Windows
```powershell
# Download installer from https://quarto.org/docs/get-started/
# Or using winget
winget install Posit.Quarto
```

### 2. Install Node.js Dependencies

```bash
# Install Mermaid CLI for diagram rendering
npm install -g @mermaid-js/mermaid-cli

# Verify installation
mmdc --version
```

### 3. Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd projects-presentation

# Verify Quarto installation
quarto --version
```

## 🎨 Project Structure

```
projects-presentation/
├── index.qmd              # Main presentation file
├── _quarto.yml           # Quarto configuration
├── css/
│   └── custom.css        # Custom styling
├── assets/
│   ├── *.png            # Architecture diagrams
│   ├── *.svg            # Rendered Mermaid diagrams
│   └── github-mark-white.svg  # GitHub logo
├── docs/                 # Rendered output (for GitHub Pages)
├── render_mermaid.py     # Python script for Mermaid rendering
└── README.md            # This file
```

## 🚀 Development

### Local Preview

```bash
# Start development server with live reload
quarto preview index.qmd

# Or specify port
quarto preview index.qmd --port 4200

# Preview without opening browser
quarto preview index.qmd --no-browser
```

The presentation will be available at `http://localhost:4200` (or specified port).

### Render Presentation

```bash
# Render to HTML (reveal.js)
quarto render index.qmd

# Render to specific format
quarto render index.qmd --to revealjs

# Render to PDF (requires Chrome/Chromium)
quarto render index.qmd --to revealjs-pdf
```

## 🎯 Customization

### Modifying Content

1. **Edit slides**: Modify `index.qmd` using Markdown syntax
2. **Add images**: Place in `assets/` directory and reference in slides
3. **Update styling**: Modify `css/custom.css` for custom appearance

### Adding New Diagrams

1. **Create Mermaid diagram** in your preferred tool
2. **Render to SVG**:
   ```bash
   python render_mermaid.py
   # Or manually:
   mmdc -i diagram.mmd -o assets/diagram.svg
   ```
3. **Reference in slides**:
   ```markdown
   ![Diagram Description](assets/diagram.svg)
   ```

### Theme Customization

The presentation uses the `night` theme with custom CSS. Key customization areas:

- **Colors**: Modify color variables in `css/custom.css`
- **Fonts**: Update font families and sizes
- **Layout**: Adjust spacing, margins, and column layouts
- **Animations**: Add CSS transitions and transforms

## 🌐 Deployment

### GitHub Pages

1. **Configure GitHub Pages**:
   - Go to repository Settings → Pages
   - Set source to "Deploy from a branch"
   - Choose `main` branch and `/docs` folder

2. **Render and commit**:
   ```bash
   # Render to docs directory
   quarto render index.qmd --output-dir docs
   
   # Commit and push
   git add docs/
   git commit -m "Update presentation"
   git push origin main
   ```

3. **Access**: Your presentation will be available at:
   `https://yourusername.github.io/repository-name/`

### Other Platforms

- **Netlify**: Drag and drop the `docs/` folder
- **Vercel**: Import repository and set build command to `quarto render`
- **Self-hosted**: Upload `docs/` contents to your web server

## 🔧 Troubleshooting

### Common Issues

1. **Mermaid diagrams not rendering**:
   ```bash
   # Ensure mmdc is installed
   npm install -g @mermaid-js/mermaid-cli
   
   # Re-render diagrams
   python render_mermaid.py
   ```

2. **Fonts not loading**:
   - Check internet connection (fonts loaded from CDN)
   - Verify CSS paths in `custom.css`

3. **Images not displaying**:
   - Verify file paths are relative to `index.qmd`
   - Check file extensions match exactly

4. **Preview not updating**:
   - Stop and restart `quarto preview`
   - Clear browser cache

### Development Tips

- **Live reload**: Use `quarto preview` for real-time updates
- **Incremental builds**: Quarto only rebuilds changed files
- **Version control**: Commit frequently, especially before major changes
- **Testing**: Preview on different screen sizes and browsers

## 📚 Resources

- **Quarto Documentation**: https://quarto.org/docs/
- **Reveal.js Guide**: https://revealjs.com/
- **Mermaid Syntax**: https://mermaid.js.org/
- **GitHub Pages**: https://pages.github.com/

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test locally
4. Commit changes: `git commit -m "Description"`
5. Push to branch: `git push origin feature-name`
6. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**🚀 Ready to create impressive technical presentations with Quarto!**