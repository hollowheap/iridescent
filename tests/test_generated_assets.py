from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent.parent


class GeneratedAssetTests(unittest.TestCase):
    def test_generated_skill_assets_match_canonical_sources(self):
        result = subprocess.run(
            [sys.executable, "-B", "scripts/sync-skill-assets", "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("skill assets verified", result.stdout)


if __name__ == "__main__":
    unittest.main()
