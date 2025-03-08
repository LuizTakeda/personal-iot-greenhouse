FROM golang:1.24.1

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY cmd/save_data_service ./cmd/save_data_service
COPY internal ./internal
COPY pkg ./pkg
COPY Makefile ./

RUN make save_data_service

CMD ["./bin/save_data_service"]
