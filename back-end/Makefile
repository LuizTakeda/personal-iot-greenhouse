all: save_data stream_data

save_data_service:
	@mkdir -p bin
	go build -o bin/save_data_service ./cmd/save_data_service/main.go

stream_data_service:
	@mkdir -p bin
	go build -o bin/stream_data_service ./cmd/stream_data_service/main.go

clean:
	rm -rf bin

.PHONY: all save_data stream_data clean
