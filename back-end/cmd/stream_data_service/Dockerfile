FROM golang:1.24.1

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY cmd/stream_data_service ./cmd/stream_data_service
COPY internal ./internal
COPY pkg ./pkg
COPY Makefile ./

RUN make stream_data_service

CMD ["./bin/stream_data_service"]
