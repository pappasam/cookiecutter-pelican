GITHUB_PAGES_BRANCH=master
PELICAN_THEME_GIT_URL=git@github.com:nairobilug/pelican-alchemy.git

.PHONY: help
help:  ## Print this help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: pelican-themes/pelican-theme  ## Install local dependencies
	poetry install

.PHONY: serve
serve:  ## Run a local development server
	poetry run pelican --autoreload --listen --relative-urls

.PHONY: publish
publish: build-publish  ## Publish the website to Github Pages
	poetry run ghp-import \
		--message="Generate Pelican site" \
		--branch=$(GITHUB_PAGES_BRANCH) \
		--cname="mydomain.com" \
		output
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: build-dev
build-dev:  ## Build a static, development version of the website
	poetry run pelican --settings pelicanconf.py content

.PHONY: build-publish
build-publish:  ## Build a static, production version of the website
	poetry run pelican --settings publishconf.py content

.PHONY: clean
clean:  ## Remove the output directory
	rm -r output
	rm -rf pelican-themes

pelican-themes/pelican-theme:
	git clone $(PELICAN_THEME_GIT_URL) $@
