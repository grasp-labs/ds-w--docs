# RequestID

RequsetID can be set by client applications for the purpose of tracking request from its origin to completion. RequestID has to be a valid UUID or a new RequestID will be generated.

```go
requestID := req.Header.Get("X-Request-ID")

// Validate RequestID
_, err := uuid.Parse(requestID)
if err != nil {
  requestID = uuid.New().String()
}
```

# OwnerID

OwnerID (partition) can be set by client applications to allocate usage and audit to specified partition. Services do not check if OwnerID mapps to a Tenant partition.

```go
var ownerID *string
if val := request.Header.Get("X-Owner-ID"); val != "" {
  ownerID = &val
}
´´´
