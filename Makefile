docker:
	docker build -t digodiego/scrap-resident-evil:latest .
	docker build -t digodiego/scrap-resident-evil:0.0.1 .
	docker login -u digodiego --password-stdin