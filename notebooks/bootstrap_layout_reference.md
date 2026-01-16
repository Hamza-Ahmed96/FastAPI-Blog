# Bootstrap Layout Template - Reference Guide

This is a reusable template breakdown. Sections marked with ✏️ are the parts you'll typically customize for each project.

---

## Document Structure Overview

```
<!DOCTYPE html>
<html>
  <head>     ← Metadata, styles, fonts (invisible to user)
  </head>
  <body>
    <header>  ← Navigation bar
    </header>
    <main>    ← Your page content goes here
    </main>
    <footer>  ← Bottom of page
    </footer>
    <script>  ← JavaScript (Bootstrap + custom)
    </script>
  </body>
</html>
```

---

## HEAD Section

### Essential Meta Tags (Keep These)
```html
<meta charset="utf-8">                                    <!-- Character encoding -->
<meta name="viewport" content="width=device-width, initial-scale=1">  <!-- Mobile responsive -->
```
> **Never remove these** - they ensure your site works on all devices.

---

### ✏️ Site Info (CUSTOMIZE THIS)
```html
<title>FastAPI Blog - {{ title }}</title>           <!-- Browser tab title -->
<meta name="description" content="FastAPI Tutorial">  <!-- Google search description -->
<meta name="author" content="Corey Schafer">          <!-- Your name -->
```

**Jinja2 conditional title:**
```html
{% if title %}
  <title>FastAPI Blog - {{ title }}</title>   <!-- Shows: "FastAPI Blog - Home" -->
{% else %}
  <title>FastAPI Blog</title>                  <!-- Fallback if no title passed -->
{% endif %}
```

---

### Open Graph Tags (Social Media Previews)
```html
<meta property="og:title" content="FastAPI Blog">     <!-- Title when shared on social -->
<meta property="og:type" content="website">           <!-- Type: website, article, etc -->
<meta property="og:url" content="">                   <!-- ✏️ Your full URL -->
<meta property="og:image" content="">                 <!-- ✏️ Preview image URL -->
```
> These control what your link looks like when shared on Facebook, LinkedIn, Twitter, etc.

---

### ✏️ Fonts (CUSTOMIZE THIS)
```html
<!-- Step 1: Preconnect (speeds up loading) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Step 2: Load the font -->
<link href="https://fonts.googleapis.com/css2?family=Montserrat:...&family=Nunito:...&display=swap"
      rel="stylesheet">
```

