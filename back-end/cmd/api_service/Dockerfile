FROM golang:1.24.1

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY cmd/api_service ./cmd/api_service
COPY internal ./internal
COPY pkg ./pkg
COPY Makefile ./

RUN make api_service

CMD ["./bin/api_service"]
