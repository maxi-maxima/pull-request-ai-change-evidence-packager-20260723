import json, subprocess, sys, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class CliTest(unittest.TestCase):
    def run_cli(self,*args):
        return subprocess.run([sys.executable,'-m','pull_request_ai_change_evidence_packager_20260723',*args],cwd=ROOT,text=True,capture_output=True,check=True).stdout

    def test_package(self):
        data=json.loads(self.run_cli('examples/pr')); self.assertEqual(len(data['evidence_files']),2)

    def test_markdown_output(self):
        out=self.run_cli('examples/pr','--format','markdown')
        self.assertIn('## AI Change Evidence',out)
        self.assertIn('| File | Short hash | Evidence lines |',out)
