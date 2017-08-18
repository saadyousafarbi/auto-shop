.PHONY: migrate quality requirements test

help:
	@echo "Please use \`make <target>\` where <target> is one of"
	@echo "  clean                      delete generated byte code and coverage reports"
	@echo "  help                       display this help message"
	@echo "  migrate                    apply database migrations"
	@echo "  requirements               install requirements for autoshop app environment"
	@echo "  serve                      start autoshop server at 0.0.0.0:8888"
	@echo "  static                     build and compress static assets"
	@echo "  clean_static               delete compiled/compressed static assets"
	@echo ""

clean:
	find . -name '*.pyc' -delete

clean_static:
	rm -rf autoshop/static/build/

requirements:
	pip install -qr requirements.txt --exists-action w

static:
	python manage.py collectstatic --noinput

serve:
	python manage.py runserver 0.0.0.0:8888

migrate:
	python manage.py migrate
