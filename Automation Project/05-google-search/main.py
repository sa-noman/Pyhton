"""Open Google searches from Python without scraping results."""

from pathlib import Path
from urllib.parse import quote_plus
import argparse
import webbrowser


def search_url(query: str) -> str:
    query = query.strip()
    if not query:
        raise ValueError("query cannot be empty")
    return f"https://www.google.com/search?q={quote_plus(query)}"


def open_search(query: str) -> str:
    url = search_url(query)
    webbrowser.open_new_tab(url)
    return url


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?")
    parser.add_argument("--file", type=Path)
    args = parser.parse_args()

    queries = []
    if args.file:
        queries.extend(line.strip() for line in args.file.read_text(encoding="utf-8").splitlines() if line.strip())
    if args.query:
        queries.append(args.query)

    if not queries:
        raise SystemExit("Provide a query or --file.")

    for query in queries:
        print(open_search(query))


if __name__ == "__main__":
    main()
