FROM golang:1.24.1

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY cmd/data_stream_service ./cmd/data_stream_service
COPY internal ./internal
COPY pkg ./pkg
COPY Makefile ./

RUN make data_stream_service

CMD ["./bin/data_stream_service"]
