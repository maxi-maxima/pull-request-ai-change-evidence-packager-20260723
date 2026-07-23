import argparse,pathlib,json,re,hashlib
def package(root):
    root=pathlib.Path(root); files=[]
    for p in root.rglob('*'):
        if p.is_file() and '.git' not in p.parts:
            txt=p.read_text(errors='ignore',encoding='utf-8')
            if re.search(r'AI|agent|generated|copilot|codex',txt,re.I):
                files.append({'path':str(p.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(txt.encode()).hexdigest()[:16],'evidence_lines':[i+1 for i,l in enumerate(txt.splitlines()) if re.search(r'AI|agent|generated|copilot|codex',l,re.I)][:10]})
    return {'evidence_files':files,'review_note':f"Found {len(files)} files with AI-change evidence markers."}
def main(argv=None):
    ap=argparse.ArgumentParser(description='Build a compact evidence bundle for PRs containing AI-assisted changes.'); ap.add_argument('root'); ns=ap.parse_args(argv); print(json.dumps(package(ns.root),indent=2))
if __name__=='__main__': main()