**To change fonts:**
1. Go to [fonts.google.com](https://fonts.google.com)
2. Select fonts → Click "Get embed code"
3. Replace the `<link href="...">` with the new one

---

### Bootstrap CSS (KEEP AS-IS)
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-..."    <!-- Security hash - ensures file wasn't tampered with -->
      crossorigin="anonymous">
```
> This single line gives you access to ALL Bootstrap styles.

---

### ✏️ Custom Stylesheet
```html
<link rel="stylesheet" type="text/css" href="/static/css/main.css">
```
> Your custom CSS goes in `main.css` to override/extend Bootstrap.

---

### ✏️ Favicon & Icons (CUSTOMIZE THIS)
```html
<link rel="icon" href="/static/icons/favicon.ico">              <!-- Browser tab icon -->
<link rel="apple-touch-icon" href="/static/icons/icon.png">     <!-- iOS home screen -->
<meta name="theme-color" content="#527c9f">                     <!-- Mobile browser color -->
```

---

## BODY Section

### Body Classes Explained
```html
<body class="d-flex flex-column min-vh-100">
```

| Class | Meaning | Why Use It |
|-------|---------|------------|
| `d-flex` | Display: flexbox | Enables flexible layout |
| `flex-column` | Stack children vertically | Header → Main → Footer |
| `min-vh-100` | Minimum height = 100% viewport | Footer stays at bottom even on short pages |

---

## NAVIGATION BAR (Header)

### Full Structure
```html
<nav class="navbar navbar-expand-md bg-steel fixed-top" data-bs-theme="dark">
```

| Class/Attribute | What It Does |
|----------------|--------------|
| `navbar` | Base Bootstrap navbar styling |
| `navbar-expand-md` | Collapses to hamburger menu on screens smaller than "medium" (768px) |
| `bg-steel` | ✏️ Custom background color (defined in your CSS) |
| `fixed-top` | Navbar stays at top when scrolling |
| `data-bs-theme="dark"` | Forces dark theme on navbar |

---

### ✏️ Brand/Logo
```html
<a class="navbar-brand me-4" href="#">FastAPI Blog</a>
```
- `navbar-brand` = Logo styling
- `me-4` = Margin-end (right margin) of size 4
- ✏️ Change `FastAPI Blog` to your site name
- ✏️ Change `href="#"` to `href="/"` for home link

---

### Mobile Hamburger Button
```html
<button class="navbar-toggler"
        data-bs-toggle="collapse"
        data-bs-target="#navbarToggle">
  <span class="navbar-toggler-icon"></span>
</button>
```
> This only appears on small screens. Clicking it reveals the menu.

---

### ✏️ Navigation Links (Left Side)
```html
<div class="navbar-nav me-auto">
  <a class="nav-link active" href="#">Home</a>
  <!-- Add more links here -->
</div>
```

| Class | Meaning |
|-------|---------|
| `navbar-nav` | Container for nav links |
| `me-auto` | Push everything after this to the right |
| `nav-link` | Styling for individual links |
| `active` | Highlights current page |

**To add more links:**
```html
<a class="nav-link" href="/about">About</a>
<a class="nav-link" href="/contact">Contact</a>
```

---

### ✏️ Right Side (Login/Register Buttons)
```html
<div class="navbar-nav">
  <a class="btn btn-outline-light mb-2 mb-md-0 me-md-2" href="#">Login</a>
  <a class="btn btn-light" href="#">Register</a>
</div>
```

| Class | Meaning |
|-------|---------|
| `btn` | Makes it look like a button |
| `btn-outline-light` | White border, transparent background |
| `btn-light` | Solid light/white button |
| `mb-2` | Margin-bottom on mobile |
| `mb-md-0` | No margin-bottom on medium+ screens |
| `me-md-2` | Margin-right on medium+ screens |

---

### Dark Mode Dropdown
```html
<div class="nav-item dropdown">
  <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown">
    <span id="bd-theme-text">🌗 Auto</span>
  </a>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><button data-bs-theme-value="light">🌝 Light</button></li>
    <li><button data-bs-theme-value="dark">🌚 Dark</button></li>
    <li><button data-bs-theme-value="auto">🌗 Auto</button></li>
  </ul>
</div>
```

| Class | Meaning |
|-------|---------|
| `dropdown` | Container for dropdown |
| `dropdown-toggle` | Shows arrow, enables clicking |
| `dropdown-menu` | The menu that appears |
| `dropdown-menu-end` | Aligns menu to right edge |

---

## MAIN CONTENT AREA

```html
<main role="main" class="container">
  <div class="row">
    <div class="col-md-8">           <!-- Main content: 8/12 columns -->
      {% block content %}
      {% endblock content %}
    </div>
    <aside class="col-md-4">         <!-- Sidebar: 4/12 columns -->
      <!-- Sidebar content -->
    </aside>
  </div>
</main>
```

### Bootstrap Grid System (IMPORTANT)
Bootstrap divides the screen into **12 columns**.

```
|------ col-md-8 (8/12 = 66%) ------|-- col-md-4 (4/12 = 33%) --|

┌────────────────────────────────────┬──────────────────────────┐
│                                    │                          │
│         MAIN CONTENT               │        SIDEBAR           │
│         (Your posts)               │        (Links, etc)      │
│                                    │                          │
└────────────────────────────────────┴──────────────────────────┘
```

| Class | Meaning |
|-------|---------|
| `container` | Centered box with max-width and padding |
| `row` | Horizontal group of columns |
| `col-md-8` | 8 columns wide on medium+ screens |
| `col-md-4` | 4 columns wide on medium+ screens |

> On mobile, both become full-width (stacked vertically).

---

### ✏️ Jinja2 Content Block
```html
{% block content %}
{% endblock content %}
```
> This is where child templates (like `home.html`) inject their content.

---

### ✏️ Sidebar Content
```html
<div class="content-section py-3 px-4 mb-4">
  <h3>Our Sidebar</h3>
  <p class="text-body-secondary">You can put any information here.</p>
  <ul class="list-group">
    <li class="list-group-item">Latest Posts</li>
    <li class="list-group-item">Announcements</li>
  </ul>
</div>
```

| Class | Meaning |
|-------|---------|
| `py-3` | Padding top & bottom (y-axis) = 3 |
| `px-4` | Padding left & right (x-axis) = 4 |
| `mb-4` | Margin bottom = 4 |
| `text-body-secondary` | Muted/gray text |
| `list-group` | Styled list container |
| `list-group-item` | Individual list item |

---

## FOOTER

```html
<footer class="mt-auto py-3 bg-body-tertiary border-top">
  <div class="container text-center">
    <p class="text-body-secondary mb-0">
      © <span id="year"></span> Corey Schafer
    </p>
  </div>
</footer>
```

| Class | Meaning |
|-------|---------|
| `mt-auto` | Margin-top: auto → pushes footer to bottom |
| `py-3` | Vertical padding |
| `bg-body-tertiary` | Light gray background |
| `border-top` | Thin line above footer |
| `text-center` | Center the text |
| `mb-0` | No margin below paragraph |

**Dynamic year script:**
```html
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
```
> Automatically shows current year (e.g., "© 2026").

---

## SCRIPTS (Bottom of Body)

### Bootstrap JavaScript (KEEP AS-IS)
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js">
</script>
```
> Required for: dropdowns, modals, tooltips, hamburger menu, etc.

---

### Dark Mode Script
```javascript
const setTheme = (theme) => {
  if (theme === 'auto') {
    // Use system preference
    document.documentElement.setAttribute('data-bs-theme',
      window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  } else {
    document.documentElement.setAttribute('data-bs-theme', theme);
  }
  localStorage.setItem('theme', theme);  // Remember choice
};
```
> This handles the dark/light mode toggle and remembers user preference.

---

## Bootstrap Spacing Cheat Sheet

Bootstrap uses a consistent numbering system for spacing:

| Number | Size |
|--------|------|
| 0 | 0 |
| 1 | 0.25rem (4px) |
| 2 | 0.5rem (8px) |
| 3 | 1rem (16px) |
| 4 | 1.5rem (24px) |
| 5 | 3rem (48px) |

**Pattern:** `{property}{side}-{size}`

| Letter | Meaning |
|--------|---------|
| `m` | margin |
| `p` | padding |
| `t` | top |
| `b` | bottom |
| `s` | start (left) |
| `e` | end (right) |
| `x` | left & right |
| `y` | top & bottom |

**Examples:**
- `mt-3` = margin-top: 1rem
- `px-4` = padding-left & padding-right: 1.5rem
- `mb-0` = margin-bottom: 0

---

## Quick Customization Checklist

When starting a new project, change these:

- [ ] `<title>` - Your site name
- [ ] `<meta name="description">` - Your description
- [ ] `<meta name="author">` - Your name
- [ ] `og:` tags - Social media info
- [ ] Font links - Your preferred fonts
- [ ] `navbar-brand` - Your logo/site name
- [ ] Nav links - Your pages
- [ ] Sidebar content - Your widgets
- [ ] Footer copyright - Your name
- [ ] `theme-color` - Your brand color
- [ ] Favicon files - Your icons
