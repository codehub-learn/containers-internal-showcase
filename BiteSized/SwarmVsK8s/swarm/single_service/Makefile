TAG ?= latest
create: clean
	docker service create --name indian --publish published=8900,target=80 indian:$(TAG)

update:
	docker service update --image indian:$(TAG) indian

rollback:
	docker service rollback indian

clean:
	-docker service rm indian
