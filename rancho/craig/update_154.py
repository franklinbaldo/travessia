import re
import os
from datetime import datetime

# 1. Update FooterNav.astro
with open("site/src/components/FooterNav.astro", "r") as f:
    footer_content = f.read()

target_style = re.search(r'<style>.*?</style>', footer_content, re.DOTALL).group(0)

new_style = """<style>
  .footer-nav {
    display: flex;
    justify-content: space-between;
    gap: 1.5rem;
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px dashed var(--meta-color);
  }

  .footer-nav a {
    font-size: 1rem;
  }

  .footer-nav-link {
    --notebook-bg: #f9f8f3;
    --notebook-lines: #cce0e5;
    --notebook-margin: #e8a2a2;
    --notebook-ink: #2b2b2b;
    --notebook-meta: #666666;

    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    position: relative;
    max-width: 45%;
    flex: 1;
    padding: 1.5rem;

    background-color: var(--notebook-bg);
    background-image: repeating-linear-gradient(
      transparent,
      transparent 1.5rem,
      var(--notebook-lines) 1.5rem,
      var(--notebook-lines) 1.6rem
    );
    background-position: 0 1rem;

    border: none;
    border-radius: 2px 8px 8px 2px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.04);
    border-left: 2px solid var(--notebook-margin);

    text-decoration: none;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease, border-width 0.2s ease;
  }

  :global([data-theme="dark"]) .footer-nav-link {
    --notebook-bg: #1e2022;
    --notebook-lines: #32383d;
    --notebook-margin: #7a4646;
    --notebook-ink: #e8e6e3;
    --notebook-meta: #aaaaaa;
    border-left: 2px solid var(--notebook-margin);
  }

  .footer-nav-link.next {
    text-align: right;
    align-items: flex-end;
    margin-left: auto;
    border-left: none;
    border-right: 2px solid var(--notebook-margin);
    border-radius: 8px 2px 2px 8px;
  }

  /* Microinteractions: lift, tilt, and paper corner curl */
  .footer-nav-link:hover {
    transform: translateY(-4px) rotate(-1.5deg);
    box-shadow: 4px 8px 15px rgba(0,0,0,0.08);
  }

  .footer-nav-link.next:hover {
    transform: translateY(-4px) rotate(1.5deg);
  }

  /* "Corner fold" pure CSS effect similar to BlogCard but customized for the footer */
  .footer-nav-link::after {
    content: "";
    position: absolute;
    bottom: 0;
    right: 0;
    border-width: 0;
    border-style: solid;
    border-color: rgba(0,0,0,0.1) var(--bg-color) var(--bg-color) rgba(0,0,0,0.05);
    transition: border-width 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border-radius: 0 0 8px 0;
  }

  .footer-nav-link.next::after {
    right: auto;
    left: 0;
    border-color: rgba(0,0,0,0.1) rgba(0,0,0,0.05) var(--bg-color) var(--bg-color);
    border-radius: 0 0 0 8px;
  }

  .footer-nav-link:hover::after {
    border-width: 18px;
  }

  .footer-nav-dir {
    font-family: var(--font-meta);
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--notebook-meta);
    transition: color 0.3s ease, transform 0.3s ease;
    display: inline-block;
  }

  .footer-nav-link:hover .footer-nav-dir {
    color: var(--notebook-ink);
  }

  .footer-nav-link.prev:hover .footer-nav-dir {
    transform: translateX(-4px);
  }

  .footer-nav-link.next:hover .footer-nav-dir {
    transform: translateX(4px);
  }

  .footer-nav-autor {
    font-family: var(--font-meta);
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.03em;
    color: var(--notebook-ink);
    opacity: 0.85;
  }

  .footer-nav-titulo {
    font-family: 'Courier New', Courier, monospace;
    font-size: 1.1rem;
    color: var(--notebook-ink);
    line-height: 1.4;
    font-weight: bold;
    letter-spacing: -0.02em;
    position: relative;
    display: inline-block;
  }

  /* Animated strikethrough/underline microinteraction */
  .footer-nav-titulo::before {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: var(--notebook-ink);
    transform: scaleX(0);
    transform-origin: left center;
    transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1);
  }

  .footer-nav-link.next .footer-nav-titulo::before {
    transform-origin: right center;
  }

  .footer-nav-link:hover .footer-nav-titulo::before {
    transform: scaleX(1);
  }

  @media (max-width: 600px) {
    .footer-nav {
      flex-direction: column;
      gap: 1.5rem;
    }

    .footer-nav-link {
      max-width: 100%;
    }

    .footer-nav-link.next {
      text-align: right;
      align-items: flex-end;
    }
  }
</style>"""

with open("site/src/components/FooterNav.astro", "w") as f:
    f.write(footer_content.replace(target_style, new_style))


# 2. Update EXPERIENCE.md
with open("rancho/craig/EXPERIENCE.md", "r") as f:
    exp_content = f.read()

new_log = """
In Sessão 154, addressing the constraints of "microinterações e detalhes" with the aesthetic inspiration of a "manuscrito/caderno" while restricting focus to "focar numa única página/componente", I reimagined the `FooterNav.astro` component at the bottom of the reading pages. I discarded the generic brutalist borders and pseudo-elements in favor of making the "Anterior" and "Próximo" navigation links resemble torn, interactive pieces of lined notebook paper. The micro-interactions were deeply detailed: on hover, the paper links physically tilt and lift (`translateY(-4px) rotate(-1.5deg)`), the directional arrow shifts slightly to indicate forward/backward motion, an animated ink underline expands beneath the title simulating a swift pen stroke, and a pure CSS corner fold curls up at the bottom edge. This distills the requested tactile, notebook aesthetic into a focused set of rich component-level interactions."""

parts = exp_content.split('## 2. My Goals for the Future')
exp_content = parts[0] + new_log + "\n## 2. My Goals for the Future" + parts[1]

with open("rancho/craig/EXPERIENCE.md", "w") as f:
    f.write(exp_content)

# 3. Create 154-journal.md
journal_content = """---
data: 2026-03-11
---

# Sessão 154
**Tema:** Redesign do FooterNav com estética de manuscrito e microinterações

**O que eu fiz:**
Focando em uma única página/componente (`FooterNav.astro`), substituí o estilo brutalista antigo por uma estética de "manuscrito/caderno". Transformei os botões de navegação "Anterior" e "Próximo" em pequenos pedaços de papel pautado, com uma linha de margem vermelha. Para atender à restrição de "microinterações e detalhes", adicionei efeitos altamente refinados ao estado de hover:
1. Uma animação de "corner fold" (dobra no canto do papel).
2. O botão inteiro levanta e sofre uma leve rotação de 1.5 graus.
3. As setas direcionais se deslocam levemente na direção da navegação.
4. Um sublinhado animado que surge sob o título, simulando um traço rápido de caneta.

Essas adições alinham a navegação com o tema de cadernos e rascunhos sem prejudicar a performance ou modificar estruturalmente o HTML."""

with open("rancho/craig/154-journal.md", "w") as f:
    f.write(journal_content)

print(f"Update 154 generated. target_style length: {len(target_style)}")
