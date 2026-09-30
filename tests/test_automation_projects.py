import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "Automation Project"


def load(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


instagram = load("instagram_messages", "01-instagram-messages")
birthday_post = load("birthday_post", "02-facebook-birthday-post")
birthday_mail = load("birthday_mail", "03-birthday-mail")
software_testing = load("software_testing", "04-software-testing")
google_search = load("google_search", "05-google-search")
linkedin = load("linkedin_connections", "06-linkedin-connections")
facebook_bulk = load("facebook_bulk", "07-facebook-bulk-posting")
auto_email = load("auto_email", "08-automated-email-messages")
backup = load("backup", "09-automate-backup")
hotword = load("hotword", "10-hotword-detection")


class AutomationProjectTests(unittest.TestCase):
    def test_instagram_preview(self):
        message = instagram.InstagramMessage("123", "Hello")
        self.assertIn("Hello", instagram.preview(message))

    def test_birthday_message(self):
        text = birthday_post.build_birthday_message("Noman")
        self.assertIn("Happy Birthday, Noman", text)

    def test_birthday_mail(self):
        msg = birthday_mail.build_mail("friend@example.com", "Friend", "me@example.com")
        self.assertEqual(msg["To"], "friend@example.com")

    def test_test_summary(self):
        summary = software_testing.TestSummary(5, 0, 0, 0)
        self.assertTrue(summary.passed)

    def test_google_search_url(self):
        self.assertEqual(
            google_search.search_url("python automation"),
            "https://www.google.com/search?q=python+automation",
        )

    def test_linkedin_profile_loader(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "profiles.csv"
            path.write_text(
                "name,profile_url\nTest,https://www.linkedin.com/in/test/\n",
                encoding="utf-8",
            )
            rows = linkedin.load_profiles(path)
            self.assertEqual(len(rows), 1)

    def test_facebook_bulk_limit(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "jobs.json"
            path.write_text('[{"page_id":"1","message":"hello"}]', encoding="utf-8")
            jobs = facebook_bulk.load_jobs(path)
            self.assertEqual(jobs[0].page_id, "1")

    def test_email_contact_loader(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "contacts.csv"
            path.write_text(
                "name,email,subject\nA,a@example.com,Hi\n",
                encoding="utf-8",
            )
            contacts = auto_email.load_contacts(path)
            self.assertEqual(contacts[0]["name"], "A")

    def test_backup(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source = root / "source"
            destination = root / "backups"
            source.mkdir()
            (source / "file.txt").write_text("hello", encoding="utf-8")
            archive, checksum = backup.create_backup(source, destination)
            self.assertTrue(archive.exists())
            self.assertEqual(len(checksum), 64)

    def test_hotword(self):
        self.assertEqual(
            hotword.contains_hotword("Hey Computer, start", ["computer"]),
            "computer",
        )


if __name__ == "__main__":
    unittest.main()
