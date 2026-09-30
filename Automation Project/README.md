# Automation Projects

A collection of practical Python automation projects covering messaging workflows, browser actions, email, testing, backup, and voice-related utilities.

## Projects

1. **Instagram Messages** - prepare and optionally send a direct message through Meta's supported messaging API.
2. **Birthday Post on Facebook** - generate a birthday message and optionally publish it to a Facebook Page you manage.
3. **Birthday Mail** - create and send birthday greetings through SMTP.
4. **Software Testing** - discover and run Python unit tests automatically and summarize the results.
5. **Google Search** - open one or multiple Google searches from Python.
6. **LinkedIn Connections** - load profile URLs, open them for review, and record connection decisions.
7. **Bulk Posting on Facebook** - publish content to multiple Facebook Pages you manage with configurable delay and dry-run support.
8. **Automated Email Messages** - send personalized email messages from a CSV contact list.
9. **Automate Backup** - create timestamped ZIP backups and calculate SHA-256 checksums.
10. **Hotword Detection** - detect configured hotwords from text input or an optional microphone source.

## Usage

Projects that interact with external services may require API credentials, environment variables, or account configuration.

Example:

```bash
python "Automation Project/09-automate-backup/main.py" ./source ./backups
```

## Optional Dependencies

```bash
pip install -r "Automation Project/requirements.txt"
```
