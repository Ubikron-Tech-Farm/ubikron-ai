# Flattens the plugin's investigate skill into one Markdown file for the website.
# Usage, from this repo: python3 scripts/flatten-skill.py ubikron/skills/investigate ../public/ubikron-skill.md
import re, sys, pathlib

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
ORDER = ['tools', 'terminal', 'side-panel', 'chrome', 'widget', 'analysis', 'methodology', 'mimic-sequences', 'report']

refs = {}
for name in ORDER:
    text = (src / 'references' / f'{name}.md').read_text().strip()
    title = re.match(r'# (.+)', text).group(1)
    refs[name] = (title, text)

def relink(text):
    # "references/foo.md" or "foo.md" becomes the section's title, pointing below
    def sub(m):
        return f'the "{refs[m.group(1)][0]}" section below'
    pattern = r'`(?:references/)?(' + '|'.join(map(re.escape, ORDER)) + r')\.md`(?:, section "[^"]+")?'
    text = re.sub(pattern, sub, text)
    text = text.replace('then read the one file that matches', 'then read the one section that matches')
    return text.replace('The recording check in SKILL.md', 'The recording check at the top of this skill')

skill = (src / 'SKILL.md').read_text().strip()
skill = skill.replace('name: investigate\n', 'name: ubikron-investigate\n', 1)
head, body = skill.split('\n---\n', 1)
note = ('\n\n<!-- One-file version of the Ubikron plugin\'s investigate skill, for agents that '
        'take a single SKILL.md. The plugin (Ubikron-Tech-Farm/ubikron-ai) is the source; '
        'regenerate this file from it rather than editing it here. -->\n')
parts = [head + '\n---' + note + relink(body)]
for name in ORDER:
    parts.append(relink(refs[name][1]))
out.write_text('\n\n---\n\n'.join(parts) + '\n')
print(f'{out}: {sum(1 for _ in out.open())} lines')
