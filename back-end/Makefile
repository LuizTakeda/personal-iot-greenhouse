all: api_service save_data_service data_stream_service

api_service:
	@mkdir -p bin
	go build -o bin/api_service ./cmd/api_service/main.go

data_stream_service:
	@mkdir -p bin
	go build -o bin/data_stream_service ./cmd/data_stream_service/main.go

save_data_service:
	@mkdir -p bin
	go build -o bin/save_data_service ./cmd/save_data_service/main.go

clean:
	rm -rf bin

.PHONY: all api_service save_data_service data_stream_service clean
