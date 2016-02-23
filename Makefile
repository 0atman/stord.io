OUTPUTDIR=_site
GITHUB_PAGES_BRANCH=gh-pages

github:
		ghp-import -m "Generate Jekyll site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
			git push origin $(GITHUB_PAGES_BRANCH)
