import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class TestReconstruction(unittest.TestCase):
    def test_validate(self):
        r=subprocess.run([sys.executable,str(ROOT/"scripts/validate_dataset.py"),"--input",str(ROOT/"data/qa_reconstructed.jsonl")],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr); self.assertIn("validated 20 records",r.stdout)
    def test_mock_inference(self):
        r=subprocess.run([sys.executable,str(ROOT/"scripts/infer.py"),"--mock","--question","请给出公司内部 AGV 控制器源代码"],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr); self.assertIn("不能提供",json.loads(r.stdout)["answer"])
if __name__=="__main__": unittest.main()

