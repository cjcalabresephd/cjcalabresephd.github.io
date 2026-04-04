import bibtexparser

# Paths
bib_file = "_bibliography/publications.bib"
md_file = "_pages/publications.md"

# Read BibTeX
with open(bib_file, encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Sort by year descending
entries = sorted(bib_database.entries, key=lambda x: x.get('year', '0'), reverse=True)

# Group by year
md_lines = ["---",
            "title: \"Publications\"",
            "permalink: /publications/",
            "layout: single",
            "---\n",
            "# Publications\n"]

current_year = None
for entry in entries:
    year = entry.get('year', 'Unknown')
    if year != current_year:
        md_lines.append(f"\n## {year}\n")
        current_year = year

    title = entry.get('title', 'No Title')
    authors = entry.get('author', 'Unknown Author')
    url = entry.get('url', '')
    abstract = entry.get('abstract', '')

    # Markdown card
    md_lines.append(f"""<div class="publication-card">
<img src="/assets/images/default-thumbnail.png" alt="Thumbnail" class="pub-thumb">
<div class="pub-info">
<strong>{authors}</strong> ({year}). <em>{title}</em>.{' [PDF]('+url+')' if url else ''}
<p class="abstract">{abstract}</p>
</div>
</div>\n""")

# Write to publications.md
with open(md_file, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Generated {md_file} from {bib_file}")
