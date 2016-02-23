OUTPUTDIR=_site
GITHUB_PAGES_BRANCH=gh-pages

github:
	jekyll build
	echo "www.stord.io" >> _site/CNAME
	ghp-import -m "Generate Jekyll site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)
