YouTube Automation Agent

Mission

Build a mobile-friendly AI workflow that helps create original YouTube videos from topic research to script, visuals, voiceover, video preview, and eventual publishing.

Core Workflow

1. Accept a user-provided topic.
2. Research and verify factual claims.
3. Draft an original script.
4. Suggest a title, description, and thumbnail concept.
5. Prepare scene-by-scene visual and voiceover instructions.
6. Assemble or prepare the video using available tools.
7. Check quality, copyright risks, and factual accuracy.
8. Show the preview and request user approval.
9. Publish only after explicit approval and authorized YouTube API access.
10. Record errors and provide a clear report.

Safety Rules

- Never expose API keys, OAuth secrets, access tokens, or refresh tokens.
- Never publish, delete, or modify a YouTube video without explicit authorization.
- Never claim a video was uploaded unless the upload is confirmed.
- Do not copy other creators' scripts, videos, music, or thumbnails.
- Do not fabricate facts, sources, views, or analytics.
- Respect YouTube policies, copyright, and applicable API requirements.
- Ask for human review when a decision is uncertain or high-impact.

Engineering Rules

- Keep secrets in environment variables or an approved secret manager.
- Never commit credentials to Git.
- Test scripts before using them on real accounts.
- Use least-privilege permissions.
- Log failures without logging secrets.
- Keep each workflow step modular and replaceable.
- Document setup instructions in README.md.

Current Phase

Phase 1: Create the repository foundation and a safe workflow specification.

Do not implement automatic publishing until the content workflow, tests, and OAuth authorization are ready.
