# Decisions log

## Home page shows the latest 3 announcements
- **Decision:** the query uses `ORDER BY publication_time DESC LIMIT 3`.
- **Why:** `LIMIT` alone returns arbitrary rows. Sorting newest first guarantees the home page shows the 3 most recent announcements, and keeps the page short.
- **Alternative:** showing all announcements on the home page, rejected because the full list already exists on `/announcements`.

## Shared layout with `base.html`
- **Decision:** all pages extend one `base.html` template (header, navigation, footer) using Jinja blocks.
- **Why:** avoids repeating the same HTML on every page and keeps the style consistent. One CSS file (`static/style.css`) restyles every page.
- **Alternative:** a full HTML page per route, rejected because every change would need editing several files.

## One helper for database connections
- **Decision:** a `get_db_connection()` function reads `DATABASE_URL` from the environment.
- **Why:** the same code works on the VM (Docker) and on Render, because only the environment variable changes. No password or address is written in the code.
- **Alternative:** hardcoding the connection string, rejected for security and portability.

## Simple visual design
- **Decision:** navy and white with one amber accent, serif headings, cards for content.
- **Why:** an academic but young look, and cards make announcements and departments easy to read. Kept simple to focus on the architecture and deployment.