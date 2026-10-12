"""Verify packaged evidence against the supplied SHA-256 manifest."""
import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'artifact_manifest.json').read_text(encoding='utf-8'))
for relative, expected in manifest['files'].items():
    target = ROOT / relative
    assert target.is_file(), f'Missing: {relative}'
    actual = hashlib.sha256(target.read_bytes()).hexdigest()
    assert actual == expected, f'Changed: {relative}'
for path in ROOT.glob('*.ipynb'):
    notebook = json.loads(path.read_text(encoding='utf-8'))
    for i, cell in enumerate(notebook['cells'], 1):
        if cell['cell_type'] == 'code':
            ast.parse(''.join(cell['source']), filename=f'{path.name}:cell{i}')
print(f"PASS: {len(manifest['files'])} artifact hashes and notebook syntax.")
print('Training output availability:', manifest['training_notebook_outputs_available'])
