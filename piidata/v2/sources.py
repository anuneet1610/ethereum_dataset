"""Real documentation sources, by role.

Each role uses *different* repositories, so a model that only memorises one writing
style is caught on dev/test:

- train:        library and developer-tool READMEs/docs, plus GitHub's UI help pages
- dev:          other docs sites (checkpoint selection and threshold choice only)
- test_docs:    Kubernetes and MDN docs, never used for training or tuning
- test_wallet:  ethereum.org wallet, security and how-to guides (real wallet help text)

All are permissively licensed; licences are recorded in data/v2/SOURCES.md at build time.
"""

# (repo, subtree, licence, role, max_files)
SOURCES = [
    # ---- train: general instructional and technical prose ----
    ('fastapi/fastapi', 'docs/en/docs', 'MIT', 'train', 70),
    ('pydantic/pydantic', 'docs', 'MIT', 'train', 60),
    ('encode/httpx', 'docs', 'BSD-3-Clause', 'train', 40),
    ('astral-sh/uv', 'docs', 'MIT OR Apache-2.0', 'train', 60),
    ('squidfunk/mkdocs-material', 'docs', 'MIT', 'train', 50),
    ('python-poetry/poetry', 'docs', 'MIT', 'train', 40),
    ('jestjs/jest', 'docs', 'MIT', 'train', 50),
    ('prettier/prettier', 'docs', 'MIT', 'train', 40),
    ('github/docs', 'content/authentication', 'CC-BY-4.0', 'train', 80),
    ('github/docs', 'content/account-and-profile', 'CC-BY-4.0', 'train', 60),
    ('wevm/viem', 'site/pages/docs', 'MIT', 'train', 80),
    ('rust-lang/book', 'src', 'MIT OR Apache-2.0', 'train', 40),
    # ---- dev: different sites, used for checkpoint and threshold selection ----
    ('vitejs/vite', 'docs/guide', 'MIT', 'dev', 30),
    ('wevm/wagmi', 'site/react', 'MIT', 'dev', 40),
    ('microsoft/vscode-docs', 'docs/getstarted', 'CC-BY-3.0', 'dev', 30),
    ('microsoft/vscode-docs', 'docs/sourcecontrol', 'CC-BY-3.0', 'dev', 20),
    # ---- test_docs: real documentation, never seen in training or tuning ----
    ('kubernetes/website', 'content/en/docs/tasks/configure-pod-container', 'CC-BY-4.0', 'test_docs', 40),
    ('kubernetes/website', 'content/en/docs/concepts/configuration', 'CC-BY-4.0', 'test_docs', 20),
    ('kubernetes/website', 'content/en/docs/concepts/security', 'CC-BY-4.0', 'test_docs', 20),
    ('mdn/content', 'files/en-us/learn_web_development/getting_started', 'CC-BY-SA-2.5', 'test_docs', 40),
    # ---- test_wallet: real wallet help-centre style text ----
    ('ethereum/ethereum-org-website', 'public/content/guides', 'MIT', 'test_wallet', 40),
    ('ethereum/ethereum-org-website', 'public/content/security', 'MIT', 'test_wallet', 5),
    ('ethereum/ethereum-org-website', 'public/content/bridges', 'MIT', 'test_wallet', 3),
    ('ethereum/ethereum-org-website', 'public/content/payments', 'MIT', 'test_wallet', 3),
    ('ethereum/ethereum-org-website', 'public/content/wrapped-eth', 'MIT', 'test_wallet', 2),
    ('ethereum/ethereum-org-website', 'public/content/what-is-ether', 'MIT', 'test_wallet', 2),
    ('ethereum/ethereum-org-website', 'public/content/nft', 'MIT', 'test_wallet', 2),
]

DOC_EXTENSIONS = ('.md', '.mdx', '.rst', '.adoc')

# Sentence caps per role after extraction and filtering.
ROLE_CAPS = {'train': 4500, 'dev': 900, 'test_docs': 1200, 'test_wallet': 700}
PER_SOURCE_CAP = {'train': 520, 'dev': 300, 'test_docs': 400, 'test_wallet': 700}
